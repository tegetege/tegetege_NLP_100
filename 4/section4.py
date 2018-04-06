

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
				



	'''
	(※)問題を読み違えていたため、このコメント部分は全てお釈迦
	#名詞の連接
	def ss5(self):
		
		#名詞の連接（連続して出現する名詞）を最長一致で抽出せよ．

		#最長一致を、2つのリストを利用して実現する。
		
		noun_continuous_count = 0	#名詞の連接回数をカウント

		self.make_data() #データ生成

		for i in range(len(self.word_list)):
			judge_ans = int(self.judge_noun(i))
			if judge_ans == 0:
				noun_continuous_count += 1
			else:
				#名詞じゃない場合はカウントリセット
				noun_continuous_count = 0 
			#カウント数が最長になった時にカウント数を更新する
			self.compare_count(noun_continuous_count,i)
		print('リスト番号 :' , self.longest_list_num)
		print('連接回数   :' , self.longest_count)
		start = int(self.longest_list_num)
		end   = int(self.longest_list_num + self.longest_count)
		print(self.word_list[start:end])
		print(self.morphemes[start][0])

	#SS5で利用関数
	def compare_count(self,continuous_count,list_num):
		
		#連接回数を比較して、カウントの入れ替えが必要な時は、入れ替える
		
		if self.longest_count < continuous_count :
			self.longest_count = continuous_count
			self.longest_list_num = int(list_num - continuous_count)
		return

	#SS5で利用関数
	def judge_noun(self,list_num):
		
		#形態素結果が名詞なら"1"を返して、それ以外なら"0"を返す
		
		if self.morphemes[list_num][0] == '名詞':
			return 1
		else:
			return 0
	'''

num = input('サブセクション番号入力:')
do  = Section_4()
ss_num = 'ss' + str(num)

eval('do.' + ss_num + '()') #入力した数字の関数を実行