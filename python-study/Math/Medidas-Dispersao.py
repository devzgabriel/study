
def most_frequent(List):
  curr_frequency = 0
  for i in range(0, len(List)):
    frequency = 1
    for j in range(i+1, len(List)):    
      if(List[i] == List[j]):    
        frequency = frequency + 1
    if(frequency > curr_frequency):
          curr_frequency = frequency
          num = i 

  return num


dados_agrupados = [ 149, 163, 151, 135, 137, 167, 95, 119, 147, 153, 127, 90, 202, 172, 148, 154, 149, 158, 82, 206, 123, 144, 109, 167, 157, 141, 150, 130, 187, 139, 183, 114, 191, 129, 149, 158, 108, 178, 102, 197, 165, 168, 171, 116, 111, 213, 128, 166, 185, 175 ]
qtd_total_grupo = len(dados_agrupados)
print(qtd_total_grupo)
#tendência central

#media
soma_media = 0
for n in dados_agrupados:
  soma_media += n
media = soma_media / qtd_total_grupo

#moda
moda = most_frequent(dados_agrupados)

#mediana
dados_agrupados_ordenados = sorted(dados_agrupados)
print(dados_agrupados_ordenados)
'''if qtd_total_grupo % 2 == 0:
  mediana = (dados_agrupados_ordenados[(qtd_total_grupo/2)-1] + dados_agrupados_ordenados[int(qtd_total_grupo/2)]) / 2
else:
  mediana = dados_agrupados_ordenados[int(qtd_total_grupo/2)]'''

print('Média Aritimética: ', media)
print('Moda: ', moda)
#print('Mediana: ', mediana)


#medidas de dispersão
somatoria = 0
for n in dados_agrupados:
  denominador = (n - media)**2
  somatoria += denominador
variancia = somatoria / (qtd_total_grupo-1)
print(somatoria)

print('Variância: ', variancia)
print('Desvio padrão: ', variancia**(1/2))


