### funçao que soma 2 numeros diferentes, mas que tem um limite de 0 - 1000.               ###
### enquanto não for satisfeito o critério ros numeros 1 e 2, o código continua rodando    ###

def soma(a, b):
    conta = a + b
    answ = print(f"The result is: {conta}")
    return answ

aux = 0

while aux == 0:

    numA = int(input("Insert 1st num:   "))
    numB = int(input("Insert 2nd num:   "))

    if numA > 0 and numA < 1000:
        soma(numA, numB)
        aux += 1
    elif numB > 0 and numB < 1000:
        soma(numA, numB)
        aux += 1
    else:
        aux = 0
        print("Only accepted 0 - 1000")
