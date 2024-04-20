import tkinter as tk
from tkinter import messagebox
import csv
import datetime

data = []

def login():
    with open('employee.csv', mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            data.append(row)
    username = username_entry.get()
    password = password_entry.get()
    inp=[username,password]

    # Dummy login check (replace with actual authentication logic)
    if inp in data:
        show_form_page()
    else:
        messagebox.showerror("Error", "Invalid username or password")
        
def show_form_page():
    login_frame.pack_forget()
    form_frame.pack()

def save_to_csv():
    with open('FIR1.csv', mode='a', newline='') as file:
        reader = list(csv.reader(file))
        last_row = reader[-1]
        fir_id = last_row[0]
        file.close()
    caller_name = caller_name_entry.get()
    caller_num = caller_num_entry.get()
    house_id = house_id_entry.get()
    society = society_entry.get()
    area = area_entry.get()
    code = code_entry.get()
    victim = victim_entry.get()
    current_datetime = datetime.datetime.now()
    report_date_time = current_datetime.strftime('%Y-%m-%d %H:%M:%S')
    medical_help = medical_help_entry.get()

    if '' in (fir_id, caller_name, caller_num, house_id, society, area, code, victim, report_date_time, medical_help):
        messagebox.showerror("Error", "Please fill in all fields.")
    else:
        with open('FIR1.csv', mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([fir_id, caller_name, caller_num, house_id, society, area, code, victim, report_date_time, medical_help])
        messagebox.showinfo("Success", "Data saved successfully.")

root = tk.Tk()
root.title("MultiPage App")

login_frame = tk.Frame(root)
login_frame.pack()

login_label = tk.Label(login_frame, text="Login Page")
login_label.pack(pady=10)

username_frame = tk.Frame(login_frame)
username_frame.pack()

username_label = tk.Label(username_frame, text="Username:")
username_label.pack(side="left")

username_entry = tk.Entry(username_frame)
username_entry.pack(side="right", padx=10)
username_entry.focus_set()

password_frame = tk.Frame(login_frame)
password_frame.pack()

password_label = tk.Label(password_frame, text="Password:")
password_label.pack(side="left")

password_entry = tk.Entry(password_frame, show="*")
password_entry.pack(side="right", padx=10)

login_button = tk.Button(login_frame, text="Login", command=login)
login_button.pack(pady=5, padx=10)

form_frame = tk.Frame(root)

form_label = tk.Label(form_frame, text="Form Page")
form_label.pack(pady=10)

caller_name_frame = tk.Frame(form_frame)
caller_name_frame.pack()

caller_name_label = tk.Label(caller_name_frame, text="Caller Name:")
caller_name_label.pack(side="left")

caller_name_entry = tk.Entry(caller_name_frame)
caller_name_entry.pack(side="right", padx=10)

caller_num_frame = tk.Frame(form_frame)
caller_num_frame.pack()

caller_num_label = tk.Label(caller_num_frame, text="Caller Number:")
caller_num_label.pack(side="left")

caller_num_entry = tk.Entry(caller_num_frame)
caller_num_entry.pack(side="right", padx=10)

house_id_frame = tk.Frame(form_frame)
house_id_frame.pack()

house_id_label = tk.Label(house_id_frame, text="House ID:")
house_id_label.pack(side="left")

house_id_entry = tk.Entry(house_id_frame)
house_id_entry.pack(side="right", padx=10)

society_frame = tk.Frame(form_frame)
society_frame.pack()

society_label = tk.Label(society_frame, text="Society:")
society_label.pack(side="left")

society_entry = tk.Entry(society_frame)
society_entry.pack(side="right", padx=10)
society_entry.focus_set()

area_frame = tk.Frame(form_frame)
area_frame.pack()

area_label = tk.Label(area_frame, text="Area:")
area_label.pack(side="left")

area_entry = tk.Entry(area_frame)
area_entry.pack(side="right", padx=10)

code_frame = tk.Frame(form_frame)
code_frame.pack()

code_label = tk.Label(code_frame, text="Code:")
code_label.pack(side="left")

code_entry = tk.Entry(code_frame)
code_entry.pack(side="right", padx=10)

victim_frame = tk.Frame(form_frame)
victim_frame.pack()

victim_label = tk.Label(victim_frame, text="Victim:")
victim_label.pack(side="left")

victim_entry = tk.Entry(victim_frame)
victim_entry.pack(side="right", padx=10)

medical_help_frame = tk.Frame(form_frame)
medical_help_frame.pack()

medical_help_label = tk.Label(medical_help_frame, text="Medical Help:")
medical_help_label.pack(side="left")

medical_help_entry = tk.Entry(medical_help_frame)
medical_help_entry.pack(side="right", padx=10)

save_button = tk.Button(form_frame, text="Save", command=save_to_csv)
save_button.pack(pady=5, padx=10)

form_frame.pack_forget()

root.geometry("400x500")
root.mainloop()
