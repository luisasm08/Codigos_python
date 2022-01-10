salario = float(input('Qual o salário de contribuição? '))
if salario <= 1045.00:
    desc = 0.075 * salario
elif salario > 1045.00 and salario <= 2089.60:
    desc = ((salario - 1045) * 0.09) + (1045 * 0.075)
elif salario > 2089.60 and salario <= 3134.40:
    t = salario - 2089.60
    desc = (t * 0.12) + ((2089.60 - 1045) * 0.09) + (1045 * 0.075)
elif salario > 3134.40 and salario <= 6101.06:
    t = salario - 3134.40
    desc = (t * 0.14) + ((3134.40 - 2089.60) * 0.12) + ((2089.60 - 1045) * 0.09) + (1045 * 0.075)
elif salario > 6101.06:
    desc = ((6101.06 - 3134.40) * 0.14) + ((3134.40 - 2089.60) * 0.12) + ((2089.60 - 1045) * 0.09) + (1045 * 0.075)
print(f'O desconto sobre o salário de {salario} é {desc:.2f}.')


