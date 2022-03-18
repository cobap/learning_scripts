/*
 * CromossomoGAOrdem.java
 *
 * Created on 21 de Janeiro de 2006, 11:05
 *
 * To change this template, choose Tools | Options and locate the template under
 * the Source Creation and Management node. Right-click the template and choose
 * Open. You can then make changes to the template in the Source Editor.
 */

package gaordem;

import java.util.*;
import java.lang.Math.*;


/**
 *
 * @author Ricardo
 */
public class CromossomoGAOrdem implements Cloneable {
    
int cidades[];
    /**Cria um novo cromossomo para o GA baseado em ordem. 
     *@param num número de cidades que o cromossomo deve armazenar.
     */
    public CromossomoGAOrdem(int num) {
        Vector aux=new Vector();
        int i,j;        
        cidades=new int[num];
        //Cria um vetor auxiliar que vai servir para nos ajudar
        //a escolher os números a serem colocados dentro do 
        //nosso vetor
        for(j=0;j<num;j++) {
            aux.add(new Integer(1+j));
        }
        j=0;
        while (aux.size()>0) {
            //Escolhe um número dentro do vetor
            i=(int) Math.round(Math.random()*aux.size());            
            if (i==aux.size()) {i--;}
            //coloca-o no array e apaga-o do vetor, garantindo
            //que não teremos cidades duplicadas no array.
            cidades[j++]=((Integer) aux.get(i)).intValue();
            aux.remove(i);            
        }
    }
    
    /**
     *Realiza a mutação em um cromossomo causando disrupções aleatórias em
     *um pedaço do mesmo.
     */
    public void mutacaoMisturaSublista() {
        int i,j,inicio,fim;        
        inicio=(int) Math.round(Math.random()*cidades.length);
        if (inicio==cidades.length) {inicio--;}
        fim=inicio+(int) Math.round(Math.random()*(cidades.length-inicio));
        if (fim==cidades.length) {fim--;}        
        Vector aux=new Vector();
        //copia as cidades na ordem invertida para o array auxiliar
        for (i=inicio;i<=fim;i++) {
            aux.add(new Integer(cidades[i]));
        }
        j=inicio;        
        while (aux.size()>0) {            
            //Escolhe um número dentro do vetor
            i=(int) Math.round(Math.random()*aux.size());            
            if (i==aux.size()) {i--;}            
            //coloca-o no array e apaga-o do vetor, garantindo
            //que não teremos cidades duplicadas na sublista.
            cidades[j]=((Integer) aux.get(i)).intValue();
            aux.remove(i);            
            j++;
        }
    }
    
    /**
     *Realiza a mutação em um cromossomo invertendo um pedaço do mesmo. É o operador
     *de mutação que causa a disrupção no menor número de arestas (considerando
     *o problema simético).
     */
    public void mutacaoInversao() {
        int i,inicio,fim;        
        inicio=(int) Math.round(Math.random()*cidades.length);
        if (inicio==cidades.length) {inicio--;}
        fim=inicio+(int) Math.round(Math.random()*(cidades.length-inicio));
        if (fim==cidades.length) {fim--;}                
        int aux[]=new int[fim-inicio+1];
        //copia as cidades na ordem invertida para o array auxiliar
        for (i=inicio;i<=fim;i++) {
            aux[i-inicio]=cidades[fim-i+inicio];
        }
        //copia as cidades em uma ordem aletatória de volta para o array
        for (i=inicio;i<=fim;i++) {
            cidades[i]=aux[i-inicio];
        }        
    }
    
    /**
     *Realiza a mutação invertendo a posição de apenas dois elementos sorteados
     *de forma aleatória dentro do cromossomo. Causa a disrupção de até 4 arestas.
     */
    public void mutacaoInv2() {
        int i,inicio,fim;
        inicio=(int) Math.round(Math.random()*cidades.length);
        if (inicio==cidades.length) {inicio--;}
        fim=inicio;
        i=0;
        while ((fim==inicio)&&(i<3)) {
            fim=inicio+(int) Math.round(Math.random()*(cidades.length-inicio));
            if (fim==cidades.length) {fim--;}                
            i++;
        }
        i=cidades[inicio];
        cidades[inicio]=cidades[fim];
        cidades[fim]=i;
    }
    
