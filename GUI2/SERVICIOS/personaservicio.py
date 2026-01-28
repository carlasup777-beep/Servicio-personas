from PySide6.QtGui import QIntValidator
from PySide6.QtWidgets import QMainWindow, QMessageBox

from DATOS.persona_DAO import PersonaDAO
from UI.vtnPrincipal import Ui_vtnPrincipal
from DOMINIO.Persona import Persona

class PersonaServicio(QMainWindow):
    '''
    Clase que genera la logica de los objetos de la persona
    '''

    def __init__(self):
        super(PersonaServicio, self).__init__()
        self.ui = Ui_vtnPrincipal()
        self.ui.setupUi(self)
        self.ui.btnGuardar.clicked.connect(self.guardar)
        self.ui.btnLimpiar.clicked.connect(self.limpiar)
        self.ui.txtCedula.setValidator(QIntValidator())

    def guardar(self):
        # Recoleccion de datos del formulario
        nombre = self.ui.txtNombre.text()
        cedula = self.ui.txtCedula.text()
        apellido = self.ui.txtApellido.text()
        sexo = self.ui.cbSexo.currentText()

        # Validacion de datos
        if nombre == "":
            QMessageBox.warning(self, "Advertencia", "Debe ingresar un Nombre")
        elif not nombre.replace(" ", "").isalpha():
            QMessageBox.warning(self, "Advertencia", "ERROR NOMBRE. Debe ingresar texto")
        elif apellido == "":
            QMessageBox.warning(self, "Advertencia", "Debe ingresar un Apellido")
        elif not apellido.replace(" ", "").isalpha():
            QMessageBox.warning(self, "Advertencia", "Debe ingresar texto")
        elif len(cedula) > 10:
            QMessageBox.warning(self, "Advertencia", "Debe ingresar una Cedula válida")
        elif sexo == "Selecione..." or sexo == "Seleccione...":
            QMessageBox.warning(self, "Advertencia", "Debe seleccionar un Sexo")
        else:
            persona = Persona(cedula=cedula, nombre=nombre, apellido=apellido, sexo=sexo)
            PersonaDAO.insertar_persona(persona)
            print(nombre)
            print(apellido)
            print(cedula)
            print(sexo)

            # Muestra confirmacion de guardado en la barra de estado
            self.ui.statusbar.showMessage("Se guardo la persona", 1500)
            self.limpiar()

    def limpiar(self):
        # Limpia los datos del formulario
        self.ui.txtNombre.setText("")
        self.ui.txtCedula.setText("")
        self.ui.txtApellido.setText("")
        self.ui.cbSexo.setCurrentText("Seleccione...")