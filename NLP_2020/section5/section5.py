import CaboCha
from morph import Morph

class Section_5:
    def __init__(self):
        # self.parse_text() # ai.ja.txtをparseする
        self.morph = Morph()
    
    # ai.ja.txtを係り受け解析をする
    def parse_text(self):
        f = open('ai.ja.txt', 'r')
        data = f.read()
        f.close()
        parse_target = [i for i in data.split('\n') if i != ''] # '' を削ぎ落とす

        # CaboChaの解析について
        # https://qiita.com/ayuchiy/items/c3f314889154c4efa71e
        c = CaboCha.Parser()
        f_w = open('ai.ja.txt.parsed', 'w')
        for i in range(len(parse_target)):
            f_w.write(c.parse(parse_target[i]).toString(CaboCha.FORMAT_LATTICE))
        f_w.close()
        
    def ss0(self):
        self.morph.parse()

num = input('サブセクション番号入力:')
do = Section_5()
ss_num = 'ss' + str(num)

eval('do.' + ss_num + '()')