    /**
     *Imprime o conteúdo do cromossomo (cidades na ordem visitada).
     */
    public String toString() {
        int i;
        String s="";
        for(i=0;i<cidades.length;i++) {
            s=s+cidades[i];
            if (i<(cidades.length-1)) {s=s+"/";}
        }
        return(s);
    }
    
    public CromossomoGAOrdem crossoverOrdem(CromossomoGAOrdem outro) {
        CromossomoGAOrdem retorno=new CromossomoGAOrdem(this.cidades.length);
        int i,j,inicio,fim;
        Vector v=new Vector();
        inicio=(int) Math.round(Math.random()*cidades.length);
        if (inicio==cidades.length) {inicio--;}
        fim=inicio+(int) Math.round(Math.random()*(cidades.length-inicio));        
        if (fim==cidades.length) {fim--;}                
        System.out.println(inicio+"   "+fim);
        for(i=0;i<cidades.length;i++) {
            if ((i<inicio)||(i>fim)) {
               v.add(new Integer(this.cidades[i]));               
            } else {
               retorno.cidades[i]=this.cidades[i]; 
            }            
        }
        j=0;
        for(i=0;i<cidades.length;i++) {
            if (j==inicio) {j=fim+1;}
            if (v.indexOf(new Integer(outro.cidades[i]))>=0) {
                retorno.cidades[j]=outro.cidades[i];
                j++;
            }
        }
        return(retorno);
    }
    
    
    public CromossomoGAOrdem crossoverUniformeOrdem(CromossomoGAOrdem outro) {
        CromossomoGAOrdem retorno=new CromossomoGAOrdem(this.cidades.length);
        int i,j,inicio,fim;
        Vector v=new Vector();                
        for(i=0;i<cidades.length;i++) {
            if (Math.random()<0.5) {
               //Vamos pegar a equivalente do segundo pai. Logo,
               //acrescentamos a cidade corrente na lista de não usadas 
               v.add(new Integer(this.cidades[i]));
               retorno.cidades[i]=-1;
            } else {
               retorno.cidades[i]=this.cidades[i]; 
            }            
        }
        System.out.println("Neste momento, retorno="+retorno);
        j=0;
        for(i=0;i<cidades.length;i++) {
            //procuramos a primeira posição livre
            while((j<cidades.length)&&(retorno.cidades[j]!=-1)) {j++;}
            if (v.indexOf(new Integer(outro.cidades[i]))>=0) {
                System.out.println("Acrescentei a cidade"+outro.cidades[i]);
                retorno.cidades[j]=outro.cidades[i];
                j++;
            }
        }
        return(retorno);
    }
    
