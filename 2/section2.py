class Section_2():

	def __init__(self):
		self.input_file = 'hightemp.txt' #読み込むtxtファイル


	#指定ファイルを読み込み、ファイルの中身を返す
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

num = input('サブセクション番号入力:')
do  = Section_2()
ss_num = 'ss' + str(num)

eval('do.' + ss_num + '()') #入力した数字の関数を実行

