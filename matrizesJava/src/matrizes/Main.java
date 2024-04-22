package matrizes;
import org.junit.runner.JUnitCore;
import org.junit.runner.Result;
import org.junit.runner.notification.Failure;

public class Main {

	public static void main(String[] args) {
		
		Result result = JUnitCore.runClasses(MatrizTest.class);

        for (Failure failure : result.getFailures()) {
            System.out.println(failure.toString());
        }

        if (result.wasSuccessful()) {
            System.out.println("Todos os testes passaram!");
        } else {
            System.out.println("Alguns testes falharam.");
        	
        }
	}
}
	
	