def contagem(url):
    import requests

    requisição = requests.get(url)#Requisição
    resposta = requisição.json()#Transformando em leitura py
    completas = 0
    incompletas = 0
    for i in resposta:
        if i['completed'] == True: #Sempre que estiver completed ele le mais 1 no contador
            completas += 1
        else:#Se não estiver completed ele le mais 1 no contador incompleta
            incompletas +=1
    print(f"Temos {completas} tasks completas")
    print(f"Temos {incompletas} tasks pendentes")

contagem("https://jsonplaceholder.typicode.com/todos")

#Foi a forma mais limpa que pensei