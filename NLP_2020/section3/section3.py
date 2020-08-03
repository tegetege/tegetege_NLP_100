import re
import json


class Section_3:
    def __init__(self):
        self.target = str()
        pass


    def read_json(self):
        f = open('jawiki-country.json', 'r')
        data = f.read()
        f.close()
        data = list(map(str,data.split('\n')))

        for i in range(len(data)):
            data_json = json.loads(data[i])
            if data_json['title'] == 'イギリス':
                self.target = data_json['text']
                break

    def ss0(self):
        self.read_json()
        print(self.target) # wikiの本文が全部でるよ
    
    def ss1(self):
        # [[Category:イギリス|*]] この辺りを抜き出すのかな
        self.read_json()
        target_list =  self.target.split('\n')

        pattern = r'\[\[Category:'
        for i in range(len(target_list)):
            match = re.match(pattern,target_list[i])
            if match:
                print(target_list[i])
        

num = input('サブセクション番号入力:')
do  = Section_3()
ss_num = 'ss' + str(num)

eval('do.' + ss_num + '()') #入力した数字の関数を実行
