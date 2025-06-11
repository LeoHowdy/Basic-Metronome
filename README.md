# Basic-Metronome
Um metrônomo digital simples, leve e funcional, desenvolvido em Python com interface gráfica. Ideal para músicos que precisam praticar mantendo o tempo com precisão. A batida é reproduzida com som real (arquivo .wav) e permite ajustar o BPM facilmente.
# Basic Metrônomo em Python

Este projeto é um metrônomo simples desenvolvido em Python, com interface gráfica utilizando **Tkinter** e áudio gerenciado pela biblioteca **Pygame**. Foi criado para oferecer uma ferramenta funcional e didática para quem deseja aprender programação Python, manipulação de áudio e multithreading.

---

## 📌 Funcionalidades Principais

- Configuração dinâmica do **BPM (batidas por minuto)** via interface gráfica.
- Controle para **iniciar** e **parar** o metrônomo com botões intuitivos.
- Som de batida (“tick”) sincronizado perfeitamente com o BPM configurado.
- Utilização de **threads** para garantir que a interface permaneça responsiva durante a execução.
- Suporte para execução via script Python e executável empacotado com PyInstaller (inclui mecanismo para localizar o arquivo de som corretamente).

## 🎯 Como Executar

### Opção 1: Executar pelo código fonte (requer Python instalado)

1. Clone este repositório ou faça download dos arquivos.

2. Instale a biblioteca necessária:

```bash
pip install pygame

Garanta que o arquivo tick.wav esteja na mesma pasta do script Python.

Execute o programa com o Python:

python basic_metronomo.py

Opção 2: Executar via executável (Windows)
Para quem não possui o Python instalado, disponibilizamos um executável pronto para uso. Basta baixar, descompactar (se necessário) e executar:

🔗 Baixar Executável Basic Metrônomo (Google Drive)

https://drive.google.com/file/d/1uy6_9DqKr8dPqcEddg99D8tCMRGdBA1G/view?usp=drive_link



📝 Sobre o Código
O script principal contém:

resource_path(): função que adapta o caminho do arquivo de som para funcionar tanto em modo script quanto quando empacotado com PyInstaller.

Controle da execução do metrônomo via variável global rodando para iniciar/parar o loop de batidas.

Uso de threading para não travar a interface Tkinter.

Interface gráfica simples e intuitiva, com entrada para BPM e botões coloridos para iniciar e parar.

💡 Possíveis Melhorias Futuras em projeto - sem data definida de lançamento.

Adicionar ajuste de volume do som.

Permitir seleção de diferentes sons para as batidas.

Visualizador gráfico ou animação sincronizada com as batidas.

Salvamento da última configuração de BPM para inicialização automática.

Compatibilidade com sistemas operacionais diferentes do Windows.

📄 Licença
Este projeto está sob a licença MIT. Sinta-se livre para copiar, modificar e redistribuir.

📬 Contato
Dúvidas, sugestões ou contribuições são muito bem-vindas! Abra uma issue ou envie mensagem.

Obrigado por usar o Basic Metrônomo! Bons estudos e bons códigos!
