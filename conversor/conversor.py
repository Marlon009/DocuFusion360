import os
import tkinter as tk
from tkinter import filedialog, messagebox
import subprocess
from pathlib import Path
from tkinter import ttk
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import sys

# Função para retornar o caminho do executável pdftotext
def get_pdftotext_path():
    try:
        if getattr(sys, 'frozen', False):
            # Caminho correto quando o script é executado no modo congelado pelo PyInstaller
            pdftotext_path = Path(sys._MEIPASS) / "poppler" / "pdftotext.exe"
        else:
            # Caminho no ambiente de desenvolvimento
            pdftotext_path = Path(__file__).parent / "poppler" / "pdftotext.exe"
        
        if not pdftotext_path.exists():
            raise FileNotFoundError("pdftotext.exe não encontrado.")
        return pdftotext_path
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao localizar o pdftotext.exe: {e}")
        return None
    
# Função para converter TXT para PDF
def convert_txt_to_pdf(input_txt, output_pdf):
    try:
        with open(input_txt, "r", encoding="utf-8") as txt_file:
            text_content = txt_file.read()

        c = canvas.Canvas(output_pdf, pagesize=letter)
        width, height = letter
        text_object = c.beginText(40, height - 40)  # Posição inicial do texto no PDF
        text_object.setFont("Helvetica", 10)
        text_object.setTextOrigin(40, height - 40)

        # Adiciona o texto do arquivo TXT ao PDF
        for line in text_content.splitlines():
            text_object.textLine(line)

        c.drawText(text_object)
        c.save()
    except Exception as e:
        messagebox.showerror("Erro", f"Ocorreu um erro ao converter o TXT para PDF: {str(e)}")

# Função para extrair texto de PDF usando pdftotext
def extract_pdf_to_text(input_pdf, output_txt, dll_path):
    try:
        pdftotext_path = get_pdftotext_path()
        if pdftotext_path and pdftotext_path.exists():
            # Adicionar o caminho da DLL ao ambiente
            env = os.environ.copy()
            env["PATH"] = dll_path + ";" + env["PATH"]
            
            # Verificar e formatar corretamente o comando para não ocorrer erro de caminho
            input_pdf = input_pdf.replace("/", "\\")  # Trocar barras para barras invertidas
            output_txt = output_txt.replace("/", "\\")  # Trocar barras para barras invertidas

            # Executar o comando pdftotext com a opção -layout
            subprocess.run([str(pdftotext_path), "-layout", input_pdf, output_txt], check=True, env=env)

            # Após a conversão, o arquivo .txt estará com a formatação preservada.
        else:
            raise FileNotFoundError("O executável pdftotext não foi encontrado.")
    except Exception as e:
        messagebox.showerror("Erro", f"Ocorreu um erro ao processar o arquivo: {str(e)}")

# Função para selecionar os arquivos
def select_files():
    files = filedialog.askopenfilenames(filetypes=[("Arquivos PDF", "*.pdf"), ("Arquivos TXT", "*.txt")])
    return files

# Função para iniciar a conversão
def start_conversion():
    files = listbox_files.get(0, tk.END)
    if not files:
        messagebox.showwarning("Aviso", "Nenhum arquivo selecionado!")
        return

    dll_path = filedialog.askdirectory(title="Selecione o diretório contendo a DLL")
    if not dll_path:
        messagebox.showwarning("Aviso", "Nenhum diretório da DLL selecionado!")
        return

    loading_label.config(text="Convertendo... Aguarde.")
    progress_bar["value"] = 0

    for i, file in enumerate(files):
        extension = Path(file).suffix
        # Verificando a extensão para fazer a conversão correta
        if extension == ".pdf":
            output_txt = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Arquivos TXT", "*.txt")], initialfile=Path(file).stem + ".txt")
            if output_txt:
                extract_pdf_to_text(file, output_txt, dll_path)
        elif extension == ".txt":
            output_pdf = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("Arquivos PDF", "*.pdf")], initialfile=Path(file).stem + ".pdf")
            if output_pdf:
                convert_txt_to_pdf(file, output_pdf)

        progress_bar["value"] = (i + 1) / len(files) * 100

    loading_label.config(text="Conversão concluída!")
    messagebox.showinfo("Sucesso", "Conversão concluída!")

# Criação da interface gráfica
root = tk.Tk()
root.title("Conversor PDF/TXT")

root.minsize(500, 400)

label_files = tk.Label(root, text="Arquivos selecionados:")
label_files.pack(pady=10)

listbox_files = tk.Listbox(root, width=50, height=10)
listbox_files.pack(pady=5)

button_select_files = tk.Button(root, text="Selecionar Arquivos", command=lambda: [listbox_files.insert(tk.END, file) for file in select_files()])
button_select_files.pack(pady=10)

progress_bar = ttk.Progressbar(root, length=400, maximum=100, mode='determinate')
progress_bar.pack(pady=20)

loading_label = tk.Label(root, text="")
loading_label.pack(pady=5)

button_convert = tk.Button(root, text="Converter", command=start_conversion)
button_convert.pack(pady=10)

root.mainloop()
