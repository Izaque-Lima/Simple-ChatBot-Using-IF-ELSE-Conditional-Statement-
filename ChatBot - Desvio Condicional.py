# Base de conhecimento
respostas = {
    "ola": "Olá! Como posso ajudar você hoje?",
    "oi": "Oi! O que te traz por aqui?",
    "como voce esta": "Eu sou um programa de computador, mas estou ótimo! E você?",
    "o que e python": "Python é uma linguagem de programação popular, usada em Data Science, desenvolvimento web e mais!",
    "tchau": "Até mais! Volte sempre!",
    "to bem": "Fico muito feliz! O que mais posso fazer para te ajudar?"
}

def chatbot_simples():
    print("--- Chatbot Simples (Digite 'tchau' para sair) ---")
    
    # Loop principal para manter o chat aberto
    while True:
        # Pede a entrada do usuário
        entrada = input("Você: ").lower().strip()
        
        # Condição de saída
        if entrada == "tchau":
            print("Chatbot: Até mais! Foi um prazer conversar.")
            break
            
        # 1. Tenta encontrar uma resposta exata ou por palavra-chave
        resposta_encontrada = False
        
        # 2. Verifica as respostas exatas no dicionário
        if entrada in respostas:
            print(f"Chatbot: {respostas[entrada]}")
            resposta_encontrada = True
        
        # 3. Se não encontrou, tenta encontrar por palavra-chave
        if not resposta_encontrada:
            for palavra_chave, resposta_pronta in respostas.items():
                # Verifica se a palavra-chave está na entrada do usuário
                if palavra_chave in entrada:
                    print(f"Chatbot: {resposta_pronta}")
                    resposta_encontrada = True
                    break # Para o loop assim que encontrar a primeira resposta
        
        # 4. Resposta padrão para o que não foi entendido
        if not resposta_encontrada:
            print("Chatbot: Desculpe, não entendi. Você pode tentar reformular ou perguntar algo mais simples?")

# Chama a função para iniciar o chatbot
chatbot_simples()