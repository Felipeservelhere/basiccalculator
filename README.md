import os
import subprocess
import platform

readme_path = "README.md"

def open_readme():
    if platform.system() == "Windows":
        # Comando para abrir o arquivo no Bloco de Notas no Windows
        subprocess.run(["notepad.exe", readme_path])
    elif platform.system() == "Darwin":
        # Para MacOS, pode-se usar TextEdit ou outro editor
        subprocess.run(["open", "-a", "TextEdit", readme_path])
    else:
        # Para Linux ou outras plataformas, usa-se o comando de editor de texto padrão
        subprocess.run(["xdg-open", readme_path])

open_readme()



Este é um projeto de uma calculadora simples que realiza as operações matemáticas básicas: adição, subtração, multiplicação e divisão.

# Como Rodar o Projeto

Para rodar a calculadora, siga os seguintes passos:

1. **Instale o repositório**:
   
   Instale este repositório no seu computador:

2.  **Instale o Python**:

Se você ainda não tiver o Python instalado, baixe e instale a versão mais recente do Python em python.org. Lembre-se de marcar a opção "Add Python to PATH" durante a instalação.

3.  **Navegue até a pasta do projeto**:

Abra o repositório no seu computador

4.  **Execute o arquivo calculator.py**:

Se você estiver usando Windows, clique duas vezes no arquivo


### Conclusão:
Para garantir que o `calculator.py` rode diretamente no Python, você precisa garantir que o Python esteja instalado corretamente e configurar os atalhos para facilitar a execução.