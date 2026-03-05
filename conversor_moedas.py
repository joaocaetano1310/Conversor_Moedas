# Conversor de moedas

import time
import os
import requests

def pegar_cotacao(par):
    url = f"https://economia.awesomeapi.com.br/json/last/{par}"
    resposta = requests.get(url)
    dados = resposta.json()

    chave = par.replace("-", "")
    valor = float(dados[chave]["bid"])

    return valor

def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")

def conversor():

    print("🪙 CONVERSOR DE MOEDAS 🪙")

    par = input("Digite o par de moedas (ex: USD-BRL): ").upper()
    valor = float(input("Digite o valor que deseja converter: "))

    cotacao_anterior = 0

    while True:

        cotacao = pegar_cotacao(par)
        convertido = valor * cotacao

        if cotacao > cotacao_anterior:
            status = "↑"
        elif cotacao < cotacao_anterior:
            status = "↓"
        else:
            status = "-"

        cotacao_anterior = cotacao

        limpar_tela()

        print("=== CONVERSOR DE MOEDAS ===\n")
        print(f"Par de moedas: {par}")
        print(f"Valor digitado: {valor}")
        print(f"Cotação atual: {cotacao} {status}")
        print(f"Valor convertido: {round(convertido,2)}")

        time.sleep(30)


conversor()