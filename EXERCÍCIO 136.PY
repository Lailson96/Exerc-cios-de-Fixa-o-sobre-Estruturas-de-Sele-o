NOME= str(input('\nEntre com o Nome: '))
IDADE= int(input('\nEntre com a idade: '))

if IDADE<=10:
    print(f'\n{NOME} pagara: R$ 30.00 ')
elif IDADE<=29:
    print(f'\n{NOME} pagara: R$ 60.00 ')
elif IDADE<=45:
    print(f'\n{NOME} pagara: R$ 120.00 ')
elif IDADE<=59:
    print(f'\n{NOME} pagara: R$ 150.00 ')
elif IDADE<=65:
    print(f'\n{NOME} pagara: R$ 250.00 ')
else:
    print(f'\n{NOME} pagara: R$ 400.00 ')
print('\n')
