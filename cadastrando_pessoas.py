galera = []
dados = []
maior = menor = 0
while True:
    dados.append(str(input('Digite seu nome: ')))
    dados.append(float(input('Digite seu peso: ')))
    if len(galera) == 0:
        menor = maior = dados[1]
    else:
        if dados[1] < menor:
            menor = dados[1]
        if dados[1] > maior:
            maior = dados[1]
    galera.append(dados[:])
    dados.clear()
    resp = str(input('Deseja continuar? [s/n]'))
    if resp in 'Nn':
        break
print(f'Foram cadastradas {len(galera)} pessoas.')
print(f'Maior peso foi de {maior:.2f}kg. Peso de ', end='')
for p in galera:
    if p[1] == maior:
        print(f'[{p[0]}]', end='')
print(f'\nMenor peso foi de {menor:.2f}kg. Peso de ', end='')
for p in galera:
    if p[1] == menor:
        print(f'[{p[0]}] ', end='')
