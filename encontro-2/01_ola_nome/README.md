# 01 - Olá Mundo (com Nome)

## 📄 Arquivo: `main.py`

Este script é muito simples. Seu objetivo é perguntar o nome do usuário e depois saudá-lo, imprimindo seu nome todo em letras maiúsculas.

### Explicação Linha por Linha:

```python
def main():
```
Define a função principal, chamada `main()`. Isso serve para organizar melhor o nosso código, em vez de deixar instruções soltas por todo o arquivo.

```python
    nome = input("Qual é o seu nome? ")
```
Usamos a função `input()` para mostrar uma mensagem na tela e esperar que a pessoa digite algo. Tudo o que for digitado será guardado na nossa variável chamada `nome`.

```python
    print(f"Olá, {nome.upper()}!")
```
Usamos a função `print()`. Ao colocar um `f` no início (`f"..."`), indicamos ao Python que injetaremos variáveis reais dentro do texto usando as chaves `{}`.
O comando `.upper()` transforma o texto que havia em `nome` para letras puramente MAIÚSCULAS antes de imprimir a saudação final.

```python
if __name__ == "__main__":
    main()
```
Esta é a convenção básica do Python. Ela avalia se este arquivo está sendo executado de forma principal (por exemplo, a partir do terminal). Se for o caso, manda executar as instruções que preparamos na função `main()`.
