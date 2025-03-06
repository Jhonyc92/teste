def menu():

    meu_bichinho = BichinhoVirtual("Buddy")
    
    while True:
        
        meu_bichinho.status()
        
        acao = input("O que você quer fazer? (alimentar/brincar/sair): ")
        
        if acao == "alimentar":
            
            quantidade = int(input("Quantidade de comida: "))
            
            meu_bichinho.alimentar(quantidade)
            
        elif acao == "brincar":
            
            tempo = int(input("Tempo de brincadeira: "))
            
            meu_bichinho.brincar(tempo)
            
        elif acao == "sair":
            
            break
            
        else:
            
            print("Ação inválida!")
