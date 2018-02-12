import json


class Section_3():

	#ss1-ss9で利用 jsonを読んでデータを返す
	def read_json(self):

		f = open('jawiki-country.json','r')

		for count,line in enumerate(f): 
			data_json = json.loads(line)
			if data_json['title'] == 'イギリス':
				text_data = data_json['text']
				break
		f.close()		#ファイルクローズをお忘れなく	
		return text_data

	#JSONデータの読み込み
	#read_jsonとやってることは同じ
	def ss0(self):


		#jsonファイルは一行ずつ読まないと怒られる...
		f = open('jawiki-country.json','r')

		for count,line in enumerate(f): 
			'''
			enumerate()はカウントと値を返すので、
			for文の引数も"num,line"となる
			'''
			data_json = json.loads(line)
			if data_json['title'] == 'イギリス':
				print(data_json['text'])
		f.close()

	#カテゴリ名を含む行を抽出
	def ss1(self):
		'''
		>[[Category:英連邦王国|*]]
		これを抜き出す
		'''
		import re 

		#全文データを取得
		data = self.read_json()
		lines = data.split('\n') #リスト化

		pattern = r'\[\[Category:' #正規表現で探す時のパターン
		for i in range(len(lines)):
			matchOB = re.match(pattern,lines[i])
			if matchOB :
				print(lines[i])

	#カテゴリ名の抽出
	def ss2(self):
		'''
		>[[Category:英連邦王国|*]]
		これから、以下のように抜き出す
		>英連邦王国|*
		'''
		import  re

		#全文データを取得
		data = self.read_json()
		lines = data.split('\n') #リスト化

		pattern1 = r'\[\[Category:' #正規表現で探す時のパターン
		pattern2 = r'\S*'

		for i in range(len(lines)):
			matchOB_1 = re.match(pattern1,lines[i])
			if matchOB_1 :
				matchOB_2 = re.match(pattern2,lines[i])
				if matchOB_2 :
					#pattern1のマッチ部分を抜き出す
					re_pattern1 = matchOB_1.group()
					#いらない部分をreplaceで削除
					category_name = matchOB_2.group().replace(re_pattern1,'').replace(']]','')
					print(category_name)

	#セクション構造
	def ss3(self):



num = input('サブセクション番号入力:')
do  = Section_3()
ss_num = 'ss' + str(num)

eval('do.' + ss_num + '()') #入力した数字の関数を実行

