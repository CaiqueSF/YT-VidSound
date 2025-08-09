from tkinter import Tk, Label, Entry, Button, PhotoImage, Frame
from PIL import Image, ImageTk
from tkinter import ttk

from services.download_video import Video
from services.download_musica import Musica
from utils.resource_path import resource_path

#= = = = = = = = = = = = = = = = = = = = = CONFIG JANELA TKINTER = = = = = = = = = = = = = = = = = = = = =
janelaYT = Tk()                 # INICAR A JANELA 'TK INTER'
janelaYT.geometry('494x335')    # Largura x Altura
janelaYT.minsize(494, 335)
janelaYT.resizable(width=True, height=False)  # Permite redimensionamento horizontal, bloqueia vertical
janelaYT.title('YT VidSound')
janelaYT.iconbitmap(resource_path("src/images/YT-VidSound.ico"))
janelaYT['bg'] = '#D3D3D3'


# Frames para organizar os widgets #####################################################
frame_imagem = Frame(janelaYT, bg='#D3D3D3', bd=0, highlightthickness=0)
frame_imagem.pack(pady=10)

frame_topo = Frame(janelaYT, bg='#D3D3D3')
frame_topo.pack(pady=10)

frame_1 = Frame(janelaYT, bg='#D3D3D3')
frame_1.pack(pady=10)  # Expande horizontalmente

frame_baixo = Frame(janelaYT, bg='#D3D3D3')
frame_baixo.pack(pady=10, fill='x')  # Expande horizontalmente


# Frame Imagem #########################################################################
image = Image.open(resource_path("src/images/YT-VidSound.png"))
image = image.resize((250, 100), Image.Resampling.LANCZOS)

photoYTP = ImageTk.PhotoImage(image)
Label(frame_imagem, image=photoYTP, bg='#D3D3D3', bd=0, highlightthickness=0).pack(pady=5)

# Frame Topo - Entrada do Link e Imagem ################################################
Label(frame_topo, text='Inserir Link', font='arial 14 bold', bg='#D3D3D3').pack(side='left', padx=5)

link_entry = Entry(frame_topo, font='arial 16 bold', width=27)
link_entry.pack(side='left', padx=5)


# Frame 1 - Botões #####################################################################
photoDW = PhotoImage(file=resource_path("src/images/download.png")).subsample(15, 15)

bt1 = Button(frame_1, text='MÚSICA MP3', font='arial 12 bold', image=photoDW, compound='bottom')
bt1.pack(side='left', padx=20, pady=10)

bt2 = Button(frame_1, text='VÍDEO MP4', font='arial 12 bold', image=photoDW, compound='bottom')
bt2.pack(side='left', padx=20, pady=10)

progress_bar = ttk.Progressbar(frame_1, orient='horizontal', length=200, mode='determinate')
progress_bar.pack(side='left', pady=10, before=bt2)


# Frame Baixo - Nome do Vídeo ##########################################################
def copiar_texto(event):
    janelaYT.clipboard_clear()
    janelaYT.clipboard_append(nome.cget("text"))

Label(frame_baixo, text='Título: ', font='arial 15 bold', bg='#D3D3D3').pack(side='left', padx=20)
nome = Label(frame_baixo, text='', font='arial 15 bold', bg='#D3D3D3')
nome.pack(side='left', padx=5, pady=5, anchor='w')
nome.bind("<Double-Button-1>", copiar_texto)


# Instânciando as classes Video e Musica
video_downloader = Video(janelaYT, nome, progress_bar, link_entry)
musica_downloader = Musica(janelaYT, nome, progress_bar, link_entry)

# Comandos dos botões para download de vídeo/música
bt1.config(command=musica_downloader.download_musica)
bt2.config(command=video_downloader.download_video)


janelaYT.mainloop() #EXIBIR A JANELA ATÉ FECHAR
