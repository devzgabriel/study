#include <stdio.h>
#include <stdlib.h>
#include <new>


int main(){

    int linhas=3,colunas=3,i,j;
    int **matriz;
    //digitando tamanho
    printf("\ndigite quantidade de lnhas");
    scanf("%d",&linhas);
    printf("\ndigite quantidade de colunas");
    scanf("%d",&colunas);
    //alocando memoria para as linhas
    matriz = (int**) new int[linhas];
    //alocando memoria para as colunas
    for(i=0;i<linhas;i++){
        matriz[i]= (int*) new int[colunas];
    }
    for(i=0;i<linhas;i++){
        for(j=0;j<colunas;j++){
            matriz[i][j] = i*j;
            printf("%d ", matriz[i][j]);
        }
        printf("\n");
    }
    free(matriz);
    return 0;

}
