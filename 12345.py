import tkinter as tk
from tkinter import ttk
from tkinter.filedialog import asksaveasfile

def format_string_out(items):
    return '\n-1\n'.join(items)

def save_to_file(*args):
    
    firstName, middleInitial, lastName, userLinkedin, userGithub, userPhone, userEmail, userWork, userEducation, userSkills, userProjects = args

  
    personal_info = [firstName.get(), middleInitial.get(), lastName.get(), 
                     userLinkedin.get(), userGithub.get(), userPhone.get(),
                     userEmail.get()]
    string_to_save = format_string_out(personal_info)

   
    for user_data in [userEducation, userWork, userSkills, userProjects]:
        if len(user_data) > 0:
            user_data_str = '\n'.join([str(d) for d in user_data])
            string_to_save += '\n-1\n' + user_data_str

    
    with asksaveasfile(filetypes=[('All Files', "*.*"), ('Text Document', '*.txt')], defaultextension='.txt') as file:
        if file:
            file.write(string_to_save)

def make_settings_tab(parent, *args):
    new_frame = tk.Frame(parent)
    save_button = tk.Button(new_frame, text="Save As", command=lambda: save_to_file(*args))
    save_button.grid(column=0, row=0)
    return new_frame
