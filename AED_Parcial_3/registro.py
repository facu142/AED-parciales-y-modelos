import random

FORMATO = '{:^5} {} {:<70} {} {:^8} {} {:^10} {} {:^5}'
titulos = 'Eclipse Foundation Launches New Eclipse IDE Working Group', 'Infragistics Advances Low-Code Development with Latest Release', 'Synopsys Adds Code Dx to AppSec Portfolio', 'Online Tech Trainer Pluralsight to Acquire A Cloud Guru', 'Microsoft and IBM Collaborate on WebSphere Java EE App Server Solution', 'Google I/O: From Android 12 to Firebase and Flutter', 'JetBrains Updates Java IDEs, Launches Code with Me', 'Gitpod Announces Features, Forum, Funding', 'Microsoft Rolls Out OpenJDK Preview Release', 'Is AI Coming for Your Dev Job or Not? A Tale of Two Surveys', 'Wasserstein Distance Using C# and Python', 'VS Code Python Tool Revamps Jupyter Notebooks Experience', 'Microsoft Plans .NET Community Toolkit', 'JavaScript Debugging Now Built-In to VS Code'


class Trabajo:
    def __init__(self, n_id, titulo, paginas, autores, codigo_area):
        self.n_id = n_id
        self.titulo = titulo
        self.paginas = paginas
        self.autores = autores
        self.codigo_area = codigo_area

    def __str__(self):
        return FORMATO.format(self.n_id, '|', self.titulo, '|', self.paginas, '|', self.autores, '|', self.codigo_area)


def crear_trabajo_aleatorio():
    n_id = random.randint(1, 100)
    titulo = random.choice(titulos)
    paginas = random.randint(1, 20)
    autores = random.randint(1, 20)
    codigo_area = random.randint(0, 9)

    return Trabajo(n_id, titulo, paginas, autores, codigo_area)
