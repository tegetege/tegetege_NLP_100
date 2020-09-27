import re
import sre_constants

class Morph:
    def __init__(self):
        self.data = list()
        self.surface = str()
        self.base = str()
        self.pos = str()
        self.pos1 = str()

    def __read_target(self):
        f_r = open('ai.ja.txt.parsed', 'r')
        data = f_r.read()
        f_r.close()
        data 
        self.data = data.split('\n')
    
    def __print(self):
        print(self.surface, ':', self.base, ':', self.pos, ':', self.pos1)

    def parse(self):
        self.__read_target()
        
        for i in range(len(self.data)):
            if self.data[i] != 'EOS':
                if not re.match(r'\* ', self.data[i]):
                    try:
                        parse_1 = self.data[i].split('\t')[0]
                        parse_2 = self.data[i].split('\t')[1].split(',')
                        self.surface = parse_1
                        self.base = parse_2[6]
                        self.pos = parse_2[0]
                        self.pos1 = parse_2[1]
                        if i <= 20:
                            self.__print()
                    except IndexError:
                        pass # 最後の一行を削ればいいんだけど、めんどくさがって...
    