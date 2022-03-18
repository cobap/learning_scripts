/*
 * CromossomoGP.java
 *
 * Created on 15 de Março de 2006, 17:00
 *
 * To change this template, choose Tools | Options and locate the template under
 * the Source Creation and Management node. Right-click the template and choose
 * Open. You can then make changes to the template in the Source Editor.
 */

package programacaogenetica;

/**
 *
 * @author rlinden
 */
public class CromossomoGP implements Cloneable {
    
    public String conteudo;
    public CromossomoGP esquerda,direita;
    
    /** Creates a new instance of CromossomoGP */
    public CromossomoGP() {
        this(1);
    }
    
    public CromossomoGP(int altura) {
        if (altura>0) {
            if (Math.random()<(1.0/(altura+1))) {
                //Vamos aumentar em um a altura da árvore, logo o nível corrente é um operador
                double aux=Math.random();
                if (aux<0.2) {conteudo="+";}
                if ((aux>=0.2)&&(aux<0.4)) {conteudo="-";}
                if ((aux>=0.4)&&(aux<0.6)) {conteudo="*";}
                if ((aux>=0.6)&&(aux<0.8)) {conteudo="/";}
                if (aux>=0.8) {conteudo="^";}  
                esquerda=new CromossomoGP(altura++);
                direita=new CromossomoGP(altura++);
            } else {
                if (Math.random()<0.5) {conteudo="x";}
                else {conteudo=Double.toString(Math.random()*2-1);}
                esquerda=null;  
                direita=null;
            }
        }
    }
    
    public void mutacao(double p) {
        if (Math.random()<p) {
            CromossomoGP aux=new CromossomoGP(2);
            this.conteudo=aux.conteudo;
            this.esquerda=aux.esquerda;
            this.direita=aux.direita;
        } else {
            if (this.esquerda!=null) {
                if (Math.random()<0.5) {
                    this.esquerda.mutacao(p);
                } else {
                    this.direita.mutacao(p);
                }
            }
        }
    }
    
    public CromossomoGP crossover(CromossomoGP outro, double p) {
        CromossomoGP retorno=(CromossomoGP) this.clone();
        if (Math.random()<p) {
            retorno.conteudo=outro.conteudo;
            if (outro.esquerda!=null) {
                retorno.esquerda=(CromossomoGP) outro.esquerda.clone();
                retorno.direita=(CromossomoGP) outro.direita.clone();
            } else {
                retorno.esquerda=null;
                retorno.direita=null;                
            }    
        } else {
           if ((this.esquerda!=null)&&(outro.esquerda!=null)) {
                if (Math.random()<0.5) {
                    retorno.esquerda=this.esquerda.crossover(outro.esquerda,p);
                } else {
                    retorno.direita=this.direita.crossover(outro.direita,p);
                }
            } 
        }        
        return(retorno);
    }
    
    public String toString() {
        String retorno=conteudo+" ";
        if (esquerda!=null) {retorno=retorno+esquerda.toString();}
        if (direita!=null) {retorno=retorno+direita.toString();}
        return(retorno);
    }
    
    public Object clone() {
        CromossomoGP retorno=new CromossomoGP(0);
        retorno.conteudo=this.conteudo;
        retorno.esquerda=null;
        retorno.direita=null;
        if (this.esquerda!=null) {retorno.esquerda=(CromossomoGP) this.esquerda.clone();}
        if (this.direita!=null) {retorno.direita=(CromossomoGP) this.direita.clone();}
        return (retorno);
    }
    
}
