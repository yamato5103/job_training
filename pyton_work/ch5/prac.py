import mod as m

# m.profile("ymd",19,"食べ歩き")


# answer=m.plus(100,50)
# print(f"答えは{answer}")



# ymd_scores=m.input_scores("山田")
# m.cal_avg("yamada",ymd_scores)


# print("8月1日")
# m.eat_menu("トースト","おにぎり")
# print("8月2日")
# m.eat_menu("納豆ご飯",dnr="カレーうどん")
# print("8月3日")
# m.eat_menu("バナナ","そば","焼肉")
# print("8月4日")
# m.eat_menu("サンドウィッチ","シュウマイ弁当","チョコ","クレープ")


# cr_year=int(input("うるう年？>>"))

# if m.is_leapyear(cr_year):
#     print(f"西暦{cr_year}年は、うるう年です")
# else:
#     print(f"西暦{cr_year}年はうるう年ではない")


# 引数で項目の名前付けしつつreturn値を渡す
amount=m.int_input("総額");ppl=m.int_input("人数")
# 入力値を関数c_p内で計算し、その結果をpay,orgに渡す
[pay,payorg]=m.calc_pymnt(amount,ppl)
# 入力値の人数と幹事、非幹事の値を渡している
m.show_pymnt(pay,payorg,ppl)