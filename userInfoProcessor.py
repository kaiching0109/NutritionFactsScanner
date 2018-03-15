class userInfoProcessor:

    name = ""
    gender = ''
    weight_in_kilograms = 0
    height_in_centimeters = 0
    age = 0

    def __init__(self, name, gender, age, weight, height):
        self.name = name
        self.gender = gender
        self.age = age
        self.weight_in_kilograms = weight
        self.height_in_centimeters = height

    def setName(self, name):
        self.name = name

    def setGender(self, gender):
        self.gender = gender

    def setAge(self, age):
        self.age = age

    def setWeight(self, weight):
        self.weight_in_kilograms = weight

    def setHeight(self, height):
        self.height_in_centimeters = height

    def getProfile(self):
        profile = {
                    "NAME":     self.name,
                    "GENDER":   self.gender,
                    "AGE":      self.age,
                    "HEIGHT":   self.height_in_centimeters,
                    "WEIGHT":   self.weight_in_kilograms
                    }
        return profile