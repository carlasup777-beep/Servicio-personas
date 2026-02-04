import pyodbc as bd
from DATOS.conexion import Conexion
from DOMINIO.Persona import Persona

class PersonaDAO:
    _INSERT = ("INSERT INTO Personas (nombres, apellidos, cedula, sexo, campo, email) "
               "VALUES (?, ?, ?, ?, ?, ?)")

    _SELECT = ("SELECT idPersona, nombres, apellidos, cedula, sexo, campo, email "
               "FROM Personas WHERE cedula = ?")

    _UPDATE = ("UPDATE Personas set nombres = ?, apellidos = ?, sexo = ?, campo  = ?, email = ? "
               "WHERE cedula=?")

    _DELETE = ("DELETE FROM Personas WHERE cedula = ?")

    @classmethod
    def insertar_persona(cls, persona):
        try:
            with Conexion.obtenerCursor() as cursor:
                datos = (persona.nombre, persona.apellido, persona.cedula,
                         persona.sexo, persona.estado, persona.email,)
                cursor.execute(cls._INSERT, datos)
                respuesta = cursor.rowcount
                if respuesta == 1:
                    return {"ejecuto": True, "mensaje": "Se guardó con éxito"}
                else:
                    return {"ejecuto": False, "mensaje": "No se insertó ningún registro"}
        except bd.IntegrityError as e_bb:
            print("Error en la inserción:", e_bb)
            if "UQ_cedula" in str(e_bb):
                return {"ejecuto": False, "mensaje": "La cédula ya existe"}
            elif "UQ_email" in str(e_bb):
                return {"ejecuto": False, "mensaje": "El email ya existe"}
            else:
                return {"ejecuto": False, "mensaje": "Error de integridad"}
        except Exception as e:
            print("Error general:", e)
            return {"ejecuto": False, "mensaje": "Error al guardar los datos, comuníquese con sistemas."}

    @classmethod
    def seleccionar_persona(cls, cedula):
        persona = None
        try:
            with Conexion.obtenerCursor() as cursor:
                datos = (cedula,)
                cursor.execute(cls._SELECT, datos)
                registro = cursor.fetchone()
                if registro:
                    persona = Persona(nombre=registro[1], apellido=registro[2], cedula=registro[3], sexo=registro[4], estado=registro[5], email=registro[6] if registro[6] is not None else "" )
                return persona
        except Exception as e:
            print("Error general:", e)
            return None

    @classmethod
    def actualizar_persona(cls, persona):
        try:
            with Conexion.obtenerCursor() as cursor:
                datos = (persona.nombre, persona.apellido, persona.sexo, persona.estado, persona.email, persona.cedula)
                cursor.execute(cls._UPDATE, datos)
                respuesta = cursor.rowcount
                if respuesta == 1:
                    return {"ejecuto": True, "mensaje": "Se guardó con éxito"}
                else:
                    return {"ejecuto": False, "mensaje": "No se insertó ningún registro"}
        except bd.IntegrityError as e_bb:
            print("Error en la inserción:", e_bb)
            if "UQ_cedula" in str(e_bb):
                return {"ejecuto": False, "mensaje": "La cédula ya existe"}
            elif "UQ_email" in str(e_bb):
                return {"ejecuto": False, "mensaje": "El email ya existe"}
            else:
                return {"ejecuto": False, "mensaje": "Error de integridad"}
        except Exception as e:
            print("Error general:", e)
            return {"ejecuto": False, "mensaje": "Error al guardar los datos, comuníquese con sistemas."}

    @classmethod
    def eliminar_persona(cls, persona):
        try:
            with Conexion.obtenerCursor() as cursor:
                datos = (persona.cedula,)
                cursor.execute(cls._DELETE, datos)
                respuesta = cursor.rowcount
                if respuesta == 1:
                    return {"ejecuto": True, "mensaje": "Se elimino con exito"}
        except Exception as e:
            print("Error general:", e)
            print(type(e))
            return {"ejecuto": False, "mensaje": "Error al eliminar persona."}