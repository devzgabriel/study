/*import math

t = 0
c = 0
n = int(input())
lista=input().split()
while c < n:
    if c == 0:
        t = int(lista[c])
    elif abs(int(lista[c])) < abs(t):
        t = int(lista[c])
    elif abs(int(lista[c])) == abs(t):
        if int(lista[c]) >= t:
            t = int(lista[c])
    c += 1
print(t)*/


const n = parseInt(readline()); // the number of temperatures to analyse
var inputs = readline().split(' ');

let result = 0;

for (let i = 0; i < n; i++) {
  const t = parseInt(inputs[i]);
  if(i==0){
    result = Number(t);
  }else if(Math.abs(Number(t)) < Math.abs(result)){
    result = Number(t);
  }else if(Math.abs(Number(t)) == Math.abs(result)){
    if(Number(t) > result){
      result = Number(t);
    }
  }
}

console.log(result);
