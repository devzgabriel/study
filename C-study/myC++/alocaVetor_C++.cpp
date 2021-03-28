
#include <stdio.h>
#include <stdlib.h>
#include <new>


int main (){
    int tamanho, cont;

    printf("Digite o tamanho do vetor: ");
    scanf("%d", &tamanho);

    int *vetor = new int[tamanho];

    for(cont=0; cont<tamanho; cont++){
        vetor[cont] = cont;
        printf("%d\n" , vetor[cont] );
    }

    return 0;
}
