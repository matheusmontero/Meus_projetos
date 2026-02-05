Este projeto é um **simulador simples de caixa eletrônico** feito em Python, executado no terminal.
Ele permite ao usuário consultar saldo, realizar depósitos, efetuar saques e encerrar o programa por meio de um menu interativo.
* ✅ Definir saldo inicial
* 💰 Consultar saldo atual
* ➕ Realizar depósitos
* ➖ Efetuar saques com verificação de saldo
* ❌ Encerrar o programa com segurança
* ⚠️ Validação básica de opções e valores

* **Python 3**
* Execução via **terminal / console**
1. Certifique-se de ter o Python 3 instalado:

   ```bash
   python --version
   ```

2. Salve o código em um arquivo, por exemplo:

   ```bash
   caixa_eletronico.py
   ```

3. Execute no terminal:

   ```bash
   python caixa_eletronico.py
   ```
Ao iniciar o programa:

1. O usuário informa um **saldo inicial**
2. Um menu é exibido com as opções:

   ```
   1 - Ver saldo
   2 - Depositar
   3 - Fazer saque
   4 - Sair
   ```
3. O sistema permanece em execução até que a opção **4 - Sair** seja escolhida

* Depósitos só são aceitos com valores **positivos**
* Saques só podem ser realizados se houver **saldo suficiente**
* Opções inválidas são tratadas com mensagem de erro

```text
==================== CAIXA ELETRÔNICO ====================
Diga um saldo para começarmos: 100
Saldo inicial de R$100.00
1 - Ver saldo | 2 - Depositar | 3 - Fazer saque | 4 - Sair
Escolha uma opção: 1
Seu saldo é de R$100.00
```

* 🔐 Implementar senha de acesso
* 📄 Histórico de transações
* 🧮 Limite diário de saque
* 🖥️ Interface gráfica (GUI)

Projeto desenvolvido para fins **educacionais**, ideal para treinar:

* Estruturas condicionais
* Laços de repetição
* Entrada e saída de dados em Python
