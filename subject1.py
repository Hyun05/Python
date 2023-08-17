from tkinter import *

def insertData() :
    pass

def selectData() :
    pass


root = Tk()
root.title("컴퓨터과 3학년1반 2번 강현묵")

editFrame = Frame(root)
editFrame.pack()
listFrame = Frame(root)
listFrame.pack(side=BOTTOM, fill=BOTH,expand=1)

edt1 = Entry(editFrame, width=10)
edt2 = Entry(editFrame, width=10)
edt3 = Entry(editFrame, width=10)
edt4 = Entry(editFrame, width=10)
edt1.pack(side = LEFT, padx=10, pady=10)
edt2.pack(side = LEFT, padx=10, pady=10)
edt3.pack(side = LEFT, padx=10, pady=10)
edt4.pack(side = LEFT, padx=10, pady=10)

bininsert = Button(editFrame, text="입력", command = insertData)
bininsert.pack(side = LEFT, padx=10, pady=10)

btnSelect = Button(editFrame, text="조회", command = selectData)
btnSelect.pack(side = LEFT, padx=10, pady=10)

lstData1 = Listbox(listFrame, bg = "green")
lstData1.pack(side=LEFT, fill=BOTH,expand=1)

lstData2 = Listbox(listFrame, bg = "green")
lstData2.pack(side=LEFT, fill=BOTH,expand=1)

lstData3 = Listbox(listFrame, bg = "green")
lstData3.pack(side=LEFT, fill=BOTH,expand=1)

lstData4 = Listbox(listFrame, bg = "green")
lstData4.pack(side=LEFT, fill=BOTH,expand=1)
root.mainloop()
