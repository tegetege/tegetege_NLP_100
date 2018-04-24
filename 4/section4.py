

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
		'''
		(※)問題を読み違えていたため、このコメント部分はお釈迦
		#ss5で利用変数
		#self.longest_list_num = 0 #最も長い連接の最初のリストナンバー
		#self.longest_count = 0	  #最も長い連接回数を記録
		'''
	
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

	#「AのB」
	def ss4(self):
		'''
		2つの名詞が「の」で連結されている名詞句を抽出せよ
		・「の」しか入っていないword_list番号を記録して、その前後の形態素を確認する

		'''
		self.make_data() #データ生成

		for i in range(len(self.word_list)):
			if self.word_list[i] == 'の':
				if self.morphemes[i-1][0] == '名詞' and self.morphemes[i+1][0] == '名詞':
					print('-------------------------')
					print('番号:',i)
					print(self.word_list[i-1],self.word_list[i],self.word_list[i+1])
					print(self.morphemes[i-1][0],self.morphemes[i][0],self.morphemes[i+1][0])
	
	#名詞の連接
	def ss5(self):
		'''
		(※)出題内容がわからなかったため「素人の言語処理100本ノック」を
		　　参考にさせていただきました。
		https://qiita.com/segavvy/items/bda3a16d8bb54bd01f73
		'''
		self.make_data() #データ生成

		noun_list = []	#重複ありのリスト
		nouns = []		#一時的に名詞を保持するリスト

		for i in range(len(self.word_list)):
			if self.morphemes[i][0] == '名詞' :
				nouns.append(self.word_list[i]) #一時保持
			else:
				#名詞ではないときは、一時保持リストからアペンドして本リストに入れる
				if len(nouns) > 1:
					noun_list.append(''.join(nouns))
				nouns = [] 

		nouns_set = set(noun_list) #集合化することで、重複を消す!! ⇦ これ、知った時に感動した
		print(nouns_set)
				
	#単語の出現頻度
	def ss6(self):
		'''
		文章中に出現する単語とその出現頻度を求め，出現頻度の高い順に並べよ．
		参考:http://www.freia.jp/taka/blog/356/index.html
		'''
		self.make_data() #データ生成

		words_dic = {}

		#カウンティング
		for i in range(len(self.word_list)):
			#.get()メソッドを利用すれば、辞書にアイテムが無い場合の初期値を設定できる
			words_dic[self.word_list[i]] = words_dic.get(self.word_list[i],0) + 1

		#辞書の降順ソート
		for k, v in sorted(words_dic.items(), key=lambda x: -x[1]):
			#降順 → x: -x[1] 昇順　→ x: x[1]
			if int(v) > 500: #500以下は表示しない
 				print(str(k) + ": " + str(v))

	#ss6と同じもの、最後に辞書データをreturnする
	def sorted_word_dic(self):
		self.make_data() #データ生成

		words_dic = {}

		#カウンティング
		for i in range(len(self.word_list)):
			#.get()メソッドを利用すれば、辞書にアイテムが無い場合の初期値を設定できる
			words_dic[self.word_list[i]] = words_dic.get(self.word_list[i],0) + 1

		#辞書の降順ソート
		return	sorted(words_dic.items(), key=lambda x: -x[1])

	#ソートしていない単語と出現頻度の辞書データをreturnする
	def word_dic(self):
		self.make_data() #データ生成

		words_dic = {}

		#カウンティング
		for i in range(len(self.word_list)):
			#.get()メソッドを利用すれば、辞書にアイテムが無い場合の初期値を設定できる
			words_dic[self.word_list[i]] = words_dic.get(self.word_list[i],0) + 1

		#辞書の降順ソート
		return	words_dic
		
	#頻度上位10語
	def ss7(self):
		'''
		出現頻度が高い10語と語とその出現頻度をグラフで表示すること
		matplotlibを利用する
		'''
		import matplotlib.pyplot as plt
		import numpy as np
		#日本語を表示するフォントを指定する
		import matplotlib as mpl 
		mpl.rcParams['font.family'] = 'AppleGothic'

		sorted_dic = {}
		sorted_dic = self.sorted_word_dic() #出現頻度によってソート済みのリストを受け取る
		'''
		sorted_dic = [('の', 9114), ('。', 7484), ('、', 6772), ....]
		'''
		label = []
		count  = []

		for i in range(0,10):
			
			label.append(sorted_dic[i][0]) #x軸の名前
			count.append(sorted_dic[i][1]) #y軸
		
		left = np.array(range(0,10)) #x軸には、0から始まるリストを入れる
		height = np.array(count) 

		plt.bar(left,height,tick_label=label, align="center")
		plt.show()

	#ヒストグラム
	def ss8(self):
		'''
		単語の出現頻度のヒストグラム（横軸に出現頻度，縦軸に出現頻度をとる単語の種類数を棒グラフで表したもの）を描け．
		X軸　出現頻度
		Y軸　単語の種類数
		[1]
		参考になりそうなサイト：
		https://pythondatascience.plavox.info/matplotlib/%E3%83%92%E3%82%B9%E3%83%88%E3%82%B0%E3%83%A9%E3%83%A0
		[2]
		1つのキーに複数の値が対応するハッシュを作る:
		http://lightson.dip.jp/zope/ZWiki/1191_e3_81_a4_e3_81_ae_e3_82_ad_e3_83_bc_e3_81_ab_e8_a4_87_e6_95
		_b0_e3_81_ae_e5_80_a4_e3_81_8c_e5_af_be_e5_bf_9c_e3_81_99_e3_82_8b_e3_83_8f_e3_83_83_e3_82_b7_e3_83
		_a5_e3_82_92_e4_bd_9c_e3_82_8b

		'''
		import matplotlib.pyplot as plt
		#日本語を表示するフォントを指定する
		import matplotlib as mpl 
		mpl.rcParams['font.family'] = 'AppleGothic'

		word_dic = {}
		word_dic = self.word_dic() #出現頻度によってソート済みのリストを受け取る
		count_frequency = {} #出現回数と、その単語のリストが入った辞書

		for k,v in word_dic.items():
			count_frequency.setdefault(v,[]).append(k) #サイト[2]を参考にした
		

		'''
		count_frequency =
		{...,278: ['寒月'], 974: ['です'], 97: ['ええ'], 
		146: ['私'], 343: ['迷亭'], 433: ['…']...}

		↓
		↓
		
		ヒストグラムに投げるデータ(リスト型)
		[1,1,1,1,....,234,234,235,235,235,236,236....]

		'''


		count_frequency_sort = sorted(count_frequency.items(), key=lambda x: x[0])
		hist_list = []
		
		for i in range(len(count_frequency_sort)):

			for j in range(len(count_frequency_sort[i][1])):
				#ここ頭悪い
				#出現回数分、出現回数をリストに追加する
				hist_list.append(int(count_frequency_sort[i][0]))
		#ヒストグラムにデータをセットしていく		
		plt.hist(
			hist_list,
			bins = 20,
			range=(1,20))
		plt.xlim(xmin=1, xmax=20)

		# グラフのタイトル、ラベル指定
		plt.title("38. ヒストグラム")
		plt.xlabel('出現頻度')
		plt.ylabel('単語の種類数')

		# グリッドを表示
		plt.grid(axis='y')

		# 表示
		plt.show()


	#出現頻度が入ったリストが帰ってくる
	def frequency_list(self):
		import matplotlib.pyplot as plt

		word_dic = {}
		word_dic = self.word_dic() #出現頻度によってソート済みのリストを受け取る
		count_frequency = {} #出現回数と、その単語のリストが入った辞書

		for k,v in word_dic.items():
			count_frequency.setdefault(v,[]).append(k) 

		count_frequency_sort = sorted(count_frequency.items(), key=lambda x: x[0])

		return count_frequency_sort


	#Zipfの法則	
	def ss9(self):
		'''
		単語の出現頻度順位を横軸，その出現頻度を縦軸として，両対数グラフをプロットせよ．
		'''
		import matplotlib.pyplot as plt
		import numpy as np
		#日本語を表示するフォントを指定する
		import matplotlib as mpl 
		mpl.rcParams['font.family'] = 'AppleGothic'

		frequency_2D_list = self.frequency_list()
		frequency_list = []		#x軸:順位
		word_count_list = []	#y軸:出現頻度
		for i in range(len(frequency_2D_list)):
			frequency_list.append(frequency_2D_list[i][0])
			word_count_list.append(len(frequency_2D_list[i][1]))
		
		plt.xscale('log')
		plt.yscale('log')

		plt.xlim(1,len(frequency_list)+1)
		plt.ylim(1,word_count_list[0])

		x = frequency_list
		y = word_count_list

		plt.title("39. Zipfの法則")

		plt.plot(x,y,'o')
		plt.show()
		
		




num = input('サブセクション番号入力:')
do  = Section_4()
ss_num = 'ss' + str(num)

eval('do.' + ss_num + '()') #入力した数字の関数を実行