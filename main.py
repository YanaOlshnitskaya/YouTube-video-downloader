# Импорт необходимых пакетов
import tkinter as tk
from tkinter import *
from pytube import YouTube
from tkinter import messagebox, filedialog


# Определение функции CreateWidgets()
# для создания необходимых виджетов tkinter
def widgets():

	head_label = Label(root, text="Загрузчик видео с YouTube",
					padx=10,
					pady=10,
					font="SegoeUI 14",
					bg="#de74e8",
					fg="black",
					   )
	head_label.grid(row=1,
					column=1,
					pady=10,
					padx=5,
					columnspan=3)

	link_label = Label(root,
					text="Ссылка на видео :      ",
					bg="thistle1",
					pady=5,
					padx=5)
	link_label.grid(row=2,
					column=0,
					pady=5,
					padx=5)

	root.linkText = Entry(root,
						width=35,
						textvariable=video_Link,
						font="Arial 14")
	root.linkText.grid(row=2,
					column=1,
					pady=5,
					padx=5,
					columnspan=2)


	destination_label = Label(root,
							text="Место сохранения :",
							bg="thistle1",
							pady=5,
							padx=9)
	destination_label.grid(row=3,
						column=0,
						pady=5,
						padx=5)


	root.destinationText = Entry(root,
								width=27,
								textvariable=download_Path,
								font="Arial 14")
	root.destinationText.grid(row=3,
							column=1,
							pady=5,
							padx=5)


	browse_B = Button(root,
					text="Путь",
					command=Browse,
					width=10,
					bg="bisque",
					relief=GROOVE)
	browse_B.grid(row=3,
				column=2,
				pady=1,
				padx=1)

	Download_B = Button(root,
						text="Сохранить видео",
						command=Download,
						width=20,
						bg="thistle1",
						pady=10,
						padx=15,
						relief=GROOVE,
						font="Georgia, 13")
	Download_B.grid(row=4,
					column=1,
					pady=20,
					padx=20)


# Определение Browse() для выбора
# папки назначения для сохранения видео

def Browse():
	# Предоставляем пользователю всплывающее окно для выбора каталога. Аргумент начального каталога не является обязательным
	# Получение каталога назначения введенных пользователем данных и сохранение его в downloadDirectory
	download_Directory = filedialog.askdirectory(
		initialdir="YOUR DIRECTORY PATH", title="Save Video")

	# Отображение каталога в каталоге
	# текстовое окно
	download_Path.set(download_Directory)

# Определение Download() для загрузки видео


def Download():
	youtube_link = video_Link.get()

	# выбираем оптимальное место для
	# сохранение файла
	download_Folder = download_Path.get()

	# Создание объекта YouTube()
	getVideo = YouTube(youtube_link)

	# Получение всех доступных потоков
	# видео на YouTube и выбираем первое
	# из
	videoStream = getVideo.streams.first()

	# Загрузка видео в место назначения
	# каталог
	videoStream.download(download_Folder)

	# Отображение сообщения
	messagebox.showinfo("Успешно",
						"СКАЧАНО И СОХРАНЕНО В\n"
						+ download_Folder)


# Создание объекта класса tk
root = tk.Tk()

# Установка заголовка, цвета фона
# и размер окна tkinter и
# отключение свойства изменения размера
root.geometry("570x280")
root.resizable(False, False)
root.title("Загрузчик YouTube Video")
root.config(background="#de74e8")

# Создание переменных tkinter
video_Link = StringVar()
download_Path = StringVar()

# Вызов функции Виджеты()
widgets()

# Определение бесконечного цикла для запуска
# приложения
root.mainloop()
