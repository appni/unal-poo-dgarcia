import tkinter as tk
from tkinter import messagebox, scrolledtext
import os

class ContactManager:
    def __init__(self, filename="friendsContact.txt"):
        self.filename = filename
        self.create_file_if_not_exists()
    
    def create_file_if_not_exists(self):
        if not os.path.exists(self.filename):
            open(self.filename, 'a').close()
    
    def contact_exists(self, name, number):
        try:
            with open(self.filename, 'r') as f:
                for line in f:
                    line = line.strip()
                    if line:
                        parts = line.split('!')
                        existing_name = parts[0]
                        existing_number = parts[1]
                        if existing_name == name or existing_number == str(number):
                            return True
        except:
            pass
        return False
    
    def add_contact(self, name, number):
        try:
            if not name or not number:
                return "Error: Name and number cannot be empty"
            
            number_str = str(number)
            if self.contact_exists(name, number_str):
                return "Error: Contact already exists"
            
            with open(self.filename, 'a') as f:
                f.write(f"{name}!{number_str}\n")
            return "Friend added successfully"
        except Exception as e:
            return f"Error: {str(e)}"
    
    def read_contacts(self):
        try:
            contacts = []
            with open(self.filename, 'r') as f:
                for line in f:
                    line = line.strip()
                    if line:
                        parts = line.split('!')
                        if len(parts) == 2:
                            contacts.append((parts[0], parts[1]))
            return contacts
        except Exception as e:
            return []
    
    def update_contact(self, old_name, new_number):
        try:
            contacts = self.read_contacts()
            found = False
            
            for i, (name, number) in enumerate(contacts):
                if name == old_name:
                    contacts[i] = (name, str(new_number))
                    found = True
                    break
            
            if not found:
                return "Error: Contact not found"
            
            with open(self.filename, 'w') as f:
                for name, number in contacts:
                    f.write(f"{name}!{number}\n")
            return "Friend updated successfully"
        except Exception as e:
            return f"Error: {str(e)}"
    
    def delete_contact(self, name):
        try:
            contacts = self.read_contacts()
            
            contacts = [(n, num) for n, num in contacts if n != name]
            
            if len(contacts) == len(self.read_contacts()):
                return "Error: Contact not found"
            
            with open(self.filename, 'w') as f:
                for n, num in contacts:
                    f.write(f"{n}!{num}\n")
            return "Friend deleted successfully"
        except Exception as e:
            return f"Error: {str(e)}"


class ContactManagerGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Friends Contact Manager")
        self.root.geometry("600x700")
        self.root.configure(bg="#f0f0f0")
        
        self.manager = ContactManager()
        
        self.create_widgets()
    
    def create_widgets(self):
        title = tk.Label(self.root, text="Friends Contact Manager", 
                        font=("Arial", 18, "bold"), bg="#f0f0f0")
        title.pack(pady=10)
        
        input_frame = tk.LabelFrame(self.root, text="Contact Information", 
                                   font=("Arial", 10, "bold"), bg="#f0f0f0")
        input_frame.pack(padx=10, pady=10, fill="x")

        tk.Label(input_frame, text="Name:", bg="#f0f0f0").grid(row=0, column=0, sticky="w", padx=5, pady=5)
        self.name_entry = tk.Entry(input_frame, width=20)
        self.name_entry.grid(row=0, column=1, padx=5, pady=5)
        
        tk.Button(input_frame, text="READ", command=self.display_contacts, 
                 bg="#2196F3", fg="white", font=("Arial", 9, "bold"), width=10).grid(row=0, column=2, padx=5, pady=5)
        
        tk.Button(input_frame, text="CLEAR", command=self.clear_fields, 
                 bg="#9C27B0", fg="white", font=("Arial", 9, "bold"), width=10).grid(row=0, column=3, padx=5, pady=5)
        
        tk.Label(input_frame, text="Number:", bg="#f0f0f0").grid(row=1, column=0, sticky="w", padx=5, pady=5)
        self.number_entry = tk.Entry(input_frame, width=20)
        self.number_entry.grid(row=1, column=1, padx=5, pady=5)
        
        tk.Button(input_frame, text="UPDATE", command=self.update_contact, 
                 bg="#FF9800", fg="white", font=("Arial", 9, "bold"), width=10).grid(row=1, column=2, padx=5, pady=5)
        
        tk.Button(input_frame, text="CREATE", command=self.add_contact, 
                 bg="#4CAF50", fg="white", font=("Arial", 9, "bold"), width=10).grid(row=2, column=0, padx=5, pady=5)
        
        tk.Button(input_frame, text="DELETE", command=self.delete_contact, 
                 bg="#f44336", fg="white", font=("Arial", 9, "bold"), width=10).grid(row=2, column=1, padx=5, pady=5)
        
        display_frame = tk.LabelFrame(self.root, text="Contacts List", 
                                     font=("Arial", 10, "bold"), bg="#f0f0f0")
        display_frame.pack(padx=10, pady=10, fill="both", expand=True)
        
        self.display_text = scrolledtext.ScrolledText(display_frame, height=15, width=70, 
                                                      font=("Courier", 10))
        self.display_text.pack(padx=5, pady=5, fill="both", expand=True)
        self.display_text.config(state="disabled")
        
        self.status_var = tk.StringVar(value="Ready")
        status_bar = tk.Label(self.root, textvariable=self.status_var, 
                             bg="#e0e0e0", anchor="w", font=("Arial", 9))
        status_bar.pack(side="bottom", fill="x", padx=5, pady=5)
    
    def add_contact(self):
        name = self.name_entry.get().strip()
        number = self.number_entry.get().strip()
        
        if not name or not number:
            messagebox.showerror("Error", "Please enter both name and number")
            return
        
        try:
            number = int(number)
        except ValueError:
            messagebox.showerror("Error", "Number must be a valid integer")
            return
        
        result = self.manager.add_contact(name, number)
        if result.startswith("Error"):
            messagebox.showerror("Error", result)
        else:
            messagebox.showinfo("Success", result)
            self.clear_fields()
            self.display_contacts()
        
        self.status_var.set(result)
    
    def display_contacts(self):
        name_filter = self.name_entry.get().strip()
        number_filter = self.number_entry.get().strip()
        
        all_contacts = self.manager.read_contacts()
        
        filtered_contacts = []
        for name, number in all_contacts:
            name_match = (not name_filter) or (name_filter.lower() in name.lower())
            number_match = (not number_filter) or (number_filter in number)
            
            if name_match and number_match:
                filtered_contacts.append((name, number))
        
        self.display_text.config(state="normal")
        self.display_text.delete(1.0, tk.END)
        
        if not filtered_contacts:
            self.display_text.insert(tk.END, "No contacts found.\n")
        else:
            self.display_text.insert(tk.END, "=" * 50 + "\n")
            self.display_text.insert(tk.END, f"{'Name':<25} {'Contact Number':<20}\n")
            self.display_text.insert(tk.END, "=" * 50 + "\n")
            
            for name, number in filtered_contacts:
                self.display_text.insert(tk.END, f"{name:<25} {number:<20}\n")
            
            self.display_text.insert(tk.END, "=" * 50 + "\n")
            self.display_text.insert(tk.END, f"Total Contacts: {len(filtered_contacts)}\n")
        
        self.display_text.config(state="disabled")
        self.status_var.set(f"Displaying {len(filtered_contacts)} contact(s)")
    
    def update_contact(self):
        name = self.name_entry.get().strip()
        number = self.number_entry.get().strip()
        
        if not name or not number:
            messagebox.showerror("Error", "Please enter both name and new number")
            return
        
        try:
            number = int(number)
        except ValueError:
            messagebox.showerror("Error", "Number must be a valid integer")
            return
        
        result = self.manager.update_contact(name, number)
        if result.startswith("Error"):
            messagebox.showerror("Error", result)
        else:
            messagebox.showinfo("Success", result)
            self.clear_fields()
            self.display_contacts()
        
        self.status_var.set(result)
    
    def delete_contact(self):
        name = self.name_entry.get().strip()
        
        if not name:
            messagebox.showerror("Error", "Please enter the name to delete")
            return
        
        if messagebox.askyesno("Confirm", f"Are you sure you want to delete '{name}'?"):
            result = self.manager.delete_contact(name)
            if result.startswith("Error"):
                messagebox.showerror("Error", result)
            else:
                messagebox.showinfo("Success", result)
                self.clear_fields()
                self.display_contacts()
            
            self.status_var.set(result)
    
    def clear_fields(self):
        self.name_entry.delete(0, tk.END)
        self.number_entry.delete(0, tk.END)
        self.status_var.set("Fields cleared")


if __name__ == "__main__":
    root = tk.Tk()
    gui = ContactManagerGUI(root)
    root.mainloop()
