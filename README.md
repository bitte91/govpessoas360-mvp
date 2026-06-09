# GOVPESSOAS 360 MVP

MVP da Plataforma de Governança, Compliance Trabalhista, Previdenciário e Gestão de Riscos para Municípios.

## Objetivo do MVP

Entregar uma primeira versão funcional para:

- cadastrar organizações públicas;
- importar dados simplificados de servidores;
- calcular índices IGP, ICT, IEP e IMSST;
- registrar riscos trabalhistas, previdenciários e de SST;
- calcular exposição financeira mínima, provável e máxima;
- disponibilizar dashboard executivo simples;
- gerar base para parecer técnico situacional.

## Stack

- Backend: Python + FastAPI
- Banco: PostgreSQL em produção, SQLite para teste local
- Frontend: HTML, CSS e JavaScript
- IA: arquitetura prevista para agentes especializados

## Como executar localmente

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn backend.app.main:app --reload
```

Acesse:

```text
http://127.0.0.1:8000
```

## Estrutura

```text
backend/      API, modelos, regras de cálculo e serviços
frontend/     telas HTML/CSS/JS do MVP
docs/         documentação técnica e funcional
data_samples/ exemplos de dados para teste
scripts/      utilitários de carga e setup
```

## Aviso

Este MVP não substitui parecer jurídico, auditoria formal, laudo de SST ou cálculo atuarial oficial. Ele organiza dados, calcula indicadores gerenciais e apoia diagnóstico técnico preliminar.
