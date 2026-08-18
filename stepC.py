def stepC(self):

    # STEP C:
    # create a new unit corresponding to the PERCEPT

    self.PERCEPTNUM = self.TOTunit

    self.TOTunit += 1

    self.unit.append(self.PERCEPT)

    self.SizeUnit.append(self.PERCEPTsize)

    # move to STEP D

    self.stepD()