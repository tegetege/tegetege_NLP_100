import csv

class Section_2:
    def __init__(self):
        self.path = 'popular-names.txt'
    
    def file_read(self):
        f = open(self.path)
        data = f.read()
        f.close()
        return data

    def ss0(self):
        data = self.file_read()

        lines = data.split('\n')
        print(len(lines)-1)

    def ss1(self):
        data = self.file_read()

        print(data.replace('\t',' '))
        # print(type(data))

num = input('サブセクション番号入力:')
do  = Section_2()
ss_num = 'ss' + str(num)

eval('do.' + ss_num + '()') #入力した数字の関数を実行
