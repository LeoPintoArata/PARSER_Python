from stepA import stepA
from stepB import stepB
from stepC import stepC
from stepD import stepD
from stepE import stepE
from stepF import stepF
from stepG import stepG
from cleaning import cleaning
from learn import learn

class Parser98:

    def __init__(self,
             primitives,
             thresh=1,
             forg=0.05,
             interf=0.005):

    # parameters

        self.thresh = thresh
        self.forg = forg
        self.interf = interf

    # total number of units

        self.TOTunit = len(primitives)

    # number of primitives

        self.TOTprimitives = self.TOTunit

    # weights

        self.weight = [1.0 for _ in range(self.TOTunit)]

    # sizes

        self.SizeUnit = [1 for _ in range(self.TOTunit)]

    # units

        self.unit = []

        for i in range(len(primitives)):

            self.unit.append(primitives[i])

    # variables used during learning

        self.PERCEPT = ""
        self.PERCEPTsize = 0
        self.PERCEPTNUM = 0

        self.segment = []
        self.segmentSIZE = []
        self.segmentNUM = []

        self.Nunit = 0

        self.maxSize = 0
        self.pos = 0
        self.limit = 0

        self.Target = ""

        self.sequence = ""
        self.N = 0

Parser98.stepA = stepA
Parser98.stepB = stepB
Parser98.stepC = stepC
Parser98.stepD = stepD
Parser98.stepE = stepE
Parser98.stepF = stepF
Parser98.stepG = stepG

Parser98.cleaning = cleaning
Parser98.learn = learn