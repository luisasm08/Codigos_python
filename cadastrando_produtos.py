tot = t = menor = c = 0
while True:
    c = c + 1
    nome=str(input('Qual é o nome do produto? '))
    preco=float(input('Qual é o preço do produto? '))
    if c == 1:
        menor = preco
    if preco<menor:
        menor=preco
        n=nome
    if preco>1000:
        t=t+1
    tot=tot+preco
    resp=str(input('Quer continuar? [sim/nao] '))
    if resp == 'nao':
        break
print(f'O nome do produto mais barato é {n}\nO total gasto é {tot:.2f}\nO número de produtos que custam mais de 1000 é {t}.')