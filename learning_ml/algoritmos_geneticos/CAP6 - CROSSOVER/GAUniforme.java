import java.util.*;

 public class GAUniforme extends GA {
 
   public void inicializaPopulacao() {   
	int i;
	this.populacao=new Vector();	
	for(i=0;i<this.tamanho_populacao;++i) {	   
	   this.populacao.add(new ElementoGA_Avancado()); 
	}
   }
   
   public void geracao() {
	nova_populacao=new Vector();
        ElementoGA_Avancado pai1,pai2, filho;
	int i;
	System.out.println("Calculando nova geracao...\n");
	for(i=0;i<this.populacao.size();++i) {
		pai1 = (ElementoGA_Avancado)populacao.get(this.roleta());
		pai2 = (ElementoGA_Avancado) populacao.get(this.roleta());		
	        filho= pai1.crossoverUniforme(pai2);
		filho.mutacao(chance_mutacao);
		System.out.println("Vou adicionar...");
		nova_populacao.add(filho);
	}
   }
   
   /****************/
   /* Construtores */
   /****************/

   public GAUniforme(int num_geracoes,int tam_populacao, double prob_mut) {
   	super(num_geracoes,tam_populacao,prob_mut);
   }
   
   public GAUniforme(int tam_populacao, double prob_mut) {
   	super(60,tam_populacao,prob_mut);
   }
   
   public GAUniforme(double prob_mut) {
   	super(60,100,prob_mut);
   }
   
   public GAUniforme() {
   	super(60,100,0.001);
   }
   
 }