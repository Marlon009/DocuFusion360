# DocuFusion 360

[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Linux%20%7C%20macOS-lightgrey)

Solução completa para conversão e manipulação de documentos com suporte avançado a OCR e templates personalizáveis.

![docufusion](https://github.com/user-attachments/assets/89fbdc34-db1c-4937-ae84-a6169226aef5)


## 🚀 Recursos Principais
- **Conversão entre formatos**: PDF ↔ DOCX ↔ TXT
- **OCR Integrado**: Reconhecimento de texto em PDFs digitalizados
- **Drag and Drop**: Interface intuitiva com arrastar e soltar
- **Temas Personalizáveis**: Modos claro e escuro
- **Sistema de Templates**: Estilos predefinidos para documentos
- **Histórico de Conversões**: Log detalhado de todas as operações
- **Multiplataforma**: Compatível com Windows, Linux e macOS

## 📦 Instalação

### Pré-requisitos
bash
pip install -r requirements.txt

Dependências Especiais
Tesseract OCR: Instalação para Windows

bash
Copy
# Linux (Debian/Ubuntu)
sudo apt install tesseract-ocr libtesseract-dev

# macOS (Homebrew)
brew install tesseract


🛠 **Como Usar**

### Conversão Básica
1. Arraste arquivos para a área destacada ou clique em "Selecionar Arquivos".
2. Selecione o formato de saída.
3. Clique em "Converter".
4. Escolha o local de salvamento.

### Usando OCR
1. Marque a opção **"Usar OCR para PDFs"**.
2. Selecione arquivos PDF digitalizados.
3. Converta para **DOCX** ou **TXT**.

### Personalização
- Acesse o menu **Temas** para alternar entre modo claro/escuro.
- Carregue templates personalizados em **JSON** pelo menu **Templates**.

🔄 **Formatos Suportados**

| De/Para       | PDF | DOCX | TXT  |
|---------------|-----|------|------|
| **PDF**       | -   | ✓    | ✓ (OCR) |
| **DOCX**      | ✓   | -    | ✓    |
| **TXT**       | ✓   | ✓    | -    |

⚙️ **Detalhes Técnicos**

**Dependências Principais**:
- PyMuPDF (Fitz)
- pytesseract
- python-docx
- reportlab
- tkinterdnd2

**Sistemas Suportados**:
- Windows 10/11
- Linux (Ubuntu/Debian)
- macOS 10.15+

**Limites**:
- Tamanho máximo de arquivo: 2GB
- Resolução OCR recomendada: 300dpi

❓ **FAQ**

**Q: Como resolver erros de OCR?**  
A: Verifique a instalação do Tesseract e adicione ao PATH.

**Q: Arquivos não aparecem na lista?**  
A: Formatos suportados: .pdf, .txt, .docx.

**Q: Erro ao converter PDF para DOCX?**  
A: Instale as DLLs do Poppler no diretório correto.

⚠️ **Aviso Legal**

Este software destina-se exclusivamente para:
- Conversão de documentos pessoais.
- Digitalização de materiais próprios.
- Pesquisa acadêmica.

**É estritamente proibido**:
- Violar direitos autorais.
- Processar documentos confidenciais.
- Uso comercial não autorizado.

📄 **Licença**  
Distribuído sob licença GPL-3.0. Veja o arquivo LICENSE para detalhes.

👨💻 **Desenvolvedor**  
Marlon - [GitHub](https://github.com/Marlon009)

🙌 **Contribuição**  
Contribuições são bem-vindas! Siga estes passos:
1. Fork o repositório.
2. Crie sua branch (`git checkout -b feature/nova-funcionalidade`).
3. Commit suas mudanças (`git commit -m 'Add nova funcionalidade'`).
4. Push para a branch (`git push origin feature/nova-funcionalidade`).
5. Abra um Pull Request.
