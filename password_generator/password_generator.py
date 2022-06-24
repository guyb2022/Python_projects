from tkinter import *
from tkinter import messagebox
from random import shuffle, randint, choice
import pyperclip
import json

YELLOW = "#f7f5dd"
BLACK = '#000000'
FONT_NAME = "Courier"
FONT = ("Ariel", 10)
DEFAULT_EMAIL = 'my_email@gmail.co.il'

# SAVE CREDENTIALS
def add_password():
    """Handel the required data from user """
    is_ok = False
    password = password_input.get()
    website = website_input.get()
    email = email_username_input.get()
    new_data ={
        website: {
        'email': email,
        'password': password,
        }
    }
    messages = f'These are the details to be saved: \nEmail: {email} ' \
               f'\nPassword: {password} \n Is it OK to save?'
    if password and website:
        is_ok = True
        #is_ok = messagebox.askokcancel(title='Title', message=messages)
    else:
        messagebox.showerror(title='Not all data was entered', message="You need to fill all fields\n"
                                                                       "Website: \n"
                                                                       "Password:  ")
    if is_ok:
        try:
            with open('registration.json', 'r') as file:
                data = json.load(file)
        except FileNotFoundError:
            print(f"File: registration.json was not located")
            with open('registration.json', 'w') as file:
                json.dump(new_data, file, indent=4)
        else:
            data.update(new_data)
            with open('registration.json', 'w') as file:
                json.dump(data, file, indent=4)
        finally:
            password_input.delete(0, END)
            website_input.delete(0, END)


# PASSWORD GENERATOR
def generate_password():
    """Create the random password"""
    password_input.delete(0, END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
               'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A',
               'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O',
               'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_numbers = [choice(symbols) for _ in range(randint(2, 4))]
    password_symbols = [choice(numbers) for _ in range(randint(2, 4))]
    password_list = password_letters+password_numbers+password_symbols
    shuffle(password_list)
    password = "".join(password_list)
    password_input.insert(0, password)
    pyperclip.copy(password)


# Search the json for specific web data
def search_website():
    """Search a password for a specific website"""
    password_input.delete(0, END)
    email_username_input.delete(0, END)
    website = website_input.get()
    try:
        with open('registration.json', 'r') as file:
            data = json.load(file)
        messagebox.showinfo(title=website, message=f'Email: {data[website]["email"]} \
                                                   \nPassword: {data[website]["password"]}'
                                                   f'\nPassword copied to clipboard')

        password_input.insert(0, data[website]["password"])
        email_username_input.insert(0, data[website]["email"])
        pyperclip.copy(data[website]["password"])

    except FileNotFoundError:
        print(f"No File {file} was found, folder is empty")
        messagebox.showerror(title="File not Found", message=f'File is empty')
        email_username_input.insert(0, DEFAULT_EMAIL)
    except KeyError:
        print(f"No Key: {website}  was found")
        messagebox.showerror(title="Web not Found", message=f'The website: {website} \nWas not found in data')
        website_input.delete(0, END)
        email_username_input.insert(0, DEFAULT_EMAIL)


# UI SETUP
# Init of window
window = Tk()
window.title("Password Generator")
window.config(padx=20, pady=50, bg=YELLOW)

# creating the canvas
canvas = Canvas(width=300, height=200, bg=YELLOW, highlightthickness=0)
lock_img = PhotoImage(file="lock.png")
canvas.create_image(150, 100, image=lock_img)
canvas.grid(column=1, row=0)

# Labels
# Website Label
website_label = Label(text="Website :", font=FONT, fg=BLACK, bg=YELLOW)
website_label.grid(column=0, row=1)
website_label.focus()
# Email/Username Label
email_username_label = Label(text="Email/Username :", font=FONT, fg=BLACK, bg=YELLOW)
email_username_label.grid(column=0, row=2)
# Password label
password_label = Label(text="Password :", font=FONT, fg=BLACK, bg=YELLOW)
password_label.grid(column=0, row=4)

# Inputs
# website input
website_input = Entry(width=35)
website_input.focus()
website_input.grid(column=1, row=1)
# Email/Username input
email_username_input = Entry(width=35)
email_username_input.grid(column=1, row=2)
email_username_input.insert(0, DEFAULT_EMAIL)
# password input
password_input = Entry(width=35)
password_input.grid(column=1, row=4)

# Buttons
# Generate Password button
generate_pass_button = Button(text='Generate Password', command=generate_password,
                              highlightthickness=1, width=15)
generate_pass_button.grid(column=2, row=4)
# Add button
add_button = Button(text='Add', command=add_password, highlightthickness=0, width=30)
add_button.grid(column=1, row=5)
# Search button
search_button = Button(text='Search', command=search_website, highlightthickness=0, width=15)
search_button.grid(column=2, row=1)

window.mainloop()


