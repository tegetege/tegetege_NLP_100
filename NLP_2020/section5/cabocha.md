# [CaboCha](https://taku910.github.io/cabocha/)

## install
#### CRF++ のインストール
```bash
$brew install crf++
```
CRF++ が無いとあとのCabocha installの時に  
 `fatal error: crfpp.h: No such file or directory` が発生します.

#### CaboCha のインストール
公式(?) のGoogle Driveからバージョンの新しいものをダウンロードしてくる
https://drive.google.com/drive/folders/0B4y35FiV1wh7cGRCUUJHVTNJRnM

```bash
$cd cabocha-*.*
$./configure --with-mecab-config=`which mecab-config` --with-charset=UTF8
$make 
$sudo make install
```

```bash
$cabocha -v
cabocha of 0.69 # バージョンが表示されればOK
```


#### CaboCha を python で使えるようにする
ダウンロードしてきた `cabocha-*` の中にある `python/` を利用してインストール

```bash
$cd cabocha-*.*
$pip install python/
```
動作確認
```bash
$python 
Python 3.6.2 |Anaconda, Inc.| (default, Sep 21 2017, 18:29:43) 
[GCC 4.2.1 Compatible Clang 4.0.1 (tags/RELEASE_401/final)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import CaboCha
>>> cp  = CaboCha.Parser()
>>> print(cp.parseToString("今日はお仕事で少し炎上した。"))
    今日は-----D
    お仕事で---D
          少し-D
      炎上した。
EOS

>>> 
```
いい感じ!
