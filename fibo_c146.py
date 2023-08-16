from tkinter import *

root=Tk()
root.title("Fibonacci Series")
root.geometry("300x400")



label_series = Label(root, text="Fibonacci Series: ")
label_flower = Label(root)
label_spiral = Label(root)
def Fibonacci():
    num = 10
    first_no = 0
    secound_no = 1
    sum = 0
    counter = 1
    while (counter <= num):
        label_series["text"] += str(sum) + ""
        counter = counter + 1
        first_no = secound_no
        secound_no=sum
        sum = first_no + secound_no
    label_flower['text'] = "Flower is fully bloomed"
    label_spiral["text"] = "Spirals in right direction are " + str(first_no) + " and spirals in left direction are " + str(secound_no) + "\n. Total spiral are " + str(sum)
    
btn = Button(root, text="Show Fibonacci Series", command=Fibonacci)
btn.pack()
label_series.pack()
label_flower.pack()
label_spiral.pack()

root.mainloop()