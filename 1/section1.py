#http://www.cl.ecei.tohoku.ac.jp/nlp100/


class Section_1(): 

	#文字列の逆順
	def ss0(self):
		target_string = 'stressed'
		ans = ''	#これが無いとforループ内で怒られる

		ts_list = list(target_string)	#文字列のリスト化
		ts_list.reverse() 				#リストの逆転

		for list_num in ts_list :
			ans += list_num

		print(ans)

	#「パタトクカシーー」	
	def ss1(self):
		target_string = 'パタトクカシーー'

		ts_list = list(target_string)
		ans = ts_list[0] + ts_list[2] + ts_list[4] + ts_list[6]

		print(ans)

	#「パトカー」+「タクシー」＝「パタトクカシーー」
	def ss2(self):
		target_string1 = 'パトカー'
		target_string2 = 'タクシー'
		ans = ''	#これが無いとforループ内で怒られる

		ts1_list = list(target_string1)
		ts2_list = list(target_string2)

		for i in range(len(ts1_list)) :   #文字数分繰り返す
			ans += ts1_list[i] + ts2_list[i]

		print(ans)

	#円周率
	def ss3(self):
		target_string = 'Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics.'

		ts = target_string.replace(',','').replace('.','') #カンマ,ピリオド処理
		ts_list = ts.split(' ') #分ち書きで区切ってリスト化

		#リストの中身を"文字　→ 文字数"に変換
		for i in range(len(ts_list)):
			ts_list[i] = len(ts_list[i])

		print(ts_list)

	#元素記号
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

	#n-gram
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

	#集合
	def ss6(self):
		target_string1 = 'paraparaparadise'
		target_string2 = 'paragraph'
		#空リストの宣言
		x_bi_char_list = [] #target_string1の文字バイグラムリスト
		y_bi_char_list = [] #target_string2の文字バイグラムリスト


		for i in range(len(target_string1)-1):
			#文字バイグラムをリストに入れる
			x_bi_char_list.append(target_string1[i]+target_string1[i+1]) 

		for i in range(len(target_string2)-1):
			#文字バイグラムをリストに入れる
			y_bi_char_list.append(target_string2[i]+target_string2[i+1]) 	

		#リスト → 集合
		x_bi_char_set = set(x_bi_char_list)
		y_bi_char_set = set(y_bi_char_list)	

		#和集合
		print('和集合 :',x_bi_char_set | y_bi_char_set)
		#積集合
		print('積集合 :',x_bi_char_set & y_bi_char_set)
		#差集合
		print('差集合 :',x_bi_char_set - y_bi_char_set)

		#'se'がXリストに含まれているか調べる
		if 'se' in x_bi_char_list :
			print('Xに"se"が含まれています。')
		else:
			print('Xに"se"は含まれていません。')

		#'se'がYリストに含まれているか調べる
		if 'se' in y_bi_char_list :
			print('Yに"se"が含まれています。')
		else:
			print('Yに"se"は含まれていません。')

	#テンプレートによる文生成
	def ss7(self):
		x = input('引数xを入力:')
		y = input('引数yを入力:')
		z = input('引数zを入力:')

		print(x,'時の',y,'は',z)

	#暗号文生成
	def ss8(self):
		target = input('平文を入力 :')
		#指定された"cipher"関数に平文を投げる
		cipher_text = self.cipher(target)

		print('暗号文 :', cipher_text)


	#ss8で利用する指定関数 暗号文の生成を行う
	def cipher(self,target):
		import re
	
		cipher_text = ''
		target_list = list(target)
		for i in range(len(target_list)):
			if re.search('[a-z]',target_list[i]): 	#正規表現で英小文字判定
				#ord()で文字コードのポイントを返して、chr()で文字コードのポイントから文字に変換
				target_list[i] = chr(219 - ord(target_list[i])) 

			else: #非英小文字の場合は何もしない
				pass

		for i in range(len(target_list)) :   #リストを全て結合する
			cipher_text += target_list[i]

		return cipher_text


	#Typoglycemia
	def ss9(self):
		from numpy import random 

		target_string = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
		ts_list = target_string.split(' ') #分ち書きで区切ってリスト化	
		shuffled_string = "" #シャッフル後の文を入力	

		for i in range(len(ts_list)):
			shuffled_word = ''
			'''
			単語の文字の長さが4以上の場合のみ、各単語の先頭と末尾の文字は残し，
			それ以外の文字の順序をランダムに並び替える
			'''
			if 4 < len(ts_list[i]): 
				#単語のオリジナルは"ts_list[i]"より呼び出し可能
				char_list = list(ts_list[i]) #対象の単語を一文字ずつリスト化
				
				'''
				[方針]
				数字配列[0~]を必要な部分だけシャッフルする
				'''
				
				#シャッフルする範囲の数値リスト[1~]を生成
				num_list =list(range(1,len(char_list)-1))
				random.shuffle(num_list)	#リストの数値をシャッフル
				#リストの最初と最後に0と"文字数-1"の数値を追加
				num_list.insert(0,0)
				num_list.append(len(list(ts_list[i]))-1)

				#リスト化されていたものを一つに再形成
				for j in range(len(num_list)):
					shuffled_word += char_list[num_list[j]]

				#リストのオリジナルとシャッフル後の単語を入れ替える
				#以後、リストのオリジナルはこのfor文内より呼び出し不可
				ts_list[i] = shuffled_word
			else:
				pass
				
		#最後にリスト化したものを再形成
		for k in range(len(ts_list)):
			shuffled_string += ts_list[k] + ' '
		print(shuffled_string)




num = input('サブセクション番号入力:')
do  = Section_1()
ss_num = 'ss' + str(num)

eval('do.' + ss_num + '()') #入力した数字の関数を実行

