# 02 - Conversor de Temperatura

## 📄 Arquivo: `temperatura.py`

Script que recebe uma temperatura em **Celsius**, converte para **Fahrenheit** e exibe o resultado formatado. Também trata o caso em que o usuário digita letras em vez de números, evitando que o programa quebre.

### Explicação Linha por Linha:

```python
def converter_celsius_para_fahrenheit():
```
Define a função responsável por toda a lógica de conversão.

```python
    print("--- Conversor de Celsius para Fahrenheit ---")
```
Exibe um cabeçalho para o usuário saber em qual programa está.

```python
    try:
```
Inicia um bloco de tentativa. O Python vai executar o código dentro dele e, se acontecer algum erro, desvia para o `except`.

```python
        celsius = float(input("Digite a temperatura em graus Celsius: "))
```
Pede um número ao usuário com `input()`. Como o `input()` sempre retorna texto, o `float()` converte esse texto para número decimal (ex: `25.5`), salvando o resultado na variável `celsius`.

```python
        fahrenheit = (celsius * 9/5) + 32
```
Aplica a fórmula matemática de conversão `(°C × 9/5) + 32` e guarda o resultado em `fahrenheit`.

```python
        print(f"\nResultado: {celsius:.1f}°C equivalem a {fahrenheit:.1f}°F")
```
Exibe o resultado. O `\n` pula uma linha antes, e o `:.1f` limita a exibição a uma casa decimal (evitando números como `25.3333333°C`).

```python
    except ValueError:
```
Se o usuário digitar algo que não seja um número (ex: "Pato"), o `float()` vai gerar um erro do tipo `ValueError`. O `except` captura esse erro e evita que o programa trave.

```python
        print("\nErro: Por favor, digite um número válido (ex: 25 ou 25.5).")
```
Avisa o usuário sobre o erro e mostra como ele deve digitar corretamente.

```python
if __name__ == "__main__":
    converter_celsius_para_fahrenheit()
```
Garante que a função só seja executada quando o arquivo for rodado diretamente pelo terminal.
