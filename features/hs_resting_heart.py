class restingHeartRate:
     #Lists containing age and resting heart-rate tuple values associated with a person's health types
        athlete = [
                (range(18,25),range(49,55)),
                (range(26,35),range(49,54)),
                (range(36,45),range(50,56)),
                (range(46,55),range(50,57)),
                (range(56,65),range(51,56)),
                (range(65,90),range(50,55))
                ]

        excellent = [
                (range(18,25),range(56,61)),
                (range(26,35),range(55,61)),
                (range(36,45),range(57,62)),
                (range(46,55),range(58,63)),
                (range(56,65),range(57,61)),
                (range(65,90),range(56,61))
                ]

        good =      [
                (range(18,25),range(62,65)),
                (range(26,35),range(62,65)),
                (range(36,45),range(63,66)),
                (range(46,55),range(64,67)),
                (range(56,65),range(62,67)),
                (range(65,90),range(62,65))
                ]

        above_average = [
                (range(18,25),range(66,69)),
                (range(26,35),range(66,70)),
                (range(36,45),range(67,70)),
                (range(46,55),range(68,71)),
                (range(56,65),range(68,71)),
                (range(65,90),range(66,69))
                ]

        average = [
                (range(18,25),range(70,73)),
                (range(26,35),range(71,74)),
                (range(36,45),range(71,75)),
                (range(46,55),range(72,76)),
                (range(56,65),range(72,75)),
                (range(65,90),range(70,73))
                ]

        below_average = [
                (range(18,25),range(74,81)),
                (range(26,35),range(75,81)),
                (range(36,45),range(76,82)),
                (range(46,55),range(77,83)),
                (range(56,65),range(76,81)),
                (range(65,90),range(74,79))
                ]

        poor = [
                (range(18,25),range(82,100)),
                (range(26,35),range(82,100)),
                (range(36,45),range(83,100)),
                (range(46,55),range(84,100)),
                (range(56,65),range(82,100)),
                (range(65,90),range(80,100))]

#Constructor defining the attributes within the  health_status_resting_heart_rate method    
def __init__(self, age, restingHeart):
     self.age = age
     self.restingHeart = restingHeart

#Determine fitness based on resting heart rate
def health_status_resting_heart_rate(self,age,restingHeart):
    """
    We are going to define a series of lists containing tuples with age as the first metric and heart rate as the second metric
    for a series of health types.
    """

    #List cotaining the different health types
    health_list = [self.athlete,self.excellent,self.good,self.above_average,self.average,self.below_average,self.poor]

    #Logic to determine a person's health type based on age and heart-rate
    for i in range(len(health_list)):
        print("Code1")
        for j in range(len(health_list[i])):
            print("Code2")
            if (age in health_list[0][j][0]) and (restingHeart in health_list[0][j][1]):
                print("Athlete")
                break
            elif (age in health_list[1][j][0]) and (restingHeart in health_list[1][j][1]):
                print("Excellent")
                break
            elif (age in health_list[2][j][0]) and (restingHeart in health_list[2][j][1]):
                print("Good")
                break
            elif (age in health_list[3][j][0]) and (restingHeart in health_list[3][j][1]):
                print("Above Average")
                break
            elif (age in health_list[4][j][0]) and (restingHeart in health_list[4][j][1]):
                print("Average")
                break
            elif (age in health_list[5][j][0]) and (restingHeart in health_list[5][j][1]):
                print("Below Average")
                break
            elif (age in health_list[6][j][0]) and (restingHeart in health_list[6][j][1]):
                print("Poor")
                break
        break

