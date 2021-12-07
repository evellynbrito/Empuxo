def empuxo():
    mo = float(input('Qual a massa do objeto? (em kg): '))
    vo = float(input('Qual o volume do objeto? (m^3): '))
    do = float(input('Qual a densidade do objeto? (kg/m^3): '))
    p = mo * 9.8
    e = do * vo * 9.8

    print('Valor do empuxo é igual a ', e)
    if p == e:
        print('O objeto está em repouso na superfície')
    elif p > e:
        print('O objeto afunda')
    elif p < e:
        print('O objeto flutua')

def ajuda():
    print('Inserira a massa em kg')
    print('Insira o volume do objeto m^3')
    print('Insira a densidade do objeto (kg/m^3)')
    print('Após inserir os valores e calcular o empuxo,'
          'o programa irá dizer se o objeto permanece em repouso, afunda, ou se o objeto irá flutuar')
