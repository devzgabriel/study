#include <stdio.h>
#include <stdlib.h>

int* alocaVetor(int tamanho){

    int auxiliar;
    // aloca o tamanho digitado multiplicado o tamanho ocupado por cada posição na memória
    // e forçando tornar um ponteiro
    auxiliar = malloc(tamanho * sizeof(int));
    //retorna o ponteiro com a primeira posição na memória do vetor
    return auxiliar;
}

int main (){
    int *vetor, tamanho;

    printf("Digite o tamanho do vetor: ");
    scanf("%d, &tamanho");

    vetor = alocaVetor(tamanho);

    for(cont=0; cont<tamanho; cont++){
        vetor[cont] = 0;
    }

    for(cont=0; cont<tamanho; cont++){
        printf("%d\n" , vetor[cont] );
    }

    //libera espaço na memória
    free(vetor);

    return 0;
}
