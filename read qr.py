import cv2
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
import os

window = Tk()
window.geometry('310x435+340+100')
window.title('QR CODE READ')
#=====================================================
def open():
    file = filedialog.askopenfile(mode='r',filetypes=[('Files','*.jpg'),('Files','*.png')])
    if file:
        filepass = os.path.abspath(file.name)
        en.insert(0,str(filepass))


def scan():
    d = en.get()
    res = cv2.QRCodeDetector()
    val , points , s_qr = res.detectAndDecode(cv2.imread(d))
    messagebox.showinfo('QR-SCAN',val)





text = Label(window,text='QR SCANNER',fg='white',bg='black')
text.pack(fill=X)


l1 = Label(window,text='QR CODE SCANNER',font=('Tajawal',12))
l1.place(x=90,y=250)

en = Entry(window,font=('Tajawal',12),width=31)
en.place(x=15,y=290)

b1 =Button(window,text='SELECT IMG',fg='white',bg='green',width=30,font=('Tajawal',12),command=open)
b1.place(x=10,y=340)


b2 =Button(window,text='READ IMAGE',fg='white',bg='red',width=30,font=('Tajawal',12),command=scan)
b2.place(x=10,y=383)





























window.mainloop()
