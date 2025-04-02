import os
import winsound

# Construir o caminho absoluto para o arquivo de som
som_sucesso = os.path.join(os.path.dirname(__file__), '..', 'utils', 'sucess.wav')

# Reproduzir o som
winsound.PlaySound(som_sucesso, winsound.SND_FILENAME | winsound.SND_ASYNC)

print(som_sucesso)  # Verificar o caminho gerado