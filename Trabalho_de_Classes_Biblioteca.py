"""=== Sistema de Biblioteca ===
1. Cadastrar livro
2. Cadastrar usuário
3. Emprestar livro
4. Devolver livro
0. Sair

Escolha uma opção: _"""

# ============================================================
# CLASSES UM
# ============================================================

class Shelf:
    def __init__(self, shelf_number):
        self._shelf_number = shelf_number
    def __str__(self):
        return f"Estante: {self._shelf_number}"

class Bookcase(Shelf):
    def __init__(self, shelf_number, row):
        super().__init__(shelf_number)
        self._row = row
    def __str__(self):
        return f"Estante: {self._shelf_number} | Prateleira: {self._row}"  # ← herdando _shelf_number do pai

# ============================================================
# CLASSES DOIS
# ============================================================

class LibraryItem:
    """Classe base para qualquer item que uma biblioteca pode guardar."""
    def __init__(self, title, isbn):
        self._title = title     # título do item
        self._isbn = isbn       # código internacional de registro de livro

    def __str__(self):
        return f"Item: {self._title} | ISBN: {self._isbn}"

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value

    @property
    def isbn(self):
        return self._isbn

    @isbn.setter
    def isbn(self, value):
        self._isbn = value


class Book(LibraryItem):
    """Livro é um ItemBiblioteca, com dados autorais e status de disponibilidade."""
    def __init__(self, title, isbn, author, year, genre, language, century):
        super().__init__(title, isbn)
        self._author = author       # nome do autor
        self._year = year           # ano de publicação
        self._isbn = isbn           # código internacional de registro de livro
        self._genre = genre         # gênero literário
        self._language = language   # língua original
        self._century = century     # século de publicação
        self._available = True      # True = disponível, False = emprestado
        self._location = None       # localização na estante/prateleira

    def __str__(self):
        status_text = "Disponível" if self._available else "Emprestado"
        return (f"Livro: {self._title} | ISBN: {self._isbn} | Autor: {self._author} | Gênero: {self._genre}\n"
                f"Ano: {self._year} | Século: {self._century} | Língua: {self._language} | Status: {status_text}\n"
                f"Localização: {self._location}")

    def is_available(self):
        return self._available

    def lend(self):
        self._available = False     # marca como emprestado

    def return_book(self):
        self._available = True      # marca como disponível

    @property
    def author(self):
        return self._author

    @property
    def available(self):
        return self._available

    @property
    def location(self):
        return self._location

    @location.setter
    def location(self, value):
        self._location = value

# ============================================================
# CLASSES DE USUÁRIO E BIBLIOTECA
# ============================================================

class User:
    """Representa um usuário cadastrado na biblioteca."""
    def __init__(self, user_id, name):
        self._user_id = user_id                 # id do usuário
        self._name = name                       # nome do usuário
        self._loan_history = []                 # lista de livros emprestados

    def __str__(self):
        return f"Usuário(ID:{self._user_id}) Nome: {self._name}"

    @property
    def user_id(self):
        return self._user_id

    @property
    def name(self):
        return self._name

    def add_loan(self, book):
        """Adiciona um livro ao histórico de empréstimos do usuário."""
        self._loan_history.append(book)

    def remove_loan(self, book):
        """Remove um livro do histórico ao devolvê-lo."""
        if book in self._loan_history:
            self._loan_history.remove(book)

    def check_history(self):
        """Exibe todos os livros já emprestados pelo usuário."""
        if not self._loan_history:
            print(f"{self._name} não possui empréstimos ativos.")
        else:
            for book in self._loan_history:
                print(f"Histórico de {self._name} - {book.title}")

