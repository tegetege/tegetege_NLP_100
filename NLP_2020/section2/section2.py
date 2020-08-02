import csv

class Section_2:
    def __init__(self):
        self.path = 'popular-names.txt'
        self.path_col1 = 'col1.txt'
        self.path_col2 = 'col2.txt'
        self.merged_file = 'merged_file.txt'
    
    def file_read(self,path):
        f = open(path)
        data = f.read()
        f.close()
        return data

    def get_writable(self, path):
        f = open(path, 'w')
        return f

    def ss0(self):
        data = self.file_read(self.path)

        lines = data.split('\n')
        print(len(lines)-1)

    def ss1(self):
        data = self.file_read(self.path)
        print(data.replace('\t',' '))

    def ss2(self):
        data = self.file_read(self.path)
        data_list = data.split('\n')
        col1 = self.get_writable(self.path_col1)
        col2 = self.get_writable(self.path_col2)

        for i in range(len(data_list)):
            data = data_list[i].split('\t')
            if len(data) >= 2:
                print(data)
                col1.write(data[0]+'\n')
                col2.write(data[1]+'\n')
        print('書き込み完了')
        col1.close()
        col2.close()
    
    def ss3(self):
        data_col1 = self.file_read(self.path_col1)
        data_col1 = data_col1.split('\n')
        data_col2 = self.file_read(self.path_col2)
        data_col2 = data_col2.split('\n')
        merged_file = self.get_writable(self.merged_file)

        for i in range(len(data_col1)):
            data = data_col1[i] + '\t' + data_col2[i] + '\n'
            print(data)
            merged_file.write(data)
        print('書き込み完了')
        merged_file.close()

    def ss4(self):
        data = self.file_read(self.path)
        lines = data.split('\n')
        target = int(input('表示する行数を入力 : '))
        for i in range(target):
            print(i+1, ' : ', lines[i])
    
    def ss5(self):
        data = self.file_read(self.path)
        lines = data.split('\n')
        lines.pop(-1)
        target = int(input('表示する行数を入力(末尾から) : '))
        for i in range(-1, (target+1)*(-1), -1):
            print(i*(-1), ' : ', lines[i])

    def ss6(self):
        N = int(input('何分割にする？ : '))
        data = self.file_read(self.path)
        lines = data.split('\n')
        print(N, '分割にする場合、一つ', (len(lines)-1) // N, '行' )
    
    def ss7(self):
        data = self.file_read(self.path)
        lines = data.split('\n')
        lines.pop(-1)
        lines_splited = list(map(lambda l : l.split('\t'), lines))
        target = list(map(lambda l : l[0], lines_splited))
        print(set(target))
    
    def ss8(self):
        data = self.file_read(self.path)
        lis = data.split('\n')
        lis.pop(-1)
        lis_splited = list(map(lambda l : l.split('\t'),lis))
        lis_sorted = sorted(lis_splited, reverse=True, key=lambda x: x[2])
        print(lis_sorted[:10])

    def ss9(self):
        data = self.file_read(self.path)
        lis = data.split('\n')
        lis.pop(-1)
        lis = list(map(lambda l : l.split('\t'),lis))
        lis = list(map(lambda l : l[0],lis)) # 1コラム目の文字列のリスト生成

        # 利用頻度情報を入れた辞書作成
        index_dict = dict()
        for i in range(len(lis)):
            if lis[i] in index_dict:
                index_dict[lis[i]] += 1
            else:
                index_dict[lis[i]] = 1
        # 辞書のソート(昇順しかできなかった...)
        index_sorted = sorted(index_dict.items(), key=lambda x:x[1])
        for i in range(len(index_sorted)-1, -1, -1):
            print(index_sorted[i][0])
        


num = input('サブセクション番号入力:')
do  = Section_2()
ss_num = 'ss' + str(num)

eval('do.' + ss_num + '()') #入力した数字の関数を実行
