def cleaning(self):

    # Here we clean the units by removing units having
    # a weight smaller than 0

    # We first reinitialize the weights of primitives

    for i in range(self.TOTprimitives):

        if self.weight[i] < 1:

            self.weight[i] = 1

    # Copy of all variables

    unit2 = self.unit.copy()
    SizeUnit2 = self.SizeUnit.copy()
    weight2 = self.weight.copy()

    # erase the old variables

    self.unit = []
    self.SizeUnit = []
    self.weight = []

    n = 0

    for t in range(self.TOTunit):

        if weight2[t] > 0:

            self.unit.append(unit2[t])

            self.SizeUnit.append(SizeUnit2[t])

            self.weight.append(weight2[t])

            n += 1

    self.TOTunit = n