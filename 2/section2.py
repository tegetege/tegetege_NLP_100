class Section_2():

	def __init__(self):
		self.input_file = 'hightemp.txt' #読み込むtxtファイル


	#指定ファイル'hightemp.txt'を読み込み、生データを返す
	def file_read(self):
		f = open(self.input_file) #ファイルオープン
		data = f.read()			  #データ読み込み
		f.close()				  #ファイルクローズ
		return data


	#行数のカウント
	def ss0(self):
		data = self.file_read() #ファイルのデータを受け取る

		#改行で区切りを入れて、リスト化する
		lines = data.split('\n')
		print(len(lines))


	#タブをスペースに置換
	def ss1(self):
		data = self.file_read()

		print(data)
		print('--------------')
		t_data = data.replace('\t',' ') #分ち書き処理

		print(t_data)

		'''
		unixコマンド(expand)での方法

		$ expand -t 4 hightemp.txt

		４はタブ置換後のスペース幅指定
		'''


	#1列目をcol1.txtに,2列目をcol2.txtに保存
	def ss2(self):
		data = self.file_read()

		lines = data.split('\n') #ラインでリスト化

		#ファイルを書き込みモードでオープン
		fout1 = open('col1.txt','w')
		fout2 = open('col2.txt','w')
		for i in range(len(lines)):
			#各行をタブで区切って必要なところを指定して取得
			row1 = lines[i].split('\t')[0] 
			row2 = lines[i].split('\t')[1]
			#書き込み
			print(row1,file=fout1)
			print(row2,file=fout2)

		
		fout1.close()
		fout2.close() 
		print('書き込み完了')


	#col1.txtとcol2.txtをマージ
	def ss3(self):
		#必要なデータファイルを読み込み、リスト化する
		f_1 = open('col1.txt')
		f_2 = open('col2.txt') 
		data_1 = f_1.read()
		data_2 = f_2.read()	
		data_1_list = data_1.split('\n')	
		data_2_list = data_2.split('\n')	  
		f_1.close()
		f_2.close()				  
		
		#書き込むファイルを読み込みモードでオープン
		fout = open('marge_col1_col2.txt','w')
		#フォーマット関数でデータを形成して書き込む
		for i in range(len(data_1_list)):
			row = '{}\t{}'.format(data_1_list[i],data_2_list[i]) #フォーマット関数

			print(row,file=fout,end='\n')
		fout.close()
		print('書き込み完了')


	#先頭からN行を出力
	def ss4(self):
		line_num = input('先頭から何行を出力する？')
		
		#データを読み込んで、リスト化
		data = self.file_read()
		data_list = data.split('\n')

		for i in range(int(line_num)):
			print(data_list[i])


	#末尾のN行を出力
	def ss5(self):
		line_num = input('末尾から何行を出力する？')

		#データを読み込んで、リスト化
		data = self.file_read()
		data_list = data.split('\n')

		for i in range(1,int(line_num)+1):
			i = '-' + str(i)  #マイナスをつけて、リストの逆回しを実現
			print(data_list[int(i)])


	#ファイルをN分割する
	def ss6(self):
		'''	
		・入力ファイルを"hightemp.txt"とする

		・リストの個数が割り切れない時は、初めの方の分割個数を多くすることで調節
		・"readline()"は毎行ずつの処理なので、リストの個数で管理する必要がない
		　最後に忘れずにclose()

		'''
		division_num = input('ファイルを何分割する？')
		count = 0
		
		#ファイルデータを取得しリスト化
		data = self.file_read()
		list_data = data.split('\n')
		
		#一つのファイル内のリストの個数を計算
		num_list_each_division = len(list_data) / int(division_num)

		f = open('hightemp.txt')

		#(※)int型かどうかの判定で、リストの個数が割り切れるかの判定をする
		if num_list_each_division == int(num_list_each_division): #リストが割り切れる
			
			for i in range(int(division_num)) : #分割数だけ繰り返す
				print(i,'分割')
				for j in  range(int(num_list_each_division)): #分割内の個数分繰り返す
					print(f.readline())

		else: #リストが割り切れず、余り処理が必要
			
			surplus_num = len(list_data) % int(division_num) #余剰

			for i in range(int(division_num)) :
				print(i,'分割')
				if i < int(surplus_num) : #余剰分だけ、　分割内個数を+1でリストを出力
					for j in range(int(num_list_each_division)+1): #+1
						print(f.readline())
				else:
					for j in range(int(num_list_each_division)):
						print(f.readline())
		
		f.close() #忘れずにファイルクローズ


	#1列目の文字列の異なり
	def ss7(self):
		ans_set = ()

		data = self.file_read()
		lines = data.split('\n') 

		for i in range(len(lines)):
			chr_list = list(lines[i].split('\t')[0]) #一文字ずつリスト化できる
			for j in range(len(chr_list)):

				ans_set = set(ans_set) | set(chr_list)        #和集合
				#ans_set = set(ans_set).union(set(chr_list))  #こっちでもOK

		print(ans_set)


	#各行を3コラム目の数値の降順にソート
	def ss8(self):
		row_3 = []

		data = self.file_read()
		lines = data.split('\n')

		for i in range(len(lines)):
			row_3.append(lines[i].split('\t')[2])

		row_3.sort(reverse = True) #ここでprintしてもNoneが帰ってくるだけ
		#"reverse = Trueを消せば昇順になる"
		print(row_3)

	#各行の1コラム目の文字列の出現頻度を降順に表示
	def ss9(self):
		'''
		方針
		・辞書で一つずつ数える
		・キー値の降順にキーを表示する
		'''

		#データの数え上げで利用する辞書
		row_1 = {} #dic

		#データの読み取りと、リスト化
		data = self.file_read()
		lines = data.split('\n')

		#データの数え上げを行う
		for i in range(len(lines)):
			#辞書のキーを見て、同一のキーがあるかどうかの判定
			if row_1.get(lines[i].split('\t')[0]) == None :
				#print('同じものなし')
				#辞書型にデータを形成
				key = lines[i].split('\t')[0]

				add_dic = {key:1}
				row_1.update(add_dic)#辞書登録
			else:
				#print('同じものあり')
				#キー値を+1
				#辞書型にデータを形成
				key = lines[i].split('\t')[0]
				value = row_1.get(lines[i].split('\t')[0])

				add_dic = {key :value +1}
				row_1.update(add_dic)#辞書登録

		#使用頻度の高い順にキーを表示する
		for (k,v) in sorted(row_1.items(), key=lambda x: -x[1]):
			print('キー: ',k , '値: ',v)
			'''
			このソート方法については、以下のサイトを参照
			https://qiita.com/n10432/items/e0315979286ea9121d57

			無名関数"lambda"はよくわからずじまい...
			'''


			

num = input('サブセクション番号入力:')
do  = Section_2()
ss_num = 'ss' + str(num)

eval('do.' + ss_num + '()') #入力した数字の関数を実行

