funcaoCaracteres = []
palavra = ""
isMax = False
funcaoC = []
contadorN = 0
funcaoB = [[]]

with (open("funcao.txt", "r") as f):
    lista = f.readlines()
    for linhas in lista:
        for letras in list(linhas):
            if letras == ' ' :
                funcaoCaracteres.append(palavra)
                palavra = ''
            elif letras == '\n':
                funcaoCaracteres.append(palavra)
                funcaoCaracteres.append('\n')
                palavra = ''
            else:
                palavra += letras

    funcaoCaracteres.append(palavra)

print(funcaoCaracteres)
for elemento in funcaoCaracteres:
    if elemento == 'Max':
        isMax = True
    if elemento == '\n':
        contadorN += 1
    if elemento != '\n' and contadorN == 0:
        if elemento[0].isdigit():
            funcaoC.append(elemento[0])
    if elemento != '\n' and contadorN >= 1:
        if elemento[0].isdigit():
            funcaoB.append(elemento[0])

print(funcaoC)
print(funcaoB)
