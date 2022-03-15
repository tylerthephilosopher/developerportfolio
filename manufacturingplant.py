from tkinter import *
root = Tk()
root.title("ManufacturingPlant")
def get_results():
    product_name= E1.get()
    product_num = E2.get()
    product_vendor = E3.get()

    file = open("manufacturingplantrecords.txt", "a")
    file.write(product_name + ":" + product_num + ":" + product_vendor + ":" + "\n")
    file.close()


L1 = Label(root, text="Product Name: ")
L1.grid(column=0, row=1)
E1 = Entry(root)
E1.grid(column=1, row=1)
L2 = Label(root, text="Product #: ")
L2.grid(column=0, row=2)
E2 = Entry(root)
E2.grid(column=1, row=2)
L3 = Label(root, text="Vendor: ")
L3.grid(column=0, row=3)
E3 = Entry(root)
E3.grid(column=1, row=3)

process_button = Button(root, text="Process", command=get_results)
process_button.grid(column=0, row=4)

root.mainloop()