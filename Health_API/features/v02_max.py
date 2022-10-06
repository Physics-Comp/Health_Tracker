class VO2:
    """
    Define typical VO2 max fitness scores for both men and women. VO2 max is the maximum rate of oxygen your body is able to use 
    during exercise. 
    """
    #Constructor
    def __init__(self,fitness_level,age):
       self.fitness_level = fitness_level
       self.age = age

        #VO2 calculation level
    def VO2_calculate(self,fitness_level,age):
        define = "Null"

class Men(VO2):
    """
    VO2 max matrix for men, inheriting properties from the VO2 parent class into the Men child class
    """
    health_metric = [(range(20,24), range(62,72)), range()
                    (range(25,29), range(59,62)),
                    (range(30,34), range(56,66)),
                    (range(35,39), range(54,64)),
                    (range(40-44), range(51,61)),
                    (range(45-49), range(48,58)),
                    (range(50-54), range(46,56)),
                    (range(55-59), range(43,53)),
                    (range(60-65), range(40,50)),
                    ]
    """
    Define the fitness type and age parameters for men
    """

    #Constructor
    def __init__(self,fit_level,age):
        self.fit_level = fit_level
        self.age = age

    VO2.VO2_calculate(self,fitness_level,age)

class Women(V02):
