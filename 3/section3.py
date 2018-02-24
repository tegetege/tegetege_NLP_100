import json
'''
>wikiのマークアップ早見表

wikiのデータ形式に関することは以下のリンク先に書かれている
https://ja.wikipedia.org/wiki/Help:%E6%97%A9%E8%A6%8B%E8%A1%A8
'''

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
		import re

		data = self.read_json()
		lines = data.split('\n')

		pattern1 = r'='
		print('レベル : セクション名')

		for i in range(len(lines)):
			matchOB_1 = re.match(pattern1,lines[i])
			if matchOB_1 :
				#パターンにマッチした全てをリストとして返す,"="がリストに含まれる
				matchedlist = re.findall(pattern1,lines[i])
				if matchedlist:
					#リストをカウントして ÷2
					section_num = int(len(matchedlist)/2)
					#セクション名のみ抜き出す,リプレイスで空白にして要らない部分を除去
					section_name = lines[i].replace(matchOB_1.group(),'')
					print(section_num,' : ',section_name)

	#ファイル参照の抽出
	def ss4(self):
		import re

		data = self.read_json()
		lines = data.split('\n')
		#以下の2つのパターンで書かれている,カンマ以下を抜き出したい
		pattern_1 = r'\[\[File:'     #正規表現パターン
		pattern_2 = r'\[\[ファイル:'   #正規表現パターン

		for i in range(len(lines)):

			matchOB_1 = re.match(pattern_1,lines[i])
			matchOB_2 = re.match(pattern_2,lines[i])

			if matchOB_1 :
				#pattern_1分を消去
				file_name = lines[i].replace(matchOB_1.group(),'')
				#"|"でスプリットしリスト化して、その0要素目を呼び出す
				file_name_list = file_name.split('|')
				print(file_name_list[0])


			elif matchOB_2 :
				file_name = lines[i].replace(matchOB_2.group(),'')
				file_name_list = file_name.split('|')
				print(file_name_list[0])

	#テンプレートの抽出
	def ss5(self):
		import re

		data = self.read_json()
		lines = data.split('\n')
		#テンプレートを使っている行の抜き出し
		#()で正規表現のグループ化,コードの可読性を上げるために利用
		pattern_1 = r'^\|(\w*)(\s*)=' #正規表現パターン
		temple_dic = {}

		for i in range(len(lines)):
			matchOB_1 = re.findall(pattern_1,lines[i])

			if matchOB_1 :
				temple = lines[i].replace('|','')
				temple_list = temple.split('=',1)
				temple_dic[temple_list[0]] = temple_list[1] #辞書に格納完了
		print('辞書に格納完了')
		for item in temple_dic :
			print(item,':',temple_dic[item]) 

	#ss5と同じ動き,最後に辞書を返す
	def return_dic_ss5(self):
		import re

		data = self.read_json()
		lines = data.split('\n')
		#テンプレートを使っている行の抜き出し
		#()で正規表現のグループ化,コードの可読性を上げるために利用
		pattern_1 = r'^\|(\w*)(\s*)='
		temple_dic = {}

		for i in range(len(lines)):
			matchOB_1 = re.findall(pattern_1,lines[i])

			if matchOB_1 :
				temple = lines[i].replace('|','')
				temple_list = temple.split('=',1)
				temple_dic[temple_list[0]] = temple_list[1] #辞書に格納完了
		print('辞書に格納完了')
		return temple_dic

	#強調マークアップの除去
	def ss6(self):
		import re

		#ss5の処理を行った辞書を受け取る
		temple_dic = self.return_dic_ss5()

		for item in temple_dic :
			temple_dic[item] = temple_dic[item].replace('\'','') #置換
			print(item,':',temple_dic[item]) 			

	#ss6と同じ動き,最後に辞書を返す
	def return_dic_ss6(self):
		import re

		data = self.read_json()
		lines = data.split('\n')

		temple_dic = self.return_dic_ss5()

		for item in temple_dic :
			temple_dic[item] = temple_dic[item].replace('\'','')
		return temple_dic

	#内部リンクの除去
	def ss7(self):
		#内部リンクは"[[]]"で覆われている

		import re
		#ss6の処理を行った辞書を受け取る
		temple_dic = self.return_dic_ss6()

		pattern_1 =r'\[\[' #正規表現パターン
		for item in temple_dic :
			matchOB_1 = re.findall(pattern_1,temple_dic[item])
			if matchOB_1:
				#大括弧を置換
				temple_dic[item] = temple_dic[item].replace('[[','').replace(']]','')
			print(item,':',temple_dic[item]) 


num = input('サブセクション番号入力:')
do  = Section_3()
ss_num = 'ss' + str(num)

eval('do.' + ss_num + '()') #入力した数字の関数を実行

