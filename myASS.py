# -*- coding: utf-8 -*-
import Tkinter
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )
import tkMessageBox,requests,hashlib,time

lanfrom="en"
lanto="zh"
top = Tkinter.Tk()
state=True
#top.protocol('WM_DELETE_WINDOW',lambda:False)
#top.wm_attributes('-toolwindow',True)
top.geometry('400x300')
top.title("myASS                                                                                                                                        ISTANT")
toBeTransl="apple"
top.attributes("-topmost",1)

L1 = Tkinter.Label(top, text="start")

def helloCallBack(event=None):
    global L1,toBeTransl
    if E1.get()!=toBeTransl and E1.get()!="":
        L1.destroy()
        ss = translate(E1.get())
        L1 = Tkinter.Label(top, text=ss)

        file_handleres=open("d:/myDictionary.txt","a+")
        file_handleres.writelines("%s---------%s\n"%(str(E1.get()).encode('gb2312'),str(ss).encode('gb2312')))
        file_handleres.close()
        L1.pack( )
        top.update()
        toBeTransl=E1.get()

def translate(txt):
    global lanfrom,lanto
    m2 = hashlib.md5()
    m2.update("#username#%s1435660288O#password#"%(txt))
    para={"q":txt,
        "from":lanfrom,
        "to":lanto,
        "appid":#username#,
        "salt":1435660288,
        "sign":m2.hexdigest(),
        }
    l=requests.post("http://api.fanyi.baidu.com/api/trans/vip/translate",params=para).json()["trans_result"][0]["dst"]
    return l
def blackoutorin(event=None):
    global state
    if state==True:
        top.attributes("-alpha",0)
        state=not state
    else:
        top.attributes("-alpha",1)
        state=not state
def shink():
    global L1,lanfrom,lanto
    if lanfrom=="en":
        L1.destroy()
        L1 = Tkinter.Label(top, text="输完鼠标左键翻译，粘贴自动翻译\nTab键隐藏、再显示窗口\n网不好用起来会卡\n当前汉译英")
        L1.pack( )
        lanfrom="zh"
        lanto="en"
    else:
        L1.destroy()
        L1 = Tkinter.Label(top, text="After finish filling the blank,click left mouce button to translate\nCtrl+v will translate automaticly\nUse Tab button to hide or reappear window\nIt will stuck when using under a bad net state\nTrans English to Chinese now")
        L1.pack( )
        lanfrom="en";
        lanto="zh"
    #top.geometry('0x00')
    top.title("myASS Version:0.8 功能尚不完全，待我继续发扬光大")



B = Tkinter.Button(top, text =":)", command = shink)

B.pack()

E1 = Tkinter.Entry(top, bd =1,width=380)



top.bind("<Button-1>", helloCallBack)
top.bind("<KeyPress-v>", helloCallBack)
top.bind("<KeyPress-Tab>", blackoutorin)

E1.pack()



top.mainloop()
