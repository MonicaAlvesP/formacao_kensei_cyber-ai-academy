def iniciar_quiz():
    perguntas = [
        {
            "pergunta": "O que é Phishing?",
            "opcoes": [
                "A) Uma técnica de programação avançada.",
                "B) Um ataque que tenta enganar usuários para obter dados sensíveis.",
                "C) Um tipo de antivírus gratuito."
            ],
            "resposta_correta": "B"
        },
        {
            "pergunta": "Qual é a principal função de um Firewall?",
            "opcoes": [
                "A) Monitorar e controlar o tráfego de rede baseado em regras de segurança.",
                "B) Aumentar a velocidade da sua conexão com a internet.",
                "C) Apagar arquivos duplicados no disco rígido."
            ],
            "resposta_correta": "A"
        },
        {
            "pergunta": "O que o termo 'Malware' significa?",
            "opcoes": [
                "A) Uma marca de computador de alta performance.",
                "B) Uma rede social para hackers éticos.",
                "C) Um termo geral para softwares maliciosos (vírus, ransomwares, etc.)."
            ],
            "resposta_correta": "C"
        },
        {
            "pergunta": "Por que a Autenticação de Dois Fatores (2FA) é importante?",
            "opcoes": [
                "A) Porque ela substitui a necessidade de ter uma senha forte.",
                "B) Porque adiciona uma camada extra de segurança além da senha.",
                "C) Porque impede que o computador pegue vírus através de pendrives."
            ],
            "resposta_correta": "B"
        },
        {
            "pergunta": "O que faz um ataque de Ransomware?",
            "opcoes": [
                "A) Rouba a senha do seu Wi-Fi.",
                "B) Criptografa seus arquivos e cobra um resgate para liberá-los.",
                "C) Envia e-mails de propaganda (spam) para seus contatos."
            ],
            "resposta_correta": "B"
        }
    ]

    pontuacao = 0
    total_perguntas = len(perguntas)

    print("="*45)
    print("   QUIZ DE CYBERSEGURANÇA (5 Perguntas)   ")
    print("="*45)
    print("-> Digite A, B ou C para responder.")
    print("-> Você precisa de pelo menos 3 acertos para passar!\n")

    for i, p in enumerate(perguntas, start=1):
        print(f"Pergunta {i}: {p['pergunta']}")
        for opcao in p['opcoes']:
            print(f"  {opcao}")
        
        while True:
            resposta = input("Sua resposta: ").strip().upper()
            if resposta in ['A', 'B', 'C']:
                break
            print("Entrada inválida. Por favor, digite A, B ou C.")

        if resposta == p['resposta_correta']:
            print("-> ✅ Correto!\n")
            pontuacao += 1
        else:
            print(f"-> ❌ Incorreto! A resposta certa era: {p['resposta_correta']}\n")

    print("="*45)
    print("               RESULTADO FINAL             ")
    print("="*45)
    print(f"Você acertou: {pontuacao} de {total_perguntas}\n")

    if pontuacao >= 3:
        print("🎉 STATUS: APROVADO!")
        print("Parabéns! Você tem uma boa base em segurança digital.")
    else:
        print("⚠️ STATUS: REPROVADO.")
        print("Recomendamos que você estude um pouco mais sobre como se proteger online.")
    print("="*45)

if __name__ == "__main__":
    iniciar_quiz()
