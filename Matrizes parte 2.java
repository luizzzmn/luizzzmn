public boolean matrizDiagonal(int matriz[][]) {
  
        int posicaoInicial = matriz[0][0];
        
        for (int i = 1; i < matriz.length; i++) {
            if (matriz[i][i] != posicaoInicial) {
                return false; 
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
    
