"""Word Finder: finds random words from a dictionary."""

import random

# "/Users/barkliegriggs/Documents/Springboard/Python/python-oo-practice/words.txt", "r")

class WordFinder:
    
    def __init__(self, path):
        self.path = path
    
    def random(self):
        """Generates a random word from and .txt file granted you use the file's path as an input when creating a new instance of the WordFinder Class"""
        with open(self.path) as f:
            contents_of_file = f.read()
            lines = contents_of_file.splitlines()
            line_number = random.randrange(0, len(lines))
        return lines[line_number]

    # def random(self):



class SpecialWordFinder(WordFinder):

    def __init__(self, path):
        super().__init__(path)
    
    def filtered_random(self):
        # def get_line():
        #     with open(self.path) as f:
        #         contents_of_file = f.read()
        #         lines = contents_of_file.splitlines()
        #         line_number = random.randrange(0, len(lines))
        #     return lines[line_number]

        success = False

        while success == False:
            line = super().random()
            if line != "" and line[0] != '#':
                print(line[0])
                success = True
                return line
            
            else:
                # line == "" or line[0] == '#':
                success = False


        
        
    
        






      