class Library:
    """Gerencia o acervo de livros, a localização atribuída automaticamente e os usuários cadastrados."""
    MAX_ROWS_PER_SHELF = 5  # quantas prateleiras por estante
    
    def __init__(self):
        self._catalog = []
        self._users = []
        self._current_shelf = 1   # estante atual
        self._current_row = 1     # prateleira atual

    def _next_location(self):
        location = Bookcase(self._current_shelf, self._current_row)

        self._current_row += 1
        if self._current_row > self.MAX_ROWS_PER_SHELF:
            self._current_row = 1
            self._current_shelf += 1

        return location

    def add_book(self, book):
        """Adiciona um livro ao catálogo e atribui localização."""
        book.location = self._next_location()
        self._catalog.append(book)
        print(f"Livro '{book.title}' cadastrado com sucesso!")

    def register_user(self, user):
        """Cadastra um usuário na biblioteca."""
        self._users.append(user)
        print(f"Usuário '{user.name}' cadastrado com sucesso!")

    # --- Métodos auxiliares privados para busca ---

    def _find_book(self, isbn):
        """Busca um livro pelo ISBN. Retorna o objeto ou None."""
        for book in self._catalog:
            if book.isbn == isbn:
                return book
        return None

    def _find_user(self, user_id):
        """Busca um usuário pelo ID. Retorna o objeto ou None."""
        for user in self._users:
            if user.user_id == user_id:
                return user
        return None

    # --- Emprestar livro ---

    def lend_book(self, isbn, user_id):
        """Empresta um livro a um usuário, se disponível."""
        book = self._find_book(isbn)
        user = self._find_user(user_id)

        if not book:
            print("Livro não encontrado no catálogo.")
            return
        if not user:
            print("Usuário não encontrado.")
            return
        if not book.is_available():
            print(f"O livro '{book.title}' está indisponível no momento.")
            return

        book.lend()             # marca como emprestado
        user.add_loan(book)     # registra no histórico do usuário
        print(f"Livro '{book.title}' emprestado para {user.name} com sucesso!")


    # --- Devolver livro ---

    def return_book(self, isbn, user_id):
        """Registra a devolução de um livro por um usuário."""
        book = self._find_book(isbn)
        user = self._find_user(user_id)

        if not book:
            print("Livro não encontrado.")
            return
        if not user:
            print("Usuário não encontrado.")
            return
        if book.is_available():
            print(f"O livro '{book.title}' já foi devolvido.")
            return
        
        book.return_book()          # marca como disponível
        user.remove_loan(book)      # remove do histórico ativo
        print(f"Livro '{book.title}' devolvido por {user.name} com sucesso!")

    # --- Consultar status do livro ---

    def check_book_status(self, isbn):
        """Exibe o status de disponibilidade de um livro."""
        book = self._find_book(isbn)
        if not book:
            print("Livro não encontrado.")
            return
        status = "Disponível" if book.is_available() else "Emprestado"
        print(f"'{book.title}' | Status: {status}")

    def check_user_history(self, user_id):
        """Exibe o histórico de empréstimos de um usuário."""
        user = self._find_user(user_id)
        if not user:
            print("Usuário não encontrado.")
            return
        user.check_history()

    def check_book_location(self, isbn):
        """Exibe a localização física do livro na biblioteca."""
        book = self._find_book(isbn)
        if not book:
            print("Livro não encontrado.")
            return
        print(f"'{book.title}' → Localização: {book.location}")



# ============================================================
# INSTÂNCIAS DE EXEMPLO
# ============================================================

library = Library()

user1 = User(1, "João Silva")
user2 = User(2, "Maria Porto")
book1 = Book("Dom Casmurro", "978-0-00-001", "Machado de Assis", 1899, "Romance", "Português", 19)
book2 = Book("Dona Flor e seus Dois Maridos", "978-0-00-002", "Jorge Amado", 1966, "Romance", "Português", 20)

print()

# Cadastro
library.add_book(book1)
print()
library.add_book(book2)
print()
library.register_user(user1)
print()
library.register_user(user2)

print()

# Empréstimo
library.lend_book("978-0-00-001", 1)
print()
library.lend_book("978-0-00-002", 2)

print()

# Consultar status
library.check_book_status("978-0-00-001")   # → Emprestado
library.check_book_status("978-0-00-002")   # → Emprestado

print()

# Histórico
library.check_user_history(1)
print()
library.check_user_history(2)
print()

# Devolução
library.return_book("978-0-00-001", 1)
print()
library.return_book("978-0-00-002", 2)

print()

# Consultar status novamente
library.check_book_status("978-0-00-001")   # → Disponível
print()
library.check_book_status("978-0-00-002")   # → Disponível

print()

# Consultar localização dos livros
library.check_book_location("978-0-00-001")
print()
library.check_book_location("978-0-00-002")



