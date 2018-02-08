class Section_3():

	def ss0(self):
		import json

		#jsonファイルは一行ずつ読まないと怒られる...

		temp = {}
		f = open('jawiki-country.json','r')
		
		i = 0


		for num,line in enumerate(f): 

			temp[line] = json.loads(line)
			print(temp[line])

			i+=1			

		f.close()
		#print()





num = input('サブセクション番号入力:')
do  = Section_3()
ss_num = 'ss' + str(num)

eval('do.' + ss_num + '()') #入力した数字の関数を実行

