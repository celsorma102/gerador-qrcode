import qrcode
from tkinter import *
from tkinter import ttk, messagebox, filedialog
from PIL import ImageTk, Image

class QRCodeGenerator:
    def __init__(self, root):
        self.root = root
        self.root.geometry("800x600")
        self.root.title("Gerador de QRCode")
        
        self.img_label = None  # Armazena o Label da imagem para evitar recriações

        Label(root, text="Gerador de QR Code", font=("Arial", 20)).pack(pady=(5, 5))
        
        Label(root, text="Digite o URL/texto para gerar o QR Code:", font=("Arial", 11)).pack(pady=(20, 5))
        self.input_text = Entry(root, justify=CENTER, width=80)
        self.input_text.pack()
        
        Label(root, text="Digite o nome da imagem:", font=("Arial", 11)).pack(pady=(20, 5))
        self.file_name = Entry(root, justify=CENTER, width=50)
        self.file_name.pack()

        Label(root, text="Escolha o local para salvar a imagem:", font=("Arial", 11)).pack(pady=(20, 5))
        Button(root, text="Selecionar Pasta e Salvar", width=20, command=self.save_qr_code).pack()

    def save_qr_code(self):
        text = self.input_text.get().strip()
        file_name = self.file_name.get().strip()

        if not text or not file_name:
            messagebox.showerror("Erro", "Por favor, preencha todos os campos!")
            return

        directory = filedialog.askdirectory()
        if not directory:
            return  # Se o usuário cancelar a seleção da pasta

        file_path = f"{directory}/{file_name}.png"

        try:
            qr_code = qrcode.make(text)
            qr_code.save(file_path)
            self.show_qr_code(file_path)
            messagebox.showinfo("Sucesso", f"QR Code salvo em:\n{file_path}")
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao salvar a imagem:\n{e}")

    def show_qr_code(self, file_path):
        img = Image.open(file_path).resize((250, 250))
        img = ImageTk.PhotoImage(img)

        if self.img_label is None:
            self.img_label = Label(self.root, image=img)
            self.img_label.image = img
            self.img_label.pack(pady=20)
        else:
            self.img_label.config(image=img)
            self.img_label.image = img