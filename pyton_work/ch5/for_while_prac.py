
# today_weather=input("今日の天気は晴れ? y or n >>")

# if today_weather =="y" or today_weather =="Y":
#   print("遊園地へ行こう")
# elif today_weather=="n":
#   print("映画を観に行こう")
# print("その後はえいがを観て帰ろう")


#  for文

# 復習 0405
# count=0
# scores_list=list()
# while count<4:
#   score=int(input("number"))
#   scores_list.append(score)
#   count+=1
# print(f"{scores_list},合計点{sum(scores_list)}")


# scores=[80,20,75,80]

# for data in scores:
#     if data>=60:
#         print("合格")
#     else:
#         print("不合格")

# ages_list=[28,50,8,20,78,25,22,10,27,23]

# num=5
# sample=list()
# for age in ages_list:
#     if 20<=age<30:
#         sample.append(age)
#         if len(sample)==num:
#             break

# print(sample)

# スキップ(continue)
# ages_list=[28,50,"secret",20,78,25,22,10,"無回答",33]

# sample=list()
# for age in ages_list:
#     if not isinstance(age,int):
#         continue
#     if age<20 or age>=30:
#         continue
#     sample.append(age)

# print(sample)


# 4.5
# 4-2
# count=0
# ans=True
# print("カレーを召し上がれ")
# while ans==True:
#     print(f"{count}皿のカレーを食べました")
#     key=input("お代わりいる？(y/n)>>")
#     if key=="y":
#         count+=1
#     elif key=="n":
#         False
# print("ごちそさまでした")

# 4-3 難しい

# for n in range(10):
#     print(f"{10-n},",end="")
# print("Lite off!")

# 4-4 range関数をよく勉強






# for a in range(1,10):
#     if a%2 ==0:
#         continue
#     for b in range(1,10):
#         print(f"{a*b} ",end='')
#     print('')

# for a in range(1,10):
#     for b in range(1,10):
#       if a*b>=50:
#         continue
#       print(f"{a*b} ",end="")
#     print("")


# 4-5
# (1)

temp=list() 

for n in range(10):
    data=float(input(f"{n+1}個目のデータ入力"))
    temp.append(data)
time=list()


# (2)
for count in range(len(temp)):
    print(f"{count+8}時,{temp[count]}度")

# (3)

temp_new=list()
for i in range(len(temp)):
    if i ==5:
        temp_new.append("N/A")
    else:
        temp_new.append(temp[i])
print(temp)
print(temp_new)
# 13時が文字列であり、平均を求めるために1つ引く(文字列の13時)
for data in temp_new:
    if isinstance(float,data):
        ttl=ttl+data
print(ttl/len(temp_new)-1)


# 4-6
numbers=(1,1)
data=sum(numbers)
count=2
while data<=1000:
    data=data+numbers[count-1]





# 該当の温度の場所に時間を入力
# b=0
# for a in temp:
#     time_data=input(f"{temp[b]}度の時の時間を入力してください>>")
#     b+=1
#     time.append(time_data)

# 時間気温のListを結合して辞書にする

# dict_time_temp=dict(zip(time,temp))
# print(dict_time_temp)

