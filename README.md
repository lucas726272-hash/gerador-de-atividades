# Gerador de Atividades de Português

Aplicação web para professores criarem folhas de atividades em português para o ensino fundamental (1º ao 5º ano), com geração automática de exercícios, desafio final e exportação em PDF A4.

## Funcionalidades

- Seleção de **ano escolar**, **tema** e **nível de dificuldade**.
- Geração de **10 exercícios automáticos** + **1 desafio final**.
- Inclusão de **ilustrações infantis** (ícones/cartoon).
- Layout com:
  - título,
  - instruções,
  - espaço para nome e data,
  - estilo otimizado para impressão.
- Exportação com botão **Baixar PDF (A4)**.
- Botão de **Regenerar exercícios** com um clique.

## Estrutura do projeto

```text
.
├── app/
│   ├── generator.py      # Regras e banco de modelos de exercícios
│   ├── main.py           # FastAPI + rotas HTML/API/PDF
│   └── models.py         # Modelos Pydantic e enums
├── static/
│   ├── css/style.css     # Estilo moderno + impressão A4
│   └── js/app.js         # Interações frontend e chamadas API
├── templates/
│   └── index.html        # Página principal
├── requirements.txt
└── README.md
```

## Como executar localmente

1. Crie e ative um ambiente virtual:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

2. Instale as dependências:

```bash
pip install -r requirements.txt
```

3. Execute o servidor:

```bash
uvicorn app.main:app --reload
```

4. Abra no navegador:

- http://127.0.0.1:8000

## Endpoints úteis

- `GET /` — interface web.
- `POST /api/generate` — gera worksheet em JSON.
- `POST /api/export-pdf` — recebe worksheet e retorna PDF para download.
