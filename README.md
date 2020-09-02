# tegetege_NLP_100

てげてげに[言語処理100本ノック 2020(Rev1)](https://nlp100.github.io/ja/)に取り組んでいきます。

### mecab install
```bash
# mecab の install と python で使えるようにする
$ brew install mecab mecab-ipadic 
$ conda install -c anaconda swig    # anaconda環境の場合は、次のpipコマンドを有効化するために必要らしい
$ pip install mecab-python3 


# mecab-ipadic-neologd のインストール
$ cd ~/Downloads
$ git clone --depth 1 git@github.com:neologd/mecab-ipadic-neologd.git
$ cd mecab-ipadic-neologd
$ brew install  xz
$ ./bin/install-mecab-ipadic-neologd -n     # インストール

$ls /usr/local/lib/mecab/dic/ 
ipadic/               mecab-ipadic-neologd/    # 2つの辞書が入っていればOK

```
