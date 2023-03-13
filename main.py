from tkinter import *


window = Tk()
window.title("My first GUI program")
window.minsize(width=500, height=300)

#Label

my_label = Label(text="I am a label", font=("Arial", 18))
my_label.pack()

my_label["text"] = "Write Something in the Box Below"
my_label.config(text="Write Something in the Box Below")

#Button

def button_clicked():
  print("I got clicked")
  new_text = input.get()
  my_label.config(text=new_text)
  
button = Button(text="Click Me", command=button_clicked)
button.pack()

#Entry

input = Entry(width=10)
input.pack()
print(input.get())

#Scale
#Called with current scale value.
def scale_used(value):
  print(value)
scale = Scale(from_=0, to=100, command=scale_used)
scale.pack()

#Listbox
def listbox_used(event):
  #Gets current selection from listbox
  print(listbox.get(listbox.curselection()))

listbox = Listbox(height=4)
women = ["Ashley", "Jennifer", "Wendy", "Cara", "Sarah", "Carrie", "Gina"]
for item in women:
  listbox.insert(women.index(item), item)
listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.pack()
