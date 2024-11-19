import tkinter as tk
from tkinter import ttk
from commontools2 import create_label_entry

def makePersonalInformationtab(parent, firstName, middleInitial, lastName, userLinkedin, 
                               userGithub, userPhone, userEmail):
    """
    Creates a personal information tab and populates it with input fields.
    
    Args:
        parent (tk.Widget): The parent widget for the tab frame.
        firstName (tk.StringVar): Variable for storing the first name.
        middleInitial (tk.StringVar): Variable for storing the middle initial.
        lastName (tk.StringVar): Variable for storing the last name.
        userLinkedin (tk.StringVar): Variable for storing the LinkedIn profile.
        userGithub (tk.StringVar): Variable for storing the GitHub profile.
        userPhone (tk.StringVar): Variable for storing the phone number.
        userEmail (tk.StringVar): Variable for storing the email address.
    
    Returns:
        tk.Frame: The created frame for the personal information tab.
    """
    newFrame = tk.Frame(parent)
    curCol, currRow = 0, 0

    # First Name Entry
    newEntry, newLabel = create_label_entry(newFrame, "First name: ", firstName)
    newLabel.grid(column=curCol, row=currRow)
    curCol += 1
    newEntry.grid(column=curCol, row=currRow)
    curCol, currRow = 0, currRow + 1

    # Middle Initial Entry
    newEntry, newLabel = create_label_entry(newFrame, "Middle Initial: ", middleInitial)
    newLabel.grid(column=curCol, row=currRow)
    curCol += 1
    newEntry.grid(column=curCol, row=currRow)
    curCol, currRow = 0, currRow + 1

    # Last Name Entry
    newEntry, newLabel = create_label_entry(newFrame, "Last name: ", lastName)
    newLabel.grid(column=curCol, row=currRow)
    curCol += 1
    newEntry.grid(column=curCol, row=currRow)
    curCol, currRow = 0, currRow + 1

    # LinkedIn Entry
    newEntry, newLabel = create_label_entry(newFrame, "LinkedIn: ", userLinkedin)
    newLabel.grid(column=curCol, row=currRow)
    curCol += 1
    newEntry.grid(column=curCol, row=currRow)
    curCol, currRow = 0, currRow + 1

    # GitHub Entry
    newEntry, newLabel = create_label_entry(newFrame, "Github: ", userGithub)
    newLabel.grid(column=curCol, row=currRow)
    curCol += 1
    newEntry.grid(column=curCol, row=currRow)
    curCol, currRow = 0, currRow + 1

    # Phone Number Entry
    newEntry, newLabel = create_label_entry(newFrame, "Phone Number: ", userPhone)
    newLabel.grid(column=curCol, row=currRow)
    curCol += 1
    newEntry.grid(column=curCol, row=currRow)
    curCol, currRow = 0, currRow + 1

    # Email Entry
    newEntry, newLabel = create_label_entry(newFrame, "Email: ", userEmail)
    newLabel.grid(column=curCol, row=currRow)
    curCol += 1
    newEntry.grid(column=curCol, row=currRow)
    curCol, currRow = 0, currRow + 1

    return newFrame
