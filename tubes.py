import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QListWidget, QComboBox, QLineEdit, QMessageBox
from PyQt5.QtCore import Qt
import random
import time

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sorting NIM - Angkatan 22")
        self.setGeometry(100, 100, 600, 400)

        # Label
        self.label_prodi = QLabel("Pilih Prodi:", self)
        self.label_num_nim = QLabel("Jumlah NIM:", self)

        # Combo Box untuk Pilihan Prodi
        self.prodi_combo = QComboBox(self)
        self.prodi_combo.addItems([
            "Teknik Informatika", "Bisnis Digital", "Fisika", "Matematika", "Mesin", 
            "Teknik Elektro", "Teknik Kimia", "TMM", "Teknik Sipil", "PWK", 
            "Kapal", "Sistem Informasi", "Teknik Industri", "Teknik Lingkungan", 
            "Kelautan", "Arsitektur", "Statistika", "Aktuaria", "Rekayasa Keselamatan", 
            "Teknologi Pangan", "Teknik Logistik", "DKV"
        ])
        self.prodi_combo.setCurrentIndex(0)  # Prodi default adalah Teknik Informatika
        
        # Line Edit untuk Jumlah NIM
        self.num_nim_input = QLineEdit(self)
        self.num_nim_input.setText("50")

        # List Widget untuk Menampilkan Daftar NIM
        self.list_widget = QListWidget(self)
        
        # Button
        self.generate_button = QPushButton("Generate NIM", self)
        self.generate_button.clicked.connect(self.generate_nim)

        self.sort_button = QPushButton("Sort NIM", self)
        self.sort_button.clicked.connect(self.sort_nim)

        # Status Label
        self.status_label = QLabel("Status: ", self)
   
        # Layout
        layout = QVBoxLayout()
        layout.addWidget(self.label_prodi)
        layout.addWidget(self.prodi_combo)
        layout.addWidget(self.label_num_nim)
        layout.addWidget(self.num_nim_input)
        layout.addWidget(self.list_widget)
        
        button_layout = QHBoxLayout()
        button_layout.addWidget(self.generate_button)
        button_layout.addWidget(self.sort_button)
        
        layout.addLayout(button_layout)
        layout.addWidget(self.status_label)
        
        self.setLayout(layout)
     
        #Dictionary untuk Menyimpan Daftar NIM per Prodi
        self.prodi_nim_lists = {
            "Teknik Informatika": [], "'Bisnis Digital":[], "Fisika": [], "Matematika": [], 
            "Mesin": [], "Teknik Elektro": [], "Teknik Kimia": [], "TMM": [], "Teknik Sipil": [], 
            "PWK": [], "Kapal": [], "Sistem Informasi": [], "Teknik Industri": [], 
            "Teknik Lingkungan": [], "Kelautan": [], "Arsitektur": [], "Statistika": [], 
            "Aktuaria": [], "Rekayasa Keselamatan": [], "Teknologi Pangan": [], 
            "Teknik Logistik": [], "DKV": []
        }
        
        #Dictionary untuk Kode Prodi
        self.prodi_codes = {
            "Teknik Informatika": 112210, "'Bisnis Digital": 202210 , "Fisika": 12210,
            "Matematika": 22210, "Mesin": 32210, "Teknik Elektro": 42210, "Teknik Kimia": 52210,
            "TMM": 62210, "Teknik Sipil": 72210, "PWK": 82210, "Kapal": 92210,
            "Sistem Informasi": 102210, "Teknik Industri": 122210, "Teknik Lingkungan": 132210,
            "Kelautan": 142210, "Arsitektur": 152210, "Statistika": 162210, 
            "Aktuaria": 172210, "Rekayasa Keselamatan": 182210, "Teknologi Pangan": 192210, 
            "Teknik Logistik": 212210, "DKV": 222210
        }
        
    def generate_nim(self):
        # Memeriksa apakah jumlah NIM valid
        try:
            num_nim = int(self.num_nim_input.text())
            if num_nim <= 0:
                raise ValueError
        except ValueError:
            QMessageBox.critical(self, "Error", "Masukkan jumlah NIM yang valid (bilangan bulat positif).")
            return

        # Mendapatkan prodi yang dipilih
        selected_prodi = self.prodi_combo.currentText()
        prodi_code = self.prodi_codes[selected_prodi]
        current_list = self.prodi_nim_lists[selected_prodi]

        # Membuat daftar NIM baru untuk prodi yang dipilih
        nim_list = [f"{prodi_code}{str(i).zfill(2)}" for i in range(1, 100)]
        random.shuffle(nim_list)
        
        # Memotong daftar NIM baru sesuai jumlah yang diminta dan menambahkannya ke daftar NIM prodi yang ada
        self.prodi_nim_lists[selected_prodi].extend(nim_list[:num_nim])

        # Menghapus prodi yang sudah digenerate dari combo box
        index = self.prodi_combo.findText(selected_prodi)
        self.prodi_combo.removeItem(index)

        # Menggabungkan semua daftar NIM dari semua prodi
        all_nim_list = sum(self.prodi_nim_lists.values(), [])
        random.shuffle(all_nim_list)

        # Menampilkan daftar NIM yang digenerate
        self.list_widget.clear()
        for nim in all_nim_list:
            self.list_widget.addItem(nim)

    def sort_nim(self):
        # Menggabungkan semua daftar NIM dari semua prodi
        all_nim_list = sum(self.prodi_nim_lists.values(), [])
    
        start_time = time.time()
        all_nim_list = sorted(all_nim_list, key = lambda x: int (x))
        end_time = time.time()

        # Menampilkan daftar NIM yang sudah diurutkan
        self.list_widget.clear()
        for nim in all_nim_list:
            self.list_widget.addItem(nim)
        
        duration = end_time - start_time
        n = len(all_nim_list)

        # Menghitung status algoritma sorting
        if n == 0:
            status = "Tidak ada NIM yang diurutkan."
        elif duration <= 0.0001 * n:
            status = "Best Case"
        elif duration >= 0.1 * n * (n - 1):
            status = "Worst Case"
        else:
            status = "Average Case"

        # Menampilkan status dan jumlah NIM dari setiap prodi yang memiliki NIM
        status_text = f"Status: {status}\n"
        for prodi, nim_list in self.prodi_nim_lists.items():
            if nim_list:  # Hanya menampilkan prodi yang memiliki NIM
                status_text += f"{prodi}: {len(nim_list)} NIM\n"
        status_text += f"Total: {n} NIM"

        self.status_label.setText(status_text)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())