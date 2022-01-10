num = []
while True:
    n = (int(input('Digite um valor: ')))
    if n not in num:
        num.append(n)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado! Não vou adicionar...')
    resp = str(input('Deseja continuar? [s/n] ')).strip().lower()
    if resp == 'n':
        break
print('------------------------------------------')
print(f'Você digitou os valores: {num.sort()}')

