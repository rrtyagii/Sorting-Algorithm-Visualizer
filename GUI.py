from tkinter import *
import tkinter
from tkinter import ttk
import random
from SortingAlgoClass import*



root = Tk()
root.title('Sorting Algorithm Visualizer')
root.maxsize(900, 600)


def selected_algo():
    print("Algorithm Selected: "+currAlgorithms.get())
    arr = []
    try:
        for i in range(sizeEntryString.get()):
            arr.insert(i, random.randint(minEntryString.get() , maxEntryString.get()))
    except:
        for i in range(5):
            arr.insert(i, random.randint(0,9))

    draw_array(arr)



def draw_array(array):
    canvas.delete('all')
    canvas_height = 380
    canvas_width = 600
    barGraph_width = canvas_width/ (len(array) + 1)
    offset = 30
    spacing = 10
    norm_arr = [i/max(array) for i in array]
    for i, height in enumerate(norm_arr):
        x1 = i* barGraph_width + offset + spacing
        y1 = canvas_height - height * 340
        x2 =  (i+1) * barGraph_width + offset
        y2 = canvas_height

        canvas.create_rectangle(x1, y1, x2, y2, fill = 'yellow')
        canvas.create_text(x1 +2, y1, anchor= SW, text= str(array[i]))


currAlgorithms = StringVar()


root.config(bg = 'black')
mainFrame = Frame(root, width = 600, height = 150, bg ='#49A')
mainFrame.grid(row =0, column =0, padx =10, pady=5)

canvas = Canvas(root, width = 700, height = 420,bg= 'white')
canvas.grid(row = 1, column = 0, padx =10, pady=5)

#Row[0]
label=Label(mainFrame, text="Algorithm : ", bg='light blue').grid(row=0, column =0, padx =5, pady=5, sticky = W)
algMenu= ttk.Combobox(mainFrame, textvariable=currAlgorithms, values=['Bubble Sort', 'Insertion Sort', 'Selection Sort','Quick Sort', 'Merge Sort'])
#algMenu.grid(row=0, column =0, padx =80, pady=5)
algMenu.grid(row=0, column =1, padx =5, pady=5, sticky = W)
algMenu.current(3)

#Button(mainFrame, text='Select', command = selected_algo, bg='light blue').grid(row=1, column =0, padx =5, pady=5, sticky = W )
Button(mainFrame, text='Generate Data', command = selected_algo, bg='light blue').grid(row=0, column =2, padx =5, pady=5)
Button(mainFrame, text = "Sort", bg='light blue').grid(row=0, column =3, padx =5, pady=5)

#Row[1]
Label(mainFrame, text = 'Size of the array: ', bg ='light blue').grid(row =1, column=0, padx=5, pady=5, sticky= W)
sizeEntryString=tkinter.IntVar()
sizeEntry = Entry(mainFrame,textvariable=sizeEntryString).grid(row =1, column=1, padx=5, pady=5, sticky=W)
#sizeEntryString = sizeEntry.get()



Label(mainFrame, text = 'Min Value: ', bg ='grey').grid(row =1, column=2, padx=5, pady=5, sticky= W)
minEntryString = tkinter.IntVar()
minEntry = Entry(mainFrame, textvariable=minEntryString).grid(row =1, column=3, padx=5, pady=5, sticky=W)
#minEntryString = minEntry.get()


Label(mainFrame, text = 'Max Value: ', bg ='grey').grid(row =1, column=4, padx=5, pady=5, sticky= W)
maxEntryString = tkinter.IntVar()
maxEntry = Entry(mainFrame, textvariable=maxEntryString).grid(row =1, column=5, padx=5, pady=5, sticky=W)
#maxEntryString = maxEntry.get()

root.mainloop()