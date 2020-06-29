from tkinter import *
import tkinter
from tkinter import ttk
import random
from sorting_function import sorting_function


sortingClass= sorting_function()
root = Tk()
root.title('Sorting Algorithm Visualizer')
root.maxsize(900, 600)
currAlgorithms = StringVar()
arr=[]

def algorithm_selected():
    print("Algorithm Selected: "+currAlgorithms.get())

def random_array_generator():
    global arr
    algorithm_selected()
    arr = []
    try:
        for i in range(sizeEntryString.get()):
            arr.insert(i, random.randint(minEntryString.get() , maxEntryString.get()))
    except:
        for i in range(5):
            arr.insert(i, random.randint(0,9))

    draw_array(arr,['#6c9ff0' for x in range(len(arr))])



def draw_array(array,colourArray):
    canvas.delete('all')
    canvas_height = 380
    canvas_width = 600
    barGraph_width = canvas_width/ (len(array) + 1)
    offset = 30
    spacing = 7
    norm_arr = [i/max(array) for i in array]
    for i, height in enumerate(norm_arr):
        x1 = i* barGraph_width + offset + spacing
        y1 = canvas_height - height * 340
        x2 =  (i+1) * barGraph_width + offset
        y2 = canvas_height

        canvas.create_rectangle(x1, y1, x2, y2, fill = colourArray[i])
#        canvas.create_text(x1 +2, y1, anchor= SW, text= str(array[i]))
    root.update_idletasks()


def sorting():
# 'Bubble Sort', 'Insertion Sort', 'Selection Sort','Quick Sort', 'Merge Sort'
    global arr
    if currAlgorithms.get() == 'Bubble Sort':
        sortingClass.bubble_sort(arr, draw_array,speedScale.get())
        print("starting bubble sort")
    if currAlgorithms.get() == 'Insertion Sort':
        sortingClass.insertion_sort(arr,draw_array, speedScale.get())
    if currAlgorithms.get() == 'Selection Sort':
        sortingClass.selection_sort(arr,draw_array, speedScale.get())
    if currAlgorithms.get() == 'Quick Sort':
        sortingClass.quick_sort(arr,0, len(arr)-1,draw_array, speedScale.get())


def swap_two_pos(pos_0, pos_1):
#    x_00
    pass


def random_sort():
    pass


def from_rgb(rgb):
    """Trying to translate an rgb tuple of into a tkinter friendly colour code"""
    return "#%02x%02x%02x" %rgb


root.config(bg = 'black')
mainFrame = Frame(root, width = 600, height = 150, bg ='#34495e')
mainFrame.grid(row =0, column =0, padx =10, pady=5)

canvas = Canvas(root, width = 700, height = 420,bg= 'white')
canvas.grid(row = 1, column = 0, padx =10, pady=5)

#Row[0]
label=Label(mainFrame, text="Algorithm : ", bg='#b5bdc4').grid(row=0, column =0, padx =5, pady=5, sticky = W)
algMenu= ttk.Combobox(mainFrame, textvariable=currAlgorithms, values=['Bubble Sort', 'Insertion Sort', 'Selection Sort','Quick Sort', 'Merge Sort'])
#algMenu.grid(row=0, column =0, padx =80, pady=5)
algMenu.grid(row=0, column =1, padx =5, pady=5, sticky = W)
algMenu.current(3)

speedScale = Scale(mainFrame, from_=0.001, to=0.5, length =200, digits=2, resolution=0.001, orient= HORIZONTAL, label = 'Select Speed[s]')
speedScale.grid(row=0, column=5, padx=5, pady=5, sticky=E)
#speedScale.pack()



#Button(mainFrame, text='Select', command = selected_algo, bg='light blue').grid(row=1, column =0, padx =5, pady=5, sticky = W )
Button(mainFrame, text='Generate Data', command = random_array_generator, bg='#b5bdc4').grid(row=0, column =2, padx =5, pady=5)
Button(mainFrame, text = "Start the Sort", command=sorting, bg='#b5bdc4').grid(row=0, column =3, padx =5, pady=5)

#Row[1]
Label(mainFrame, text = 'Size of the array: ', bg ='#b5bdc4').grid(row =1, column=0, padx=5, pady=5, sticky= W)
sizeEntryString=tkinter.IntVar()
sizeEntry = Entry(mainFrame,textvariable=sizeEntryString).grid(row =1, column=1, padx=5, pady=5, sticky=W)
#sizeEntryString = sizeEntry.get()


Label(mainFrame, text = 'Min Value: ', bg ='#b5bdc4').grid(row =1, column=2, padx=5, pady=5, sticky= W)
minEntryString = tkinter.IntVar()
minEntry = Entry(mainFrame, textvariable=minEntryString).grid(row =1, column=3, padx=5, pady=5, sticky=W)
#minEntryString = minEntry.get()


Label(mainFrame, text = 'Max Value: ', bg ='#b5bdc4').grid(row =1, column=4, padx=5, pady=5, sticky= W)
maxEntryString = tkinter.IntVar()
maxEntry = Entry(mainFrame, textvariable=maxEntryString).grid(row =1, column=5, padx=5, pady=5, sticky=W)
#maxEntryString = maxEntry.get()

root.mainloop()