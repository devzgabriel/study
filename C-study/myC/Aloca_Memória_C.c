#include <stdio.h>
#include <stdlib.h>

int* alocaVetor(int tamanho){

    int aux;

    //aloca na memória
    aux = (int *) malloc(tamanho * sizeof(int));
    return aux;
}


int main(){
    int *vetor, tamanho,i;
    printf("digite um tamanho pars o vetor:");
    scanf("%d", &tamanho);
    vetor = alocaVetor(tamanho);

    for(i=0;i<tamanho;i++){
        vetor[i] = 90;
    }

    for(i=0;i<tamanho;i++){
        printf("%d \n", vetor[i]);
    }

    return 0;
}
