from imageProcessor import imageProcessor

def main():
    image_Processor = imageProcessor()
    image_Processor.setImage('test2.png')
    image_Processor.processOCR()
    image_Processor.display()

main()