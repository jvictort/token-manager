import sys
import pathlib
import pyperclip

# Substitua pelo diretório onde você armazena seus tokens
TOKEN_FOLDER_PATH = "/home/jvictort/Programming/Tokens"

TOKEN_FOLDER = pathlib.Path(TOKEN_FOLDER_PATH)

FILE_FLAG = sys.argv[1].replace("-", "")

for file in TOKEN_FOLDER.rglob(f"*{FILE_FLAG}*.*"):
    with open(file, "r") as f:
        pyperclip.copy(f.read())
