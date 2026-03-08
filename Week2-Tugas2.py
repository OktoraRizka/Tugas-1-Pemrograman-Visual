# Nama : Oktora Rizka Arifin
# NIM  : F1D02410145
# Kelas : 6C

import sys
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton

class MainWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.init_ui()
    
    def init_ui(self):
        self.setWindowTitle("Konversi Suhu")
        self.resize(400, 300)
        self.setStyleSheet("""
            QLineEdit {
                background-color:#D5EDDB;
                border: 1px solid #2ecc71;
                padding: 10px;
                border-radius: 5px;
            }

            QPushButton {
                background-color:#2980b9;
                color: #ffffff;
                padding: 10px;
            }
                           
            QPushButton:hover {
                background-color: #3498db;
            }

            QPushButton:pressed {
                background-color: #1f618d;
            }

            #Judul {
                background-color:#3498db;
                font-weight: bold;
                color: #ffffff;
                font-size: 18px;
                padding: 10px;           
                border-radius: 5px;
            }
            
            #labelKonver {
               background-color:#C8E2FF;
                padding: 10px;
                font-size: 14px;
                border-radius: 5px;
            }
            
            * {
            background-color: #f5f6fa;
            color : #2c3e50;
            }        
            
        """)
        
        # Label
        self.labelJudul = QLabel("KONVERSI SUHU:")
        self.labelNama = QLabel("Masukkan Suhu (Celcius):")

        self.labelJudul.setObjectName("Judul")        


        # Input
        self.inputCelsius = QLineEdit()
        self.inputCelsius.setPlaceholderText("Masukkan Angka")
        

        # Button
        self.layoutButton = QHBoxLayout()
        self.tombolFahrenheit = QPushButton("Fakrenheit")
        self.tombolKelvin = QPushButton("Kelvin")
        self.tombolReamur = QPushButton("Reamur")     


        self.tombolFahrenheit.clicked.connect(self.konversiFahrenheit)
        self.tombolKelvin.clicked.connect(self.konversiKelvin)
        self.tombolReamur.clicked.connect(self.konversiReamur)

        self.layoutButton.addWidget(self.tombolFahrenheit)
        self.layoutButton.addWidget(self.tombolKelvin)
        self.layoutButton.addWidget(self.tombolReamur)

        # Tampil konversi
        self.labelHasil = QLabel("Hasil Konversi:")
        self.labelKonversi = QLabel("")
        self.labelHasil.setStyleSheet("color:navi;font-weight: bold;")

        self.labelKonversi.setObjectName("labelKonver")        

        # Layout
        layoutUtama = QVBoxLayout()
        layoutUtama.addWidget(self.labelJudul)
        layoutUtama.addWidget(self.labelNama)
        layoutUtama.addWidget(self.inputCelsius)
        layoutUtama.addLayout(self.layoutButton)
        layoutUtama.addWidget(self.labelHasil)
        layoutUtama.addWidget(self.labelKonversi)
        

      
        self.setLayout(layoutUtama)

    def ambil_input(self):
        teks = self.inputCelsius.text()
        try:
            if teks == "":
                self.labelKonversi.setText("Input masih kosong!")
            else:
                return float(teks)
        except ValueError:
            self.labelKonversi.setText("Input bukan angka!")
            return None
        
    def konversiFahrenheit(self):
        celsius = self.ambil_input()
        if celsius is not None:
            fahrenheit = (celsius * 9/5) + 32
            self.labelKonversi.setText(f"{celsius} °C = {fahrenheit :.2f} °F")

    def konversiKelvin(self):
        celsius = self.ambil_input()
        if celsius is not None:
            kelvin = celsius + 273.15
            self.labelKonversi.setText(f"{celsius} °C = {kelvin:.2f} °K")
    
    def konversiReamur(self):
        celsius = self.ambil_input()
        if celsius is not None:
            reamur = celsius * 4/5
            self.labelKonversi.setText(f"{celsius} °C = {reamur:.2f} °R")

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()

    sys.exit(app.exec())
    
if __name__ == "__main__":
    main()