/*
 * Main.java
 *
 * Created on 4 de Fevereiro de 2006, 11:18
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
public class Main {
    
    /** Creates a new instance of Main */
    public Main() {
        
    }
    
    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // TODO code application logic here
        CromossomoReal aux=new CromossomoReal(5);
        CromossomoReal aux2=new CromossomoReal(5);
        System.out.println("Resultado="+aux.calcula_elemento(0.5));
        /*System.out.println("Aux:"+aux);
        System.out.println("Aux2:"+aux2);
        System.out.println("Fazendo o crossover:"+aux.crossoverDiscreto(aux2));*/
    }
    
}
