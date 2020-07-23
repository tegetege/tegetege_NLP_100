# https://nlp100.github.io/ja/ch01.html

class Section_1:
    def ss0(self):
        text = 'stressed'
        target = list(text)
        ans = list()
        for i in reversed(target):
            ans.append(i)
        print(''.join(ans)) 

    def ss1(self):
        text = 'パタトクカシーー'
        target = list(text)
        target_index = [1, 3, 5, 7]
        ans = list()
        for i in target_index:
            ans.append(target[i-1])
        print(''.join(ans))

    def ss2(self):
        text_1 = 'パトカー'
        text_2 = 'タクシー'
        ans = list()
        for i in range(len(text_1)):
            ans.append(text_1[i])
            ans.append(text_2[i])
        print(''.join(ans))
    
    def ss3(self):
        text = 'Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics.'
        target = text.split(' ')
        ans = list()
        for i in range(len(target)):
            # 前処理
            target[i] = target[i].replace(',', '')
            target[i] = target[i].replace('.', '')

            ans.append(len(list(target[i])))
        print(ans)
    
    def ss4(self):
        text = 'Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can.'
        target_num = [1, 5, 6, 7, 8, 9, 15, 16, 19]
        target = text.split(' ')
        ans = dict()
        for i in range(len(target)):
            # 前処理
            target[i] = target[i].replace(',', '')
            target[i] = target[i].replace('.', '')
            if (i + 1) in target_num:
                ans[i+1] = list(target[i])[0]
                # print(i,':',list(target[i])[0])
            else:
                ans[i+1] = ''.join(list(target[i])[:2])
                # print(list(target[i])[:2])
        print(ans)
    
    # n-gramを作成する関数を作成する
    def ss5(self):
        text = 'I am an NLPer'
        self.n_gram('charactor', text, 2)
        self.n_gram('word', text, 2)
    
    def ss6(self):
        text_1 = 'paraparaparadise'
        text_1 = set(self.n_gram('charactor', text_1, 2))
        text_2 = 'paragraph'
        text_2 = set(self.n_gram('charactor', text_2, 2))

        # 和集合
        print('和集合: ', text_1.union(text_2))

        # 積集合
        print('積集合: ', text_1.intersection(text_2))

        # 差集合
        print('差集合: ', text_1.difference(text_2))




    # target :: character or word
    def n_gram(self, target, target_text, num):
        bi_gram = list()
        if (target == 'charactor'): # 文字区切り
            target_list = list(str(target_text))
            for i in range(len(target_list) - num+1):
                bi_gram.append(target_list[i] + target_list[i+1])
        else: # 単語区切り
            target_list = target_text.split(' ')
            for i in range(len(target_list)):
                # 前処理
                target_list[i] = target_list[i].replace(',', '')
                target_list[i] = target_list[i].replace('.', '')
            for i in range(len(target_list) - num +1):
                bi_gram.append(list([target_list[i], target_list[i+1]]))
        # print(bi_gram)
        return bi_gram
            
        


num = input('サブセクション番号入力:')
do  = Section_1()
ss_num = 'ss' + str(num)

eval('do.' + ss_num + '()') #入力した数字の関数を実行
