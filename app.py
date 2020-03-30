"""
Alumno:                       Adolfo León Barrón
Profesor:             Salvador Hernández Mendoza
Materia: Aplicaciones web Orientadas a servicios
Cuatrimestre:                                4to
"""

import web

urls = (
    '/alumnos/?', 'application.controllers.alumnos.Alumnos',
)
app = web.application(urls, globals())

if __name__ == "__main__":
    web.config.debug = False
    app.run()
