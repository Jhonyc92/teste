def atualizar_humor(self):
    
    self.humor = 100 - (abs(self.fome - 50) + abs(self.saude - 50)) // 2
    
    if self.humor > 100:
        
        self.humor = 100
