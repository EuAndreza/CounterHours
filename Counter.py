#imports
from datetime import datetime
dataAtual = datetime.now().strftime('%d/%m/%y %H:%M')
#dataHora = dataAtual.strftime('%d/%m/%y %H:%M')
print(dataAtual)

#adicionar em um arquivo de texto
def adicionar(h, m, dataAtual):  
    with open('dados.txt', 'a') as arquivo:
        arquivo.write(dataAtual)
        arquivo.write(' Quantidade de horas: ')
        arquivo.write(str(h))
        arquivo.write(' Quantidade de Minutos: ')
        arquivo.write(str(m))
        arquivo.write('\n')
        arquivo.close()

h = int(input("digite a hora"))
m = int(input("digite os minutos"))

adicionar(h, m, dataAtual)

conver = h * 60
calcConver = m + conver
calcMin = calcConver % 60
calcHr = calcConver // 60
totalMin = calcMin
totalHr = calcHr


p = input("deseja colocar mais horas?")
c = 0

while(p == "sim"):
    h = int(input("digite a hora"))
    m = int(input("digite os minutos"))
    conver = h * 60
    calcConver = m + conver
    calcMin = calcConver % 60
    calcHr = calcConver // 60
    totalMin = totalMin + calcMin
    totalHr = totalHr + calcHr
    if totalMin >= 60:
        totalHr +=1
        totalMin -=60
    adicionar(h, m, dataAtual)
    
    p = input("deseja colocar mais horas?")
c +=1

print("O total de horas é : ", totalHr, "\nO total de minutos é: " , totalMin)
input("Pressione <enter> para sair")
