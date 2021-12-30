from tkinter import *

root = Tk()
root.title('ID Card')
root.geometry('400x400')
root.configure(bg='gray')

canvas = Canvas(root, width=400, height=400)
canvas.create_image(0, 0, anchor=NW)
canvas.create_rectangle(5, 0, 390, 50, fill='orange')
# canvas.create_rectangle(5, 400, 390, 25, fill='blue')
labelheading = canvas.create_text(200, 40, font=('Times', 24, 'bold'), text='Your ID')
namelabel = canvas.create_text(70, 120, font=('Times', 16), text='Name: ')
gradelabel = canvas.create_text(70, 140, font=('Times', 16), text='Grade: ')
subjectlabel = canvas.create_text(70, 160, font=('Times', 16), text='Subject: ')
# labelheading = Label(root)
namelabel = Label(root)
gradelabel = Label(root)
subjectlabel = Label(root)

def carddetails():
    name='HELLO'
    print(type(name))
    grade='7th'
    print(type(grade))
    subject=['Science', 'History', 'Math', 'English', 'Band']
    print(type(subject))
    namelabel['text'] = name
    gradelabel['text'] = grade
    subjectlabel['text'] = subject[0] + subject[1] + subject[2] + subject[3] + subject[4]

button1 = Button(root, text='Show Details', command=carddetails)
button1.configure(width=20, activebackground='blue')
button1_window = canvas.create_window(200, 390, anchor=CENTER, window=button1)
# labelheading_window = canvas.create_window(120, 10, anchor=CENTER, window=labelheading)
namelabel_window = canvas.create_window(120, 120, anchor=CENTER, window=namelabel)
gradelabel_window = canvas.create_window(110, 140, anchor=CENTER, window=gradelabel)
subjectlabel_window = canvas.create_window(190, 160, anchor=CENTER, window=subjectlabel)
canvas.pack()

root.mainloop()