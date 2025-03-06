def brincar(self, tempo):
    
    self.saude += tempo
    
    if self.saude > 100:
        
        self.saude = 100
