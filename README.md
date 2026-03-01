# 📚 Sistema de Biblioteca — Python + OOP
Projeto de gerenciamento de biblioteca desenvolvido em Python com foco na prática de Programação Orientada a Objetos (OOP).

# 📋 Funcionalidades

Cadastrar livros com atribuição automática de localização (estante e prateleira)
Cadastrar usuários
Emprestar livros para usuários cadastrados
Devolver livros
Consultar status de disponibilidade de um livro
Consultar histórico de empréstimos de um usuário
Consultar a localização física de um livro na biblioteca


# 🗂️ Estrutura das Classes
Shelf
└── Bookcase          → representa a localização física de um livro

LibraryItem
└── Book              → herda título e ISBN, adiciona dados autorais e status

User                  → usuário com histórico de empréstimos
Library               → gerencia catálogo, usuários e operações de empréstimo

# ▶️ Como executar

Certifique-se de ter o Python 3 instalado
Clone o repositório
Execute o arquivo principal:

bashpython biblioteca.py
O terminal vai exibir um exemplo completo com cadastro, empréstimo, consulta e devolução.

# 🧪 Exemplo de saída

Livro 'Dom Casmurro' cadastrado com sucesso!
Livro 'Dona Flor e seus Dois Maridos' cadastrado com sucesso!

Usuário 'João Silva' cadastrado com sucesso!
Usuário 'Maria Porto' cadastrado com sucesso!

Livro 'Dom Casmurro' emprestado para João Silva com sucesso!

'Dom Casmurro' | Status: Emprestado
'Dom Casmurro' → Localização: Estante: 1 | Prateleira: 1

Histórico de João Silva - Dom Casmurro

Livro 'Dom Casmurro' devolvido por João Silva com sucesso!
'Dom Casmurro' | Status: Disponível
