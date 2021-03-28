#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main (){
     FILE *file;
     //abre o arquivp
     file = fopen("teste.txt", "r");
    //verifica e lê
    if(file){
        int c;
        while((c=getc(file))!=EOF){
            printf("%c", c);
        }
    fclose(file);
    }
     return 0;
}
