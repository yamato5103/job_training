# usrinfo=input("names & blood type")
# [names, blood]=usrinf
#o.split(",")
# blood=b
#lood.upper().strip()
# print(f"{names}さんは{blood}型なので大吉です")


# class Hero:
#     names="まつだ"
#     hp=100
#     def sleep(self,hours):
#         print(f"{self.names}は{hours}ねた")
#         self.hp+=hours

# print("スッキリファンタジーⅫ ~金色の理想郷~")
# h=Hero()
# h.sleep(3)
# print(f"{h.names}の現在のHPは{h.hp}です")


# scores1=[80,40,50]
# scores2=[80,40,50]
# print(f"scores1の先頭要素は{scores1[0]}")
# print(f"scores2の先頭要素は{scores2[0]}")
# print("変数scores2の中身を変数scores1に代入します")
# scores1=scores2

# print("scores1の先頭要素を90に書き換えます")
# scores1[0]=90

# print(f"90を代入したscores1の先頭要素は{scores1[0]}")
# print(f"90を代入していないscores2の先頭要素は{scores2[0]}")

# def add_suffix(names):
#     for i in range(len(names)):
#         names[i]=names[i]+"さん"
#     return names

# bf_names=["matuda","asagi","kudo"]
# cp_names=list()
# for n in bf_names:
#     cp_names.append(n)
# af_names=add_suffix(cp_names)
# print("さん付け前"+bf_names[0])
# print("さん付け後"+af_names[0])



def welcome(u):
  print(f"ようこそ{u['name']}さん")
  u["age"]=u["age"]+1
  print(f'アナタは来年{u["age"]}歳だから大吉')

usrname=input("name input")
usrage=int(input("age input"))
usr={"name":usrname,"age":usrage}
cp_usr=usr.copy()
welcome(cp_usr)
print(f"{usr['age']}歳の{usr['name']}さん、またプレイしてください")
