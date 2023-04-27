
def profile(name,age,hobby):
    print(f"私の名前は{name}です")
    print(f"年齢は{age}歳です")
    print(f"趣味は{hobby}です")


# 名前表示と、平均点を求める関数
def cal_avg(name,scores):
    avg=sum(scores)/len(scores)
    print(f"{name}さんの平均点は{avg}点です")
    

# 各科目の点数を入力する関数
def input_scores(name):
    print(f"{name}さんの試験結果を入力")
    nw=int(input("ネットワークの得点>>"))
    db=int(input("データベースの得点>>"))
    security=int(input("セキュリティの得点>>"))
    scores=[nw,db,security]
    return scores
# return値のscoresは中の値のみ(nw,db,sec)を返す
    

def plus(x,y):
    answer=x+y
    return answer

# デフォルト値がある関数
def eat_menu(bf,lnh="ラーメン",dnr="カレー",*dsrt):
    print(f"朝は{bf}を食べました")
    print(f"昼は{lnh}を食べました")
    print(f"夜は{dnr}を食べました")

    for d in dsrt:
        print(f"おやつに{d}を食べました")
# 可変長引数を使う際にはデフォルト関数を使うのはよそう


# global変数
# ↑を使うと複数の関数で1つの変数を使いまわせる
# 
def change_name():
    global name
    name="X"

def hello():
    print(f"hello"+name+"さん")


# 練習問題
# 引数yearの値を計算し戻り値で計算結果を外部に渡す
def is_leapyear(year):
    return (year%400==0 or(year%4==0 and  year%100!=0))   




# (1)
# 引数で項目の種類名を決める
# return値で入力値を渡す
def int_input(mesg):
    return int(input(f"{mesg}を入力してください"))
    
(2)
def calc_pymnt(amount,ppl=2):
    # 総数で割る
    dnum=amount/ppl
    # 100円未満を切り捨て
    pay=dnum//100*100
    # 元値と比較し小さいなら100円未満なので上乗せ
    if dnum>pay:
        pay=int(pay+100)
    # 幹事支払額
    payorg=amount-pay*(ppl-1)
    return(int(pay),int(payorg))

def show_pymnt(pay,payorg,ppl=2):
    print("支払額")
    print(f"1人あたり{pay}円{ppl-1}人、幹事は{payorg}円です")




