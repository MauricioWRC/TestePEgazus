lista = ["   joao   ","   maria   ","  joana  "]
lista2=[]
for item in lista:
    item = item.strip() #Tirando os espaços no inicio e fim
    lista2.append(item) #Integrando na lista 2
print(lista2)
#Forma mais simples e utilizando funções pre definidas no python