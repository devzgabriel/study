/*  vetores
    strings
*/

#include <stdio.h>
#include <stdlib.h>


void main(){

    char palavra[255];
    printf("Digite uma palavra:");
    setbuf(stdin, 0);
    fgets(palavra, 255, stdin);
    printf("%d",stdlen(palavra));
    palavra[stdlen(palavra)-1] = '\0';
    printf("%s",palavra);

    system("pause");

 }
