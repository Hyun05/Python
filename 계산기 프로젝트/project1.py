from tkinter import *

root = Tk()
root.title("SImple Calculator")
root.geometry("300x150")

frame1 = Frame(root, relief="ridge", bd=2, padx=5, pady=5)
frame1.pack()

frame2= Frame(root, relief="ridge", bd=2, padx=5, pady=5)
frame2.pack()

frame3= Frame(root, relief="ridge", bd=2)
frame3.pack()

label_x = Label(frame1, text="첫번쨰 숫자를 입력하세요",font=("Arial",12))
label_x.pack(side="left")

enter_x = Entry(frame1,font=("Arial",12),width=10,justify="center")
enter_x.pack(side="right")

label_y = Label(frame2, text="두번쨰 숫자를 입력하세요",font=("Arial",12))
label_y.pack(side="left")

enter_y = Entry(frame2,font=("Arial",12),width=10,justify="center")
enter_y.pack(side="right")


def calc(op) :
    global label_result_text
    if op =="+":
        add = float(enter_x.get()) + float(enter_y.get())
        label_result_text.set("결과:" + str(add))
    elif op == "-":
        sub = float(enter_x.get()) - float(enter_y.get())
        label_result_text.set("결과:" + str(sub))
    elif op == "/":
        div = float(enter_x.get()) / float(enter_y.get())
        label_result_text.set("결과:" + str(round(div,3)))
    elif op == "x":
        mul = float(enter_x.get()) * float(enter_y.get())
        label_result_text.set("결과:" + str(round(mul,3)))
    elif op == "%":
        rem = float(enter_x.get()) % float(enter_y.get())
        label_result_text.set("결과:" + str(round(rem,3)))
    elif op == "^":
        power = float(enter_x.get()) ** float(enter_y.get())
        label_result_text.set("결과:" + str(round(power,3)))

btn1 = Button(frame3, text = "+", width=4, height=2, command=lambda:calc("+"))
btn1.grid(row=0, column=0)

btn2 = Button(frame3, text = "-", width=4, height=2, command=lambda:calc("-"))
btn2.grid(row=0, column=1)

btn3 = Button(frame3, text = "/", width=4, height=2, command=lambda:calc("/"))
btn3.grid(row=0, column=2)

btn4 = Button(frame3, text = "x", width=4, height=2, command=lambda:calc("x"))
btn4.grid(row=0, column=3)

btn5 = Button(frame3, text = "%", width=4, height=2, command=lambda:calc("%"))
btn5.grid(row=0, column=4)

btn6 = Button(frame3, text = "x^y", width=4, height=2, command=lambda:calc("^"))
btn6.grid(row=0, column=5)

label_result_text = StringVar()
label_result_text.set("결과:")
label_result = Label(root, textvariable = label_result_text, font=("Arial", 14))
label_result.config(bg="yellow")
label_result.pack()


root.mainloop()
