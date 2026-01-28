from DATOS.conexion import Conexion
from DOMINIO.Persona import Persona


class PersonaDAO:
    _INSERT = ("INSERT INTO Personas (Nombres, apellidos, cedula, sexo, email)" "VALUES (?, ?, ?, ?, null)")

    @classmethod
    def insertar_persona(cls, persona):
        with Conexion.obtenerCursor() as cursor:
            datos = (persona.nombre, persona.apellido, persona.cedula, persona.sexo)
            cursor.execute(cls._INSERT, datos)


if __name__ == '__main__':
    p1 = Persona(cedula="0921748395", nombre="Carla", apellido="Villao", sexo="Femenino")
    PersonaDAO.insertar_persona(p1)