public static boolean MatrizDiagonal(int[][] matriz) {
        if (matriz.length != matriz[0].length) // se nao for quadrada
            return false;

        for (int i = 0; i < matriz.length; i++) {
            for (int j = 0; j < matriz[i].length; j++) {
                if (i != j && matriz[i][j] != 0) { // verifica se os elementos fora da diagonal principal são zero
                    return false;
                }
            }
        }

        return true;
    }
    
    public boolean matrizTriangularInferior(int matriz[][]) {
    	
        if (matriz == null || matriz.length == 0)
            return false;

        for (int i = 0; i < matriz.length; i++) {
            for (int j = i + 1; j < matriz[i].length; j++) { //verificando se os elementos acima da diagonal principal nao sao 0
            												
            	if (matriz[i][j] != 0) {
                    return false;
                }
            }
        }

        return true;
    }
    
    public boolean matrizTriangularSuperior(int matriz[][]) {
      
        if (matriz == null || matriz.length == 0) 
            return false;

        for (int i = 0; i < matriz.length; i++) {
            for (int j = 0; j < i; j++) { //verificando se todos os elementos abaixo da diagonal principal nao sao 0
                if (matriz[i][j] != 0) {
                    return false;
                }
            }
        }

        return true;
    }
    
