from tkinter import *
import requests
from tkinter import messagebox as mb
from tkinter import filedialog as fd
from tkinter import ttk
import pyperclip

def upload():
    try:
        filepath = fd.askopenfilename()
        if filepath:
            with open(filepath, 'rb') as f:
                files = {'file': f}
                response = requests.post('https://file.io', files= files)
                response.raise_for_status()
                download_link = response.json()['link']
                entry.insert(0, download_link)
                pyperclip.copy(download_link)
                mb.showinfo('Успешно!','Ссылка успешно скопирована')
        else:
            raise ValueError('Не удалось отправить файл')
    except ValueError as v:
        mb.showerror('Ошибка!', f'Произошла ошибка {v}')
    except Exception as e:
        mb.showerror('Ошибка!', f'Произошла ошибка {e}')


w = Tk()
w.title('Файл в облако')
w.geometry('400x200')

upload_button = ttk.Button(text = 'Загрузить файл', command = upload)
upload_button.pack()

entry = ttk.Entry()
entry.pack()

w.mainloop()

