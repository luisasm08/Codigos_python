def voto(ano):
    idade = 2022 - ano
    if idade >= 18:
        print(f'Com {idade} anos: VOTO OBRIGATÓRIO')
    elif idade >= 16 and idade < 18:
        print(f'Com {idade} anos: VOTO OPCIONAL')
    elif idade < 16:
        print(f'Com {idade} anos: VOTO NEGADO')


n = int(input('Em que ano você nasceu? '))
voto(n)
