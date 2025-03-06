def alimentar(self, quantidade):
    
    self.fome -= quantidade
    
    if self.fome < 0:
        
        self.fome = 0
        
    self.atualizar_humor()
