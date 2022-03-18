/*
 * CromossomoRealLimiteSuperiorException.java
 *
 * Created on 4 de Fevereiro de 2006, 15:08
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
public class CromossomoRealLimiteSuperiorException extends CromossomoRealException { 
    
    /** Creates a new instance of CromossomoRealLimiteSuperiorException */
    public CromossomoRealLimiteSuperiorException() {
        super("Limite superior de uma coordenada violado.");
    }
    
     public CromossomoRealLimiteSuperiorException(String s) {
        super(s);
    }
    
    
}
