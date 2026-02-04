import re
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
        #Botones
        self.ui.btnGuardar.clicked.connect(self.guardar)
        self.ui.btnLimpiar.clicked.connect(self.limpiar)
        self.ui.btnEliminar.clicked.connect(self.eliminar)
        self.ui.btnBuscar.clicked.connect(self.buscar)
        self.ui.btnActualizar.clicked.connect(self.actualizar)
        #Texto
        self.ui.txtCedula_Buscar.setValidator(QIntValidator())
        self.ui.txtCedula.setValidator(QIntValidator())

    def guardar(self):
        # Recoleccion de datos del formulario
        nombre = self.ui.txtNombre.text()
        cedula = self.ui.txtCedula.text()
        apellido = self.ui.txtApellido.text()
        email = self.ui.txtEmail.text()
        regex_email = r'^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,4}$'
        sexo = self.ui.cbSexo.currentText()
        estado = self.ui.cbEstado.currentText()

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
        elif cedula == "":
            QMessageBox.warning(self, "Advertencia", "El campo cedula no debe estar vacio")
        elif sexo == "Selecione..." or sexo == "Seleccione...":
            QMessageBox.warning(self, "Advertencia", "Debe seleccionar un Sexo")
        elif estado == "Selecione..." or estado == "Seleccione...":
            QMessageBox.warning(self, "Advertencia", "Debe seleccionar un Estado civil")
        elif email == "":  # <--- Validación para el Gmail
            QMessageBox.warning(self, "Advertencia", "Debe ingresar un correo electrónico")
        elif not re.match(regex_email, email.lower()):
            QMessageBox.warning(self, "Advertencia",
                                "El formato del correo electrónico no es válido (ejemplo@dominio.com)")
        else:
            persona = Persona(cedula=cedula, nombre=nombre, apellido=apellido, sexo=sexo, estado=estado, email=email)
            respuesta_dic = PersonaDAO.insertar_persona(persona)
            if respuesta_dic["ejecuto"]:
                print (persona)
                self.ui.statusbar.showMessage("Se guardo la persona", 1500)

                self.limpiar()
            else:
                QMessageBox.critical(self, "Error", "Error al guardar persona.")

            # Muestra confirmacion de guardado en la barra de estado

    def buscar(self):
        cedula = self.ui.txtCedula_Buscar.text().zfill(10)
        if len(cedula) > 10:
            QMessageBox.warning(self, "Advertencia", "Debe ingresar una Cedula válida")
        else:
            persona = PersonaDAO.seleccionar_persona(cedula)
            if persona:
                self.ui.txtNombre.setText(persona.nombre)
                self.ui.txtCedula.setText(persona.cedula)
                self.ui.txtApellido.setText(persona.apellido)
                self.ui.txtEmail.setText(persona.email)
                self.ui.cbSexo.setCurrentText(persona.sexo)
                self.ui.cbEstado.setCurrentText(persona.estado)
                print(persona)
            else:
                QMessageBox.warning(self, 'Advertencia', 'No existe persona registrada con'
                                                 'la cedula buscada.')

    def limpiar(self):
        # Limpia los datos del formulario
        self.ui.txtNombre.setText("")
        self.ui.txtCedula.setText("")
        self.ui.txtApellido.setText("")
        self.ui.txtEmail.setText("")
        self.ui.cbSexo.setCurrentText("Seleccione...")
        self.ui.cbEstado.setCurrentText("Seleccione...")
        self.ui.txtCedula_Buscar.setText("")

    def eliminar (self):
        nombre = self.ui.txtNombre.text()
        cedula = self.ui.txtCedula.text()
        apellido = self.ui.txtApellido.text()
        email = self.ui.txtEmail.text()
        regex_email = r'^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,4}$'
        sexo = self.ui.cbSexo.currentText()
        estado = self.ui.cbEstado.currentText()
        if len(cedula) > 10:
            QMessageBox.warning(self, "Advertenccia", "Debe ingresar una cedula con 10 digitos")
        else:
            persona = Persona(cedula=cedula, nombre=nombre, apellido=apellido, sexo=sexo, estado=estado, email=email)
            if QMessageBox.question(self, "Pregunta", "¿Esta seguro de querer eliminar?") == QMessageBox.Yes:
                print("Elimino a la persaona", nombre)
                PersonaDAO.eliminar_persona(persona)
                self.ui.txtNombre.setText("")
                self.ui.txtCedula.setText("")
                self.ui.txtApellido.setText("")
                self.ui.txtEmail.setText("")
                self.ui.cbSexo.setCurrentText("Seleccione...")
                self.ui.cbEstado.setCurrentText("Seleccione...")
                self.ui.txtCedula_Buscar.setText("")
            else:
                print("Usted cancelo la acción")


    def actualizar (self):
        nombre = self.ui.txtNombre.text()
        cedula = self.ui.txtCedula.text()
        apellido = self.ui.txtApellido.text()
        email = self.ui.txtEmail.text()
        regex_email = r'^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,4}$'
        sexo = self.ui.cbSexo.currentText()
        estado = self.ui.cbEstado.currentText()

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
        elif cedula == "":
            QMessageBox.warning(self, "Advertencia", "El campo cedula no debe estar vacio")
        elif sexo == "Selecione..." or sexo == "Seleccione...":
            QMessageBox.warning(self, "Advertencia", "Debe seleccionar un Sexo")
        elif estado == "Selecione..." or estado == "Seleccione...":
            QMessageBox.warning(self, "Advertencia", "Debe seleccionar un Estado civil")
        elif email == "":  # <--- Validación para el Gmail
            QMessageBox.warning(self, "Advertencia", "Debe ingresar un correo electrónico")
        elif not re.match(regex_email, email.lower()):
            QMessageBox.warning(self, "Advertencia",
                                "El formato del correo electrónico no es válido (ejemplo@dominio.com)")
        else:
            persona = Persona(nombre=nombre, apellido=apellido, cedula=cedula, email=email, sexo=sexo, estado=estado)
            respuesta_dic = PersonaDAO.actualizar_persona(persona)
            if respuesta_dic["ejecuto"]:
                print(persona)
                self.ui.statusbar.showMessage("Se actualizo la persona", 1500)
                self.limpiar()
            else:
                QMessageBox.critical(self, "Error", "Error al actualizar persona.")

