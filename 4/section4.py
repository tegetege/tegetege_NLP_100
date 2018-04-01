

class Section_4(): 
	'''
	[問い]
	夏目漱石の小説『吾輩は猫である』の文章（neko.txt）をMeCabを使って形態素解析し，
	その結果をneko.txt.mecabというファイルに保存せよ．
	
	[使用コマンド]
	$mecab -d /usr/local/lib/mecab/dic/mecab-ipadic-neologd neko.txt -o neko.txt.mecab
	
	辞書にはオプションで、"mecab-ipadic-NEologd"を利用
	'''

	'''
	[概要]
	・neko.txt ファイルをmecabに通したものがneko.txt.mecab
	・self.word_listはneko.txt.mecabの単語部分のリスト
	・self.morphemesはneko.txt.mecabの形態素部分のリスト
	'''

	def __init__(self):
		#クラス内でデータを格納するリストを管理
		self.word_list = [] #単語部分のリスト
		self.morphemes = [] #形態素部分のリスト,word_listに同期

	#形態素解析結果の読み込み
	def ss0(self):
		'''
		こんな感じで表現したい
		{
		  surface: '皇帝',
		  base: '皇帝',
		  pos: '名刺',
		  pos1: '一般'
		},
		'''

		'''
		########
		データ形成をする上でエラーが出るため、neko.txt.mecabの最後の
		空白行を消去した。
		########
		'''

		with open("neko.txt.mecab", "r") as f:
			data = f.read()

		data = data.split('\n') #データ形成 : リスト化
		#データ形成 : 不要なEOS要素を削除
		while 'EOS' in data:
			data.remove('EOS')
		for i in range(len(data)):
			data[i]= data[i].split('\t') #データ形成 2次元配列化
			self.word_list.append(data[i][0]) #単語の部分をリスト化
			if len(data[i]) > 1: #エラー回避
				self.morphemes.append(data[i][1].split(',')) #形態素部分をリスト化
			else:
				pass
		
		for i in range(len(self.word_list)):
			print(i)
			print('surface',':',self.word_list[i])
			print('base',':',self.morphemes[i][6])
			print('pos',':',self.morphemes[i][0])
			print('pos1',':',self.morphemes[i][1])
			print('-------------------------')	
		
	def make_data(self):

		with open("neko.txt.mecab", "r") as f:
			data = f.read()

		data = data.split('\n') #データ形成 : リスト化
		#データ形成 : 不要なEOS要素を削除
		while 'EOS' in data:
			data.remove('EOS')
		for i in range(len(data)):
			data[i]= data[i].split('\t') #データ形成 2次元配列化
			self.word_list.append(data[i][0]) #単語の部分をリスト化
			if len(data[i]) > 1:
				self.morphemes.append(data[i][1].split(',')) #形態素部分をリスト化
			else:
				pass

	#動詞
	def ss1(self):
		self.make_data() #データ生成
		for i in range(len(self.word_list)):
			if self.morphemes[i][0] =='動詞':
				print('-------------------------')
				print('surface',':',self.word_list[i])
				print('pos',':',self.morphemes[i][0])

	#動詞の原形
	def ss2(self):
		self.make_data() #データ生成
		for i in range(len(self.word_list)):
			if self.morphemes[i][0] =='動詞':
				print('-------------------------')
				print('surface',':',self.word_list[i])
				print('base',':',self.morphemes[i][6])

	#サ変名詞
	def ss3(self):
		'''
		>見当	名詞,サ変接続,*,*,*,*,見当,ケントウ,ケントー

		これを抜き出してくれば良いだけなので難しくない
		'''
		self.make_data() #データ生成
		for i in range(len(self.word_list)):
			if self.morphemes[i][0] == '名詞' and self.morphemes[i][1] == 'サ変接続':
				print('-------------------------')
				print('サ変名詞',':',self.word_list[i])


		

num = input('サブセクション番号入力:')
do  = Section_4()
ss_num = 'ss' + str(num)

eval('do.' + ss_num + '()') #入力した数字の関数を実行