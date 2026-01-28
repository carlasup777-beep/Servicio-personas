# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MenuNombreApellido.ui'
##
## Created by: Qt User Interface Compiler version 6.10.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QLabel, QLineEdit,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QWidget)

class Ui_vtnPrincipal(object):
    def setupUi(self, vtnPrincipal):
        if not vtnPrincipal.objectName():
            vtnPrincipal.setObjectName(u"vtnPrincipal")
        vtnPrincipal.resize(650, 474)
        font = QFont()
        font.setPointSize(10)
        vtnPrincipal.setFont(font)
        self.centralwidget = QWidget(vtnPrincipal)
        self.centralwidget.setObjectName(u"centralwidget")
        self.lblNombre = QLabel(self.centralwidget)
        self.lblNombre.setObjectName(u"lblNombre")
        self.lblNombre.setGeometry(QRect(90, 80, 69, 22))
        font1 = QFont()
        font1.setFamilies([u"Times New Roman"])
        font1.setPointSize(14)
        font1.setBold(True)
        font1.setItalic(True)
        self.lblNombre.setFont(font1)
        self.lblApellido = QLabel(self.centralwidget)
        self.lblApellido.setObjectName(u"lblApellido")
        self.lblApellido.setGeometry(QRect(90, 150, 74, 22))
        self.lblApellido.setFont(font1)
        self.txtNombre = QLineEdit(self.centralwidget)
        self.txtNombre.setObjectName(u"txtNombre")
        self.txtNombre.setGeometry(QRect(180, 80, 291, 21))
        self.txtNombre.setMaxLength(20)
        self.txtApellido = QLineEdit(self.centralwidget)
        self.txtApellido.setObjectName(u"txtApellido")
        self.txtApellido.setGeometry(QRect(180, 150, 291, 21))
        self.txtApellido.setFont(font)
        self.txtApellido.setMaxLength(20)
        self.btnGuardar = QPushButton(self.centralwidget)
        self.btnGuardar.setObjectName(u"btnGuardar")
        self.btnGuardar.setGeometry(QRect(480, 330, 101, 41))
        font2 = QFont()
        font2.setPointSize(10)
        font2.setBold(True)
        font2.setUnderline(True)
        self.btnGuardar.setFont(font2)
        self.txtCedula = QLineEdit(self.centralwidget)
        self.txtCedula.setObjectName(u"txtCedula")
        self.txtCedula.setGeometry(QRect(180, 210, 151, 21))
        self.txtCedula.setFont(font)
        self.txtCedula.setMaxLength(10)
        self.lblApellido_2 = QLabel(self.centralwidget)
        self.lblApellido_2.setObjectName(u"lblApellido_2")
        self.lblApellido_2.setGeometry(QRect(90, 210, 74, 22))
        self.lblApellido_2.setFont(font1)
        self.btnLimpiar = QPushButton(self.centralwidget)
        self.btnLimpiar.setObjectName(u"btnLimpiar")
        self.btnLimpiar.setGeometry(QRect(330, 330, 101, 41))
        self.btnLimpiar.setFont(font2)
        self.cbSexo = QComboBox(self.centralwidget)
        self.cbSexo.addItem("")
        self.cbSexo.addItem("")
        self.cbSexo.addItem("")
        self.cbSexo.addItem("")
        self.cbSexo.setObjectName(u"cbSexo")
        self.cbSexo.setGeometry(QRect(180, 260, 181, 21))
        self.lblSexo = QLabel(self.centralwidget)
        self.lblSexo.setObjectName(u"lblSexo")
        self.lblSexo.setGeometry(QRect(90, 260, 74, 22))
        self.lblSexo.setFont(font1)
        vtnPrincipal.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(vtnPrincipal)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 650, 21))
        vtnPrincipal.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(vtnPrincipal)
        self.statusbar.setObjectName(u"statusbar")
        vtnPrincipal.setStatusBar(self.statusbar)
        QWidget.setTabOrder(self.txtNombre, self.txtApellido)
        QWidget.setTabOrder(self.txtApellido, self.txtCedula)
        QWidget.setTabOrder(self.txtCedula, self.btnGuardar)

        self.retranslateUi(vtnPrincipal)

        QMetaObject.connectSlotsByName(vtnPrincipal)
    # setupUi

    def retranslateUi(self, vtnPrincipal):
        vtnPrincipal.setWindowTitle(QCoreApplication.translate("vtnPrincipal", u"Servicio Personas", None))
        self.lblNombre.setText(QCoreApplication.translate("vtnPrincipal", u"Nombre:", None))
        self.lblApellido.setText(QCoreApplication.translate("vtnPrincipal", u"Apellido:", None))
        self.btnGuardar.setText(QCoreApplication.translate("vtnPrincipal", u"Guardar", None))
        self.lblApellido_2.setText(QCoreApplication.translate("vtnPrincipal", u"Cedula:", None))
        self.btnLimpiar.setText(QCoreApplication.translate("vtnPrincipal", u"Limpiar", None))
        self.cbSexo.setItemText(0, QCoreApplication.translate("vtnPrincipal", u"Seleccione...", None))
        self.cbSexo.setItemText(1, QCoreApplication.translate("vtnPrincipal", u"Masculino", None))
        self.cbSexo.setItemText(2, QCoreApplication.translate("vtnPrincipal", u"Femenino", None))
        self.cbSexo.setItemText(3, QCoreApplication.translate("vtnPrincipal", u"Prefiero no decirlo", None))

        self.lblSexo.setText(QCoreApplication.translate("vtnPrincipal", u"Sexo:", None))
    # retranslateUi

