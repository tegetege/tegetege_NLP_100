# 第2章: UNIXコマンド
https://nlp100.github.io/ja/ch02.html

## 10.行数のカウント
ファイルを読み込んで、その行数をカウントする
```
$wc -l popular-names.txt 
    2780 popular-names.txt
```

## 11.タブをスペースに置換
```
$tr \t \b < popular-names.txt 
<省略>
Nicholas        M       22845   2001
Andrew  M       22411   2001
Joseph  M       22011   2001
Daniel  M       20989   2001
William M       20101   2001
Emily   F       24464   2002
Madison F       21773   2002
Hannah  F       18822   200
.
.
.
```

## 12.1列目をcol1.txtに, 2列目をcol2.txtに保存
```
$cat popular-names.txt | cut -f 1 > col1.txt && cat popular-names.txt | cut -f 2 > col2.txt
```

## 13.col1.txt と col2.txt をマージ
```
$paste col1.txt col2.txt > merged_file.txt
```

## 14.先頭からN行を出力
```
$head -n 3 popular-names.txt 

Mary    F       7065    1880
Anna    F       2604    1880
Emma    F       2003    1880
```

## 15.末尾のN行を出力
```
$tail -n 3 popular-names.txt 

Lucas   M       12585   2018
Mason   M       12435   2018
Logan   M       12352   2018
```

## 16.ファイルをN分割する
ファイルをN分割するには、 `split -n`を利用すれば良いみたいな記述を  
見つけたが、自分のmacでは `-n`オプションが見つからなかったので、  
`-l`で1000行区切りでファイルを分割
```
$split -l 1000 popular-names.txt 
```

## 17.１列目の文字列の異なり
一列目を切り出し(cut)て並べ直し(sort)て重複をなくす(uniq)  
(※)uniqコマンドはソート済みを前提をしているらしい
```
$cut -f 1 popular-names.txt | sort | uniq
```

## 18.各行を３コラム目の数値の降順にソート
3コラム目(-k 3)を数値(n)として降順(r)にソートする  
(※)[sortコマンド、基本と応用とワナ](https://qiita.com/richmikan@github/items/cc4494359b1ac2f72311#%E6%80%A7%E5%88%A5%E5%88%9D%E5%87%BA%E5%B9%B4%E9%80%86%E9%A0%86%E5%90%8D%E5%89%8D%E3%81%AE%E9%A0%86%E3%81%A7%E3%82%BD%E3%83%BC%E3%83%88%E3%81%9B%E3%82%88)
```
$sort -k 3rn popular-names.txt
```

## 19.各行の1コラム目の文字列の出現頻度を求め、出現頻度の高い順に並べる

`uniq -c` : 重複を無くして、カウントする  
`sort -r` : カウントの降順でソート
```
$cut -f 1 popular-names.txt | sort | uniq -c | sort -r
```
参考: [単語の出現頻度を調べるシェルスクリプトメモ(3)](http://bigfatcat.hateblo.jp/entry/20070905/1188983899)
