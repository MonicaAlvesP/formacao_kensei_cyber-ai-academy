import random
import string

def gerar_senha():
    print("="*40)
    print("      GERADOR DE SENHAS SEGURAS      ")
    print("="*40)

    try:
        tamanho = int(input("Qual o tamanho da senha desejada? (ex: 12): "))
        if tamanho < 1:
            print("Tamanho inválido. Ajustando para 8 caracteres.")
            tamanho = 8
    except ValueError:
        print("Valor inválido. Usando o tamanho padrão de 12 caracteres.")
        tamanho = 12

    incluir_maiusculas = input("Incluir letras maiúsculas? (S/N): ").strip().upper() == 'S'
    incluir_numeros = input("Incluir números? (S/N): ").strip().upper() == 'S'
    incluir_simbolos = input("Incluir símbolos especiais? (S/N): ").strip().upper() == 'S'

    # Caracteres base (minúsculas sempre inclusas para garantir que haja caracteres suficientes)
    caracteres = list(string.ascii_lowercase)
    senha_obrigatoria = [random.choice(string.ascii_lowercase)]

    if incluir_maiusculas:
        caracteres.extend(list(string.ascii_uppercase))
        senha_obrigatoria.append(random.choice(string.ascii_uppercase))
    
    if incluir_numeros:
        caracteres.extend(list(string.digits))
        senha_obrigatoria.append(random.choice(string.digits))
    
    if incluir_simbolos:
        caracteres.extend(list(string.punctuation))
        senha_obrigatoria.append(random.choice(string.punctuation))

    # Verifica se o tamanho desejado é menor do que os requisitos mínimos selecionados
    if tamanho < len(senha_obrigatoria):
        tamanho = len(senha_obrigatoria)
        print(f"\nAtenção: O tamanho foi ajustado para {tamanho} para cumprir os requisitos escolhidos.")

    # Preenche o resto da senha com opções aleatórias baseadas nas escolhas do usuário
    tamanho_restante = tamanho - len(senha_obrigatoria)
    for _ in range(tamanho_restante):
        senha_obrigatoria.append(random.choice(caracteres))

    # Embaralha a lista para que os caracteres obrigatórios não fiquem todos no início
    random.shuffle(senha_obrigatoria)
    
    # Converte a lista de volta para uma string de texto
    senha_final = "".join(senha_obrigatoria)

    print("\n" + "="*40)
    print(f"Sua senha gerada: {senha_final}")
    print("="*40)

if __name__ == "__main__":
    gerar_senha()
