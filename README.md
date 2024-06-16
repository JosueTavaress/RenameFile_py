# Renomeador de Arquivos

Este script em Python renomeia arquivos em um diretório de entrada (`input`) removendo uma string específica dos nomes dos arquivos e os salva em um diretório de saída (`output`).

## Propósito

O propósito deste script é automatizar o processo de renomeação de arquivos, removendo uma string específica dos nomes dos arquivos. Por exemplo, se você tiver arquivos com nomes como `[SPOTIFY-DOWNLOADER.COM] Best Friend.mp3`, o script removerá a parte `[SPOTIFY-DOWNLOADER.COM] `, renomeando o arquivo para `Best Friend.mp3`.

## Como Usar

1. **Preparação:**
    - Certifique-se de ter o Python instalado. Você pode verificar isso com o comando `python --version` ou `python3 --version` no terminal.

2. **Coloque os Arquivos:**
    - Coloque os arquivos que você deseja renomear na pasta `input`.

3. **Executar o Script:**
    - Abra um terminal ou prompt de comando.
    - Navegue até o diretório onde o script está localizado usando o comando `cd`.
    - Execute o script com o comando `python renomear_arquivos.py` ou `python3 renomear_arquivos.py`.

4. **Verifique o Resultado:**
    - Os arquivos renomeados serão movidos para a pasta `output`.

## Como Alterar o Código

O script é configurado para remover a string `[SPOTIFY-DOWNLOADER.COM] ` dos nomes dos arquivos. Se você quiser alterar o comportamento do script, você pode modificar os seguintes valores no código:

- `input_dir`: Diretório de entrada onde os arquivos originais estão localizados.
- `output_dir`: Diretório de saída onde os arquivos renomeados serão salvos.
- `valueRepeat`: A string que você deseja remover dos nomes dos arquivos.
- `valueReplace`: A string que substituirá `valueRepeat`. Deixe como uma string vazia (`''`) para simplesmente remover `valueRepeat`.
