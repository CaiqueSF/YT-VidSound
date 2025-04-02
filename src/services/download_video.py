import os
import winsound
from tkinter import filedialog
from pytubefix import YouTube
from pytubefix.exceptions import RegexMatchError, VideoUnavailable
from urllib.error import HTTPError


class Video:
    def __init__(self, janelaYT, nome, progress_bar, link_entry):
        self.janelaYT = janelaYT
        self.nome = nome
        self.progress_bar = progress_bar
        self.link_entry = link_entry
        
        self.sucess = os.path.join(os.path.dirname(__file__), '..', 'utils', 'sucess.wav')


    def download_video(self):
        self.progress_bar['value'] = 0
        self.janelaYT.update_idletasks()
        
        link = self.link_entry.get()
        if link:
            try: 
                mp4 = YouTube(link)  
                self.nome.config(text=f'{mp4.author} - {mp4.title}') # Título do vídeo
                stream = mp4.streams.get_highest_resolution()  # Baixar a melhor resolução do vídeo         
                
                pasta = filedialog.askdirectory()  # Escolher a pasta para salvar o vídeo
                if not pasta:
                    return
                stream.download(pasta)
                    
                # Atualizar a barra de progresso
                self.progress_bar['value'] = 0
                self.janelaYT.update_idletasks()
                self.progress_bar['value'] = 100
                self.janelaYT.update_idletasks()
                
                winsound.PlaySound(self.sucess, winsound.SND_FILENAME | winsound.SND_ASYNC)
                 
            except HTTPError as e:
                winsound.MessageBeep(winsound.MB_ICONHAND)
                self.nome.config(text='Erro de conexão com o servidor: verifique sua internet e tente novamente', fg='red')
            except RegexMatchError:
                winsound.MessageBeep(winsound.MB_ICONHAND)
                self.nome.config(text='LINK INVÁLIDO', fg='red')
            except VideoUnavailable:
                winsound.MessageBeep(winsound.MB_ICONHAND)
                self.nome.config(text='Vídeo indisponível ou restrito', fg='red')
            except Exception as e:
                winsound.MessageBeep(winsound.MB_ICONHAND)
                self.nome.config(text='Erro inesperado: tente novamente mais tarde', fg='red')
                
        else:
            winsound.MessageBeep(winsound.MB_ICONHAND)
            self.nome.config(text='INSIRA UM LINK', fg='red')
