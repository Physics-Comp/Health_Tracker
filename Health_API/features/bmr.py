class BMR:
    """
    The following class calculates the bmr of an individual which determines the numnber of calories your body burns 
    performing life-sustaining functions.
    """
    def __init__(self,age,weight,height):
        self.age = age
        self.weight = weight
        self.height = height
    
    def bmr(sex,age,weight,height):
        """
        Given the users age, weight, sex and height we can calculate the bmr

        Ex. bmr("male", 20, 140, 5.10)
        """
        bmr = 0
        if sex == "male":
            bmr_male = 88.362 + ((0.453592 * 13.397) * weight) + ((4.799 * 0.0328084) * height) - (5.677 * age)
            bmr.replace(bmr,bmr_male)
        else:
            bmr_female = 447.593 + ((0.453592 * 9.274) * weight) + ((3.098 * 0.0328084) * height) - (4.330 * age)
            bmr.replace(bmr,bmr_female)
        return bmr


