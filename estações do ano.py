#- Criar um sistema de informação que receba o dia e o mês deste ano de 2023 e seja capaz de informar a estação do ano.

print("diga um dia e um mês e eu irei falar em que estaçaõ está")


dia = int(input('dia: '))
mes = int(input('mês: '))

def estaçaodoano(dia, mes):
    if mes in (1, 2):
        return 'Verão'
    elif mes == 3:
        if dia < 20:
            return 'Verão'
        else:
            return 'Outono'
    elif mes in (4, 5):
        return 'Outono'
    elif mes == 6:
        if dia < 21:
            return 'Outono'
        else:
            return 'Inverno'
    elif mes in (7, 8):
        return 'Inverno'
    elif mes == 9:
        if dia < 23:
            return 'Inverno'
        else:
            return 'Primavera'
    elif mes in (10, 11):
        return 'Primavera'
    elif mes == 12:
        if dia < 22:
            return 'Primavera'
        else:
            return 'Verão'

resultado = estaçaodoano(dia, mes)
print(resultado)