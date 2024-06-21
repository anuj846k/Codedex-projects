import tkinter as tk
from tkinter import scrolledtext, font as tkfont
from IPython.display import Markdown

import google.generativeai as genai


genai.configure(api_key='Enter your own token here pls')
model = genai.GenerativeModel('gemini-pro')

def to_markdown(text):
    text = text.replace('•', '  *')
    return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

def generate_content():
    inp = entry.get()
    prp = "Write a paragraph about the following topic: " + inp
    response = model.generate_content(prp)
    result_text.delete(1.0, tk.END)
    result_text.insert(tk.END, str(response.text))


window = tk.Tk()
window.title("Blog Topic Generator")

window_width = 700
window_height = 700

screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

position_top = int(screen_height / 2 - window_height / 2)
position_right = int(screen_width / 2 - window_width / 2)

window.geometry(f'{window_width}x{window_height}+{position_right}+{position_top}')

custom_font = tkfont.Font(family="Helvetica", size=12)

entry_label = tk.Label(window, text="Enter your blog topic:", font=custom_font)
entry_label.grid(row=0, column=0, padx=30, pady=30, sticky="w")
entry = tk.Entry(window, width=50, font=custom_font)
entry.grid(row=1, column=0, padx=30, pady=30, sticky="ew")

generate_button = tk.Button(window, text="Generate", command=generate_content, font=custom_font, bg="#4CAF50", fg="white")
generate_button.grid(row=2, column=0, padx=20, pady=20)

result_label = tk.Label(window, text="Generated Paragraph:", font=custom_font)
result_label.grid(row=3, column=0, padx=10, pady=10, sticky="w")
result_text = scrolledtext.ScrolledText(window, wrap=tk.WORD, width=60, height=20, font=custom_font)
result_text.grid(row=4, column=0, padx=40, pady=40)

head = tk.Label(window, text="Made by Anuj Kumar", font=custom_font, fg="grey")
head.grid(row=5, column=0, padx=10, pady=10, sticky="e")

window.grid_columnconfigure(0, weight=1)

window.mainloop()
