import tkinter as tk
from tkinter import ttk
contacts = []
def add_contact():
    name = name_entry.get()
    phone = phone_entry.get()
    email = email_entry.get()
    address = address_entry.get()
    
    contacts.append({"Name": name, "Phone": phone, "Email": email, "Address": address})
    update_contact_list()
def update_contact_list():
    contact_list.delete(0, tk.END)
    for contact in contacts:
        contact_list.insert(tk.END, f"{contact['Name']} - {contact['Phone']}")
def search_contact():
    search_term = search_entry.get()
    search_results = [contact for contact in contacts if search_term in contact["Name"] or search_term in contact["Phone"]]
    
    contact_list.delete(0, tk.END)
    for contact in search_results:
        contact_list.insert(tk.END, f"{contact['Name']} - {contact['Phone']}")
def delete_contact():
    selected_contact = contact_list.curselection()
    if selected_contact:
        del contacts[selected_contact[0]]
        update_contact_list()
root = tk.Tk()
root.title("Contact Information App")
name_label = ttk.Label(root, text="Name:")
name_label.pack()
name_entry = ttk.Entry(root)
name_entry.pack()

phone_label = ttk.Label(root, text="Phone:")
phone_label.pack()
phone_entry = ttk.Entry(root)
phone_entry.pack()

email_label = ttk.Label(root, text="Email:")
email_label.pack()
email_entry = ttk.Entry(root)
email_entry.pack()

address_label = ttk.Label(root, text="Address:")
address_label.pack()
address_entry = ttk.Entry(root)
address_entry.pack()


add_button = ttk.Button(root, text="Add Contact", command=add_contact)
add_button.pack()


search_label = ttk.Label(root, text="Search:")
search_label.pack()
search_entry = ttk.Entry(root)
search_entry.pack()

search_button = ttk.Button(root, text="Search", command=search_contact)
search_button.pack()


contact_list = tk.Listbox(root)
contact_list.pack()


delete_button = ttk.Button(root, text="Delete Contact", command=delete_contact)
delete_button.pack()


root.mainloop()