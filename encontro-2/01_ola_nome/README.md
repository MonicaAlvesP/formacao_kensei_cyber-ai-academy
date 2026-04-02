# 01 - Olá Mundo (com Nome)

## 📄 Arquivo: `main.py`

Script simples que pede o nome do usuário e imprime uma saudação com o nome em letras maiúsculas.

### Explicação Linha por Linha:

```python
def main():
```
Define a função principal do programa. Usar uma função `main()` é uma boa prática para organizar o código.

```python
    nome = input("Qual é o seu nome? ")
```
Exibe uma mensagem na tela e aguarda o usuário digitar algo. O valor digitado fica salvo na variável `nome`.

```python
    print(f"Olá, {nome.upper()}!")
```
Imprime a saudação. O `f"..."` é uma f-string, que permite inserir variáveis diretamente no texto usando `{}`. O método `.upper()` converte o nome para letras maiúsculas antes de exibir.

```python
if __name__ == "__main__":
    main()
```
Essa é uma convenção padrão do Python. Ela garante que a função `main()` só será chamada quando o arquivo for executado diretamente pelo terminal, e não quando for importado por outro script.
