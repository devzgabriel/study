#include <stdio.h>
#include <string.h>
#include <iostream>
#include <new>
using namespace std;
struct fruta{
    string cor;
    string nome;
};

int main () {
    //cria novo ponteiro para struct
    fruta *primeirafruta = new fruta;
    primeirafruta -> cor = "amarela";
    primeirafruta -> nome = "banana";
    cout << "\nFruta: " << primeirafruta->nome << " cor: " << primeirafruta->cor;

    //criando lista de structs
    fruta *ponteirofruta = new fruta[2];
    ponteirofruta[0].cor = "Vermelho";
    ponteirofruta[0].nome = "morango";
    ponteirofruta[1].cor = "verde";
    ponteirofruta[1].nome = "limao";
    int i;
    for (i=0;i<2;i++){
        cout << "\n" << ponteirofruta[i].nome << " eh " << ponteirofruta[i].cor;
    }
    return 0;
}

