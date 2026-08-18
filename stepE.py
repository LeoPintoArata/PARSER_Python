def stepE(self):

    # STEP E:
    # the unit corresponding to the PERCEPT
    # receives an additional weight of .5

    self.weight[self.PERCEPTNUM] += 0.5

    # move to STEP G

    self.stepG()