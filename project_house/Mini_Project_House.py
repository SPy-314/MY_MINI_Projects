from tkinter import *

root = Tk()
root.title("РИСОВАНИЕ")

canvas = Canvas(root, width=700, height=500, bg='white')
canvas.pack()

##Небо
canvas.create_rectangle(0, 0, 700, 300, fill="#42aaff", width=0)

##Трава
canvas.create_rectangle(0, 300, 700, 500, fill="lime", width=0)

##Основа дома
canvas.create_rectangle(300, 200, 600, 350, fill="brown", width=3)

##Основа крыши
canvas.create_rectangle(270, 180, 630, 200, fill="yellow", width=3)

##Второй ярус крыши
canvas.create_rectangle(300, 160, 600, 180, fill="yellow", width=3)

##Третий ярус крыши
canvas.create_rectangle(330, 140, 570, 160, fill="yellow", width=3)

##Дверь дома
canvas.create_rectangle(350, 240, 410, 350, fill="orange", width=3)

##Ручка двери
canvas.create_rectangle(395, 300, 400, 305, fill="grey")

##Создание окна
canvas.create_rectangle(470, 250, 570, 310, fill="#00baff", width=3)

##Украшение окна внутреними рамками
canvas.create_line(470, 280, 570, 280, fill="black", width=3)
canvas.create_line(520, 250, 520, 310, fill="black", width=3)

##Cтвол дерева
canvas.create_rectangle(100, 150, 125, 350, fill="brown", width=3)

##Листва дерева
canvas.create_rectangle(75, 150, 150, 270, fill="green", width=3)
canvas.create_rectangle(90, 130, 135, 150, fill="green", width=3)
canvas.create_rectangle(90, 270, 135, 290, fill="green", width=3)

##Создаем солнце
ob = canvas.create_oval(10, 10, 70, 70, fill="yellow", outline="black")


##Функция движения
def move():
    canvas.move(ob, 1, 0)
    canvas.after(20, move)


##Вызов функции движения
move()

root.mainloop()



