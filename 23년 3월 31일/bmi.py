import tkinter;
import tkinter.messagebox

window=tkinter.Tk()
window.title("BMI계산기")
window.geometry("640x400+300+300")
window.resizable(0,0)

he = tkinter.StringVar()
we = tkinter.StringVar()
score = tkinter.StringVar()

def btclick() :
    h_value = float(he.get())
    w_value = float(we.get())
    h_value = h_value * 0.01
    result = round(w_value / (h_value* h_value),1)
    scr = score.set(result)
    
label = tkinter.Label(window, text="BMI계산기",fg="red",font=("Arial",25))
label.pack()


heightlabel = tkinter.Label(window, text="신장",font=("Arial",24))
heightlabel.place(x=30, y=70)


heightEntry = tkinter.Entry(window)
heightEntry=tkinter.Entry(window, textvariable=he)
heightEntry.place(x=120,y=82)

weightlabel = tkinter.Label(window, text="체중",font=("Arial",24))
weightlabel.place(x=30, y=140)

weightEntry = tkinter.Entry(window,textvariable=we)
weightEntry.place(x=120,y=150)


bt = tkinter.Button(window, text="확인",command=btclick,repeatdelay=1000)
bt.place(x=30,y=250)
bt = tkinter.Entry(window, textvariable=score)
bt.place(x=120,y=250)



window.mainloop()


