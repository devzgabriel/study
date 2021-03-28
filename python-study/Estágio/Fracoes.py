n=int(input())

for k in range(1, n+1):
    y = n + k
    x = n * (n + k) / k
    if x >= y and (x % n == 0 or x % 2 == 0):
        print(f'1/{n} = 1/{int(x)} + 1/{int(y)}')
