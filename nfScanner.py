from imageProcessor import imageProcessor
from informationProcessor import informationProcessor
from userInfoProcessor import  userInfoProcessor

def main():
    user_InfoProcessor = userInfoProcessor("Beth", 'F', 47, 165, 66.8)

    image_Processor = imageProcessor()
    image_Processor.setImage('test2.png')
    image_Processor.processOCR()
    image_Processor.display()


main()