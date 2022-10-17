import numpy as np

class VO2:
    """
    Define typical VO2 max fitness scores for both men and women. VO2 max is the maximum rate of oxygen your body is able to use 
    during exercise. 
    """
    #Constructor
    def __init__(self,VO2_input, age_input):
       self.VO2_input = VO2_input
       self.age_input = age_input

    #Determine index of age input
    def age_index_calculation(self,VO2_matrix):
        """
        Determine the index of the age which determines the row number. The row contains the age and the correlated fitness levels from excellent
        to very poor. 
        """
        #Extract the first column in the matrix which denotes the ages (refer to documentation regarding matrix structure)
        VO2_matrix_array = np.array(VO2_matrix)
        ages = VO2_matrix_array[:,0]
        for age in ages:
            if self.age_input in age:
                match_index = list(ages).index(age)
                return match_index
            else:
                pass
    
    #Determine the health status based on the VO2 level
    def VO2_health_status_calculation(self, age_index, VO2_matrix):
        """
        Based on the index of the age and the VO2 value, determine the VO2 health status of the individual. The function uses the age index to
        find the row containing the appropriate VO2 values for that age and there associated health status.
        """
        VO2_health_status_dict = {
        0:'Excellent',
        1:'Very Good',
        2:'Good',
        3:'Average',
        4:'Fair',
        5:'Poor',
        6:'Very Poor'
        }
        VO2_values = VO2_matrix[age_index][1:]
        for VO2_value in VO2_values:
            if self.VO2_input in VO2_value:
                match_VO2_index = list(VO2_values).index(VO2_value)
                return VO2_health_status_dict[match_VO2_index]
            else:
                pass
        

class Men_VO2(VO2):
    """
    VO2 max matrix for men will be a non-parameterized function and Men_VO2 will inherit the properties of VO2.
    """
    def __init__(self, VO2_input, age_input):
        self.VO2_matrix_men = [
                        [range(20,24), range(62,72), range(57,62), range(51,56), range(44,50), range(38,48), range(32,37), range(32,22)],
                        [range(25,29), range(59,69), range(54,59), range(49,53), range(43,48), range(36,42), range(31,35), range(31,21)],
                        [range(30,34), range(56,66), range(52,56), range(46,51), range(41,45), range(35,40), range(29,34), range(29,19)],
                        [range(35,39), range(54,64), range(49,54), range(44,48), range(39,43), range(33,38), range(28,32), range(28,18)],
                        [range(40,44), range(51,61), range(47,51), range(42,46), range(36,41), range(32,35), range(26,31), range(26,16)],
                        [range(45,49), range(48,58), range(44,48), range(40,43), range(35,39), range(30,34), range(25,29), range(25,15)],
                        [range(50,54), range(46,56), range(42,46), range(37,41), range(33,36), range(28,32), range(24,27), range(24,14)],
                        [range(55,59), range(43,53), range(40,43), range(35,39), range(31,34), range(27,30), range(22,26), range(22,12)],
                        [range(60,65), range(40,50), range(37,40), range(33,36), range(29,32), range(25,28), range(21,24), range(21,11)],
                    ]
        super().__init__(VO2_input, age_input)
    
    def VO2_men_fitness_status(self):
        """
        Define VO2 status of men given the age and the VO2 value
        """
        VO2_status = VO2(self.VO2_input, self.age_input)
        men_age_index = VO2_status.age_index_calculation(self.VO2_matrix_men)
        men_VO2_status = VO2_status.VO2_health_status_calculation(men_age_index,self.VO2_matrix_men)
        return men_VO2_status
        


class Women_VO2(VO2):
    """
    VO2 max matrix for women, inheriting properties from the VO2 parent class into the Men child class.
    """
    def __init__(self, VO2_input, age_input):
        self.VO2_matrix_women = [
                        [range(20,24), range(51,61), range(47,51), range(42,46), range(37,41), range(32,46), range(27,31), range(1,26)],
                        [range(25,29), range(49,59), range(45,49), range(41,44), range(36,30), range(31,35), range(26,30), range(25,15)],
                        [range(30,34), range(47,60), range(43,46), range(38,42), range(34,37), range(30,33), range(25,29), range(24,10)],
                        [range(35,39), range(45,60), range(41,44), range(36,40), range(32,35), range(28,31), range(24,27), range(23,10)],
                        [range(40,44), range(42,60), range(38,41), range(34,37), range(30,33), range(26,29), range(22,25), range(21,10)],
                        [range(45,49), range(39,60), range(36,38), range(32,35), range(28,31), range(24,27), range(21,23), range(20,10)],
                        [range(50,54), range(37,60), range(33,36), range(30,32), range(26,29), range(23,25), range(19,22), range(18,10)],
                        [range(55,59), range(34,60), range(31,33), range(28,30), range(24,27), range(21,23), range(18,20), range(17,10)],
                        [range(60,65), range(31,60), range(28,30), range(25,27), range(22,24), range(19,21), range(16,18), range(15,10)],
                        ]
        super().__init__(VO2_input, age_input)

    def VO2_women_fitness_status(self):
        """
        Define the fitness of women given the age and VO2 value.
        """
        VO2_status = VO2(self.VO2_input, self.age_input)
        women_age_index = VO2_status.age_index_calculation(self.VO2_matrix_women)
        women_VO2_status = VO2_status.VO2_health_status_calculation(women_age_index,self.VO2_matrix_men)
        return women_VO2_status


    
