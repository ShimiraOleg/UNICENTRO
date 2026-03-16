class LivroNaoEncontradoError(Exception):
    pass

class LivroIndisponivelError(Exception):
    pass

class UsuarioNaoEncontradoError(Exception):
    pass

class LivroNaoEmprestadoError(Exception):
    pass

class Livro:
    def __init__(self, titulo, autor, isbn):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.disponivel = True

class Usuario:
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf
        self.livros_emprestados: list[Livro] = []

class Biblioteca:
    def __init__(self):
        self._livros: dict[str, Livro] = {}
        self._usuarios: dict[str, Usuario] = {}

    def cadastrar_livro(self, livro: Livro) -> None:
        if livro.isbn in self._livros:
            print("Já existe um livro com esse INSB cadastrado no sistema\n")
            return
        self._livros[livro.isbn] = livro
        print(f"O livro '{livro.titulo}' foi cadastrado no sistema\n")

    def cadastrar_usuario(self, usuario: Usuario) -> None:
        if usuario.cpf in self._usuarios:
            print("Já existe um usuário com esse CPF cadastrado no sistema\n")
            return
        self._usuarios[usuario.cpf] = usuario
        print(f"O usuário {usuario.nome} foi cadastrado no sistema\n")

    def buscar_livro_por_isbn(self, isbn: str) -> Livro:
        livro = self._livros.get(isbn)
        if not livro:
            raise LivroNaoEncontradoError(f"Nenhum livro com ISBN {isbn} encontrado\n")
        return livro
    
    def buscar_livros_por_titulo(self, trecho: str) -> list[Livro]:
        resultado = [
            l for l in self._livros.values()
            if trecho.lower() in l.titulo.lower()
        ]
        return resultado
    
    def buscar_usuario(self, cpf: str) -> Usuario:
        usuario = self._usuarios.get(cpf)
        if not usuario:
            raise UsuarioNaoEncontradoError(f"Usuário com CPF {cpf} não encontrado\n")
        return usuario
    
    def emprestar_livro(self, isbn: str, cpf: str) -> None:
        try:
            livro = self.buscar_livro_por_isbn(isbn)
            usuario = self.buscar_usuario(cpf)
            if not livro.disponivel:
                raise LivroIndisponivelError(f"'{livro.titulo}' com ISBN '{livro.isbn}' não está disponível\n")
            livro.disponivel = False
            usuario.livros_emprestados.append(livro)
            print(f"'{livro.titulo}' foi emprestado para {usuario.nome}\n")
        except (LivroNaoEncontradoError, UsuarioNaoEncontradoError, LivroIndisponivelError) as e:
            print(f"{e}\n")

    def devolver_livro(self, isbn: str, cpf: str) -> None:
        try:
            livro = self.buscar_livro_por_isbn(isbn)
            usuario = self.buscar_usuario(cpf)
            if livro not in usuario.livros_emprestados:
                raise LivroNaoEmprestadoError(
                    f"'{livro.titulo}' não está na lista de empréstimos de {usuario.nome}\n"
                )
            livro.disponivel = True
            usuario.livros_emprestados.remove(livro)
            print(f"'{livro.titulo}' foi devolvido por {usuario.nome}\n")
        except (LivroNaoEncontradoError, UsuarioNaoEncontradoError, LivroNaoEmprestadoError) as e:
            print(f"{e}\n")

biblioteca = Biblioteca()
biblioteca.cadastrar_livro(Livro("O Guia do Mochileiro das Galáxias", "Douglas Adams", "955-0"))
biblioteca.cadastrar_livro(Livro("O Guia do Mochileiro das Galáxias", "Douglas Adams", "955-1"))
biblioteca.cadastrar_livro(Livro("O Guia do Mochileiro das Galáxias", "Douglas Adams", "955-1"))
biblioteca.cadastrar_livro(Livro("Casa de Folhas", "Mark Z. Danielewski", "955-1"))
biblioteca.cadastrar_livro(Livro("Casa de Folhas", "Mark Z. Danielewski", "955-2"))
biblioteca.cadastrar_usuario(Usuario("Raul Stafi", "111.111.111-52"))
biblioteca.cadastrar_usuario(Usuario("João Paulo", "111.111.111-52"))
biblioteca.cadastrar_usuario(Usuario("João Paulo", "111.111.111-53"))
biblioteca.emprestar_livro("955-0", "111.111.111-52")
biblioteca.emprestar_livro("955-0", "111.111.111-53")
biblioteca.devolver_livro("955-0", "111.111.111-53")
biblioteca.devolver_livro("955-0", "111.111.111-52")
