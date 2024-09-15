lista = ["joao", "ana", "joana","joao", "ricardo", "joao"]
id = len(lista) #Faz a contagem de itens na lista
for nome in range(id): #Verifica cada item
    if lista[nome] == 'joao':
        lista[nome] = 'maria'
        #se for joao vira maria
print(lista)
