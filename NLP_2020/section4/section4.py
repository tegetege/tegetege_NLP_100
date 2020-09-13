import MeCab
import matplotlib as mpl
import matplotlib.pyplot as plt
mpl.rcParams['font.family'] = 'MS Gothic'

class Section_4:
    def __init__(self):
        self.mecab = MeCab.Tagger('-d /usr/local/lib/mecab/dic/mecab-ipadic-neologd')
        self.target = list()
        self.list_formated = list()
        self.word_freq_sorted = list()
        self.neko_cooccurrence_freq_sorted = list()
    
    # neko.txt を mecab にかけた neko.txt.mecab を作成
    # 解析結果
    # → 表層形\t品詞,品詞細分類1,品詞細分類2,品詞細分類3,活用型,活用形,原形,読み,発音
    def ss_neko(self):
        f = open('neko.txt', 'r')
        data = f.read()

        f = open('neko.txt.mecab', 'w')
        f.write(self.mecab.parse(data))
        print('書き込み完了')

    def read_neko_mecab(self):
        f = open('neko.txt.mecab', 'r')
        data = f.read()
        f.close()
        self.target = list(map(str, data.split('\n')))

    # neko.txt.mecab を整形して self.list_formated に list 形式で入れる
    def neko_format(self):
        print('neko.txt.mecab format start.')
        self.read_neko_mecab()
        line_list = list()
        for i in range(len(self.target)):
            try:
                line = self.target[i].split('\t')
                surface = line[0]
                other = line[1].split(',')
                neko_dict = {
                    'surface' : line[0],
                    'base' : other[6],
                    'pos' : other[0],
                    'pos1' : other[1]
                }
                line_list.append(neko_dict)
                if neko_dict['surface'] == '。':
                    self.list_formated.append(line_list)
                    line_list = list()
            except IndexError:
                pass
        print('neko.txt.mecab format goal.')

    # 単語の出現頻度を求める
    def make_word_freq(self):
        word_freq = dict()
        for i in range(len(self.list_formated)):
            for j in range(len(self.list_formated[i])):
                if (self.list_formated[i][j]['surface'] in word_freq):
                    word_freq[self.list_formated[i][j]['surface']] += 1
                else:
                    word_freq[self.list_formated[i][j]['surface']] = 1
        
        self.word_freq_sorted = sorted(word_freq.items(), key=lambda x:x[1], reverse=True)
    
    def neko_cooccurrence_freq(self):
        neko_cooccurrence_freq = dict()
        for i in range(len(self.list_formated)):
            for j in range(len(self.list_formated[i])):
                if (self.list_formated[i][j]['surface'] in '猫'):
                    for k in range(len(self.list_formated[i])):
                        if (self.list_formated[i][k]['surface'] in neko_cooccurrence_freq):
                            neko_cooccurrence_freq[self.list_formated[i][k]['surface']] += 1
                        else:
                            neko_cooccurrence_freq[self.list_formated[i][k]['surface']] = 1
                else:
                    break
        self.neko_cooccurrence_freq_sorted = sorted(neko_cooccurrence_freq.items(), key=lambda x:x[1], reverse=True)
        self.neko_cooccurrence_freq_sorted.pop(0)
    
    def ss0(self):
        self.neko_format()
        for i in range(5):
            print(self.list_formated[i])

    def ss1(self):
        self.neko_format()
        target = set()
        for i in range(len(self.list_formated)):
            for j in range(len(self.list_formated[i])):
                if self.list_formated[i][j]['pos'] == '動詞':
                    target.add(self.list_formated[i][j]['surface'])
        print(target)
    
    def ss2(self):
        self.neko_format()
        target = set()
        for i in range(len(self.list_formated)):
            for j in range(len(self.list_formated[i])):
                if self.list_formated[i][j]['pos'] == '動詞':
                    target.add(self.list_formated[i][j]['base'])
        print(target)
    
    def ss3(self):
        self.neko_format()
        for i in range(len(self.list_formated)):
            for j in range(1, len(self.list_formated[i])-1):
                if (self.list_formated[i][j]['surface'] == 'の' and self.list_formated[i][j-1]['pos'] == '名詞' and self.list_formated[i][j+1]['pos'] == '名詞'):
                    print(self.list_formated[i][j-1]['surface'] + self.list_formated[i][j]['surface'] + self.list_formated[i][j+1]['surface'])

    def ss4(self):
        self.neko_format()
        target = list()
        ans = []
        for i in range(len(self.list_formated)):
            for j in range(len(self.list_formated[i])-1):
                if (self.list_formated[i][j]['pos'] == '名詞'):
                    if (self.list_formated[i][j+1]['pos'] == '名詞'):
                        target.append(self.list_formated[i][j]['surface'])
                        continue
                    else:
                        target.append(self.list_formated[i][j]['surface'])
                        break
            if len(ans) < len(target):
                ans = target
            target = list()
        print(ans)
    
    def ss5(self):
        self.neko_format()
        self.make_word_freq()
        for i in range(10):
            print(self.word_freq_sorted[i])
    
    def ss6(self):
        self.neko_format()
        self.make_word_freq()

        # 上位10のmapを取り出して、そのkey,valueのリストを作成する
        target_key = list(map(lambda x: x[0], self.word_freq_sorted[:10]))
        target_value = list(map(lambda x: x[1], self.word_freq_sorted[:10]))
        rank = list(range(10))

        # グラフ表示
        plt.bar(rank, target_value, tick_label=target_key)
        plt.title(' 単語の出現頻度 上位10 ')
        plt.show()
    
    def ss7(self):
        self.neko_format()

        # "猫" との共起頻度(cooccurrence freq)を求める
        self.neko_cooccurrence_freq()
        # print(self.neko_cooccurrence_freq_sorted)
        
        # 上位10を取り出して、そのkey,valueのリストを作成する
        target_key = list(map(lambda x: x[0], self.neko_cooccurrence_freq_sorted[:10]))
        target_value = list(map(lambda x: x[1], self.neko_cooccurrence_freq_sorted[:10]))
        rank = list(range(10))
        
        # グラフ表示
        plt.bar(rank, target_value, tick_label=target_key)
        plt.title(' "猫" との共起頻度 上位10 ')
        plt.show()



num = input('サブセクション番号入力:')
do  = Section_4()
ss_num = 'ss' + str(num)

eval('do.' + ss_num + '()') #入力した数字の関数を実行


'''
# 基本的な使い方

mecab = MeCab.Tagger ('-d /usr/local/lib/mecab/dic/mecab-ipadic-neologd')

text = '解析したいテキスト'
mecab.parse('')#文字列がGCされるのを防ぐ
node = mecab.parseToNode(text)
while node:
    #単語を取得
    word = node.surface
    #品詞を取得
    pos = node.feature.split(",")[1]
    print('{0} , {1}'.format(word, pos))
    #次の単語に進める
    node = node.next

'''
