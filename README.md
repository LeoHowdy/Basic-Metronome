Basic Metronome - Metrônomo Simples em Python
https://img.shields.io/badge/Python-3.8%252B-blue
https://img.shields.io/badge/License-MIT-green

Um metrônomo simples com interface gráfica desenvolvido em Python, perfeito para músicos e estudantes que precisam de uma ferramenta básica de acompanhamento rítmico.

📥 Download do Executável
⬇️ Baixar versão para Windows (.exe) (Link do Google Drive)

✨ Funcionalidades
Interface gráfica limpa e intuitiva

Ajuste de BPM (batidas por minuto)

Controle de início/parada

Som de tique audível

Sistema de threading para operação não-bloqueante

⚙️ Pré-requisitos
Python 3.8+

Bibliotecas:

bash
pip install pygame
🚀 Como Executar
Clone o repositório:

bash
git clone https://github.com/seu-usuario/basic-metronome.git
cd basic-metronome
Execute o script principal:

bash
python metronomo.py
🖥️ Como Usar
Insira o BPM desejado no campo de texto (ex: 60, 120)

Clique em "Iniciar" para começar o metrônomo

Clique em "Parar" para interromper

🛠️ Tecnologias Utilizadas
Tkinter: Interface gráfica

PyGame: Reprodução de áudio

Threading: Execução paralela

PyInstaller: Criação do executável

📦 Gerando Executável
Para gerar o executável Windows:

Instale o PyInstaller:

bash
pip install pyinstaller
Execute o comando de build:

bash
pyinstaller --onefile --windowed --add-data "tick.wav;." metronomo.py
O executável estará em dist/metronomo.exe

📝 Notas
O arquivo tick.wav deve estar no mesmo diretório do script

Testado em Windows 10/11

Volume pode ser ajustado no sistema operacional

📄 Licença
Este projeto está licenciado sob a licença MIT - veja o arquivo LICENSE para detalhes.

Desenvolvido com ❤️ por [Seu Nome] - Contribuições são bem-vindas!

