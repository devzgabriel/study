#include <stdio.h>
#include <stdlib.h>
#include <new>
//#include <string>
//#include <iostream>


int main(){
    int tamanho,i;
    printf("digite um tamanho pars o vetor:");
    scanf("%d", &tamanho);

    //aloca na memória
    int *vetor = new int(tamanho);

    for(i=0;i<tamanho;i++){
        vetor[i] = i;
        printf("\n %d");
    }
     free(vetor);
    return 0;
}

