# YT VidSound

## ➡ Linguagem Utilizada

Python: Linguagem principal utilizada para o desenvolvimento do projeto.

## ➡ Objetivo do Projeto

O YT VidSound é um programa que permite baixar vídeos e músicas do YouTube de forma simples e eficiente. Ele oferece uma interface gráfica amigável para que o usuário insira o link do vídeo e escolha entre baixar o vídeo em formato MP4 ou o áudio em formato MP3.

## ➡ Estrutura do Projeto

A estrutura do projeto está organizada da seguinte forma:

```
.
├── images/                     # Arquivos de imagens usados na interface gráfica
│   ├── download.png            # Ícone usado nos botões
│   ├── YT-VidSound.ico         # Ícone do programa
│   └── YT-VidSound.png         # Logo exibida na interface
├── src/                        # Código-fonte do programa
│   ├── services/               # Classes responsáveis pelas funcionalidades
│   │   ├── download_musica.py  # Classe para baixar músicas
│   │   └── download_video.py   # Classe para baixar vídeos
│   └── utils/                  # Recursos adicionais
│       └── sucess.wav          # Som de sucesso ao concluir o download
│   ├── main.py                 # Arquivo principal que executa o programa
├── README.md                   # Documentação do projeto
├── requirements.txt            # Lista de dependências do projeto
└── ytvidsound.exe              # Executável para rodar o programa
```

## ➡ Funcionalidades do Projeto

🔹 **Baixar vídeos do YouTube**: Permite baixar vídeos em formato MP4 na melhor resolução disponível.

🔹 **Baixar músicas do YouTube**: Permite baixar o áudio de vídeos em formato MP3.

🔹 **Interface gráfica amigável**: Desenvolvida com tkinter, a interface permite que o usuário insira o link do vídeo, escolha o formato desejado e acompanhe o progresso do download.

## ➡ Como Executar o Projeto

**Siga os passos abaixo para executar o projeto:**

1. Clone o repositório:

    ```bash
    git clone https://github.com/CaiqueSF/YT-VidSound.git
    ```

2. Navegue para o diretório do projeto:

    ```bash
    cd YT-VidSound
    ```

3. Instale as dependências listadas em **requirements.txt**

    ```bash
    pip install -r requirements.txt
    ```

4. Execute o projeto:

    ```bash
    python src/main.py
    ```

5. Caso prefira, faça o download da versão executável: [Download](https://github.com/CaiqueSF/YT-VidSound/releases/download/v1.0.0/ytvidsound.exe)

## ➡ Contribuindo

**Se você deseja contribuir para o projeto, siga estas etapas:**

1. Faça um fork do repositório.

2. Crie uma nova branch:

    ```bash
    git checkout -b [nome-da-sua-branch]
    ```

3. Faça suas alterações e commit:

    ```bash
    git add .
    git commit -m "[Descrição das suas alterações]"
    ```

4. Envie suas alterações para o repositório remoto:

    ```bash
    git push origin [nome-da-sua-branch]
    ```

5. Abra um Pull Request no GitHub.

## ➡ Contatos

🔹 **E-mail**: caiquedesousaferreira@gmail.com

🔹 **LinkedIn**: [Caíque de S. Ferreira](https://www.linkedin.com/in/ca%C3%ADque-de-s-ferreira-48105b18b/)
