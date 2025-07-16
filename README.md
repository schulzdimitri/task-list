# Task List - Gerenciador de Tarefas

Um simples gerenciador de tarefas em linha de comando desenvolvido em Python.

## 📋 Funcionalidades

- Adicionar novas tarefas
- Visualizar lista de tarefas
- Atualizar nome das tarefas
- Marcar tarefas como concluídas
- Remover tarefas concluídas
- Interface interativa via terminal

## 🛠️ Tecnologias Utilizadas

- **Python 3.x** - Linguagem de programação principal
- **Bibliotecas padrão do Python** - Não requer dependências externas

## 🏗️ Padrões de Projeto

- **Static Methods** - Implementação de métodos estáticos na classe `Task`
- **Estrutura Modular** - Separação de responsabilidades entre `main.py` e `src/task.py`
- **Type Hints** - Tipagem explícita para melhor legibilidade do código

## ⚙️ Setup e Configuração

### Pré-requisitos

- Python 3.8+ instalado no sistema

### Instalação e Execução

1. Clone o repositório:

```bash
git clone <url-do-repositorio>
cd task-list
```

2. Execute o programa:

```bash
python main.py
```

## 📁 Estrutura do Projeto

```
task-list/
├── main.py          # Arquivo principal com menu e lógica de interação
├── src/
│   └── task.py      # Classe Task com métodos de gerenciamento
└── README.md        # Documentação do projeto
```

## 📝 Exemplo de Uso

```
Menu do Gerenciador de Tarefas

1 - Adicionar Tarefa
2 - Ver Tarefas
3 - Atualizar Tarefa
4 - Completar Tarefa
5 - Deletar tarefas concluídas
6 - Sair

Digite a opção desejada: 1
Digite o nome da tarefa: Estudar Python
Tarefa 'Estudar Python' adicionada com sucesso!
```

## 🚧 Próximos Passos

### Implementação de Interface Web com Flask

O projeto tem como próximo objetivo migrar da interface de linha de comando para uma aplicação web moderna:

#### Tecnologias Planejadas

- **Flask** - Framework web para Python
- **HTML/CSS/JavaScript** - Frontend da aplicação
- **Bootstrap** - Framework CSS para interface responsiva
- **SQLite** - Banco de dados para persistência das tarefas

#### Funcionalidades Web Planejadas

- Interface web intuitiva e responsiva
- Persistência de dados em banco de dados
- API REST para operações CRUD
- Deploy em plataforma de hospedagem (Heroku, Vercel, etc.)

#### Estrutura Futura do Projeto

```
task-list-web/
├── app.py              # Aplicação Flask principal
├── models/
│   └── task_model.py   # Modelo de dados da tarefa
├── routes/
│   └── task_routes.py  # Rotas da API REST
├── templates/
│   ├── base.html       # Template base
│   └── index.html      # Página principal
├── static/
│   ├── css/
│   ├── js/
│   └── img/
├── requirements.txt    # Dependências do projeto
└── README.md
```

#### Comandos de Setup Futuros

```bash
# Instalar dependências
pip install -r requirements.txt

# Executar aplicação Flask
python app.py

# Acesso via navegador
http://localhost:5000
```
