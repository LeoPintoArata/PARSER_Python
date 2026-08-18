def learn(self, sequence):

    # sequence to be processed

    self.sequence = sequence

    # variables storing the size of the attention window,
    # the percepts and the evolution of the total number
    # of units

    self.ATTwind = []
    self.nPERCEPT = []
    self.EVOLunit = []

    count = 0

    self.N = 0

    while self.N < len(self.sequence):

        # STEP A

        self.stepA()

        # move forward in the sequence

        self.N += self.PERCEPTsize

        count += 1

        # store variables

        self.ATTwind.append(self.Nunit)

        self.nPERCEPT.append(self.PERCEPT)

        # cleaning of the PS

        self.cleaning()

        self.EVOLunit.append(self.TOTunit)