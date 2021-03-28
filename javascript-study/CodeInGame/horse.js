/*

import math


forcas=[]
n = int(input())

for i in range(n):
    pi = int(input())
    forcas.append(pi)

forcas.sort()
menor_d=forcas[0]
for i in range(len(forcas)-1):
    d=forcas[i+1] - forcas[i]
    if d < menor_d:
        menor_d = d
print(menor_d)


*/

forcas = [];

const N = parseInt(readline());

for (let i = 0; i < N; i++) {
  const pi = parseInt(readline());
  forcas.push(pi);
}

forcas.sort((a, b) => {a-b});
menorDistancia = forcas[forcas.length -1];

for (let i = 0; i < forcas.length -1; i++) {
  const distancia = forcas[i+1] - forcas[i];
  if(distancia < menorDistancia){
    menorDistancia = distancia
  }
}

console.log(menorDistancia);
