import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QMessageBox
from design import Ui_MainWindow
from PySide6.QtGui import QPixmap


class SawkaClicker(QMainWindow):
    def __init__(self):
        super(SawkaClicker, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.upgrade_cost = 20
        self.click_count = 0  # Счетчик кликов
        self.click_k = 1
        self.target_click_count = 15  # Целевое количество кликов
        self.current_image_index = 0
        
        self.image_list = [
            "img/sawka1",
            "img/sawka2",
            "img/sawka3",
            "img/sawka4",
            "img/sawka5",
            "img/sawka6",
            "img/sawka7",
            "img/sawka8",
            "img/sawka9",
            "img/sawka10",
            "img/sawka11",
        ]
        
        image_path = self.image_list[self.current_image_index]  # Берем первое изображение из списка
        pixmap = QPixmap(image_path)
        self.ui.sawka_img.setPixmap(pixmap)
        # Подключаем слот для обработки клика
        self.ui.btn_hqd.setText(f"ХЛОПНУТЬ ТЯГУ ({self.upgrade_cost})")
        self.ui.btn_beer.setText(f"ПРОПИТЬ ({self.upgrade_cost})")
        self.ui.btn_main.clicked.connect(self.increment_click_count)
        self.ui.btn_hqd.clicked.connect(self.upgrade)
        self.ui.btn_beer.clicked.connect(self.upgrade)
        
        
    def increment_click_count(self):
        # Увеличиваем счетчик кликов
        self.click_count = self.click_count + self.click_k
        self.ui.score.setText(str(self.click_count))
        progress_percentage = (self.click_count / self.target_click_count) * 100
        self.ui.progressBar.setValue(progress_percentage)
        if self.click_count >= self.target_click_count:
            self.show_next_image()
            
    def show_next_image(self):
        if self.current_image_index + 1 < len(self.image_list):
            # Увеличиваем индекс, чтобы получить следующее изображение из списка
            self.current_image_index += 1
            image_path = self.image_list[self.current_image_index]
            pixmap = QPixmap(image_path)
            self.ui.sawka_img.setPixmap(pixmap)
            self.target_click_count *= 4
            self.click_count = 0
            self.ui.progressBar.setValue(0)
        else:
            QMessageBox.information(self, "ИГРА ПРОЙДЕНА", "Рыбинкс денацифицирован!")
            app.quit()
    
    def upgrade(self):
        if self.click_count >= self.upgrade_cost:
            self.click_k *= 3
            self.click_count -= self.upgrade_cost
            self.upgrade_cost *= 3
            self.ui.score.setText(str(self.click_count))
            self.ui.btn_hqd.setText(f"ХЛОПНУТЬ ТЯГУ ({self.upgrade_cost})")
            self.ui.btn_beer.setText(f"ПРОПИТЬ ({self.upgrade_cost})")
        else:
            
         QMessageBox.warning(self, "ВНИМАНИЕ", "У вас недостаточно трупов!")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SawkaClicker()
    window.show()
    app.exec()