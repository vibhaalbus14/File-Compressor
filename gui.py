from comp_and_decomp import compressor,decompressor

import tkinter as tk
from tkinter import filedialog
def open_file():
    input_file=filedialog.askopenfilename(initialdir="/",title="select an input file")
    entry1.delete(0,tk.END)
    entry1.insert(0,input_file)

def destination_file():
    input_file=filedialog.asksaveasfilename(initialdir="/",title="select an input file")
    entry2.delete(0,tk.END)
    entry2.insert(0,input_file)

window=tk.Tk()
window.geometry("800x600")
input=tk.Label(window,text="input file : ",padx=3,pady=3,bd=3,highlightcolor="black")
output=tk.Label(window,text="output file : ",padx=3,pady=3,bd=3,highlightcolor="black")
entry1=tk.Entry(window,width=40)
entry2=tk.Entry(window,width=40)
input_bt=tk.Button(window,text="browse",padx=3,pady=3,justify="center",bd=3,relief="sunken",highlightcolor="black",command=open_file)  
output_bt=tk.Button(window,text="browse",padx=3,pady=3,justify="center",bd=3,relief="sunken",highlightcolor="black",command=destination_file) 

btn1=tk.Button(window,text="compress",padx=3,pady=3,justify="center",bd=3,relief="sunken",highlightcolor="black",command=lambda:display.config(text=compressor(entry1.get(),entry2.get())))  
btn2=tk.Button(window,text="decompress",padx=3,pady=3,justify="center",bd=3,relief="sunken",highlightcolor="black",command=lambda:display.config(text=decompressor(entry1.get(),entry2.get())))  
display=tk.Label(window)

input.grid(row=0,column=0,columnspan=2, padx=10, pady=10, sticky="we")
entry1.grid(row=0,column=2,columnspan=2, padx=10, pady=10, sticky="we")
input_bt.grid(row=0,column=4,columnspan=2, padx=10, pady=10, sticky="we")
output.grid(row=1,column=0,columnspan=2, padx=10, pady=10, sticky="we")
entry2.grid(row=1,column=2,columnspan=2, padx=10, pady=10, sticky="we")
output_bt.grid(row=1,column=4,columnspan=2, padx=10, pady=10, sticky="we")
btn1.grid(row=3,column=1,columnspan=2, padx=10, pady=10, sticky="we")
btn2.grid(row=4,column=1,columnspan=2, padx=10, pady=10, sticky="we")
display.grid(row=5,column=2,columnspan=2, padx=10, pady=10, sticky="we")


window.mainloop()