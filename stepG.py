def stepG(self):

    # STEP G:
    # computing forgetting and interference of each unit

    # -------------------------------------------------
    # INTERFERENCE
    # -------------------------------------------------
    # Interference is computed when the PERCEPT shares
    # a segment with a unit.

    for j in range(self.PERCEPTsize):

        self.Target = self.PERCEPT[j]

        for i in range(self.TOTunit):

            for k in range(self.SizeUnit[i]):

                if self.Target == self.unit[i][k]:

                    self.weight[i] = self.weight[i] - self.interf

    # -------------------------------------------------
    # FORGETTING
    # -------------------------------------------------
    # subtract forg from every unit

    for i in range(self.TOTunit):

        self.weight[i] = self.weight[i] - self.forg

    # -------------------------------------------------
    # restore the current PERCEPT
    # -------------------------------------------------

    for i in range(self.TOTunit):

        if self.PERCEPTsize == self.SizeUnit[i]:

            comparaison = (
                self.PERCEPT ==
                self.unit[i]
            )

            if comparaison:

                self.weight[i] = self.weight[i] + self.forg