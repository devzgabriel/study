#include <stdio.h>
#include <stdlib.h>
#include <fstream>
#include <string.h>
#include <iostream>

using namespace std;
int main(){
    //cria objeto de arquivo
    ofstream arquivo_saida;
    //abre ou cria arquivo
    arquivo_saida.open("teste.txt", std::ios_base::app);
    //escreve no arquivo
    arquivo_saida << "\n Gabriel";
    arquivo_saida.close();

    //lê o arquivo
    ifstream input("teste.txt");
    string texto_lido;
    //pra cada linha ele transforma em uma string com nome 'line'
    for(string line;getline(input,line);){
        texto_lido += line;
        cout << texto_lido;
    }
    arquivo_saida.close();

    //para limpar o arquivo
    arquivo_saida.open("teste.txt");
    arquivo_saida << "";
    arquivo_saida.close();
    return 0;
}
