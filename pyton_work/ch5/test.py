# # 1
# count=0
# scores=list()
# for nmbr in range(1,5):
#     nmbr=int(input("number>>"))
#     scores.append(nmbr)
#     count+=1


# print(scores)
# print(sum(scores))

# 2
# scores=int(input("点数"))
# while scores<80:
#     scores=int(input("追試"))
# print("ごうかく")
    


# 3
# for block in range(1,4):
#     for b1 in range(1,6):
#         print("■ ",end="")
#     print("")    
#     for b2 in range(1,6):
#         if block==3:
#             break
#         print("□ ",end="")
#     print("")

# 4

# for number in range(1,41):
#     if number%3==0 or "3"in str(number) :
#         print("hoge")
#     else:
#         print(number)


# 2023/04/12

# 1

# dish_yn=input("お皿ある？(y/n)>>")
# n=0
# while  "y" in dish_yn:
#     print(f"お皿が{n}枚")
#     n+=1
# if "n" in dish_yn:
#     print("一枚足りない...")
# elif not "y" in dish_yn and not  "n" in dish_yn:
#     print("ちゃんとしよう")



# 2

# com=("db","security","program")
# col=list()
# for i in (com):
#     scores=int(input(f"{i}の得点は何点？>>"))
#     col.append(scores)
# print(f"各教科は{col}で合計点は{sum(col)}点,平均点は{sum(col)/len(col)}点")

alc=["ビール","ワイン","焼酎","ウイスキー"]
alc_dr=["ロック","水割り","炭酸割り"]
madnm="y"
count=1
while madnm=="y":
    al=int(input("お酒どれ飲む？0:ビール,1:ワイン,2:焼酎,3:ウイスキー >>please number"))
    if al==0 or al==1:
        print(f"{count}杯目は{al[alc]}を飲みました")
        count+=1
    elif al==2 or al==3:
        al_dr=int(input("飲み方は？0:ロック,1:水割り,2:炭酸割り >>please number"))
        print(f"{count}杯目は{al[alc]}{al_dr[alc_dr]}を飲みました")
        count+=1
    else:
        print("ないよ")
    madnm=input("まだ飲める？(y/n)>>")





