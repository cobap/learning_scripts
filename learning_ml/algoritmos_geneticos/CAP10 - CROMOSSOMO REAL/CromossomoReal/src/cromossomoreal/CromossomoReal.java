/*
 * CromossomoReal.java
 *
 * Created on 4 de Fevereiro de 2006, 11:19
 *
 * To change this template, choose Tools | Options and locate the template under
 * the Source Creation and Management node. Right-click the template and choose
 * Open. You can then make changes to the template in the Source Editor.
 */

package cromossomoreal;

/**
 *
 * @author Ricardo
 */
public class CromossomoReal  implements Cloneable {
    
    private double[] valores;
    private double[][] limites;
    private final double delta=0.001;
    
    
    /** Creates a new instance of CromossomoReal */
    public CromossomoReal(int n) {
        valores=new double[n];
        limites=new double[n][2];
        for (int i=0;i<n;i++) {            
            limites[i][0]=0.0;
            limites[i][1]=1.0;
            this.sorteiaPosicao(i);
        }
    }
    
    public CromossomoReal(int n,double[] lim) {
        this(n);
        int i=0;        
        while((2*i+1)<lim.length) {
            this.setLimiteInferior(i,lim[2*i]);
            this.setLimiteSuperior(i,lim[2*i+1]);
            this.sorteiaPosicao(i);
            i++;
        }
    }
    
    private void sorteiaPosicao(int i) {
        valores[i]=limites[i][0]+Math.random()*(limites[i][1]-limites[i][0]);
    }
    
    private void acertaValores(int i) {
        if (limites[i][1]<limites[i][0]) {
            //Troca os limites, pois setamos o inferior para um valor maior
            //que o superior ou vice-versa
            double temp=limites[i][1];
            limites[i][1]=limites[i][0];
            limites[i][0]=temp;            
        }
        //Se o valor da psição passou a ficar fora dos novos limites setados, sorteia
        //um novo valor
        if ((this.valores[i]<limites[i][0])||(this.valores[i]<limites[i][1])) {
            this.sorteiaPosicao(i);
        }
    }
    
    public void setLimiteInferior(int i,double val) {
        if (i<valores.length) {
            limites[i][0]=val;
            this.acertaValores(i);
        }
    }
    
    public double getLimiteInferior(int i) {
        return(this.limites[i][0]);
    }
    
    public void setLimiteSuperior(int i,double val) {
        if (i<valores.length) {
            limites[i][1]=val;
            this.acertaValores(i);
        }
    }
    
    public double getLimiteSuperior(int i) {
        return(this.limites[i][1]);
    }
    
    public void setPosicao(int i, double val) throws CromossomoRealException {
        if (val<this.limites[i][0]) {
            throw new CromossomoRealLimiteInferiorException();
        }
        if (val>this.limites[i][1]) {
            throw new CromossomoRealLimiteSuperiorException();
        }
        this.valores[i]=val;
    }
    
    public double getPosicao(int i) {
        return(valores[i]);
    }
    
    public String toString() {
        String s="";
        int i;
        for(i=0;i<this.valores.length;i++) {
            s=s+this.valores[i];
            if ((i+1)<this.valores.length) {
                s=s+"/";
            }
        }
        return(s);
    }
    
    public CromossomoReal crossoverAritmetico(CromossomoReal outro, double lambda) {
        CromossomoReal filho=new CromossomoReal(this.valores.length);
        int i;
        //Faz com que os limtes do filho sejam compatíveis com o maior
        //intervalo dos pais e depois calcula o valor do filho
        for(i=0;i<this.valores.length;i++) {
            //Como este operador realiza uma operação em uma região convexa,
            //o seu resultado vai ficar entre o menor dos valores e o maior
            //dos valores. Logo, precisamos definir os limites do filho de acordo.
            if (this.getLimiteInferior(i)<outro.getLimiteInferior(i)) {
                filho.setLimiteInferior(i,this.getLimiteInferior(i));
            } else {
                filho.setLimiteInferior(i,outro.getLimiteInferior(i));
            }
            if (this.getLimiteSuperior(i)>outro.getLimiteSuperior(i)) {
                filho.setLimiteSuperior(i,this.getLimiteSuperior(i));
            } else {
                filho.setLimiteSuperior(i,outro.getLimiteSuperior(i));
            }
            try {
                filho.setPosicao(i, this.valores[i]*lambda+(1-lambda)*outro.getPosicao(i));
            } catch (CromossomoRealException e) {
                //Não precisamos fazer nada aqui, pois nós já acertamos os limites do
                //filho, e esta exceção nunca ocorrerá.
            }
        }
        return(filho);
    }
        
    
    public CromossomoReal crossoverAritmetico(CromossomoReal outro) {
        return(this.crossoverAritmetico(outro,0.5));
    }
    
