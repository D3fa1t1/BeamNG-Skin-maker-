from tkinter import ttk
import tkinter as tk
import tkinter.messagebox as mb
import tkinter.filedialog as fd
# from wand import image

import shutil
import os

path = ''
current_car = ''
name = ''
filename = ''
directory = ''


def make_skin():
    global current_car
    global path
    global name
    name = name_skin.get()
    game_name = game_name_skin.get()
    current_car = car_choice.get()
    path = 'temp/vehicles/' + current_car + '/' + name
    jbeam_path = path + '/' + current_car + '.jbeam'
    json_path = path + '/materials.json'
    os.makedirs(path)
    print(jbeam_path)
    if name:
        with open('template/template.jbeam', 'r') as file:
            repl = file.read().replace('NAME', name)
            repl = repl.replace('GNAM', game_name)
            repl = repl.replace('CARSS', current_car)
        with open(jbeam_path, 'w') as file:
            file.writelines(repl)
    if game_name:
        with open('template/' + current_car + '.json', 'r') as file:
            repl = file.read().replace('SKINNAME', name)
        with open(json_path, 'w') as file:
            file.writelines(repl)
        create_zip()


def create_zip():
    if filename[-3:] == 'dds':
        choose_directory()
        name_dds = current_car + '_skin_' + name + '.dds'
        shutil.copy2(filename, path + '/' + name_dds)
        shutil.make_archive(name, 'zip', 'temp')
        shutil.rmtree('temp')
        mb.showinfo(title='Успешно', message='Скин создан')
        shutil.copy2(name+'.zip', directory)
    # elif filename[-3:] == 'png':
    #     with image.Image(filename=filename) as img:
    #         img.compression = 'dxt5'
    #         name_dds = current_car + '_skin_' + name + '.dds'
    #         img.save(filename=path + '/' + name_dds)
    #         shutil.make_archive(name, 'zip', 'temp')
    #         shutil.rmtree('temp')
    #         mb.showinfo(title='Успешно', message='Скин создан')


def choose_file():
    global filename
    filetypes = (("Изображение", "*.dds *.png"),)
    filename = fd.askopenfilename(title="Открыть файл", initialdir="/",
                                  filetypes=filetypes)


def choose_directory():
    global directory
    directory = fd.askdirectory(title="Открыть папку", initialdir="/")


def open_json():
    pass


cars = ("coupe", "etk800", "etki")

root = tk.Tk()

root.geometry(f"300x400+1300+700")
root.title('Skin Creator v1')
root.resizable(False, False)

car_choice = ttk.Combobox(root, values=cars)
car_choice.current(0)
name_skin = ttk.Entry(root)
game_name_skin = ttk.Entry(root)


def frame():
    ttk.Label(text='Выбор машины').pack()
    car_choice.pack()
    ttk.Label(text='Имя скина(одно слово)').pack()
    name_skin.pack()
    ttk.Label(text='Название в игре').pack()
    game_name_skin.pack()
    ttk.Button(root, text='Выбрать скин', command=choose_file).pack()
    ttk.Button(root, text='Создать мод', command=make_skin).pack()


frame()
root.mainloop()