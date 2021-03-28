pagamento = int(input('método de pagamento:\n à vista-1\n dividido-2'))
if pagamento == 1:
    vista = input('dinheiro ou cheque-1\n cartão-2')
    if vista == 1:
        print('10% de desconto')
    elif vista == 2:
        print('5% de desconto')
    else:
        print('valor não válido')
elif pagamento == 2:
    vezes = int(input('Quantas vezes? '))
    if vezes <= 2:
        print('sem mudança')
    else:
        print('20% de juros')
