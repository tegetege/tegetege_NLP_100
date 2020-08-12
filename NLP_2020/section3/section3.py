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
        data = list(map(str, data.split('\n')))

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
            match = re.match(pattern, target_list[i])
            if match:
                print(target_list[i])
    
    def ss2(self):
        self.read_json()
        target_list =  self.target.split('\n')
        pattern = r'\[\[Category:'
        for i in range(len(target_list)):
            match = re.match(pattern, target_list[i])
            if match:
                print(target_list[i].replace('[[Category:', '').replace('|*', '').replace('|元', '').replace(']]', ''))

    def ss3(self):
        self.read_json()
        target_list = self.target.split('\n')
        for i in range(len(target_list)):
            me = re.match(r'=+\w+=+', target_list[i])
            if me != None:
                m = re.match(r'=+',me[0])
                print(me[0].replace('=', ''), ':', int(len(m[0])-1))

    def ss4(self):
        # [[File:Dayak2 2008New.jpg
        # [[ファイル:All Gizah Pyramids.jpg
        # こういうのを抜き出したい
        # 参考:https://qiita.com/moriwo/items/badc6432cb925676089a#24-%E3%83%95%E3%82%A1%E3%82%A4%E3%83%AB%E5%8F%82%E7%85%A7%E3%81%AE%E6%8A%BD%E5%87%BA
        self.read_json()
        target_list = self.target.split('\n')

        for i in range(len(target_list)):
            match = re.findall(r'\[\[(ファイル|File):([^]|]+?)(\|.*?)+\]\]', target_list[i])
            if match:
                print('match:', match[0][1])
    

num = input('サブセクション番号入力:')
do  = Section_3()
ss_num = 'ss' + str(num)

eval('do.' + ss_num + '()') #入力した数字の関数を実行
