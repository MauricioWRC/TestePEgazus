import requests

resposta = requests.get("https://jsonplaceholder.typicode.com/users").json()

for user in resposta:
    remover = ['name', 'username','email'] #lista de item a serem removidos
    remover2 = ["suite", 'street']# Lista de itens a serem removidos
    endereco = user['address']
    for i in remover2: #Deleta o item que estiver na lista
        del endereco[i]
    for chave in remover: #Deleta o item que estiver na lista
        del user[chave]
print(resposta)
#Escolhi essa forma pois está dentro do meu conhecimento em json() e dicionarios.