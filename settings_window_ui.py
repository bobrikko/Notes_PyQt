from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_SettingsDialog(object):
    def setupUi(self, SettingsDialog):
        SettingsDialog.setObjectName("SettingsDialog")
        self.verticalLayout = QtWidgets.QVBoxLayout(SettingsDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.themeGroupBox = QtWidgets.QGroupBox(parent=SettingsDialog)
        self.themeGroupBox.setObjectName("themeGroupBox")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.themeGroupBox)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.darkThemeRadio = QtWidgets.QRadioButton(parent=self.themeGroupBox)
        self.darkThemeRadio.setObjectName("darkThemeRadio")
        self.verticalLayout_2.addWidget(self.darkThemeRadio)
        self.lightThemeRadio = QtWidgets.QRadioButton(parent=self.themeGroupBox)
        self.lightThemeRadio.setObjectName("lightThemeRadio")
        self.verticalLayout_2.addWidget(self.lightThemeRadio)
        self.verticalLayout.addWidget(self.themeGroupBox)
        self.fontComboBox = QtWidgets.QFontComboBox(parent=SettingsDialog)
        self.fontComboBox.setObjectName("fontComboBox")
        self.verticalLayout.addWidget(self.fontComboBox)
        self.sizeSpinBox = QtWidgets.QSpinBox(parent=SettingsDialog)
        self.sizeSpinBox.setMinimum(8)
        self.sizeSpinBox.setMaximum(48)
        self.sizeSpinBox.setProperty("value", 12)
        self.sizeSpinBox.setObjectName("sizeSpinBox")
        self.verticalLayout.addWidget(self.sizeSpinBox)
        self.applyButton = QtWidgets.QPushButton(parent=SettingsDialog)
        self.applyButton.setObjectName("applyButton")
        self.verticalLayout.addWidget(self.applyButton)

        self.retranslateUi(SettingsDialog)
        QtCore.QMetaObject.connectSlotsByName(SettingsDialog)

    def retranslateUi(self, SettingsDialog):
        _translate = QtCore.QCoreApplication.translate
        SettingsDialog.setWindowTitle(_translate("SettingsDialog", "Настройки"))
        self.themeGroupBox.setTitle(_translate("SettingsDialog", "Тема"))
        self.darkThemeRadio.setText(_translate("SettingsDialog", "Темная тема"))
        self.lightThemeRadio.setText(_translate("SettingsDialog", "Светлая тема"))
        self.applyButton.setText(_translate("SettingsDialog", "Применить"))