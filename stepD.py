def stepD(self):

    # STEP D:
    # the new unit receives a weight of 1
    # and its segments receive an additional weight of .5

    self.weight.append(1.0)

    for i in range(self.Nunit):

        self.weight[self.segmentNUM[i]] += 0.5

    # move to STEP G

    self.stepG()