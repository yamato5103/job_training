# %matplotlib inline
import module_mod as mm
import math as m

# text=input("なにを記録")
# file=open("diary.txt","a")
# file.write(text+"\n")
# file.close
# print(f"円周率{m.pi}")
# print(f"小数点以下切り捨て{m.floor(m.pi)}")
# print(f"小数点以下切り上げ{m.ceil(m.pi)}")


import matplotlib.pyplot as plt
# wgt=[68.4,68.0,69.5,68.4,68.6,70.2,71.4,70.8,68.5,68.6,68.3,68.4]
# plt.plot(wgt)
# plt.show()

import requests
response=requests.get("http://abehiroshi.la.coocan.jp/")
text=response.text
print(text)


# "https://www.python.org/downloads/"










