class Videojuego:
    def __init__(self, fecha, titulo, enlace=None, plataforma=None):
        self.fecha = fecha
        self.titulo = titulo
        self.enlace = enlace
        self.plataforma = plataforma

    def mostrar_datos(self):
        print("Fecha:", self.fecha)
        print("Título:", self.titulo)
        if self.enlace:
            print("Enlace:", self.enlace)
        if self.plataforma:
            print("Plataforma:", self.plataforma)
        print()