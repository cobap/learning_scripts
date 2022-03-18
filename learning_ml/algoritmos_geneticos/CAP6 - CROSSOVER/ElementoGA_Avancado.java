import java.util.*;

public class ElementoGA_Avancado extends ElementoGA1 {
   
   
   public ElementoGA_Avancado crossoverDoisPontos(ElementoGA outroPai)  {
	   String aux1;	   
	   ElementoGA_Avancado retorno=null;
	   int pontoCorte1=(new Double(java.lang.Math.random()*(this.valor.length()-1))).intValue();           
           int pontoCorte2=(new Double(java.lang.Math.random()*(this.valor.length()-(pontoCorte1+1)))).intValue();                      
           pontoCorte2+=pontoCorte1;           
	   if (java.lang.Math.random()<0.5) {		                
	   	aux1=this.valor.substring(0,pontoCorte1);                
                aux1=aux1+outroPai.getValor().substring(pontoCorte1,pontoCorte2);                
                aux1=aux1+this.valor.substring(pontoCorte2,this.valor.length());                
	   } else {		                
		aux1=outroPai.getValor().substring(0,pontoCorte1);                
                aux1=aux1+this.valor.substring(pontoCorte1,pontoCorte2);                
                aux1=aux1+outroPai.getValor().substring(pontoCorte2,outroPai.getValor().length());	                   
	   }
	   try {
	      retorno=(ElementoGA_Avancado) outroPai.getClass().newInstance();
	      retorno.setValor(aux1);
	   } catch (Exception e) {
	   }	   	   
	   return(retorno);
	} 
	
      public ElementoGA_Avancado crossoverUniforme(ElementoGA outroPai)  {
	   String aux1="";
	   ElementoGA_Avancado retorno=null;
	   int i;
	   for(i=0;i<this.valor.length();i++) {
	   	if (java.lang.Math.random()<0.5) {	   	   
	   	   aux1=aux1+this.valor.substring(i,i+1);
	   	} else {			   	   
                   aux1=aux1+outroPai.getValor().substring(i,i+1);                                
        	}
	   }
	   try {
	      retorno=(ElementoGA_Avancado) outroPai.getClass().newInstance();
	      retorno.setValor(aux1);
	   } catch (Exception e) {
	   }	   	   
	   return(retorno);
	} 
	
 	/****************/
	/* Construtores */
	/****************/
	
	public ElementoGA_Avancado(String novoValor) {
	   super(novoValor);
	}	

	public ElementoGA_Avancado(int tamanho) {
	   super(tamanho);
	}

	public ElementoGA_Avancado() {
  	    super(100);
	}

}
