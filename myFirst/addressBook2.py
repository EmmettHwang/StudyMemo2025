import sys

try:
    from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QTextEdit
    from PyQt5.QtGui import QIcon
except ModuleNotFoundError:
    print("PyQt5가 설치되지 않은 것 같아요! 먼저 터미널이나 명령 프롬프트에서 'pip install PyQt5'를 실행해 주세요. 😊")
    sys.exit(1)

class AddressBook(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.addresses = {}

    def initUI(self):
        layout = QVBoxLayout()

        self.name_label = QLabel('이름:')
        self.name_label.setPixmap(QIcon("user_icon.png").pixmap(16, 16))  # 사람 모양 아이콘 추가
        self.name_input = QLineEdit()
        layout.addWidget(self.name_label)
        layout.addWidget(self.name_input)

        self.address_label = QLabel('주소:')
        self.address_label.setPixmap(QIcon("phone_icon.png").pixmap(16, 16))  # 전화기 모양 아이콘 추가
        self.address_input = QLineEdit()
        layout.addWidget(self.address_label)
        layout.addWidget(self.address_input)

        self.add_button = QPushButton('추가')
        self.add_button.setIcon(QIcon("add_icon.png"))  # 추가 아이콘
        self.add_button.clicked.connect(self.add_address)
        layout.addWidget(self.add_button)

        self.search_label = QLabel('검색 (이름 입력):')
        self.search_input = QLineEdit()
        layout.addWidget(self.search_label)
        layout.addWidget(self.search_input)

        self.search_button = QPushButton('검색')
        self.search_button.setIcon(QIcon("search_icon.png"))  # 검색 아이콘
        self.search_button.clicked.connect(self.search_address)
        layout.addWidget(self.search_button)

        self.result_display = QTextEdit()
        self.result_display.setReadOnly(True)
        layout.addWidget(self.result_display)

        self.setLayout(layout)
        self.setWindowTitle('주소록 프로그램')
        self.setGeometry(100, 100, 300, 300)
        # 여기 아이콘 파일이 필요함. 
        self.setWindowIcon(QIcon("address_book_icon.png"))  # 창 아이콘 추가

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