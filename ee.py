from Tkinter import *
#from Crypto.Cipher import DES3

def ci():
	plaintext = E1.get()
	key = int(E2.get())
	# encipher
	ciphertext = ""
	for c in plaintext.upper():
	    if c.isalpha(): ciphertext += I2L[ (L2I[c] + key)%26 ]
	    else: ciphertext += c

	print ciphertext
	L3 = Label(root, text="Result is :")
	L3.pack()
	L3 = Label(root, text=ciphertext)
	L3.pack()

def sel():
   selection = "You selected the option " + str(var.get())
   label.config(text = selection)

L2I = dict(zip("ABCDEFGHIJKLMNOPQRSTUVWXYZ",range(26)))
I2L = dict(zip(range(26),"ABCDEFGHIJKLMNOPQRSTUVWXYZ"))
root = Tk()
var = IntVar()
f=Frame(root,height=5,width=500)
f.pack()
text = StringVar()
L1 = Label(root, text="Enter text")
L1.pack()
E1 = Entry(root)
E1.pack()
E1.focus_set()

text = StringVar()
L2 = Label(root, text="Enter key")
L2.pack()
E2 = Entry(root)
E2.pack()
E2.focus_set()

R1 = Radiobutton(root, text="Ceaser cipher",  variable=var, value=1, command=ci)
R1.pack( anchor = W )

R2 = Radiobutton(root, text="Palyfair", variable=var, value=2,
                  command=sel)
R2.pack( anchor = W )

R3 = Radiobutton(root, text="DES", variable=var, value=3,
                  command=sel)
R3.pack( anchor = W)

label = Label(root)
label.pack()

root.mainloop()
