i = input().split()
A = float(i[0])
B = float(i[1])
C = float(i[2])
D = float(i[3])
media = (A * 2 + B * 3 + C * 4 + D * 1) / 10
print("Media: {:.1f}".format(media))
if media >= 7.0:
    print("Aluno aprovado.")
elif media < 5.0:
    print('Aluno reprovado.')
elif 5 <= media < 7.0:
    print('Aluno em exame.')
    ex = float(input())
    print("Nota do exame: {:.1f}".format(ex))
    n_m = (media + ex) / 2
    if n_m >= 5.0:
        print("Aluno aprovado.")
    else:
        print('Aluno reprovado.')
    print("Media final: {:.1f}".format(n_m))
