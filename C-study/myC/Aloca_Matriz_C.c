#include <stdio.h>
#include <stdlib.h>


int main(){

    int linhas=3,colunas=3,i,j;
    int **matriz;
    //digitando tamanho
    printf("\ndigite quantidade de lnhas");
    scanf("%d",&linhas);
    printf("\ndigite quantidade de colunas");
    scanf("%d",&colunas);
    //alocando memoria para os ponteiros (linhas)
    matriz = (int**) malloc(linhas * sizeof(int*));
    //em cada linha alocando memoria para as colunas
    for(i=0;i<linhas;i++){
        matriz[i]= (int*) malloc(colunas * sizeof(int));
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
