from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = [choice(letters) for _ in range(randint(8, 10))]
    password_list += [choice(symbols) for _ in range(randint(2, 4))]
    password_list += [choice(numbers) for _ in range(randint(2, 4))]
    shuffle(password_list)

    password = ''.join(password_list)
    password_input.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = website_input.get().title()
    email = email_input.get()
    password = password_input.get()
    new_data = {
        website: {
            'email': email,
            'password': password
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
    else:
        is_ok = messagebox.askokcancel(title=website,
                                       message=f"These are the details entered: \nEmail: {email}\n"
                                               f"Password: {password} \nIs it ok to save?")

        if is_ok:
            # with open('./data.text', mode='a') as data_file:
            #     data_file.write(f"{website} | {email} | {password}\n")
            try:
                with open('data.json', 'r') as data_file:
                    # reading old data
                    data = json.load(data_file)
            except FileNotFoundError:
                with open('data.json', 'w') as data_file:
                    # create a new file and dump new data
                    json.dump(new_data, data_file, indent=4)
            else:
                # updating old data with new data
                data.update(new_data)

                with open('data.json', 'r') as data_file:
                    # saving updated data
                    json.dump(data, data_file, indent=4)

            website_input.delete(0, END)
            password_input.delete(0, END)
            website_input.focus()


# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    user_input = website_input.get().title()
    try:
        with open('data.json', 'r') as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title='Oops', message='No Data File Found.')
    else:
        # do if else rather than try catch
        if user_input in data:
            data = data[user_input]
            messagebox.showinfo(title=user_input, message=f"Email: {data['email']}\nPassword: {data['password']}")
        else:
            messagebox.showinfo(title='Oops', message='No detail for the website exists.')


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Password Manager')
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

website_label = Label(text='Website:')
website_label.grid(row=1, column=0)
website_input = Entry(width=25)
website_input.grid(row=1, column=1)
website_input.focus()
search_btn = Button(text='Search', width=15, command=find_password)
search_btn.grid(row=1, column=2)

email_label = Label(text='Email/Username:')
email_label.grid(row=2, column=0)
email_input = Entry(width=50)
email_input.grid(row=2, column=1, columnspan=2)
email_input.insert(0, "kanyanyouth@gmail.com")

password_label = Label(text='Password:')
password_label.grid(row=3, column=0)
password_input = Entry(width=25)
password_input.grid(row=3, column=1)
password_btn = Button(text='Generate Password', width=15, command=generate_password)
password_btn.grid(row=3, column=2)

add_btn = Button(text='Add', width=45, command=save_password)
add_btn.grid(row=4, column=1, columnspan=2)

window.mainloop()
