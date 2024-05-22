import tkinter as tk
from tkinter import messagebox

class Member:
    _id_counter = 1

    def __init__(self, name, address, phone, gender, dob, id_number):
        self.member_id = Member._id_counter
        Member._id_counter += 1
        self.name = name
        self.address = address
        self.phone = phone
        self.gender = gender
        self.dob = dob
        self.id_number = id_number

    def __str__(self):
        return (f"Member ID: {self.member_id}, Name: {self.name}, Address: {self.address}, "
                f"Phone: {self.phone}, Gender: {self.gender}, DOB: {self.dob}, ID Number: {self.id_number}")

member_stack = []

def create_member():
    name = name_entry.get()
    address = address_entry.get()
    phone = phone_entry.get()
    gender = gender_var.get()
    dob = dob_entry.get()
    id_number = id_number_entry.get()

    if not (name and address and phone and dob and gender and id_number):
        messagebox.showerror("Error", "Please fill in all required fields.")
        return

    new_member = Member(name, address, phone, gender, dob, id_number)
    member_stack.append(new_member) 

    member_listbox.insert(tk.END, str(new_member))

    name_entry.delete(0, tk.END)
    address_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    dob_entry.delete(0, tk.END)
    id_number_entry.delete(0, tk.END)
    gender_var.set(None)  

    messagebox.showinfo("Success", "Member created successfully.")

def delete_member():
    selected_index = guest_listbox.curselection()
    if not selected_index:
        messagebox.showerror("Error", "Please select a member to delete.")
        return

    guest_listbox.delete(selected_index)
    del member_stack[selected_index[0]]

def center_window(win):
    win.update_idletasks()
    width = win.winfo_width()
    height = win.winfo_height()
    minwidth = 400
    minheight = 400
    if width < minwidth:
        width = minwidth
    if height < minheight:
        height = minheight
    x = (win.winfo_screenwidth() // 2) - (width // 2)
    y = (win.winfo_screenheight() // 2) - (height // 2)
    win.geometry(f'{width}x{height}+{x}+{y}')

def validate_name(char):
    return char.isalpha() or char.isspace()

def validate_number(char):
    return char.isdigit()

def opening_form():
    global abc
    abc = tk.Tk()
    abc.title("Welcome to member regristration")
    text_label = tk.Label(abc, text="welcome")
    text_label.pack()
    button = tk.Button(abc, text="registration", command=create_member_form)
    button.pack()
    button = tk.Button(abc, text="list", command=delete_member_form)
    button.pack()
    center_window(abc)
    abc.mainloop()

def create_member_form():
    abc.destroy()
    global root
    root = tk.Tk()
    root.title("Member Registration")

    root.grid_rowconfigure(0, weight=1)
    root.grid_rowconfigure(1, weight=1)
    root.grid_rowconfigure(2, weight=1)
    root.grid_rowconfigure(3, weight=1)
    root.grid_rowconfigure(4, weight=1)
    root.grid_rowconfigure(5, weight=1)
    root.grid_rowconfigure(6, weight=1)
    root.grid_rowconfigure(7, weight=1)
    root.grid_rowconfigure(8, weight=1)

    root.grid_columnconfigure(0, weight=1)
    root.grid_columnconfigure(1, weight=1)



    tk.Label(root, text="Name:").grid(row=0, column=0, sticky="w", padx=10, pady=5)
    tk.Label(root, text="Address:").grid(row=1, column=0, sticky="w", padx=10, pady=5)
    tk.Label(root, text="Phone:").grid(row=2, column=0, sticky="w", padx=10, pady=5)
    tk.Label(root, text="Gender:").grid(row=3, column=0, sticky="w", padx=10, pady=5)
    tk.Label(root, text="Date of Birth:").grid(row=4, column=0, sticky="w", padx=10, pady=5)
    tk.Label(root, text="ID Number:").grid(row=5, column=0, sticky="w", padx=10, pady=5)

    validate_name_cmd = root.register(validate_name)
    validate_number_cmd = root.register(validate_number)

    global name_entry
    name_entry = tk.Entry(root, validate="key", validatecommand=(validate_name_cmd, '%S'))
    global address_entry
    address_entry = tk.Entry(root)
    global phone_entry 
    phone_entry = tk.Entry(root, validate="key", validatecommand=(validate_number_cmd, '%S'))
    name_entry.grid(row=0, column=1, sticky="ew", padx=10, pady=5)
    address_entry.grid(row=1, column=1, sticky="ew", padx=10, pady=5)
    phone_entry.grid(row=2, column=1, sticky="ew", padx=10, pady=5)
    global gender_var
    gender_var = tk.StringVar(value="Male") 
    global male_radio
    male_radio = tk.Radiobutton(root, text="Male", variable=gender_var, value="Male")
    global female_radio
    female_radio = tk.Radiobutton(root, text="Female", variable=gender_var, value="Female")
    male_radio.grid(row=3, column=1, sticky="w", padx=10, pady=5)
    female_radio.grid(row=3, column=1, sticky="e", padx=10, pady=5)
    gender_var.set("Male")
    global dob_entry
    dob_entry = tk.Entry(root)
    dob_entry.grid(row=4, column=1, sticky="ew", padx=10, pady=5)
    global id_number_entry
    id_number_entry = tk.Entry(root, validate="key", validatecommand=(validate_number_cmd, '%S'))
    id_number_entry.grid(row=5, column=1, sticky="ew", padx=10, pady=5)

    global submit_button
    submit_button = tk.Button(root, text="Create Member", command=create_member)
    submit_button.grid(row=6, column=1, pady=10)
    global back_button
    back_button = tk.Button(root, text="back", command=lambda:back_to_home(root))
    back_button.grid(row=6, column=0, pady=10)

    global member_listbox
    member_listbox = tk.Listbox(root, height=10, width=50)
    member_listbox.grid(row=7, column=0, columnspan=2, sticky="nsew", padx=10, pady=5)
    if len(member_stack) > 0:
        for elemen in member_stack:
            member_listbox.insert(tk.END, str(elemen))

    center_window(root)
    root.mainloop()

def back_to_home(xyz):
    xyz.destroy()
    opening_form ()

def delete_member_form():
    global branch
    abc.destroy() 
    branch= tk.Tk()
    branch.title("member list")
    branch.grid_rowconfigure(0, weight=1)
    branch.grid_rowconfigure(1, weight=1)

    branch.grid_columnconfigure(0, weight=1)
    branch.grid_columnconfigure(1, weight=1)
    global guest_listbox
    guest_listbox = tk.Listbox(branch, height=10, width=50)
    guest_listbox.grid(row=0, column=0, columnspan=2, sticky="nsew", padx=10, pady=5)
    delete_button = tk.Button(branch, text="Delete Member", command=delete_member)
    delete_button.grid(row=1, column=1, pady=10)
    global return_button
    return_button = tk.Button(branch, text="back", command=lambda:back_to_home(branch))
    return_button.grid(row=1, column=0, pady=10)
    if len(member_stack) > 0:
        for elemen in member_stack:
            guest_listbox.insert(tk.END, str(elemen))
    center_window(branch)
    
opening_form()