    public CromossomoGAOrdem edgeRecombination(CromossomoGAOrdem outro) {
        CromossomoGAOrdem retorno=new CromossomoGAOrdem(this.cidades.length);
        int i,j,k, prox_cidade, tam_prox;
        int tam=this.cidades.length;
        int cid_corrente;
        Vector ja_usadas=new Vector();
        //Cria os vetores que vão armazenar as arestas
        Vector v[]=new Vector[tam];
        for (i=0;i<tam;i++) {            
            v[i]=new Vector();            
        }
        //cria a lista de arestas
        for (i=0;i<tam;i++) {                   
            v[this.cidades[i]-1].add(new Integer(this.cidades[(i+1)%tam]));            
            v[this.cidades[(i+1)%tam]-1].add(new Integer(this.cidades[i]));
            v[outro.cidades[i]-1].add(new Integer(outro.cidades[(i+1)%tam]));
            v[outro.cidades[(i+1)%tam]-1].add(new Integer(outro.cidades[i]));
            
        }
        
        //Começa a recombinação de arestas
        cid_corrente=this.cidades[0];
        k=0;
        while (ja_usadas.size()<tam) {
            System.out.print("Cidade corrente: "+cid_corrente);
            //Imprime as arestas
            for (i=0;i<tam;i++) {
                System.out.print((i+1)+":");
                for (j=0;j<v[i].size();j++) {
                    System.out.print(v[i].get(j)+"-");
                }
                System.out.println(" ");
            }
            
            //coloca a cidade corrente na posição correta
            retorno.cidades[k]=cid_corrente;
            k++;
            
            System.out.println(" ");
            System.out.println(" ");
            for (i=0;i<k;i++) {
                System.out.print("Neste momento, o retorno é:");
                for (j=0;j<ja_usadas.size();j++) {
                    System.out.print(retorno.cidades[j]+"-");
                }
                System.out.println(" ");
            }
            
            //acrescenta a cidade corrente à lista de cidades usadas
            ja_usadas.add(new Integer(cid_corrente));
            //remove a cidade corrente de todas as listas de adjacências
            for (i=0;i<tam;i++) {
                j=0;                
                while(j>=0) {
                    j=v[i].indexOf(new Integer(cid_corrente));
                    if (j>=0) {
                        v[i].remove(j);
                    }
                }
            }
            //escolhe a próxima cidade
            if (v[cid_corrente-1].size()>0) {
                prox_cidade=((Integer) v[cid_corrente-1].get(0)).intValue();
                tam_prox=v[prox_cidade-1].size();
                System.out.print("*** Prox: "+prox_cidade+" tamanho:"+tam_prox);
                for(i=1;i<v[cid_corrente-1].size();i++) {
                    j=((Integer) v[cid_corrente-1].get(i)).intValue();
                    if (v[j-1].size()<tam_prox) {
                        prox_cidade=j;
                        tam_prox=v[j-1].size();
                        System.out.print("Prox: "+prox_cidade+" tamanho:"+tam_prox);
                    }                    
                }                
            } else {
                //Não há nenhuma cidade na lista de adjacências                
                prox_cidade=-1;
                for(i=1;((prox_cidade<0)&&(i<tam));i++) {
                    if (ja_usadas.indexOf(new Integer(i))<0) {
                        prox_cidade=i;
                    }
                }
                System.out.print("Como não havia ninguém, prox: "+prox_cidade);
            }
            cid_corrente=prox_cidade;            
        }
        return(retorno);
    }
    
    protected Object clone() {
        CromossomoGAOrdem retorno=new CromossomoGAOrdem(this.cidades.length);
        int i;
        for(i=0;i<this.cidades.length;i++) {
            retorno.cidades[i]=this.cidades[i];
        }
        return(retorno);
    }
    
    public CromossomoGAOrdem PMX(CromossomoGAOrdem outro) {
        CromossomoGAOrdem retorno=(CromossomoGAOrdem) this.clone();
        int i,inicio,fim, aux1;
        int mapeamento[]=new int[this.cidades.length];        
        inicio=(int) Math.round(Math.random()*cidades.length);
        if (inicio==cidades.length) {inicio--;}
        fim=inicio+(int) Math.round(Math.random()*(cidades.length-inicio));        
        if (fim==cidades.length) {fim--;}   
        for(i=0;i<this.cidades.length;i++) {
            mapeamento[i]=-1;
        }
        System.out.println("Retorno: "+retorno);
        System.out.println(inicio+"   "+fim);
        for(i=inicio;i<=fim;i++) {            
           mapeamento[this.cidades[i]-1]=outro.cidades[i];
           mapeamento[outro.cidades[i]-1]=this.cidades[i];
           System.out.println("Mapeando "+this.cidades[i]+" para "+outro.cidades[i]);           
        }
        System.out.println("Invertendo os mapeamentos");
        for(i=0;i<cidades.length;i++) {            
            if (mapeamento[retorno.cidades[i]-1]!=-1) {
                aux1=mapeamento[retorno.cidades[i]-1];
                if (mapeamento[aux1-1]==retorno.cidades[i]) {
                    retorno.cidades[i]=mapeamento[retorno.cidades[i]-1];
                }
            } 
        }        
        return(retorno);
    }
    
    
    
}
