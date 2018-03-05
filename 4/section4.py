

class Section_4(): 
	'''
	[問い]
	夏目漱石の小説『吾輩は猫である』の文章（neko.txt）をMeCabを使って形態素解析し，
	その結果をneko.txt.mecabというファイルに保存せよ．
	
	[使用コマンド]
	$mecab -d /usr/local/lib/mecab/dic/mecab-ipadic-neologd neko.txt -o neko.txt.mecab
	
	辞書にはオプションで、"mecab-ipadic-NEologd"を利用
	'''

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
		word_list = [] #単語部分のリスト
		morphemes = [] #形態素部分のリスト

		with open("neko.txt.mecab", "r") as f:
			data = f.read()

		data = data.split('\n') #データ形成 : リスト化
		#データ形成 : 不要なEOS要素を削除
		while 'EOS' in data:
			data.remove('EOS')
		for i in range(len(data)):
			data[i]= data[i].split('\t') #データ形成 2次元配列化
			word_list.append(data[i][0]) #単語の部分をリスト化
			if len(data[i]) > 1:
				morphemes.append(data[i][1].split(',')) #形態素部分をリスト化
			else:
				pass
		
		for i in range(len(word_list)):
			print(i)
			print('surface',':',word_list[i])
			print('base',':',morphemes[i][6])
			print('pos',':',morphemes[i][0])
			print('pos1',':',morphemes[i][1])
			print('-------------------------')	
		

num = input('サブセクション番号入力:')
do  = Section_4()
ss_num = 'ss' + str(num)

eval('do.' + ss_num + '()') #入力した数字の関数を実行