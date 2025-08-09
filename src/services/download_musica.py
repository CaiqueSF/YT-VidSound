import os
import winsound
from tkinter import filedialog
from pytubefix import YouTube
from pytubefix.exceptions import RegexMatchError, VideoUnavailable
from urllib.error import HTTPError

from utils.resource_path import resource_path


class Musica:
    def __init__(self, janelaYT, nome, progress_bar, link_entry):
        self.janelaYT = janelaYT
        self.nome = nome
        self.progress_bar = progress_bar
        self.link_entry = link_entry

        self.sucess = resource_path(os.path.join('src', 'utils', 'sucess.wav'))


    def download_musica(self):
        self.progress_bar['value'] = 0
        self.janelaYT.update_idletasks()

        link = self.link_entry.get()
        if link:
            try:
                mp3 = YouTube(link)
                self.nome.config(text=f'{mp3.author} - {mp3.title}') # Título da música
                audio = mp3.streams.filter(only_audio=True).first()  # Baixar áudio em formato MP3

                pasta = filedialog.askdirectory()
                if not pasta:
                    return

                destino = str(audio.download(pasta))  # Baixar na pasta escolhida
                arquivo, extensao = os.path.splitext(destino)

                novo_arquivo = arquivo + '.mp3'
                if os.path.exists(novo_arquivo):
                    os.remove(novo_arquivo)
                os.rename(destino, novo_arquivo)

                # Atualizar a barra de progresso
                self.progress_bar['value'] = 0
                self.janelaYT.update_idletasks()
                self.progress_bar['value'] = 100
                self.janelaYT.update_idletasks()

                winsound.PlaySound(self.sucess, winsound.SND_FILENAME | winsound.SND_ASYNC)

            except HTTPError:
                winsound.MessageBeep(winsound.MB_ICONHAND)
                self.nome.config(text='Erro de conexão com o servidor: verifique sua internet e tente novamente', fg='red')
            except RegexMatchError:
                winsound.MessageBeep(winsound.MB_ICONHAND)
                self.nome.config(text='LINK INVÁLIDO', fg='red')
            except VideoUnavailable:
                winsound.MessageBeep(winsound.MB_ICONHAND)
                self.nome.config(text='Vídeo indisponível ou restrito', fg='red')
            except Exception:
                winsound.MessageBeep(winsound.MB_ICONHAND)
                self.nome.config(text='Erro inesperado: tente novamente mais tarde', fg='red')

        else:
            winsound.MessageBeep(winsound.MB_ICONHAND)
            self.nome.config(text='INSIRA UM LINK', fg='red')
