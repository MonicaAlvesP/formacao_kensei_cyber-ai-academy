# 05 - Gerador de Senhas

## 📄 Arquivo: `gerador_senhas.py`

Um script robusto que usa a biblioteca `random` e `string` do Python, para fabricar uma senha muito mais fortificada. Tudo re-apto em cima das opções do usuário: variando níveis, incluindo só números ou os símbolos difíceis misturados ao sabor do freguês.

### Explicação Linha por Linha:

```python
import random
import string
```
Trazemos (importamos) bibliotecas embutidíssimas nativas de fábrica. `random` fará da sorte para lançar suas engrenagens na mágica do azar randômico. E do lado irmão `string` traremos o conforto extra dos abecedários textuais já empacotados globalmente prontos ali mesmo, em vez da velha história de escrever manualmente teclinha com teclas inteiras de fato "a,b,c".

```python
def gerar_senha():
```
Estabelece a função central principal que alojará perante este arquivo a elaborada estrutura que desdobra todos os questionários dos mistérios propostos e da costura computacional interna.

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
Abertamente nós perguntamos da imensidão total requerida através do `input()`. Uma caçada matemática que pedimos de inteiros convertidos à força pra garantir pela blindagem que ninguém trapaceie textualmente de fora pra dentro causando a infame `ValueError` nos derrubando se fosse a limpo; salvando esse crasheo por resgatar em um pacote defensual de base 12 sem pestanejar caindo pra salvação alternativa programada.

```python
    incluir_maiusculas = input("Incluir letras maiúsculas? (S/N): ").strip().upper() == 'S'
```
Indagamos por níveis de sofisticações com questionamentos simplificados `(S ou N)`.
1. Fritamos purezas ou escapes digitados erroneamente (por desleixo) tirados fora do campo por um `.strip()`. 
2. Reduzimos ao escopo simplificado global convertendo ele em grande escala ao maiúsculo num varre final por `.upper()`.
3. Comparamos estrito pro avaliamento (`== 'S'`) em suma condensando e transmutando seu próprio resultado da validação final para sua matriz num puro verídico Booleano Real `True` ou então `False`.

```python
    caracteres = list(string.ascii_lowercase)
    senha_obrigatoria = [random.choice(string.ascii_lowercase)]
```
De cara base pegamos de um pulmo total das minúsculas textuais vindouras da importação (`string.ascii_lowercase`) e lhes convertemos com unísono na maleável mutação Listada ao array totalizante chamado `caracteres`. Garantidamente tiramos forçadamente 1 mínimo fortuito letra dessas (.choice) por via da sorte imposta e fixados na sacola de itens da array vital obrigados a estarem no meio pro nosso array provisório temporário: `senha_obrigatoria`.

```python
    if incluir_maiusculas:
        caracteres.extend(list(string.ascii_uppercase))
        senha_obrigatoria.append(random.choice(string.ascii_uppercase))
```
Dos retornos avaliados afirmativos e condicionais batidos do (`True`). Fritamos na mescla a velha varredura e colamos a fileira adicional em seu pote grandão baseando `.extend()` à totalização global agregada (letras grandes por exemplo alocadas no caldeirão total). De fato do mesmo jeitinho pegando também já a imposição da obrigatoriedade tirada fortuita, adicionadas a fila dos segurados `senha_obrigatoria` num belíssimo preenchimento no fim de seu armário `.append()`. 

```python
    tamanho_restante = tamanho - len(senha_obrigatoria)
    for _ in range(tamanho_restante):
        senha_obrigatoria.append(random.choice(caracteres))
```
Restrita de sua meta visual ideal em que pediu, retiramos fora já do bolo total as fatias pré-agendadas já capturadas nos obrigações da array supracitado avaliadas por um `len()`. Lançamos um sorteio do sorteio em cima dos totais predeterminados até a morte final de contagens com as repetentes laçadas (`for`) a partir de cima dos fundos totais (`caracteres` com ou sem numericos) preenchendo todos buracos dos retiros que lhe alçam aleatórios da engrenagem. 

```python
    random.shuffle(senha_obrigatoria)
    senha_final = "".join(senha_obrigatoria)
```
Dado dos incrustes de minúsculo ficado agindo do jeito forçoso no limiar superior, baralhamos perfeitamente de forma brutal qual copo sacudindo no `.shuffle()`. Em uma tacada imortal, colamos dos pedaços flutuantes a unificação do encadeamento por vazio espaçal textual em cima do final via a junta `" "(nada).join(do listório de embaralhamentos)`. Uma formidável e fortíssima parede das muralhas resultantes textuais numa fila limpa e pronta pro estocada string global.

```python
    print(f"Sua senha gerada: {senha_final}")
```
Expurgamos brilhando num último retorno em terminal impresso da preciosidade a enaltecer-se. O ciclo de utilidade chegou perfeitamente as ordens e comandos visualmente na caçada centralizando o script ao main de rodada das vias finais.
