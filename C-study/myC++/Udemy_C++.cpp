#include <stdio.h>
#include <stdlib.h>
#include <string>
#include <iostream>

using namespace std;

void mostraAntecessor(int numero){
    cout << "\n" << numero - 1;
}

void somadez(int *numero){
    *numero = *numero +10;
}

int main(){

    std::string palavra;
    printf("digtie:");
    std::cin >> palavra;
    std::cout << palavra <<"\n";
    //---------------------------------matriz
    int matriz [2][2],i,j;
    matriz[0][0]=1;
    matriz[0][1]=2;
    matriz[1][0]=3;
    matriz[1][1]=4;

    for(i=0;i<2;i++){
         for(j=0;j<2;j++){
            cout << matriz[i][j] <<" ";
         }
         cout << "\n";
    }
    cout << "\n";
    //--------------------------------lendo
    for(i=0;i<2;i++){
         for(j=0;j<2;j++){
            scanf("%d", &matriz[i][j]);
         }
    }
    cout << "\n";
    //--------------------------------imprimindo
    for(i=0;i<2;i++){
         for(j=0;j<2;j++){
            cout << matriz[i][j] <<" ";
         }
         cout << "\n";
    }
    cout << "\n";
    //--------------------------------funções com parâmetros
    int a;
    cout << "valor para a:";
    cin >> a;
    mostraAntecessor(a);
    somadez(&a);
    cout << "\n" << a;
    system("pause");
    return 0;
 }
