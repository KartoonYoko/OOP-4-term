from class1 import ComplexNumber
import sys  # sys нужен для передачи argv в QApplication
import os  # Отсюда нам понадобятся методы для отображения содержимого директорий
from PyQt5 import QtWidgets
import gui  # Это наш конвертированный файл дизайна

class ExampleApp(QtWidgets.QMainWindow, gui.Ui_Form):
    def __init__(self):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле design.py
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        self.pushButton_calculate.clicked.connect(self.btn_calc)
        self.lineEdit_thirdRe.textChanged.connect(self.comArgAndAbs)
        self.lineEdit_thirdIm.textChanged.connect(self.comArgAndAbs)


    def readComNum(self, x, y, z):
            str1 = x.text()
            str2 = y.text()
            try:
                str1 = float(str1)
                str2 = float(str2)
            except:
                z.setText("Wrong")
                return 0
            return ComplexNumber(str1, str2)


    def comArgAndAbs(self):
        c = self.readComNum(self.lineEdit_thirdRe, self.lineEdit_thirdIm, self.lineEdit_Absolute)
        if isinstance(c, ComplexNumber):
            self.lineEdit_Absolute.setText(str(abs(c)))
            self.lineEdit_Argument.setText(str(c.arg()))

    def btn_calc(self):
        c1 = self.readComNum(self.lineEdit_firstRe, self.lineEdit_firstIm, self.lineEdit_Answer)
        c2 = self.readComNum(self.lineEdit_secondRe, self.lineEdit_secondIm, self.lineEdit_Answer)
        if isinstance(c1, ComplexNumber) and isinstance(c2, ComplexNumber):
            if self.radioButton_plus.isChecked():
                c3 = c1 + c2
                self.lineEdit_Answer.setText(c3())
            elif self.radioButton_minus.isChecked():
                c3 = c1 - c2
                self.lineEdit_Answer.setText(c3())
            elif self.radioButton_div.isChecked():
                c3 = c1 / c2
                self.lineEdit_Answer.setText(c3())
            elif self.radioButton_mult.isChecked():
                c3 = c1 * c2
                self.lineEdit_Answer.setText(c3())


def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = ExampleApp()  # Создаём объект класса ExampleApp
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение
if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()


