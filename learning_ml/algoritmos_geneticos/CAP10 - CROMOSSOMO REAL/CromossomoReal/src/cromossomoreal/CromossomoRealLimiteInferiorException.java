/*
 * CromossomoRealLimiteInferiorException.java
 *
 * Created on 4 de Fevereiro de 2006, 15:07
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
public class CromossomoRealLimiteInferiorException extends CromossomoRealException {
    
    /** Creates a new instance of CromossomoRealLimiteInferiorException */
    public CromossomoRealLimiteInferiorException() {
        super("Limite inferior de uma coordenada violado.");
    }
    
    public CromossomoRealLimiteInferiorException(String s) {
        super(s);
    }
    
}
