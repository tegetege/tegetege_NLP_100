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
