# 05 - Gerador de Senhas

## 📄 Arquivo: `gerador_senhas.py`

Script que gera senhas seguras e personalizadas. O usuário escolhe o tamanho da senha e se quer incluir letras maiúsculas, números e símbolos. O programa usa as bibliotecas nativas `random` e `string` do Python para montar a senha.

### Explicação Linha por Linha:

```python
import random
import string
```
Importa duas bibliotecas nativas do Python. `random` é usada para fazer escolhas aleatórias, e `string` fornece conjuntos de caracteres prontos (letras, números, símbolos), sem precisar digitá-los manualmente.

```python
def gerar_senha():
```
Define a função principal que contém toda a lógica do gerador de senhas.

```python
    try:
        tamanho = int(input("Qual o tamanho da senha desejada? (ex: 12): "))
        if tamanho < 1:
            print("Tamanho inválido. Ajustando para 8 caracteres.")
            tamanho = 8
    except ValueError:
        print("Valor inválido. Usando o tamanho padrão de 12 caracteres.")
        tamanho = 12
```
Pede o tamanho da senha ao usuário e converte a resposta para inteiro com `int()`. Se o usuário digitar letras em vez de números, o `int()` gera um `ValueError`, que é capturado pelo `except` — e o programa usa 12 como valor padrão. Se o número for menor que 1, ajusta automaticamente para 8.

```python
    incluir_maiusculas = input("Incluir letras maiúsculas? (S/N): ").strip().upper() == 'S'
```
Pergunta ao usuário se quer incluir maiúsculas. O `.strip()` remove espaços extras, o `.upper()` converte para maiúscula, e a comparação `== 'S'` retorna `True` ou `False` — esse resultado fica salvo na variável `incluir_maiusculas`.

```python
    caracteres = list(string.ascii_lowercase)
    senha_obrigatoria = [random.choice(string.ascii_lowercase)]
```
Cria a lista base de caracteres disponíveis, começando pelas letras minúsculas (`string.ascii_lowercase`). Também garante que, desde o início, ao menos uma letra minúscula seja incluída na senha usando `random.choice()`.

```python
    if incluir_maiusculas:
        caracteres.extend(list(string.ascii_uppercase))
        senha_obrigatoria.append(random.choice(string.ascii_uppercase))
```
Se o usuário pediu maiúsculas, adiciona as letras maiúsculas ao pool de caracteres com `.extend()`, e garante que ao menos uma delas apareça na senha com `.append()`.

```python
    tamanho_restante = tamanho - len(senha_obrigatoria)
    for _ in range(tamanho_restante):
        senha_obrigatoria.append(random.choice(caracteres))
```
Calcula quantos caracteres ainda faltam para atingir o tamanho pedido (descontando os que já foram adicionados como obrigatórios). O `for` preenche o restante com caracteres escolhidos aleatoriamente do pool disponível.

```python
    random.shuffle(senha_obrigatoria)
    senha_final = "".join(senha_obrigatoria)
```
O `.shuffle()` embaralha a lista de caracteres para que os obrigatórios não fiquem sempre na mesma posição. O `.join()` une todos os caracteres da lista em uma única string, formando a senha final.

```python
    print(f"Sua senha gerada: {senha_final}")
```
Exibe a senha gerada para o usuário.
