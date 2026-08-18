import random
def stepA(self):

    # taille de la fenêtre attentionnelle
    self.Nunit = random.randint(1, 3)

    # STEP F
    if self.Nunit == 1:
        self.stepF()

    # STEP B
    else:
        self.stepB()