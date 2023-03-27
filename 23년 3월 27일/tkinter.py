import tkinter

window = tkinter.Tk()

window.title("강현묵")
window.geometry("640x400+100+100")
window.resizable(0, 0)


def btn():
    label.config(font=("Arial",40), text="안산공고 컴퓨터과",fg="red")
    
label = tkinter.Label(window,fg="blue",bd=40, text="안녕하세요")
label.pack()

    
btn = tkinter.Button(window,text="안산공고",command=btn)
btn.pack()



window.mainloop()
