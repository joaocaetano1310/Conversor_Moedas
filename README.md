# 🪙 Conversor de Moedas em Tempo Real

Este é um script Python desenvolvido para monitorar e converter cotações de moedas em tempo real, utilizando a interface de linha de comando (CLI). Ele consome dados da **AwesomeAPI** para garantir informações atualizadas.

---

## 🚀 Funcionalidades

* **Consulta Dinâmica**: Permite buscar qualquer par de moedas suportado pela API (ex: USD-BRL, BTC-USD, EUR-BRL).
* **Atualização Automática**: O sistema atualiza a cotação e o valor convertido a cada 30 segundos.
* **Indicadores de Tendência**: Exibe visualmente se a moeda subiu (`↑`), desceu (`↓`) ou se manteve estável (`-`) em comparação com a última leitura.
* **Interface Limpa**: Utiliza comandos do sistema para limpar o terminal a cada ciclo, mantendo apenas as informações relevantes na tela.

---

## 🛠️ Pré-requisitos

Para rodar este projeto, você precisará ter o **Python 3** instalado e a biblioteca `requests`.

Instale a dependência necessária via terminal:
```bash
pip install requests
