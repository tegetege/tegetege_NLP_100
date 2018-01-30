#http://www.cl.ecei.tohoku.ac.jp/nlp100/


class Section_1(): 

	def ss0(self):
		target_string = 'stressed'
		ans = ''	#これが無いとforループ内で怒られる

		ts_list = list(target_string)	#文字列のリスト化
		ts_list.reverse() 				#リストの逆転

		for list_num in ts_list :
			ans += list_num

		print(ans)


	def ss1(self):
		target_string = 'パタトクカシーー'

		ts_list = list(target_string)
		ans = ts_list[0] + ts_list[2] + ts_list[4] + ts_list[6]

		print(ans)


	def ss2(self):
		target_string1 = 'パトカー'
		target_string2 = 'タクシー'
		ans = ''	#これが無いとforループ内で怒られる

		ts1_list = list(target_string1)
		ts2_list = list(target_string2)

		for i in range(len(ts1_list)) :   #文字数分繰り返す
			ans += ts1_list[i] + ts2_list[i]

		print(ans)


	def ss3(self):
		target_string = 'Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics.'

		ts = target_string.replace(',','').replace('.','') #カンマ,ピリオド処理
		ts_list = ts.split(' ') #分ち書きで区切ってリスト化

		#リストの中身を"文字　→ 文字数"に変換
		for i in range(len(ts_list)):
			ts_list[i] = len(ts_list[i])

		print(ts_list)


	def ss4(self):
		from pprint import pprint

		target_string = 'Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can.'
		lucky_number = [1, 5, 6, 7, 8, 9, 15, 16, 19] 
		ans_dict = {}

		ts = target_string.replace(',','').replace('.','') #カンマ,ピリオド処理
		ts_list = ts.split(' ') #分ち書きで区切ってリスト化

		for i in range(len(ts_list)):
			#指定されたリスト番号の単語のみ先頭の文字を抜き出し(その他は2文字)
			#辞書にまとめる
			if int(i)+1 in lucky_number : 
				ans_dict[int(i)+1] = ts_list[i][0:1] #単語の先頭の1文字を取得
			else :
				ans_dict[int(i)+1] = ts_list[i][0:2] #単語の先頭の2文字を取得
		
		pprint(ans_dict)


	def ss5(self):
		target_string = 'I am an NLPer'
		bi_word_list = []
		bi_cha_list =[]

		ts_list = target_string.split(' ') #分ち書きで区切ってリスト化
			
		#バイグラム単語リストの生成
		for i in range(len(ts_list)-1):
			bi_word_list.append(ts_list[i]+ts_list[i+1]) 

		#バイグラム文字リストの生成
		ts = target_string.replace(' ','') #分ち書き処理
		for i in range(len(ts)-1):
			bi_cha_list.append(ts[i]+ts[i+1])


		print('バイグラム単語:', bi_word_list)
		print('バイグラム文字:', bi_cha_list)


	def ss6(self):

		'''
		[to do]
		リストと集合って初めに宣言が必要だっけ？？？？
		'''


		target_string1 = 'paraparaparadise'
		target_string2 = 'paragraph'
		#空リストの宣言
		x_bi_char_list = [] #target_string1の文字バイグラムリスト
		y_bi_char_list = [] #target_string2の文字バイグラムリスト
		#空集合の宣言
		x_bi_char_set = set()
		y_bi_char_set = set()

		for i in range(len(target_string1)-1):
			x_bi_char_list.append(target_string1[i]+target_string1[i+1]) 

		for i in range(len(target_string2)-1):
			y_bi_char_list.append(target_string2[i]+target_string2[i+1]) 	

		x_bi_char_set = set(x_bi_char_list)
		y_bi_char_set = set(y_bi_char_list)	

		#和集合
		print('和集合 :',x_bi_char_set | y_bi_char_set)


		


num = input('サブセクション番号入力:')
do  = Section_1()
ss_num = 'ss' + str(num)

eval('do.' + ss_num + '()') #入力した数字の関数を実行

