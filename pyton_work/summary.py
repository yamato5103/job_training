# def show_date(year,month,day):
#     print(f"{year}/{month}/{day}")

# show_date(20022,2,3)



# def odc(n):
#     return  (n%2==0)==True

# aa=odc(int(input("number")))
# if aa==True:
#     print("偶数")
# else:
#     print("奇数")



# if sn>=3:
#   print(f"{sn}月は春")
# elif sn>=4 and sn<=6:
#   print(f"{sn}月は夏")
# elif sn>=7 and sn<=9:
#   print(f"{sn}月は秋")
# else:
#   print(f"{sn}月は冬")



# 0419
# 1
# def hello():
#     print('Hello World')
# hello()

# def welcome(name):
#     name=input("your name insert")
#     print(f"ようこそ{name}さん")
#     return name
# a=welcome()


# 3
# def triangle_area(width,hight):
#         return (width*hight)/2
# width=int(input("三角形の底辺を入力(cm)"))
# hight=int(input("三角形の高さを入力(cm)"))
# answer=triangle_area(width,hight)
# print(f"三角形の面積は{answer}㎠です")


# def count_dish():
#     count=0
#     dish='y'
#     while  "y" in dish:
#         dish = input("お皿ある？(y/n)")
#         if dish =='y':
#           count+=1
#           print(f"お皿が{count}枚")
#         elif dish=="n":
#             print("一枚足りない")
#         else:
#             print("ちゃんと")
#     return count

# 今回は引数いらない
def count_dishes():
    count=1
    while True:
        dish=input("ある？(y/n)")
        # 条件式がtrueの間だけinput関数起動
        if dish=="y":
            print(f"お皿{count}枚")
            count+=1
            # yならcount加算
        elif dish=="n":
            print("一枚足りない")
            break
        # breakによってwhile文が終わり下のelseに進む
        else:
            print("ちゃんとせい")
    return count


dish=input("お皿数える？y/n")
if dish=="y":
# yなら
    cd=count_dishes()
    # count_dishes戻り値をcdに代入し合計を出力
    print(f"お皿は合計{cd}枚")    
# y以外なら
else:
  print("プログラム終了")