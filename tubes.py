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