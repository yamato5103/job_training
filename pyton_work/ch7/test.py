import math
from random import randint

# 7-4-1
# num=list()
# for i in range(1,4):
#   data=int(input(f"{i}個目の数字>>>"))

#   num.append(data)
# print(max(num))

# 7-4-2

pi=3.141592
print(round(pi))
for n in range(1,5):
    print(round(pi,n))

# 7-6
# print("数当てゲーム! 3桁の数値あてて>>>")
# answer=list()
# for n in range(3):
#   answer.append(randint(0, 9))


# is_con=True
# prediction=list()
# for n in range(3):
#   data=int(input(f"{n+1}桁目の予想を入力(0~9)>>>"))
#   prediction.append(data)


# hit=0 
# blow=0

# for n in range(3):
#   if prediction[n]==answer[n]:
#     hit+=1
#   else:
#     for m in range(3):
#       if prediction[n]==answer[m]:
#         blow+=1
#         break

# print("{hit}ヒット{blow}ボール")
# if hit==3:
#   print("正解")
#   is_con=False
# else:
#   if int(input('続けますか？ 1:続ける 2:終了>>')) == 2:
#     print(f'正解は{answer[0]},{answer[1]},{answer[2]}でした。')
        
#     is_con == False

  