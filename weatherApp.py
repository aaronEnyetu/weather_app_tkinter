import tkinter as tk

HEIGHT =700
WIDTH = 800

root = tk.Tk()


canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

frame = tk.Frame(root, bg='#80c1ff', bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

entry = tk.Entry(frame, font=40)
entry.place(relwidth=0.65, relheight=1)



button = tk.Button(frame, text="Test Button", font='20', bg="gray", fg="blue")

button.place(relx=0.7, relheight=1, relwidth=0.3)


root.mainloop()