import sys

try:
    from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QTextEdit
except ModuleNotFoundError:
    print("PyQt5가 설치되지 않았습니다. 먼저 'pip install PyQt5'를 실행하세요.")
    sys.exit(1)

class AddressBook(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.addresses = {}

    def initUI(self):
        layout = QVBoxLayout()

        self.name_label = QLabel('이름:')
        self.name_input = QLineEdit()
        layout.addWidget(self.name_label)
        layout.addWidget(self.name_input)

        self.address_label = QLabel('주소:')
        self.address_input = QLineEdit()
        layout.addWidget(self.address_label)
        layout.addWidget(self.address_input)

        self.add_button = QPushButton('추가')
        self.add_button.clicked.connect(self.add_address)
        layout.addWidget(self.add_button)

        self.search_label = QLabel('검색 (이름 입력):')
        self.search_input = QLineEdit()
        layout.addWidget(self.search_label)
        layout.addWidget(self.search_input)

        self.search_button = QPushButton('검색')
        self.search_button.clicked.connect(self.search_address)
        layout.addWidget(self.search_button)

        self.result_display = QTextEdit()
        self.result_display.setReadOnly(True)
        layout.addWidget(self.result_display)

        self.setLayout(layout)
        self.setWindowTitle('주소록 프로그램')
        self.setGeometry(100, 100, 300, 300)

    def add_address(self):
        name = self.name_input.text().strip()
        address = self.address_input.text().strip()
        
        if name and address:
            self.addresses[name] = address
            self.result_display.setText(f'추가됨: {name} - {address}')
            self.name_input.clear()
            self.address_input.clear()
        else:
            self.result_display.setText('이름과 주소를 입력하세요!')

    def search_address(self):
        name = self.search_input.text().strip()
        if name in self.addresses:
            self.result_display.setText(f'{name}의 주소: {self.addresses[name]}')
        else:
            self.result_display.setText('주소를 찾을 수 없습니다.')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = AddressBook()
    window.show()
    sys.exit(app.exec_())
