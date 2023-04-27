# What I learned from the exercise
## html
- meta name="description" content="~~"は検索した際にURLの下に出る短い概要文
- aタグやimgタグはpタグの中に入れる
- わかりやすくするためタグをしっかりと定義
- 定義できない場合はdivタグを使う


## css
- cssの適用方法は3つ
  1. linkタグを使い.cssfileを読み込む
  2. .htmlファイルのheadタグに直接書き込む
  3. .htmlファイルのタグに直接書き込む
- 色や線など種類あるものは1つずつ設定できる(上下左右の順)
- idはファイル内で1回のみで1番優先度高
- classは何回でも使える
- idとclassは併用可能(前に.を付ける)

## Emmet
- 　>で入れ子状態(例.tag1tag2tag1)
- +で親子tagを作れる(親の下に子)
- ^を入れると同じ階層に異なるタグを作れる
- *nでn個タグを作成
- tdn表記でプロパティ(background-colorはbgc)

## vscode
- alt+ctrl↑で複数カーソルを同時操作
- ctrl+shift+Lで選択した同じ文字列を一斉に編集可能
- コメントアウトをまとめてすると個別には解除できない
- ctrl+yですすむ(Zの逆)
- history でコマンド履歴表示
- ~ ←これはチルダでホームディレクトリを表す
- pathは""で囲む必要があるときがある
## 職業人講和やアドバイス
- JSの知識から身に着ける
- はじめはデータの型付けでエラーが多い
- ライブラり覚えるの大変
- **早めにアイデアを考える(5月中旬までには)**
- コメントはこまめに(未来の自分のために)

## Python
- format関数は文字列の後に.format(変数)で指定すると文字列内の{}に順番に入れてくれる
- 先頭にfを入れると{変数}で上と同じ結果(dictと併用の場合"と'を使い分ける)
- sumは合計lenは個数
- listの要素を後ろから取りたい場合-1から
- none 0 "",''[^1]コレクションはFalse

- コレクションに入力値を入れる場合、先に空のコレクションを作る(2)
```python:list
#入力値をいれる方法(2)
a_list=list()
b=input
a_list.append(b)
```
- **while文は条件がtrueになるまで実行**
- **for文はnに変数abを代入**
```python
for n in ab:
  print(n)
```
- 一定の処理で完了したら終わるためにbreakを使い終了
- if文を多く使うよりcontinueを使うことで視認性、可読性がよくなる
- isinstance(データ、データ型)が一致するとTrueに変換
- 奇数は1,3,5...

- range関数は範囲を指定するとその数値から始まる(1)
```python:range
# 九九を出力するコード(1)
for a in range(1,10):
    for b in range(1,10):
      print(f"{a*b}")

for a in range(9):
    a+=1
    for b in range(9):
      b+=1
      print(f"{a*b}")
# どちらとも同じ結果

```
- 関数内とローカル変数内は別。
- 引数は順番をまもる
- return値を使う場合は変数に格納

- **引数は関数に与える値**
- **戻り値は関数で作られた値を外部に渡す事**
```python
# 引数mesgは関数int_input内で使う値
# 戻り値のint入力値は外部に渡す値
def int_input(mesg):
    return int(input(f"{mesg}を入力してください"))


```
- return値のみの関数もある
- return値がある場合は受ける変数が必要
- global変数は多用するとエラーが増える...
- asでモジュール名を変更できる
```python:def
import abc as a
```
[^1]: 空文字列