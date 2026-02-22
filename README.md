# 📚 Acervo Literário — Sistema de Biblioteca em Python

Sistema de gerenciamento de acervo literário desenvolvido em Python com foco em **Programação Orientada a Objetos (POO)**. O projeto permite cadastrar autores e poetas, registrar livros e organizá-los em estantes de forma estruturada.

---

## 🗂️ Estrutura do Projeto

```
acervo-literario/
│
├── main.py        # Arquivo principal com as classes e execução
└── README.md
```

---

## 🧱 Classes

### `Escritor`
Representa um autor de literatura em prosa.

| Atributo | Descrição |
|---|---|
| `id_autor` | Identificador único do autor |
| `escritor` | Nome do autor |
| `seculo` | Século em que produziu suas obras |
| `origem` | País de origem |
| `genero` | Gênero literário |

---

### `Poeta` *(herda de `Escritor`)*
Especialização de `Escritor` para poetas, com um atributo adicional de movimento poético.

| Atributo | Descrição |
|---|---|
| `estilo_poetico` | Movimento ou estilo poético do autor |

---

### `Livro`
Representa um livro do acervo.

| Atributo | Descrição |
|---|---|
| `id_livro` | Identificador único do livro |
| `nome` | Título do livro |
| `escritor` | Nome do autor |
| `ano` | Ano de lançamento |
| `genero` | Gênero literário |
| `lingua` | Língua original |
| `seculo` | Século de publicação |

---

### `Estante`
Agrupa autores e livros, simulando uma prateleira de biblioteca.

| Método | Descrição |
|---|---|
| `adicionar_autor(autor)` | Adiciona um autor à estante |
| `adicionar_livro(livro)` | Adiciona um livro à estante |
| `mostrar()` | Exibe todos os autores e livros da estante |

---

## ⚙️ Conceitos de POO Aplicados

- **Herança** — `Poeta` estende `Escritor`, aproveitando e especializando seus atributos
- **Encapsulamento** — Atributos protegidos com `_` e acessados via `@property` e `setters`
- **Composição** — `Estante` agrupa objetos de `Escritor`/`Poeta` e `Livro`
- **Polimorfismo** — Cada classe possui seu próprio `__str__` para exibição personalizada

---

## ▶️ Como Executar

1. Clone o repositório:
```bash
git clone https://github.com/seu-usuario/acervo-literario.git
cd acervo-literario
```

2. Execute o arquivo principal:
```bash
python main.py
```

> Nenhuma dependência externa é necessária. Requer apenas **Python 3.6+**.

---

## 💡 Exemplo de Uso

```python
autor1 = Escritor(1, "Machado de Assis", 19, "Brasil", "Romance")
autor2 = Poeta(2, "Carlos Drummond de Andrade", 20, "Brasil", "Poesias", "Modernismo")
livro1 = Livro(1, "Dom Casmurro", "Machado de Assis", 1899, "Romance", "Português", 19)

estante1 = Estante(101)
estante1.adicionar_autor(autor1)
estante1.adicionar_autor(autor2)
estante1.adicionar_livro(livro1)

estante1.mostrar()
```

### Saída esperada:
```
----------------------------
Prateleira: 101

-------------------------------
Autores:
-------------------------------
Autor(ID:1) Nome do Autor: Machado de Assis | Gênero: Romance
Século: 19 | Nacionalidade: Brasil

Autor(ID:2) Nome do Autor: Carlos Drummond de Andrade | Gênero: Poesias
Século: 20 | Nacionalidade: Brasil | Movimento: Modernismo
-------------------------------
Livros:
-------------------------------
Livro(ID:1) Nome do Livro: Dom Casmurro | Nome Autor: Machado de Assis | Gênero: Romance
Ano de Lançamento: 1899 | Século: 19 | Língua: Português
```

---

## 🚀 Possíveis Melhorias Futuras

- Classe `Biblioteca` agrupando múltiplas `Estantes`
- Busca por gênero, século ou nacionalidade
- Persistência de dados com arquivo JSON ou banco de dados
- Interface de linha de comando (CLI) interativa

---

## 🛠️ Tecnologias

![Python](https://img.shields.io/badge/Python-3.6+-blue?logo=python&logoColor=white)

---

## 📄 Licença

Este projeto está sob a licença MIT. Sinta-se livre para usar, modificar e distribuir.
