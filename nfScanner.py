from imageProcessor import imageProcessor
from informationProcessor import informationProcessor
from userInfoProcessor import userInfoProcessor
from nutrientProfileCalculator import nutrientProfileCalculator
from referenceDataProcessor import referenceDataProcessor

def main():
    #user_InfoProcessor = userInfoProcessor("Beth", 'F', 47, 165, 66.8)
    #userProfile = user_InfoProcessor.getUserProfile()
    #nutrientProfile_Calculator = nutrientProfileCalculator(userProfile)
    #nutrientProfile_Calculator.setDRI_table()
    #information_Processor = informationProcessor()
    referenceData_Processor = referenceDataProcessor()
    referenceData_Processor.build("DRI_TABLE1.pdf")
    referenceData_Processor.build("DRI_TABLE2.pdf")
    referenceData_Processor.setAgeGroup()
    referenceData_Processor.search(15, 'M', "Magnesium")
    referenceData_Processor.search(15, 'F', "Magnesium")

    #search(self, age, gender, nutrition_element)

    #image_Processor = imageProcessor()
    #image_Processor.setImage('test2.png')
    #image_Processor.processOCR()
    #image_Processor.display()


main()

# IMPORTANT!!!! I AM GETTING THE MEDIAN OF AGES IN EACH AGE GROUP BUT I NEED THE MAXIMUM INSTEAD!