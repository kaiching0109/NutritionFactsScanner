import numpy

class informationProcessor:

    data = []
    servingSize = 0
    calories_per_serving = 0
    total_fat_in_daliy = 0
    saturated_fat = 0
    trans_fat_in_daliy = 0
    cholesterol_in_daliy = 0
    sodium_in_daliy = 0
    total_carbohydrate_in_daliy = 0
    dietary_fiber_in_daliy = 0
    sugars = 0
    protein = 0
    vitamin_A_in_daliy = 0
    vitamin_B_in_daliy = 0
    vitamin_C_in_daliy = 0
    vitamin_D_in_daliy = 0
    calcium_in_daliy = 0
    iron_in_daliy = 0

    nutrientProfile = {}

    SATURATED_FAT_RATE = 0.10
    TRANS_FAT_RATE = 0.10
    CHOLESTEROL_LOWER_BOUND = 100 #mg
    CHOLESTEROL_UPPER_BOUND = 300 #mg
    SUGAR_LOWER_RATE = 0.06
    SUGAR_UPPER_RATE = 0.10
    SODIUM_BOUND = 2300 #mg


    GRAM_OF_FAT_FACTOR = 9
    GRAM_OF_SUGAR_FACTOR = 4
    GRAM_OF_FIBER_FACTOR = 14

    DAILY_VALUE_IN_PERCENTAGE = {
        0.02: 'VERY LOW',
        0.05: 'LOW',
        0.20: 'HIGH',
        0.40: 'VERY HIGH'
    }

    NUTRIENT_ELEMENT = ["CALORIES", "PROTEIN", "FAT", "CARBOHYDRATE"]
    DAILY_ELEMENT = ["SATURATED_FAT", "TRANS_FAT", "CHOLESTEROL", "SODIUM",
                     "DIETARY_FIBER", "SUGAR", "VITAMIN_A", "VITAMIN_B", "VITAMIN_C",
                     "VITAMIN_D", "CALCIUM", "IRON", "POSTASSIUM"]
    LEVEL_ELEMENT = ['VERY LOW', 'LOW', 'HIGH', 'VERY HIGH']

    NUTRIENT_LEVELS = {
        "CALORIES": [],
        "PROTEIN": [],
        "FAT": [],
        "CARBOHYDRATE": [],
    }

    DAILY_LEVELS = {
        "SATURATED_FAT": [],
        "TRANS_FAT": [],
        "CHOLESTEROL": [],
        "SODIUM": [],
        "DIETARY_FIBER": [],
        "SUGAR": [],
        "VITAMIN_A": [],
        "VITAMIN_B": [],
        "VITAMIN_C": [],
        "VITAMIN_D": [],
        "CALCIUM": [],
        "IRON": [],
        "POSTASSIUM": []
    }

    def __init__(self, nutrientProfile, OCRdata):
        self.nutrientProfile = nutrientProfile
        self.data = OCRdata

    def setData(self, OCRdata):
        self.data = OCRdata

    def setNutrientLevels(self):
        caloreisNeed = self.nutrientProfile["CALOREIES"] / 2
        proteinNeed = self.nutrientProfile["PROTEIN"]
        fatNeed = self.nutrientProfile["FAT"]
        carbohydrateNeed = self.nutrientProfile["CARBOHYDRATE"]
        needs = [caloreisNeed, proteinNeed, fatNeed, carbohydrateNeed]
        q1, q2, q3 = self.getQs(needs)
        i = 0
        for element in self.NUTRIENT_ELEMENT:
            self.NUTRIENT_LEVELS[element] = [q1[i], q2[i], q3[i]]
            i += 1

    def setDailyLevels(self):
        caloreisNeed = self.nutrientProfile["CALOREIES"]
        fatNeed = self.nutrientProfile["FAT"]
        saturatedFatLimit = caloreisNeed * self.SATURATED_FAT_RATE / self.GRAM_OF_FAT_FACTOR
        transFatLimit = caloreisNeed * self.TRANS_FAT_RATE / self.GRAM_OF_FAT_FACTOR
        cholesterolLimit = (self.CHOLESTEROL_LOWER_BOUND + self.CHOLESTEROL_HIGHER_BOUND)/2
        sodiumLimit = self.SODIUM_BOUND / 2
        fiberNeed = caloreisNeed / 1000 * self.GRAM_OF_FIBER_FACTOR
        sugarLimit = ((caloreisNeed * self.SUGAR_UPPER_RATE +
                      caloreisNeed * self.SUGAR_LOWER_RATE)/2) / self.GRAM_OF_SUGAR_FACTOR


    # DAILY_ELEMENT = ["SATURATED_FAT", "TRANS_FAT", "CHOLESTEROL", "SODIUM",
    #                  "DIETARY_FIBER", "SUGAR", "VITAMIN_A", "VITAMIN_B", "VITAMIN_C",
    #                  "VITAMIN_D", "CALCIUM", "IRON", "POSTASSIUM"]

    def getQs(self, data):
        q1 = [x * 0.25 for x in data]
        q2 = [x * 0.5 for x in data]
        q3 = [x * 0.5 for x in data]
        return q1, q2, q3

    def compareCalories(self):
        q1, q2, q3 = self.NUTRIENT_LEVELS["CALOREIES"][0], self.NUTRIENT_LEVELS["CALOREIES"][1], self.NUTRIENT_LEVELS["CALOREIES"][2]
        if self.calories_per_serving == 0:
            print ("No Calories")
        elif self.calories_per_serving <= q1:
            print("Low Calories")
        elif self.calories_per_serving <= q2:
            print("Moderate Calories")
        elif self.calories_per_serving <= q3:
            print("High Calories")
        else:
            print("Very High Calories")

    def compareProtein(self):
        q1, q2, q3 = self.NUTRIENT_LEVELS["PROTEIN"][0], self.NUTRIENT_LEVELS["PROTEIN"][1], self.NUTRIENT_LEVELS["PROTEIN"][2]
        if self.protein == 0:
            print ("No Protein")
        elif self.protein <= q1:
            print("Low Protein")
        elif self.protein <= q2:
            print("Moderate Protein")
        elif self.protein <= q3:
            print("High Protein")
        else:
            print("Very High Protein")

    def compareFat(self):
        q1, q2, q3 = self.NUTRIENT_LEVELS["FAT"][0], self.NUTRIENT_LEVELS["FAT"][1], self.NUTRIENT_LEVELS["FAT"][2]
        if self.protein == 0:
            print ("No Fat")
        elif self.protein <= q1:
            print("Low Fat")
        elif self.protein <= q2:
            print("Moderate Fat")
        elif self.protein <= q3:
            print("High Fat")
        else:
            print("Very High Fat")

    def compareCarbohydrate(self):
        q1, q2, q3 = self.NUTRIENT_LEVELS["CARBOHYDRATE"][0], self.NUTRIENT_LEVELS["CARBOHYDRATE"][1], self.NUTRIENT_LEVELS["CARBOHYDRATE"][2]
        if self.protein == 0:
            print ("No Carbohydrate")
        elif self.protein <= q1:
            print("Low Carbohydrate")
        elif self.protein <= q2:
            print("Moderate Carbohydrate")
        elif self.protein <= q3:
            print("High Carbohydrate")
        else:
            print("Very High Carbohydrate")

    def compareSaturatedFat(self):
        q1, q2, q3 = self.DAILY_LEVELS["SATURATED_FAT"][0], self.DAILY_LEVELS["SATURATED_FAT"][1], \
                     self.DAILY_LEVELS["SATURATED_FAT"][2]
        if self.saturated_fat == 0:
            print ("No Saturated Fat")
        elif self.saturated_fat <= q1:
            print("Low Saturated Fat")
        elif self.saturated_fat <= q2:
            print("Moderate Saturated Fat")
        elif self.saturated_fat <= q3:
            print("High Saturated Fat")
        else:
            print("Very High Saturated Fat")