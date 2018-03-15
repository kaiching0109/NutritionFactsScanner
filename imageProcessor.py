from PIL import Image
from pytesseract import image_to_string
from  word_list import word_list
import difflib
import re

class imageProcessor:

    data = ""
    image = None

    def __init__(self):
        self.data = []

    def setImage(self, path):
        self.image = Image.open(path)

    def processOCR(self):
        temp_list = image_to_string(self.image, lang='eng', config='--psm 1')
        self.data = re.split('\n', temp_list)
        self.data = list(filter(None,  self.data))
        self.data = list(filter(lambda name: name.strip(), self.data))
        #self.display()
        self.compareWordList()

    def compareWordList(self):
        size = len(self.data)

        for i in range(0, size):
            word_from_data = self.data[i]
            similarString = ""
            updateString = ""
            temp = re.split('\s', word_from_data)
            for word in temp:
                highestRatio = 0
                for word_from_list in word_list:
                    word_from_list = word_from_list.value
                    #print(word + " v.s " + word_from_list)
                    sequenceMatcher = difflib.SequenceMatcher(None, word_from_list, word)
                    ratio = sequenceMatcher.quick_ratio()
                    if ratio > highestRatio:
                        similarString = word_from_list
                        highestRatio = ratio
                        if highestRatio >8.0:
                            break
                if highestRatio > 0.5:
                    updateString += similarString + " "
                else:
                    if(self.hasNumbers(word)):
                        word = self.replace_last(word, '9', 'g')
                    updateString += word + " "

            self.data[i] = updateString

        #self.display()

    def hasNumbers(self, stringToCheck):
        return any(char.isdigit() for char in stringToCheck)

    def replace_last(self, stringToUpdate, replace_char, charToReplace):
        head, _sep, tail = stringToUpdate.rpartition(replace_char)
        if not tail or not self.hasNumbers(tail):
            return head + charToReplace + tail
        else:
            return stringToUpdate

    def getData(self):
        return self.data

    def display(self):
        print(self.data)

