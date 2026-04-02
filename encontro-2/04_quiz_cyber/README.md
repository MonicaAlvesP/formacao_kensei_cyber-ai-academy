# 04 - Quiz de Cibersegurança

## 📄 Arquivo: `quiz_cyber.py`

Jogo de quiz no terminal com 5 perguntas de múltipla escolha sobre cibersegurança. As perguntas e respostas são armazenadas em dicionários Python, e ao final o programa exibe a pontuação e informa se o usuário foi aprovado.

### Explicação Linha por Linha:

```python
    perguntas = [
        {
            "pergunta": "O que é Phishing?",
            "opcoes": [ ... ],
            "resposta_correta": "B"
        },
```
Define a base de dados do quiz. É uma lista `[]` onde cada elemento é um dicionário `{}`. Cada dicionário representa uma pergunta e guarda três informações: o texto da pergunta (`"pergunta"`), as opções de resposta (`"opcoes"`) e qual é a resposta certa (`"resposta_correta"`).

```python
    pontuacao = 0
    total_perguntas = len(perguntas)
```
Inicializa o contador de pontos em zero. O `len()` conta o número de itens na lista de perguntas e guarda esse valor em `total_perguntas`.

```python
    print("="*45)
```
Imprime 45 caracteres `=` em sequência, criando um separador visual no terminal.

```python
    for i, p in enumerate(perguntas, start=1):
```
Percorre todas as perguntas da lista. O `enumerate()` fornece o número da pergunta (`i`) e o dicionário da pergunta (`p`) a cada iteração. O `start=1` faz a contagem começar em 1.

```python
        print(f"Pergunta {i}: {p['pergunta']}")
        for opcao in p['opcoes']:
            print(f"  {opcao}")
```
Exibe o número e o texto da pergunta atual acessando `p['pergunta']`. Em seguida, um segundo `for` percorre e exibe cada opção de resposta armazenada em `p['opcoes']`.

```python
        while True:
            resposta = input("Sua resposta: ").strip().upper()
            if resposta in ['A', 'B', 'C']:
                break
```
Mantém o usuário em um loop até que ele digite uma resposta válida (`A`, `B` ou `C`). O `.strip()` remove espaços acidentais e o `.upper()` converte para maiúsculas, evitando erros caso o usuário digite `a` em vez de `A`.

```python
        if resposta == p['resposta_correta']:
```
Compara a resposta digitada com a resposta correta guardada no dicionário em `p['resposta_correta']`.

```python
            pontuacao += 1
```
Se a resposta estiver certa, adiciona 1 ponto ao contador. O `+=` é um atalho para `pontuacao = pontuacao + 1`.

```python
    if pontuacao >= 3:
```
Após todas as perguntas, verifica se o usuário acertou 3 ou mais. Se sim, exibe uma mensagem de aprovação. Caso contrário, o `else` exibe uma mensagem incentivando uma nova tentativa.
