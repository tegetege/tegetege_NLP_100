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
