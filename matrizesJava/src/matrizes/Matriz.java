package matrizes;

public class Matriz {

    public int[][] soma(int x[][], int y[][]) {
        if (x.length != y.length || x[0].length != y[0].length) {
            System.out.println("Matrizes com dimensões diferentes");
            return null;
        }

        int matrizSoma[][] = new int[x.length][y[0].length];

        for (int i = 0; i < x.length; i++) {
            for (int j = 0; j < x[0].length; j++) { 
                matrizSoma[i][j] = x[i][j] + y[i][j];
            }
        }

        return matrizSoma;
    }

    public int[][] transposta(int matriz[][]) {
        int rows = matriz.length;
        int cols = matriz[0].length;

        int[][] matrizTransposta = new int[cols][rows];

        for (int linhas = 0; linhas < rows; linhas++) {
            for (int colunas = 0; colunas < cols; colunas++) {
                matrizTransposta[colunas][linhas] = matriz[linhas][colunas];
            }
        }

        return matrizTransposta;
    }

    public int[][] multiplicaPorEscalar(int matriz[][], int escalar) {
        for (int i = 0; i < matriz.length; i++) {
            for (int j = 0; j < matriz[0].length; j++) { 
                matriz[i][j] *= escalar;
            }
        }
        return matriz;
    }
}
