import tkinter as tk
from tkinter import ttk

def create_combo_set(parent, label_text, input, list_of_values):
    return ttk.Combobox(parent, textvariable=input, values=list_of_values), tk.Label(parent, text=label_text)

def create_label_entry(parent, label_text, input):
    return tk.Entry(parent, textvariable=input), ttk.Label(parent, text=label_text)

def create_check_box_label(parent, string_text, input):
    return ttk.Checkbutton(parent, text=string_text, variable=input, offvalue=False, onvalue=True)

def create_label_text_field(parent, label_text, name_of_textfield):
    return ttk.Label(parent, text=label_text, wraplength=125), tk.Text(parent, width=50, height=6, name=name_of_textfield)

def create_spin_month_year(parent, label_text, month=1, year=1950, years_list=None):
    if years_list is None:
        years_list = []
    return (ttk.Label(parent, text=label_text),
            ttk.Combobox(parent, width=5, textvariable=month, values=[i for i in range(1, 13)]),
            ttk.Label(parent, text=" - "),
            ttk.Combobox(parent, width=5, textvariable=year, values=years_list))

def make_list_from_text(text_box_in, string_detail_name):
    return [{"isRelevent": True, string_detail_name: item}
            for item in text_box_in.get("1.0", 'end-1c').split('\n') if item]
