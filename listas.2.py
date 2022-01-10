num = []
while True:
    num.append(int(input('Digite um valor: ')))
    resp = str(input('Deseja continuar? [s/n]')).strip().lower()
    if resp in 'Nn':
        break
print(f'Foram colocados na lista {len(num)} números.')
if 5 in num:
    print(f'O número 5 foi digitado na posição {num.index(5)}.')
else:
    print('O número 5 não foi digitado.')
print('A lista em ordem decrescente é: ', end='')
num.sort(reverse=True)
print(num)
