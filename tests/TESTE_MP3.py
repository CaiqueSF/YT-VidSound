from pytube import YouTube
import os

#Entrada de URL do usuário
yt = YouTube(input("Digite a URL do vídeo que deseja baixar: \n>> "))
  
#Extrair apenas áudio
audio = yt.streams.filter(only_audio=True).first()

#Substitua o destino pelo caminho onde deseja salvar o arquivo baixado
destino = "C:/Users/CaiqueSF/Downloads"
  
#Baixe o arquivo
ArquivoSaida =audio.download(output_path=destino)
'''
if os.path.exists(ArquivoSaida):
    os.remove(ArquivoSaida)
    ArquivoSaida = audio.download(output_path=destino)
'''

#Salve o arquivo
base, ext = os.path.splitext(ArquivoSaida)

ArquivoNovo = base + '.mp3'

if os.path.exists(ArquivoNovo):
    os.remove(ArquivoNovo)
    os.rename(ArquivoSaida, ArquivoNovo)
else:
    os.rename(ArquivoSaida, ArquivoNovo)
    

#Resultado do sucesso
print(yt.title)
