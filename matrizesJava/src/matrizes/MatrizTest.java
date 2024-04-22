package matrizes;

import static org.junit.Assert.assertArrayEquals;
import org.junit.Test;

public class MatrizTest {

    @Test
    public void testSomaMatrizes() {
        Matriz matriz = new Matriz();
        int[][] matrizA = {{1, 2, 3}, {4, 5, 6}, {7, 8, 9}};
        int[][] matrizB = {{9, 8, 7}, {6, 5, 4}, {3, 2, 1}};
        int[][] resultadoEsperado = {{10, 10, 10}, {10, 10, 10}, {10, 10, 10}};
        assertArrayEquals(resultadoEsperado, matriz.soma(matrizA, matrizB));
    }

    @Test
    public void testMultiplicacaoPorEscalar() {
        Matriz matriz = new Matriz();
        int[][] matrizA = {{1, 2, 3}, {4, 5, 6}, {7, 8, 9}};
        int escalar = 2;
        int[][] resultadoEsperado = {{2, 4, 6}, {8, 10, 12}, {14, 16, 18}};
        assertArrayEquals(resultadoEsperado, matriz.multiplicaPorEscalar(matrizA, escalar));
    }

    @Test
    public void testTransposta() {
        Matriz matriz = new Matriz();
        int[][] matrizA = {{1, 5}, {7, 3}, {8, 2}};
        int[][] resultadoEsperado = {{1, 7, 8}, {5, 3, 2}};
        assertArrayEquals(resultadoEsperado, matriz.transposta(matrizA));
    }
}
    