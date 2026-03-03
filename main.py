import ttkbootstrap as ttk

def generate():
    try:
        entry_int = float(entry_field.get())
        output_int = entry_int * 1.61
        output_label.config(text = str(output_int) + ' km', font= 'Calibri 22', bootstyle= 'success')
    except ValueError:
        output_label.config(text='Choose a number.', font='Helvetica 30 bold', bootstyle='danger')

app = ttk.Window(themename='darkly')
app.title('Mile to Kilometer')


window_width = 500
window_height = 200
screen_width = app.winfo_screenwidth()
screen_height = app.winfo_screenheight()
x = (screen_width // 2) - (window_width // 2)
y = (screen_height // 2) - (window_height // 2)
app.geometry(f'{window_width}x{window_height}+{x}+{y}')

label = ttk.Label(master=app, text='Mile to Kilometer converter', font='Calibri 24 bold')
label.pack()

input_frame = ttk.Frame(master=app)
input_frame.pack(pady=40)

entry_field = ttk.Entry(master=input_frame, bootstyle='light')
entry_field.pack(side='left', padx=10)

button = ttk.Button(master=input_frame, text='➤', command=generate, bootstyle='light3')
button.pack(side='left')

output_label = ttk.Label(master=app, text='Choose a value and click the button to convert', font='Calibri 20 italic', bootstyle='info')
output_label.pack()

app.mainloop()
