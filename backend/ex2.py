responsejson = {
    "nome": "Loja Exemplo",
    "endereço": {
        "rua": "Rua Exemplo",
        "cidade": "Exemplo City"
    },
    "produtos": [
        {"id": 1, "nome": "Produto A", "preço": 29.99},
        {"id": 2, "nome": "Produto B", "preço": 19.99}
    ]
}
def produto_B(json): #Novamente em Def
    produto = responsejson['produtos'] #Escolhendo apenas os produtos
    for produtoB in produto: #Entrando na lista
        for nome in produtoB.values(): #Verificando cada valor dos dicionarios
            if nome == 'Produto B': #Se algum tiver o valor de "Produto B"
                return(produtoB) #Retornando o protudo onde encontra o Produto B
print(produto_B(responsejson))
#Escolhi essa forma pois ela verificar item por item do responsejson.