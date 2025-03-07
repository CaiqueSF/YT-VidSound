'''
APP desenvolvido para downloads de vídeo mp4 e áudio mp3 diretamente do YouTube

Python version: 3.11.3
Pytube version: 15.0.0

* * * * * ANTES DE EXECUTAR O SEU PROGRAMA, FAZER CONFIGURAÇÕES ABAIXO * * * * *
• Linha 59: Alterar caminho padrão para o seu download mp3
• Linha 111: Baixar imagem PNG da internet, nomear como 'Python_YouTube' e alterar caminho correto
• Linha 116: Baixar imagem PNG da internet, nomear como 'download' e alterar caminho correto
'''

#= = = = = = = = = = = = = = = = = = = = = = = = IMPORTAR BIBLIOTECAS = = = = = = = = = = = = = = = = = = = = = = = 
import os
import winsound
from tkinter import filedialog, Tk, Label, Entry, Button, PhotoImage, Frame, Toplevel
from pytube import YouTube

from pytube.contrib.playlist import Playlist
from pytube.exceptions import RegexMatchError
from pathlib import Path

# Para exibir o caminho DA PASTA atual
# caminho_diretorio = Path()             
# print(caminho_diretorio.absolute()) 

# Para exibir o caminho DO ARQUIVO atual        
# caminho_arquivo = Path(__file__)                         
# print(caminho_arquivo) 

#= = = = = = = = = = = = = = = = = = = = = CONFIG JANELA TKINTER = = = = = = = = = = = = = = = = = = = = =
janelaYT = Tk()                 #INICAR A JANELA 'TK INTER'
janelaYT.geometry('630x230')    #Largura x Altura
janelaYT.resizable(width=None, height=None) #Largura e Altura PODEM ser redimensionadas.
janelaYT.title('YT VidSound')
janelaYT.iconbitmap('images/YT-VidSound.ico')
janelaYT['bg'] = '#D3D3D3'

#= = = = = = = = = = = = = = = = = = = = = = = = = FUNÇÕES = = = = = = = = = = = = = = = = = = = = = = = =
def video(link):
    if link:
        try: 
            mp4 = YouTube(link)       
            titulo = Label(janelaYT, bg = 'red', text = (f'Baixando: {mp4.author} \r\n {mp4.title}'), font = 'arial 12 bold')
            titulo.grid(row = 1, column = 1)             
            stream = mp4.streams.get_highest_resolution()       #Baixar a melhor resolução do vídeo         
            pasta = filedialog.askdirectory()
            stream.download(pasta)                              #Baixar na pasta Download           
                     
            baixando = Label(janelaYT, bg = 'blue', text = 'Download Concluído!', font = 'arial 15 bold')
            baixando.grid(row = 2, column = 1, ipadx = 15, ipady = 5)
            janelaYT.after(10000, lambda: baixando.config(text='STATUS DOWNLOAD'))

            frequencia = 2200  # Frequência em hertz
            duracao = 1000   # Duração em milissegundos (1 segundo)
            winsound.Beep(frequencia, duracao)
             
        except RegexMatchError:
            baixando = Label(janelaYT, bg = 'blue', text = '  LINK INVÁLIDO!  ', font = 'arial 15 bold')
            baixando.grid(row = 2, column = 1, ipadx = 15, ipady = 5)
                    
    else: 
        baixando = Label(janelaYT, bg = 'blue', text = '  LINK INVÁLIDO!  ', font = 'arial 15 bold')
        baixando.grid(row = 2, column = 1, ipadx = 15, ipady = 5)

