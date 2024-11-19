import tkinter as tk
from tkinter import ttk

def create_combo_set(parent, label_text, input, list_of_values):
    """
    Creates a combo box and a label for the given parent widget.
    
    Args:
        parent (tk.Widget): The parent widget.
        label_text (str): The text for the label.
        input (tk.StringVar): The input variable for the combo box.
        list_of_values (list): A list of values to populate the combo box.
    
    Returns:
        tuple: The created combo box and label.
    """
    return ttk.Combobox(parent, textvariable=input, values=list_of_values), tk.Label(parent, text=label_text)

def create_combo_set3(parent, label_text, input, list_of_values, nameOfCombo):
    """
    Creates a combo box with a name and a label for the given parent widget.
    
    Args:
        parent (tk.Widget): The parent widget.
        label_text (str): The text for the label.
        input (tk.StringVar): The input variable for the combo box.
        list_of_values (list): A list of values to populate the combo box.
        nameOfCombo (str): The name of the combo box.
    
    Returns:
        tuple: The created combo box and label.
    """
    return ttk.Combobox(parent, textvariable=input, values=list_of_values, name=nameOfCombo), tk.Label(parent, text=label_text)

def create_label_entry(parent, label_text, input):
    """
    Creates an entry field and a label for the given parent widget.
    
    Args:
        parent (tk.Widget): The parent widget.
        label_text (str): The text for the label.
        input (tk.StringVar): The input variable for the entry field.
    
    Returns:
        tuple: The created entry field and label.
    """
    return tk.Entry(parent, textvariable=input), ttk.Label(parent, text=label_text)

def create_check_box_label(parent, string_text, input):
    """
    Creates a check button and a label for the given parent widget.
    
    Args:
        parent (tk.Widget): The parent widget.
        string_text (str): The text for the check button.
        input (tk.Variable): The variable for the check button.
    
    Returns:
        ttk.Checkbutton: The created check button.
    """
    return ttk.Checkbutton(parent, text=string_text, variable=input, offvalue=False, onvalue=True)

def create_label_text_field(parent, label_text, name_of_textfield):
    """
    Creates a text field and a label for the given parent widget.
    
    Args:
        parent (tk.Widget): The parent widget.
        label_text (str): The text for the label.
        name_of_textfield (str): The name of the text field.
    
    Returns:
        tuple: The created label and text field.
    """
    return ttk.Label(parent, text=label_text, wraplength=125), tk.Text(parent, width=50, height=6, name=name_of_textfield)

def create_spin_month_year(parent, label_text, month=1, year=1950, years_list=None):
    """
    Creates a label and two combo boxes for selecting month and year.
    
    Args:
        parent (tk.Widget): The parent widget.
        label_text (str): The text for the label.
        month (int): The default month.
        year (int): The default year.
        years_list (list): A list of years to populate the year combo box.
    
    Returns:
        tuple: The created label and combo boxes for month and year.
    """
    if years_list is None:
        years_list = []
    return (ttk.Label(parent, text=label_text),
            ttk.Combobox(parent, width=5, textvariable=month, values=[i for i in range(1, 13)]),
            ttk.Label(parent, text=" - "),
            ttk.Combobox(parent, width=5, textvariable=year, values=years_list))

def make_list_from_text(text_box_in, string_detail_name):
    """
    Creates a list of dictionaries from the text content of a text box.
    
    Args:
        text_box_in (tk.Text): The text box widget.
        string_detail_name (str): The name of the detail to be included in the dictionary.
    
    Returns:
        list: A list of dictionaries with the text details.
    """
    return [{"isRelevent": True, string_detail_name: item}
            for item in text_box_in.get("1.0", 'end-1c').split('\n') if item]
