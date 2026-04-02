# 03 - Lista de Compras

## 📄 Arquivo: `lista_compras.py`

Programa interativo de gerenciamento de lista de compras. O usuário pode adicionar, visualizar e remover itens através de um menu, usando um loop `while` para manter o programa rodando até que ele escolha sair.

### Explicação Linha por Linha:

```python
def gerenciar_lista_compras():
```
Define a função principal que engloba toda a lógica do programa.

```python
    lista = []
```
Cria uma lista vazia `[]` para armazenar os itens que o usuário for adicionando ao longo do programa.

```python
    while True:
```
Inicia um loop infinito. O programa vai continuar exibindo o menu repetidamente até encontrar um `break`, que força a saída do loop.

```python
        print("\n--- Lista de Compras ---")
        print("1. Adicionar item")
        ...
        opcao = input("\nEscolha uma opção (1-4): ")
```
Exibe o menu de opções na tela e aguarda o usuário digitar uma escolha, que fica salva na variável `opcao`.

```python
        if opcao == '1':
            item = input("Digite o nome do item a ser adicionado: ")
            lista.append(item)
            print(f"-> '{item}' foi adicionado com sucesso!")
```
Se o usuário escolheu `'1'`, pede o nome do item e usa `.append()` para adicioná-lo ao final da lista.

```python
        elif opcao == '2':
            if not lista: ...
            else:
                for i, item in enumerate(lista, start=1):
                    print(f"{i}. {item}")
```
Se o usuário escolheu `'2'`, verifica primeiro se a lista está vazia com `if not lista`. Se houver itens, o `for` percorre a lista usando `enumerate()`, que fornece o índice e o valor de cada item. O `start=1` faz a numeração começar em 1 (e não em 0), tornando a exibição mais intuitiva (1. Arroz, 2. Feijão, etc.).

```python
        elif opcao == '3':
            # ... verificações e listagem aqui também ...
                try:
                    indice = int(input("...")) - 1
```
Se o usuário escolheu `'3'`, após exibir os itens numerados, pede que ele escolha qual remover. O número digitado é convertido para inteiro com `int()` e subtraímos 1 (`-1`) porque as listas em Python começam no índice 0, enquanto a numeração exibida ao usuário começa em 1.

```python
                    if 0 <= indice < len(lista):
                        item_removido = lista.pop(indice)
                        print(f"-> '{item_removido}' ...")
```
Verifica se o índice calculado está dentro dos limites válidos da lista usando `len(lista)`. Se estiver, `.pop()` remove e retorna o item naquela posição.

```python
                    else:
                        print("-> Erro: Número de item inválido.")
                except ValueError:
                    print("-> Erro: Por favor, digite apenas números...")
```
Cobre dois casos de erro: se o usuário digitar letras (gerando um `ValueError` no `int()`), e se digitar um número fora do intervalo válido (caindo no `else`). Em ambos os casos, o programa exibe um aviso e volta ao menu normalmente, sem travar.

```python
        elif opcao == '4':
            break
```
A única saída do programa. O `break` interrompe o `while True`, e o programa encerra normalmente.
