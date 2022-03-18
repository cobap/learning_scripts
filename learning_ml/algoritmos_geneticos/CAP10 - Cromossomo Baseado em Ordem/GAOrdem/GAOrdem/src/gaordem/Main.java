/*
 * Main.java
 *
 * Created on 21 de Janeiro de 2006, 11:04
 *
 * To change this template, choose Tools | Options and locate the template under
 * the Source Creation and Management node. Right-click the template and choose
 * Open. You can then make changes to the template in the Source Editor.
 */

package gaordem;

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
        CromossomoGAOrdem aux1=new CromossomoGAOrdem(8);        
        CromossomoGAOrdem aux2=new CromossomoGAOrdem(8);        
        System.out.println(aux1);
        System.out.println(aux2);        
        System.out.println(aux1.PMX(aux2));
    }
    
}