    public CromossomoReal crossoverSimples(CromossomoReal outro) {
        int i,corte;
        double valor,min,max;
        CromossomoReal filho=new CromossomoReal(this.valores.length);
        corte=(int) Math.round(Math.random()*this.valores.length);
        if (corte==this.valores.length) {corte--;}
        for(i=0;i<this.valores.length;i++) {
            if (i<corte) {
                min=this.getLimiteInferior(i);
                max=this.getLimiteSuperior(i);
                valor=this.getPosicao(i);
            } else {
                min=outro.getLimiteInferior(i);
                max=outro.getLimiteSuperior(i);                
                valor=outro.getPosicao(i);
            }
            filho.setLimiteInferior(i,min);
            filho.setLimiteSuperior(i,max);
            try {
                filho.setPosicao(i, valor);
            } catch (CromossomoRealException e) {
                //Não precisamos fazer nada aqui, pois nós já acertamos os limites do
                //filho, e esta exceção nunca ocorrerá.
            }
        }
        return(filho);
    }
    
    public Object clone() {
        CromossomoReal retorno=new CromossomoReal(this.valores.length);
        int i;
        for (i=0;i<this.valores.length;i++) {
            retorno.setLimiteInferior(i,this.getLimiteInferior(i));
            retorno.setLimiteSuperior(i,this.getLimiteSuperior(i));
            try {
            retorno.setPosicao(i, this.getPosicao(i));
            } catch (CromossomoRealException e) {
                
            }
        }
        return(retorno);
    }
    
     public CromossomoReal crossoverDiscreto(CromossomoReal outro) {         
	   CromossomoReal retorno=(CromossomoReal) this.clone();	   
	   for(int i=0;i<this.valores.length;i++) {
	      if (java.lang.Math.random()<0.5) {	   	   
	   	  retorno.setLimiteInferior(i,outro.getLimiteInferior(i));
                  retorno.setLimiteSuperior(i,outro.getLimiteSuperior(i));
                  try {
                      retorno.setPosicao(i, outro.getPosicao(i));
                  } catch (CromossomoRealException e) {                
                  }
	      } 
	   }
	   return(retorno);
      } 
     
     
     public CromossomoReal crossoverFlat(CromossomoReal outro) {         
         CromossomoReal retorno=(CromossomoReal) this.clone();
         double aux,min,max;
         for(int i=0;i<this.valores.length;i++) {
             if (outro.getLimiteInferior(i)<this.getLimiteInferior(i)) {
                 retorno.setLimiteInferior(i, outro.getLimiteInferior(i));
             }   
             if (outro.getLimiteSuperior(i)<this.getLimiteSuperior(i)) {
                 retorno.setLimiteSuperior(i, outro.getLimiteSuperior(i));
             }
             if (outro.getPosicao(i)>this.getPosicao(i)) {
                 min=this.getPosicao(i);
                 max=outro.getPosicao(i);
             } else {
                 min=outro.getPosicao(i);
                 max=this.getPosicao(i);
             }
             aux=min+Math.random()*(max-min);
             try {
                retorno.setPosicao(i,aux);
             } catch (CromossomoRealException e) {                
             }
         }         
         return(retorno);
     }
     
     public double normal(double x, double desvio) {
         double retorno=-0.5*((x/desvio)*(x/desvio));
         retorno=Math.exp(retorno);
         retorno=retorno/(desvio*Math.sqrt(6.283184));
         return(retorno);
     }
     
     public double integral(double lim_sup, double lim_inf, double somatorio) {
         double retorno=somatorio;         
         
         for(double i=lim_inf;i<lim_sup;i+=delta) {
             retorno+=(delta/2)*(normal(i, 1)+normal(i+delta,1));
         }
         return(retorno);
     }
     
     public double calcula_elemento(double prob) {
         double retorno=-5;
         double somatorio=0;
         while(somatorio<prob) {
             retorno+=delta;
             somatorio=integral(retorno, retorno-delta, somatorio);             
         }
         return(retorno);
     }

     
        
    
}
