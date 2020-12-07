import pathlib
import sys
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QFileDialog

import UI.diff_UI
from Src import diff_finder


class BOM_diff(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = UI.diff_UI.Ui_MainWindow()
        self.ui.setupUi(self)
        self.old_bom_address = self.ui.lineEdit
        self.new_bom_address = self.ui.lineEdit_2
        self.diff_address = self.ui.lineEdit_3
        self.info_window = self.ui.plainTextEdit

        self.path = pathlib.Path.cwd()
        self.file_to_save = pathlib.Path('')
        self.finder = diff_finder.DiffChecker()

        self.initUI()

    def initUI(self):
        btn_old_bom = self.ui.pushButton
        btn_new_bom = self.ui.pushButton_2
        btn_diff = self.ui.pushButton_3
        btn_close = self.ui.pushButton_4
        btn_apply = self.ui.pushButton_5

        btn_old_bom.clicked.connect(self.old_bom_clicked)
        btn_new_bom.clicked.connect(self.new_bom_clicked)
        btn_diff.clicked.connect(self.diff_clicked)
        btn_close. clicked.connect(self.close_clicked)
        btn_apply.clicked.connect(self.apply_clicked)

    def btn_clicked(self, name):
        return QFileDialog.getOpenFileName(self, f'Выберите {name}', str(self.path), 'XLSX files (*.xlsx)')

    def old_bom_clicked(self):
        path_file = self.btn_clicked('файл старого BOM')[0]
        self.path = pathlib.Path(path_file).parent
        self.old_bom_address.setText(str(path_file))
        self.finder.set_old_BOM(path_file)

    def new_bom_clicked(self):
        path_file = self.btn_clicked('файл нового BOM')[0]
        self.path = pathlib.Path(path_file).parent
        self.new_bom_address.setText(str(path_file))
        self.finder.set_new_BOM(path_file)

    def diff_clicked(self):
        self.file_to_save = QFileDialog.getSaveFileName(self, f'Выберите файл для сохранения',
                                                str(self.path),
                                                'XLSX files (*.xlsx)')[0]
        self.path = pathlib.Path(self.file_to_save).parent
        self.diff_address.setText(str(self.file_to_save))
        self.finder.set_diff(self.file_to_save)

    def close_clicked(self):
        self.close()

    def apply_clicked(self):
        self.finder.diff_finder()
        self.info_window.appendPlainText(f'Сравнение BOM-файлов проведено успешно!\n'
                                         fr'Результаты сравнения записаны в файл {self.file_to_save}')

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Escape:
            self.close()


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = BOM_diff()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
