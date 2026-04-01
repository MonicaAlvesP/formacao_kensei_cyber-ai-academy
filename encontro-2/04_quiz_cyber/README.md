# 04 - Quiz Cibersegurança

## 📄 Arquivo: `quiz_cyber.py`

Pequeno jogo de terminal composto por 5 perguntas de múltiplas opções baseadas numa estrutura rica de Dicionários de Python para validação automática de acertos.

### Explicação Linha por Linha:

```python
    perguntas = [
        {
            "pergunta": "O que é Phishing?",
            "opcoes": [ ... ],
            "resposta_correta": "B"
        },
```
Isso constrói a nossa base de dados. Usamos uma "Lista" `[]` que dentro contém múltiplos "Dicionários" `{}` de Python. Um Dicionário maneja as variáveis em pares de "Chave" e "Valor". Por exemplo, a chave `"pergunta"` de um deles nos outorga o texto descritivo a visualizar na tela. Do mesmo modo, guardamos silenciosamente a validade que nós compararemos sob o codinome de chave `"resposta_correta"`.

```python
    pontuacao = 0
    total_perguntas = len(perguntas)
```
Iniciamos e atribuímos do topo zero metas vitais (`pontuacao = 0`). Computaremos da nossa própria matriz graças a régua global do objeto Listas em si através do super poder de medição da formatação Dimensional `len()`. Exemplo: se havia 5 casinhas ali cadastradas, o tamanho passará pro total de perguntas o número `5`, e as comparará.

```python
    print("="*45)
```
Os caracteres matemáticos multiplicadores até se combinam perfeitamente na hora de trabalhar com textinho Strings para design. Multiplique uma carinha de unísono de igual e terá em tela os quarenta e cinco (`===================...`) repetidos horizontalmente como decorações limpas.

```python
    for i, p in enumerate(perguntas, start=1):
```
Arrancando com a laçada de cada array de perguntas que montamos no sistema da Listagem de cima. `p` passará a carregar transitatoriamente todos os mistérios da casa interna avaliada, seja do índice um dos dicionários ou o último avaliado temporalmente desta vez.

```python
        print(f"Pergunta {i}: {p['pergunta']}")
        for opcao in p['opcoes']:
            print(f"  {opcao}")
```
Fazendo reluzir `p` ao público. Como extrair uma chave guardada do seu estante correspondente, o procuramos assim: `['pergunta']`. Exibimos na tela todo este encadeamento de orçamentos e criamos na engrenagem de repetição outra sub-repetição do laçamento (`for`) iterando listagens as derivativas resguardadas em `['opcoes']`.

```python
        while True:
            resposta = input("Sua resposta: ").strip().upper()
            if resposta in ['A', 'B', 'C']:
                break
```
Uma "armadilha" (loop do `while True`). Retemos o usuário numa tranca constante até forçamo a cravar a opção certa. Capturamos do Input dele e lhe lavamos quaisquer impurezas espaciais com o polimento de `.strip()` e uniformizamos minúsculas que causariam erro por maiúsculas no formato `.upper()`. Autorizamos ele sair fora só ali e somente se ele esteve metido num array compatível visual `['A', 'B', 'C']`.

```python
        if resposta == p['resposta_correta']:
```
Ele capta a letra imbuída perfeitamente pelo apostador, logo com pulso cravado validaremos ela frente a resposta verdadeira original de `p['resposta_correta']`.

```python
            pontuacao += 1
```
No ato da verdade do correto visual. Elevamos sem vergonha através da operação adjunta, cujo equivaleria também a grafar o velho padrão `pontuacao = pontuacao + 1`. Anota-se um ponto à sacola na hora da somatória de avaliação.

```python
    if pontuacao >= 3:
```
Na conclusão do rescaldo global após que as repetições iterativas do laço escorrerem livres até o término do balcão na laçada matriz terminal total, procedemos ao teste. Caso tenhas encaixotado acima do mínimo que era almejado `(>= 3)` do teste final total te abriremos palmas no triunfo merecido. Ao contrário disto, você recebe as exortações motivadoras do `else` inferior pelo fracasso, a tentar melhor depois.
