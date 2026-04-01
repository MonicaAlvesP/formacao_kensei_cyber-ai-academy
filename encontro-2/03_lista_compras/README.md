# 03 - Lista de Tarefas e Compras

## 📄 Arquivo: `lista_compras.py`

Criação de listas dinâmicas, utilizando o laço de repetição infinito enquanto nos mantemos dentro de um painel interativo de opções de controle.

### Explicação Linha por Linha:

```python
def gerenciar_lista_compras():
```
Contêiner global de controle de execução da nossa lista de compras.

```python
    lista = []
```
Inicializa uma estrutura de dados do tipo `list` que parte vazia de fábrica `[]`. Nesta variável guardaremos todos os itens que o usuário for escrevendo.

```python
    while True:
```
Isso diz ao Python: "Fique repetindo o bloco de código abaixo para sempre", até que encontre um ponto exato onde indiquemos a palavra `break` para romper esse looping contínuo.

```python
        print("\\n--- Lista de Compras ---")
        print("1. Adicionar item")
        ...
        opcao = input("\\nEscolha uma opção (1-4): ")
```
Painel genérico visual para guiar comandos. Depois de listados na tela, o processamento para e aguarda o comprador digitar e escolher alguma das opções oferecidas, caindo o valor escolhido na variável `opcao`.

```python
        if opcao == '1':
            item = input("Digite o nome do item a ser adicionado: ")
            lista.append(item)
            print(f"-> '{item}' foi adicionado com sucesso!")
```
Se digitou '1'. O programa requer o nome do objeto ao usuário e aplica o método mágico `.append(elemento)` direto na `lista`. Esse simples comando insere no final de todas as prateleiras o novo elemento que foi digitado de uma vez só!
    
```python
        elif opcao == '2':
            if not lista: ...
            else:
                for i, item in enumerate(lista, start=1):
                    print(f"{i}. {item}")
```
Se escolheu '2'. Usando a forma condicional `if not`, revisamos que a lista realmente não esteja vazia antes de tentar exibir o nada. Se estiver com um ou mais elementos (`else`), um laço `for` varre o objeto com a ajuda de uma ferramenta chamada `enumerate()`. Com isso, enumeramos os novos elementos do 1 adiante (através do `start=1`). Isso resulta em legibilidades de leitura excelentes (1. Arroz, 2. Feijão, etc).

```python
        elif opcao == '3':
            # ... verificações e listagem aqui também ...
                try:
                    indice = int(input("...")) - 1
```
Se escolheu '3'. Após rechecos de vazios e numeração impressa na tela, requeremos a pessoa que digite o número índice a apagar. Convertendo essa seleção textual numa integer `int()` y diminuindo um valor (`-1`). Por que subtraímos um valor? Simples, porque os arrays internos nas memórias no caso de Python listam casinhas numeradas com o zero inicial [0, 1, 2] e não igual aos humanos naturais que cuentan con o dedo pulgar arrancando do 1.

```python
                    if 0 <= indice < len(lista):
                        item_removido = lista.pop(indice)
                        print(f"-> '{item_removido}' ...")
```
Revisamos que o novo cálculo negativo não esvazie el zero (`<0`), ni tampoco exceda posicionalmente al tamaño global real comprobando através da função `len(lista)`. Ao dar correto, pegaremos e erradicará o item do prato através do exato comando `.pop(A posição procurada real interna)`.

```python
                    else:
                        print("-> Erro: Número de item inválido.")
                except ValueError:
                    print("-> Erro: Por favor, digite apenas números...")
```
Tanto se ingressar letras pelo teclado e cair num problema `except ValueError`, como não caber os limites numéricos condicionalmente no `else`, evitamos o erro catastrófico (o crasheo subto) e cuspe via print a reclamação de refazer com melhores premissas. Tudo recomeçando sem drama porque ainda nos encontramos reclusos sob no painel condicional base "while True".

```python
        elif opcao == '4':
            break
```
A única escapatória programada oficialmente do aplicativo. O Break força el desarmamento do `while True` global dictado ao principal, abrindo a porta para espirar naturalmente à conclusão do Main e da memória residual de Python soltada.
