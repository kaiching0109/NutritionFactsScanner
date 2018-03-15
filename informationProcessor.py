class informationProcessor:

    data = []
    servingSize = 0
    calories_per_serving = 0
    total_fat_in_daliy = 0
    saturated_fat_in_daliy = 0
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

    DAILY_VALUE_IN_PERCENTAGE = {
        0.02: 'VERY LOW',
        0.05: 'LOW',
        0.20: 'HIGH',
        0.40: 'VERY HIGH'
    }

    CALORIES_GENERAL = {
        100: "MODERATE",
        400: "HIGH"
    }

    def setData(self, OCRdata):
        self.data = OCRdata

