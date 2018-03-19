class nutrientProfileCalculator:

    userProfile = {}

    gender_constant = 0
    weight_constant = 0
    height_constant = 0
    age_constant = 0

    calorieNeeds = 0
    proteinNeeds = 0
    fatNeeds = 0
    carbohydrateNeeds = 0

    # ALL CONSTANTS AND CALCULATIOZN ARE BASED ON  Harris-Benedict Equation for Basal Energy Expenditure (BEE)
    MALE_CONSTANT = 66.5
    MALE_WEIGHT_CONSTANT = 13.75
    MALE_HEIGHT_CONSTANT = 5.003
    MALE_AGE_CONSTANT = 6.775
    FEMALE_CONSTANT = 655.5
    FEMALE_WEIGHT_CONSTANT = 9.563
    FEMALE_HEIGHT_CONSTANT = 1.850
    FEMALE_AGE_CONSTANT = 4.676
    ACTIVITY_FACTOR = 1.2
    CALORIES_FROM_FAT_FACTOR = 0.3
    GRAM_OF_FAT_FACTOR = 9
    PROTEIN_LOWER_BOUND = 0.8
    PROTEIN_UPPER_BOUND = 1.0
    CARBOHYDRATES_LOWER_BOUND = 0.45
    CARBOHYDRATES_UPPER_BOUND = 0.60

    def __init__(self, userProfile):
        self.userProfile = userProfile
        if userProfile["GENDER"] == 'F':
            self.gender_constant = self.FEMALE_CONSTANT
            self.weight_constant = self.FEMALE_WEIGHT_CONSTANT
            self.height_constant = self.FEMALE_HEIGHT_CONSTANT
            self.age_constant = self.FEMALE_AGE_CONSTANT
        else:
            self.gender_constant = self.MALE_CONSTANT
            self.weight_constant = self.MALE_WEIGHT_CONSTANT
            self.height_constant = self.MALE_HEIGHT_CONSTANT
            self.age_constant = self.MALE_AGE_CONSTANT

    def calculate(self):
        self.calCalorieNeeds()
        self.calProteinNeeds()
        self.calFatNeeds()
        self.calCarbohydrateNeeds()

    def calCalorieNeeds(self):
        self.calorieNeeds = self.gender_constant + \
        self.weight_constant * self.userProfile["WEIGHT"] + \
                self.height_constant * self.userProfile["HEIGHT"] - \
                (self.age_constant * self.userProfile["AGE"]) * self.ACTIVITY_FACTOR

    def calProteinNeeds(self):
        weight = self.userProfile["WEIGHT"]
        self.proteinNeeds = (weight * self.PROTEIN_LOWER_BOUND + weight * self.PROTEIN_UPPER_BOUND)/2

    def calFatNeeds(self):
        self.fatNeeds = self.calorieNeeds * self.CALORIES_FROM_FAT_FACTOR / self.GRAM_OF_FAT_FACTOR

    def calCarbohydrateNeeds(self):
        self.carbohydrateNeeds = (self.calorieNeeds * self.CARBOHYDRATES_LOWER_BOUND +
                                  self.calorieNeeds * self.CARBOHYDRATES_UPPER_BOUND)/2


    def getCalorieNeeds(self):
        return self.calorieNeeds

    def getProteinNeeds(self):
        return self.proteinNeeds

    def getFatNeeds(self):
        return self.fatNeeds

    def getCarbohydrateNeeds(self):
        return self.carbohydrateNeeds

    def getNutientProfile(self):
        nutientProfile = {
                    "CALORIE":     self.calorieNeeds,
                    "PROTEIN":   self.proteinNeeds,
                    "FAT":      self.fatNeeds,
                    "CARBOHYDRATE":   self.carbohydrateNeeds,
                    }
        return nutientProfile