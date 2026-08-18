def stepF(self):

    # STEP F:
    # the random generator has selected a value of 1

    self.pos = 0

    # determine the size of the largest unit in the PS
    # whose weight is above threshold

    self.maxSize = 0

    for i in range(self.TOTunit):

        if self.weight[i] >= self.thresh:

            if self.SizeUnit[i] > self.maxSize:

                self.maxSize = self.SizeUnit[i]

    self.PERCEPTNUM = 0
    self.limit = 0

    found = False

    # largest units are considered first

    for j in range(self.maxSize, 0, -1):

        # scan all units starting from the last one

        for k in range(self.TOTunit - 1, -1, -1):

            if self.SizeUnit[k] == j and self.weight[k] >= self.thresh:

                if (self.N + j) <= len(self.sequence):

                    comparaison = (
                        self.sequence[self.N:self.N + j]
                        ==
                        self.unit[k]
                    )

                    if comparaison:

                        self.PERCEPT = self.unit[k]

                        self.PERCEPTsize = self.SizeUnit[k]

                        self.PERCEPTNUM = k

                        self.pos += self.SizeUnit[k]

                        found = True

                        break

                else:

                    self.limit = 1

        if found:

            break

    if self.limit == 0:

        # the selected unit receives an additional weight of .5

        self.weight[self.PERCEPTNUM] += 0.5

        # move to STEP G

        self.stepG()

