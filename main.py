from tkinter import *
import requests
from tkinter import messagebox as mb
from tkinter import filedialog as fd
from tkinter import ttk
import pyperclip
import json
import os


def upload():
    try:
        filepath = fd.askopenfilename()
        if filepath:
            with open(filepath, 'rb') as f:
                files = {'file': f}
                response = requests.post('https://file.io', files= files)
                response.raise_for_status()
                download_link = response.json()['link']
                # entry.delete(0, END)
                entry.insert(0, download_link)
                pyperclip.copy(download_link)
                save_history(filepath, download_link)
                mb.showinfo('Успешно!','Ссылка успешно скопирована')
        else:
            raise ValueError('Не удалось отправить файл')
    except ValueError as v:
        mb.showerror('Ошибка!', f'Произошла ошибка {v}')
    except Exception as e:
        mb.showerror('Ошибка!', f'Произошла ошибка {e}')

def save_history(file_path, download_link):
    hist_list = []
    if os.path.exists(history_file):
        with open(history_file, 'r') as file:
            history = json.load(file)

    hist_list.append({'file_path': os.path.basename(file_path),
                      'download_link': download_link})
    with open(history_file, 'w') as file:
        json.dump(hist_list, file, indent = 4)




history_file = 'History.json'

w = Tk()
w.title('Файл в облако')
w.geometry('400x200')

upload_button = ttk.Button(text = 'Загрузить файл', command = upload)
upload_button.pack()

entry = ttk.Entry()
entry.pack()

w.mainloop()

