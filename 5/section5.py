class Section_5(): 
	'''
	[準備]
	夏目漱石の小説『吾輩は猫である』の文章（neko.txt）をCaboChaを使って係り受け解析し，
	その結果をneko.txt.cabochaというファイルに保存せよ．
	
	[使用コマンド]
	> cabocha neko.txt -o neko.txt.cabocha
	'''

	#係り受け解析結果の読み込み(形態素)
	
	def ss0(self):
		import CaboCha

		with open("neko.txt.cabocha", "r") as f:
			data = f.read()

		data = data.split('。')
		#今回は２文目だけの解析
		#解析で出てきたゴミを削るための置換作業
		tg = data[2].replace('\u3000','')\
					.replace(' ','')\
					.replace('-','')\
					.replace('D','')
		cabocha = CaboCha.Parser()
		#形態素を表す
		parsing = cabocha.parse(tg).toString(CaboCha.FORMAT_LATTICE).split('\n')
		morphs = []
		for line in parsing :
			if len(line.split('\t')) == 1: #'*'から始まるものは解析結果なのでスキップ
				continue
			else:
				line = line.split('\t')
				res_line = line[1].split(',')
				Morph.print_main(line[0],res_line[6],res_line[0],res_line[1])



class Morph:
	'''
	(※)このクラスは、素人の100本ノック:40のコピペです.
	'''

	def print_main(surface,base,pos,pos1):
		print('surface[{}]\tbase[{}]\tpos[{}]\tpos1[{}]'\
            .format(surface,base,pos,pos1))




num = input('サブセクション番号入力:')
do  = Section_5()
ss_num = 'ss' + str(num)

eval('do.' + ss_num + '()') #入力した数字の関数を実行