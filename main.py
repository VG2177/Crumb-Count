#!apt-get install libzbar0
#!pip install pyzbar
#!pip install pyzbar[scripts]
#!pip install opencv-python
#from pyzbar.pyzbar import decode
#import cv2
#def BarcodeReader(image):
#  img = cv2.imread(image)
#  detectedBarcodes = decode(img)
#  if not detectedBarcodes:
#    print("Barcode Not Detected or Corrupted")
#  else:
#    for barcode in detectedBarcodes:
#      (x, y, w, h) = barcode.rect
#      cv2.rectangle(img, (x-10, y-10), (x + w+10, y + #h+10), (255, 0, 0), 2)
#      if barcode.data!="":
#        print(barcode.data)
#        print(barcode.type)
#  cv2.imshow("Image", img)
#  cv2.waitKey(0)
#  cv2.destroyAllWindows()
#if(__name__ == "__main__"):
#  image=("Scanner test.jpeg")
#  BarcodeReader(image)
import tkinter
from tkinter import *
name = input("Enter Product Name:")
date = input("Enter Expiry Date:")
m = tkinter.Tk()
m.title("Welcome to Expiry Inquiry")
m.geometry("500x900")
lbl = Label(m, text="Welcome to Expiry Inquiry", font=("Times New Roman", 20))
#name = Entry(m)
#name.insert(0, "Enter Product Name:")
#name.pack()
#date = Entry(m)
#date.insert(0, "Enter Expiry Date:")
#date.pack()
import sqlite3 as sql
database = "Python Database.db"
con = sql.connect(database)
cursor = con.cursor()
cursor.execute('''
Create table if not exists Food(
Name text,
Date Date
);''')
read = cursor.execute('''
Select * from Food;
''')
window_read = Entry(m)
window_read.insert(0, read)
window_read.pack()
m.mainloop()