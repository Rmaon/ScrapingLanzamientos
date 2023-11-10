class Videojuego:
    def __init__(self, fecha, titulo, enlace=None, plataforma=None):
        """
        Constructor de la clase Videojuego.

        Parameters:
        - fecha (str): Fecha de lanzamiento del videojuego.
        - titulo (str): Título del videojuego.
        - enlace (str, opcional): Enlace relacionado con el videojuego (por ejemplo, un enlace a más detalles).
        - plataforma (str, opcional): Plataforma en la que se lanzó el videojuego.

        """
        self.fecha = fecha
        self.titulo = titulo
        self.enlace = enlace
        self.plataforma = plataforma

    def mostrar_datos(self):
        """
        Método para imprimir los datos del videojuego.

        Imprime la fecha, el título y, opcionalmente, el enlace y la plataforma del videojuego.

        """
        print("Fecha:", self.fecha)
        print("Título:", self.titulo)

        # Verificar si hay un enlace y mostrarlo si existe
        if self.enlace:
            print("Enlace:", self.enlace)

        # Verificar si hay una plataforma y mostrarla si existe
        if self.plataforma:
            print("Plataforma:", self.plataforma)

        print()  # Imprimir una línea en blanco al final para un formato más limpio
