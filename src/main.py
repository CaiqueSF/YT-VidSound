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
from pytubefix import YouTube  # Substitua pytube por pytubefix
from PIL import Image, ImageTk
from tkinter import ttk 
from pytubefix.exceptions import RegexMatchError, VideoUnavailable  # Substitua pytube por pytubefix
from urllib.error import HTTPError

# Para exibir o caminho DA PASTA atual
# caminho_diretorio = Path()             
# print(caminho_diretorio.absolute()) 

# Para exibir o caminho DO ARQUIVO atual        
# caminho_arquivo = Path(__file__)                         
# print(caminho_arquivo) 

#= = = = = = = = = = = = = = = = = = = = = CONFIG JANELA TKINTER = = = = = = = = = = = = = = = = = = = = =
janelaYT = Tk()                 # INICAR A JANELA 'TK INTER'
janelaYT.geometry('494x335')    # Largura x Altura
janelaYT.resizable(width=True, height=False)  # Permite redimensionamento horizontal, bloqueia vertical
janelaYT.title('YT VidSound')
janelaYT.iconbitmap('images/YT-VidSound.ico')
janelaYT['bg'] = '#D3D3D3'

#= = = = = = = = = = = = = = = = = = = = = = = = = FUNÇÕES = = = = = = = = = = = = = = = = = = = = = = = =
def video():
    progress_bar['value'] = 0
    janelaYT.update_idletasks()
    
    link = link_entry.get()
    if link:
        try: 
            mp4 = YouTube(link)  
                 
            try:
                nome.config(text=f'{mp4.author} - {mp4.title}')
            except KeyError:
                nome.config(text='Erro ao acessar o título do vídeo')
                
            stream = mp4.streams.get_highest_resolution() # Baixar a melhor resolução do vídeo         
            
            pasta = filedialog.askdirectory() # Escolher a pasta para salvar o vídeo
            if not pasta:
                return
                
            # Atualizar a barra de progresso
            progress_bar['value'] = 0
            janelaYT.update_idletasks()
            stream.download(pasta)
            progress_bar['value'] = 100
            janelaYT.update_idletasks()
             
            # Som de conclusão
            frequencia = 2200  # Frequência em hertz
            duracao = 500   # Duração em milissegundos (0.5 segundo)
            winsound.Beep(frequencia, duracao)
             
        except HTTPError as e:
            nome.config(text=f'Erro de requisição HTTP: {str(e)}')
        except RegexMatchError:
            nome.config(text='LINK INVÁLIDO!')
        except VideoUnavailable:
            nome.config(text='Vídeo indisponível ou restrito.')
        except Exception as e:
            nome.config(text=f'Erro inesperado: {str(e)}')
    else:
        nome.config(text='LINK INVÁLIDO!')

def musica():
    progress_bar['value'] = 0
    janelaYT.update_idletasks()
    
    link = link_entry.get()
    if link:
        try:  
            mp3 = YouTube(link)
            
            try:
                nome.config(text=f'{mp3.author} - {mp3.title}')
            except KeyError:
                nome.config(text='Erro ao acessar o título do vídeo')
                
            audio = mp3.streams.filter(only_audio=True).first() # Baixar áudio em formato MP3
            
            pasta = filedialog.askdirectory()
            if not pasta:
                return
            
            destino = str(audio.download(pasta))                     #Baixar na pasta Download           
            base, ext = os.path.splitext(destino)

            novo_arquivo = base + '.mp3'
            if os.path.exists(novo_arquivo):
                os.remove(novo_arquivo)
            os.rename(destino, novo_arquivo)
                
            # Atualizar a barra de progresso
            progress_bar['value'] = 0
            janelaYT.update_idletasks()
            progress_bar['value'] = 100
            janelaYT.update_idletasks()
            
            # Som de conclusão
            frequencia = 2200  # Frequência em hertz
            duracao = 500   # Duração em milissegundos (0.5 segundo)
            winsound.Beep(frequencia, duracao)

        except HTTPError as e:
            nome.config(text=f'Erro de requisição HTTP: {str(e)}')
        except RegexMatchError:
            nome.config(text='LINK INVÁLIDO!')
        except VideoUnavailable:
            nome.config(text='Vídeo indisponível ou restrito.')
        except Exception as e:
            nome.config(text=f'Erro inesperado: {str(e)}')
    else:
        nome.config(text='LINK INVÁLIDO!')
    
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

frame_1 = Frame(janelaYT, bg='#D3D3D3')
frame_1.pack(pady=10)  # Expande horizontalmente

frame_baixo = Frame(janelaYT, bg='#D3D3D3')
frame_baixo.pack(pady=10, fill='x')  # Expande horizontalmente

# Frame Imagem #########################################################################
image = Image.open("images/YT-VidSound2.png")
image = image.resize((250, 100), Image.Resampling.LANCZOS)

photoYTP = ImageTk.PhotoImage(image)
Label(frame_imagem, image=photoYTP).pack(pady=5)

# Frame Topo - Entrada do Link e Imagem ################################################
Label(frame_topo, text='Inserir Link', font='arial 14 bold', bg='#D3D3D3').pack(side='left', padx=5)

link_entry = Entry(frame_topo, font='arial 16 bold', width=27)
link_entry.pack(side='left', padx=5)

# Frame 1 - Botões #####################################################################
photoDW = PhotoImage(file="images/download2.png").subsample(15, 15)

bt1 = Button(frame_1, text='MÚSICA MP3', font='arial 12 bold', command=musica, image=photoDW, compound='bottom')
bt1.pack(side='left', padx=20, pady=10)

bt2 = Button(frame_1, text='VÍDEO MP4', font='arial 12 bold', command=video, image=photoDW, compound='bottom')
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

janelaYT.mainloop() #EXIBIR A JANELA ATÉ FECHAR

#LEFT-> a imagem estará no lado esquerdo do botão
#RIGHT-> a imagem estará no lado direito do botão
#TOP-> a imagem estará no topo do botão
#BOTTOM-> a imagem estará na parte inferior do botão
#pyinstaller --onefile --noconsole .\main.py