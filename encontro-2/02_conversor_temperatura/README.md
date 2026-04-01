# 02 - Conversor de Temperatura

## 📄 Arquivo: `temperatura.py`

Este programa intercepta a entrada de uma temperatura em graus **Celsius**, calcula sua equivalência para **Fahrenheit** e imprime o resultado. Além disso, detecta se o usuário digitou letras por engano, evitando que o programa feche abruptamente com um erro (crash).

### Explicação Linha por Linha:

```python
def converter_celsius_para_fahrenheit():
```
Declara-se a função encarregada de realizar a nossa tarefa desde o início até o fim da conversão.

```python
    print("--- Conversor de Celsius para Fahrenheit ---")
```
Exibe de forma decorativa para o usuário em qual ferramenta ele acaba de entrar.

```python
    try:
```
Indica ao Python para *tentar* executar os blocos seguintes e ficar alerta a qualquer tipo de quebra (erro de digitação, por exemplo).

```python
        celsius = float(input("Digite a temperatura em graus Celsius: "))
```
Pede ao usuário um número através do `input()`. Como o input normalmente devolve um texto (string), ele é envolvido em `float(...)` para converter esse valor no formato de "ponto flutuante" (números decimais como 25.5), guardando tudo na variável `celsius`.

```python
        fahrenheit = (celsius * 9/5) + 32
```
Aplica a clássica fórmula matemática de conversão: `(°C × 9/5) + 32`. Guarda o resultado líquido na nova variável `fahrenheit`.

```python
        print(f"\\nResultado: {celsius:.1f}°C equivalem a {fahrenheit:.1f}°F")
```
Imprime um salto de linha `\n` seguido do texto final com uma formatação chamada `:.1f` — Isso limita o número de casas decimais a um único dígito (para evitar coisas como `25.333333333°C`).

```python
    except ValueError:
```
Se ocorrer uma falha dentro do bloco `try:` (digamos que o usuário digitou 'Pato' em vez de entrar com números, o `float()` iria rejeitar e provocar um erro do tipo `ValueError`), o programa desviará seu percurso imediatamente para cá.

```python
        print("\\nErro: Por favor, digite um número válido (ex: 25 ou 25.5).")
```
Avisa o usuário que houve um erro e informa suavemente para que tente com as regras certas, evitando assim a falha do sistema.

```python
if __name__ == "__main__":
    converter_celsius_para_fahrenheit()
```
Finaliza verificando a execução do arquivo principal pelo terminal, disparando a função de conversão caso seja verdade.