def musica(link):
    if link:
        try:  
            mp3 = YouTube(link)
            audio = mp3.streams.filter(only_audio=True).first() #Baixar áudio em formato MP3
            titulo = Label(janelaYT, bg = 'red', text = (f'Baixando: {mp3.author} \r\n {mp3.title}'), font = 'arial 12 bold')
            titulo.grid(row = 1, column = 1)             
            pasta = filedialog.askdirectory()
            destino = audio.download(pasta)                     #Baixar na pasta Download           
            destino = "C:/Users/CaiqueSF/Downloads"

            ArquivoSaida = audio.download(output_path=destino)
            base, ext = os.path.splitext(ArquivoSaida)

            ArquivoNovo = base + '.mp3'
            if os.path.exists(ArquivoNovo):
                os.remove(ArquivoNovo)
                os.rename(ArquivoSaida, ArquivoNovo)
            else:
                os.rename(ArquivoSaida, ArquivoNovo)

            baixando = Label(janelaYT, bg = 'blue', text = 'Download Concluído!', font = 'arial 15 bold')
            baixando.grid(row = 2, column = 1, ipadx = 15, ipady = 5)  
            janelaYT.after(10000, lambda: baixando.config(text='STATUS DOWNLOAD'))           
            
            frequencia = 2200  # Frequência em hertz
            duracao = 1000   # Duração em milissegundos (1 segundo)
            winsound.Beep(frequencia, duracao)

        except RegexMatchError:
            baixando = Label(janelaYT, bg = 'blue', text = '  LINK INVÁLIDO!  ', font = 'arial 15 bold')
            baixando.grid(row = 2, column = 1, ipadx = 15, ipady = 5)
                  
    else: 
        baixando = Label(janelaYT, bg = 'blue', text = '  LINK INVÁLIDO!  ', font = 'arial 15 bold')
        baixando.grid(row = 2, column = 1, ipadx = 15, ipady = 5)
    
#OPÇÃO POP-UP NÃO CHAMADA NA FUNÇÃO
#FUNÇÃO: Aviso de Donwload Concluído
def aviso():
    janelaYT_msg = Toplevel()
    janelaYT_msg.title('Aviso')
    janelaYT_msg.geometry('300x200')
    
    Label(janelaYT_msg, text = 'Download Concluído!', font = 'arial 12 bold', pady = 30).pack()
    Button(janelaYT_msg, text = 'OK', command = janelaYT_msg.destroy).pack()

#OPÇÃO POP-UP NÃO CHAMADA NA FUNÇÃO
#FUNÇÃO: Aviso de Erro
def aviso_erro():
    janelaYT_msg = Toplevel()
    janelaYT_msg.title('Aviso')
    janelaYT_msg.geometry('300x200')

    Label(janelaYT_msg, text = 'Insira um link válido!', font = 'arial 12 bold', pady = 30).pack()
    Button(janelaYT_msg, text = 'OK', command = janelaYT_msg.destroy).pack()

# Frames para organizar os widgets ##################################################### 
frame_imagem = Frame(janelaYT, bg='#D3D3D3')
frame_imagem.pack(pady=10)

frame_topo = Frame(janelaYT, bg='#D3D3D3')
frame_topo.pack(pady=10)

frame_meio = Frame(janelaYT, bg='#D3D3D3')
frame_meio.pack(pady=10)

frame_baixo = Frame(janelaYT, bg='#D3D3D3')
frame_baixo.pack(pady=10)

# Linha 0 - Entrada do Link e Imagem ###################################################
photoYTP = PhotoImage(file="images/YT-VidSound.png").subsample(15, 15)
Label(frame_imagem, image=photoYTP).pack()

# Linha 1 - Entrada do Link e Imagem ###################################################
Label(frame_topo, bg='blue', text='Inserir Link', font='arial 14 bold').pack(side='left', padx=5)

link = Entry(frame_topo, font='arial 16 bold', width=30)
link.pack(side='left', padx=5)

# Linha 2 - Botões e Status ############################################################
photoDW = PhotoImage(file="images/download2.png").subsample(15, 15)

bt1 = Button(frame_meio, bg='blue', text='MÚSICA MP3', font='arial 12 bold', command=lambda: musica(link.get()), image=photoDW, compound='bottom')
bt1.pack(side='left', padx=10)

status = Label(frame_meio, bg='red', text='STATUS DOWNLOAD', font='arial 12 bold')
status.pack(side='left', padx=10)

bt2 = Button(frame_meio, bg='blue', text='VÍDEO MP4', font='arial 12 bold', command=lambda: video(link.get()), image=photoDW, compound='bottom')
bt2.pack(side='left', padx=10)

# Linha 3 - Status de Download #########################################################    
baixando = Label(frame_baixo, bg='blue', text='STATUS DOWNLOAD', font='arial 15 bold')
baixando.pack(pady=5)

janelaYT.mainloop() #EXIBIR A JANELA ATÉ FECHAR

#LEFT-> a imagem estará no lado esquerdo do botão
#RIGHT-> a imagem estará no lado direito do botão
#TOP-> a imagem estará no topo do botão
#BOTTOM-> a imagem estará na parte inferior do botão
#pyinstaller --onefile --noconsole .\main.py             