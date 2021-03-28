n = int(input('Digite o valor de n: '))
fn= 1
if n==0:
  print(1)
else:
  while n> 1:
    fn *= n
    n-=1
  print(fn)
