def stepB(self):

    # STEP B:
    # attentional window is equal to 2 or 3

    self.pos = 0

    # determine the size of the largest unit
    # whose weight is above threshold

    self.maxSize = 0

    for i in range(self.TOTunit):

        if self.weight[i] >= self.thresh:

            if self.SizeUnit[i] > self.maxSize:

                self.maxSize = self.SizeUnit[i]

    # initialize segments

    self.segment = []
    self.segmentSIZE = []
    self.segmentNUM = []

    self.Nsegment = 1

    self.limit = 0

    # search for the units corresponding to the sequence

    for i in range(self.Nunit):

        found = False

        # largest units first

        for j in range(self.maxSize, 0, -1):

            # compare with each unit

            for k in range(self.TOTunit - 1, -1, -1):

                # unit has the correct size and weight

                if self.SizeUnit[k] == j and self.weight[k] >= self.thresh:

                    # verify that we do not exceed the sequence

                    if (self.N + self.pos + j) <= len(self.sequence):

                        comparaison = (
                            self.sequence[
                                self.N + self.pos:
                                self.N + self.pos + j
                            ]
                            ==
                            self.unit[k]
                        )

                        if comparaison:

                            self.segment.append(self.unit[k])

                            self.segmentSIZE.append(self.SizeUnit[k])

                            self.segmentNUM.append(k)

                            self.Nsegment += 1

                            self.pos += self.SizeUnit[k]

                            found = True

                            break

                    else:

                        self.limit = 1

            if found:

                break

    # construct the PERCEPT

    if self.limit == 0 and len(self.segment) == self.Nunit:

        self.PERCEPT = ""

        self.PERCEPTsize = 0

        for i in range(self.Nunit):

            self.PERCEPT += self.segment[i]

            self.PERCEPTsize += self.segmentSIZE[i]

        # check whether the PERCEPT already exists

        self.exist = 0

        for i in range(self.TOTunit):

            if self.SizeUnit[i] == self.PERCEPTsize:

                comparaison = (
                    self.PERCEPT
                    ==
                    self.unit[i]
                )

                if comparaison:

                    self.exist = 1

                    self.PERCEPTNUM = i

                    break

        # STEP C or STEP E

        if self.exist == 0:

            self.stepC()

        else:

            self.stepE()
