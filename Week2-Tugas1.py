# Nama : Oktora Rizka Arifin
# NIM  : F1D02410145
# Kelas : 6C

import sys
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QComboBox, QPushButton

class MainWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.init_ui()
    
    def init_ui(self):
        self.setWindowTitle("Form Biodata Mahasiswa")
        self.resize(400, 300)
        self.setStyleSheet("""
            QLineEdit {
                background-color:#D5EDDB;
                border: 1px solid #2ecc71;
                padding: 10px;
                border-radius: 5px;
            }

            #buttonTampil {
                background-color:#2980b9;
                color: #ffffff;
                padding: 10px;
            }

            #buttonTampil:hover {
                background-color: #3498db;
            }

            #buttonTampil:pressed {
                background-color: #1f618d;
            }
                                 
            #buttonReset {
                background-color:#95a5a6;
                color: #ffffff;
                padding: 10px;
            }

            #buttonReset:hover {
                background-color: #BFC9D1;
            }

            #buttonReset:pressed {
                background-color: #4C585B;
            }

            QComboBox {
                border: 1px solid #95a5a6;
                padding: 10px;
                border-radius: 5px;            
            }
            

            * {
            background-color: #f5f6fa;
            color : #2c3e50;
            }        
            
        """)
        
        
        
        # Label
        self.labelNama = QLabel("Nama Lengkap:")
        self.labelNIM = QLabel("NIM:")
        self.labelKelas = QLabel("Kelas:")  
        self.labelGender = QLabel("Jenis Kelamin:")  

        # Input
            # Nama
        self.inputNama = QLineEdit()
        self.inputNama.setPlaceholderText("Masukan Nama Lengkap")
        
            # NIM
        self.inputNIM = QLineEdit()
        self.inputNIM.setPlaceholderText("Masukkan NIM")

     
            # Kelas
        self.inputKelas = QLineEdit()
        self.inputKelas.setPlaceholderText("Contoh: TI-2A")

 
        # Combo Box
        self.comboBox = QComboBox()
        self.comboBox.addItems(["Laki-laki", "Perempuan"])

        # Button
            # Layout tombol
        self.layoutButton = QHBoxLayout()
        self.tombolTampil = QPushButton("Tampilkan")
        self.tombolReset = QPushButton("Reset")

        self.tombolTampil.setObjectName("buttonTampil")        
        self.tombolReset.setObjectName("buttonReset")        

        self.tombolTampil.clicked.connect(self.tombolT_diklik)
        self.tombolReset.clicked.connect(self.tombolR_diklik)

        self.layoutButton.addWidget(self.tombolTampil)
        self.layoutButton.addWidget(self.tombolReset)


        # Tampil Biodata

        self.labelBio = QLabel("DATA BIODATA")
        self.labelNama2 = QLabel("Nama Lengkap:")
        self.labelNIM2 = QLabel("NIM:")
        self.labelKelas2 = QLabel("Kelas:")  
        self.labelGender2 = QLabel("Jenis Kelamin:") 

        # Layout
        layoutUtama = QVBoxLayout()
        layoutUtama.addWidget(self.labelNama)
        layoutUtama.addWidget(self.inputNama)
        layoutUtama.addWidget(self.labelNIM)
        layoutUtama.addWidget(self.inputNIM)
        layoutUtama.addWidget(self.labelKelas)
        layoutUtama.addWidget(self.inputKelas)
        layoutUtama.addWidget(self.labelGender)
        layoutUtama.addWidget(self.comboBox)
        layoutUtama.addLayout(self.layoutButton)
        layoutUtama.addWidget(self.labelBio)
        layoutUtama.addWidget(self.labelNama2)
        layoutUtama.addWidget(self.labelNIM2)
        layoutUtama.addWidget(self.labelKelas2)
        layoutUtama.addWidget(self.labelGender2)  
        

      
        self.setLayout(layoutUtama)

    def tombolT_diklik(self):
        nama = self.inputNama.text()
        nim = self.inputNIM.text()
        kelas = self.inputKelas.text()
        gender = self.comboBox.currentText()

        if nama == "" or nim == "" or kelas == "":
            print("Nama / NIM / Kelas Masih kosong") 
        else:
            self.labelNama2.setText(f"Nama Lengkap: {nama}")
            self.labelNIM2.setText(f"NIM: {nim}")
            self.labelKelas2.setText(f"Kelas: {kelas}")
            self.labelGender2.setText(f"Jenis Kelamin: {gender}")
    
    def tombolR_diklik(self):
        self.inputNama.setText("")
        self.inputNIM.setText("")
        self.inputKelas.setText("")
        self.comboBox.setCurrentIndex(0)
        self.labelNama2.setText(f"Nama Lengkap:")
        self.labelNIM2.setText(f"NIM:")
        self.labelKelas2.setText(f"Kelas:")
        self.labelGender2.setText(f"Jenis Kelamin:")
        
def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()

    sys.exit(app.exec())
    
if __name__ == "__main__":
    main()