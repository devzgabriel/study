#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct data{
    int dia;
    int mes;
    int ano;
}data;

struct aluno{
    int ip;
    data nascimento;
};
int main () {
    struct aluno Gabriel;

    Gabriel.ip = 1339;
    Gabriel.nascimento.ano = 2003;
    Gabriel.nascimento.mes = 1;
    Gabriel.nascimento.dia = 13;
    printf("O aluno %d nasceu em %d/%d/%d",Gabriel.ip,Gabriel.nascimento.dia,Gabriel.nascimento.mes,Gabriel.nascimento.ano);
    return 0;
}
