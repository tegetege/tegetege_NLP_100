class Section_5():

	'''
	[準備]
	夏目漱石の小説『吾輩は猫である』の文章（neko.txt）をCaboChaを使って係り受け解析し，
	その結果をneko.txt.cabochaというファイルに保存せよ．
	
	[使用コマンド]
	> cabocha neko.txt -o neko.txt.cabocha
	'''

	#最初のデータ形成ステップを担当する関数
	def make_data(self):
		with open("neko.txt.cabocha", "r") as f:
			data = f.read()

		data = data.split('。')
		#今回は２文目だけの解析
		#解析で出てきたゴミを削るための置換作業
		tg = data[2].replace('\u3000','')\
					.replace(' ','')\
					.replace('-','')\
					.replace('D','')
		return tg 	#ターゲット文を返す


	#係り受け解析結果の読み込み(形態素)
	def ss0(self):
		import CaboCha
		tg = self.make_data() #データ生成

		cabocha = CaboCha.Parser()
		#形態素を表す
		parsing = cabocha.parse(tg).toString(CaboCha.FORMAT_LATTICE).split('\n')
		morph_list = []
		for line in parsing :
			if len(line.split('\t')) == 1: #'*'から始まるものは解析結果なのでスキップ
				continue
			else:
				line = line.split('\t')
				res_line = line[1].split(',')
				morph = Morph(line[0],res_line[6],res_line[0],res_line[1])
				morph_list.append(morph.make_morph_str())
		#第41問目として出力する場合
		for ans in morph_list:
			print(ans)
		
		#リストを返す関数として機能させる場合
		return morph_list

	#係り受け解析結果の読み込み(文節・係り受け)
	def ss1(self):
		import CaboCha
		import re

		tg = self.make_data()		#データ生成
		cabocha = CaboCha.Parser()
		#形態素を表す、ついでに要らないものを除去		
		parsing = cabocha.parse(tg).toString(CaboCha.FORMAT_XML)\
								   .replace('<sentence>\n','')\
				 				   .replace('</sentence>\n','')\
								   .replace(' ','')\
								   .split('</chunk>\n')

		#文節番号とかをまとめたリストを取得する
		chunk_id_list = self.make_chunk_list(parsing)
		'''
		chunk_id_list[i][0] : 文節番号
		chunk_id_list[i][1] : 係り先の文節番号
		要素2 ~ 5は課題に必要ないので割愛
		'''
		#文節ごとに区切ったリスト
		chunk_word_list = self.make_chunk_set()
		#係り元文節インデックスを集めたリスト
		srcs_list = self.make_srcs_list(chunk_id_list)

		chunk_list=[]
		for i in range(len(chunk_id_list)):
			chunk = Chunk(chunk_id_list[i][0],chunk_word_list[i],srcs_list[i],chunk_id_list[i][1])
			chunk_list.append(chunk.make_format())

		for ans in chunk_list:
			print(ans)

	#係り元文節インデックス番号のリストを作成する関数
	def make_srcs_list(self,chunk_id_list):
		srcs_list = ['']*len(chunk_id_list)
		dst_list = []
		for id_list in chunk_id_list :
			#print('id : ',id_list[0])
			#print('dst : ',id_list[1])
			dst_list.append(id_list[1]) 
		for i in range(len(dst_list)):
			#strとして要素の加算を行う
			srcs_list[int(dst_list[i])] += chunk_id_list[i][0]
		return srcs_list

	#文節ごとに区切ってリストにする関数
	def make_chunk_set(self):
		import CaboCha
		tg = self.make_data() #データ生成

		cabocha = CaboCha.Parser()
		#形態素を表す
		parsing = cabocha.parse(tg).toString(CaboCha.FORMAT_LATTICE).split('\n')
		str_all_list = []
		str_list = []
		a=''
		for line in parsing :
			if len(line.split('\t')) == 1: #'*'から始まるものは解析結果なのでスキップ
				if len(str_list) != 0 : 
					str_all_list.append(a.join(str_list)) 
				str_list = []
				continue
			else:
				line = line.split('\t')
				res_line = line[1].split(',')
				str_list.append(line[0])
		return str_all_list

	#文節番号とかをまとめたリストを作成する関数
	def make_chunk_list(self,parsing_ori):
		import re
		chunk_id_list = []
		for pars_1 in parsing_ori:
			pars_1 = re.split('\n',pars_1) #最後に空リストが入るのが気に入らないけど...
			
			#後の正規表現で引っかかるものを先に除去する
			pars_1[0]= pars_1[0].replace('"','')\
								.replace('=','')\
								.replace('<','')\
								.replace('>','')
			chunk_list = []
			'''
			<chunkid="0"link="1"rel="D"score="0.931303"head="0"func="1">
			↓
			['0', '1', 'D', '0.931303', '0', '1']
			'''
			chunk_list = re.findall(r'[^a-z]+',pars_1[0])
			#空リストは追加しないようにする
			if len(chunk_list) != 0 :
				chunk_id_list.append(chunk_list)

		return chunk_id_list


#クラスMorphに加えて、文節を表すクラス
class Chunk:
	def __init__(self,chunk_id,morphs,srcs,dst):
		self.id     = chunk_id
		self.morphs	= morphs	#形態素
		self.srcs	= srcs		#係り元文節インデックス番号のリスト
		self.dst	= dst		#係り先文節インデックス番号

	def make_format(self):
	 	return '[{}]{}\tsrcs[{}]\tdst[{}]'\
			.format(self.id,self.morphs,self.srcs,self.dst)


#形態素を表すクラス
class Morph:
	'''
	(※)このクラスは、素人の100本ノック:40のコピペです.
	'''
	def __init__(self,surface,base,pos,pos1):
		self.surface = surface
		self.base	 = base
		self.pos 	 = pos
		self.pos1	 = pos1

	#出力するだけ
	def print_morph(self):
		print('surface[{}]\tbase[{}]\tpos[{}]\tpos1[{}]'\
			.format(self.surface,self.base,self.pos,self.pos1))
	#形成して返す
	def make_morph_str(self):
		return 'surface[{}]\tbase[{}]\tpos[{}]\tpos1[{}]'\
			.format(self.surface,self.base,self.pos,self.pos1)


num = input('サブセクション番号入力:')
do  = Section_5()
ss_num = 'ss' + str(num)

eval('do.' + ss_num + '()') #入力した数字の関数を実行