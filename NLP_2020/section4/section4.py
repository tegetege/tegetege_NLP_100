import MeCab

class Section_4:
    def __init__(self):
        self.mecab = MeCab.Tagger('-d /usr/local/lib/mecab/dic/mecab-ipadic-neologd')
        self.target = list()
        self.list_formated = list()
    
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
