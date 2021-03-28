
/*  Numero aleatorio
    lacos
    constante
*/

#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#define CONSTANTE 1339

void main(){
    // alimenta de forma randomica
    srand((unsigned)time(NULL));
    // gera opção aleatoria
    int aleatorio = rand() % 3;
    printf("%d",aleatorio);

    int a=1,x,i;

    // Usando o While
    while(a<=10){
        printf("\n%d",a);
        a++;
    }

    //Usando o Do While executa 1 antes de conparar
    do{
        printf("\n%d",a);
        a++;
    }while(a<=10);

    //Usando o For
    for(i=1;i<=10;i++){
        x=i*5;
        printf("\n %d x 5 = %d",i,x);
    }
    printf("\nA constante eh %d\n",CONSTANTE);
    system("cls");
    system("pause");

}
