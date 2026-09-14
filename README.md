![Descrição da imagem](docs/img/mlops_banner.png)

# 🩺 Medical Triage MLOps

Projeto de Machine Learning Ops para classificação automatizada de laudos médicos com foco em triagem clínica e priorização de risco.

Resumo rápido (Vídeo Explicativo):  [Vídeo Resumo do Sistema de Recomendação.]()

## 🎯 Visão Geral

Este repositório implementa um pipeline completo de MLOps para classificação textual de dados clínicos. A solução foi concebida para:

- preprocessar e organizar dados médicos em formato adequado para treinamento;
- treinar um classificador para classificar textos clínicos por nível de risco;
- registrar experimentos, métricas e artefatos com MLflow;
- exportar o modelo para ONNX para otimizar inferência;
- servir predições por meio de uma API REST em FastAPI;
- monitorar a aplicação com Prometheus e Grafana;
- automatizar validações e pipeline de CI/CD.

A proposta do projeto combina boas práticas de MLOps, NLP e deployment de modelos em ambientes de produção leve.

---

👥 Integrante: Eduardo Marafigo Kaiser | RM370237

---

## 🏁 Objetivo do Projeto

O objetivo principal do sistema é apoiar a triagem médica por meio de uma classificação automatizada do conteúdo textual de laudos e descrições clínicas. O modelo tenta inferir a gravidade ou prioridade da condição com base em textos de entrada, ajudando a organizar e priorizar atendimentos clínicos.

## 🏛️ Arquitetura

A arquitetura do projeto foi estruturada em camadas bem definidas:

- dados e artefatos;
- pipeline de preprocessamento e treinamento;
- model registry e métricas;
- serviço de inferência;
- observabilidade e monitoramento;
- automação e validação.

Para detalhes completos, consulte:

- [docs/arquitetura.md](docs/arquitetura.md)
- [docs/action_plan.md](docs/action_plan.md)
- [docs/model_card.md](docs/model_card.md)

## 🛠️ Stack Tecnológica

- 🐍 Python 3.12
- ⚡ FastAPI
- 🛡️ Pydantic
- 🔬 scikit-learn
- 📊 MLflow
- ⚡ ONNX Runtime
- 🌬️ Airflow
- 🐳 Docker
- 🐳 Docker Compose
- 🔥 Prometheus
- 📊 Grafana
- 🧪 pytest
- 🧹 Ruff
- 📦 DVC
- ⚡ uv

## 📂 Estrutura do Repositório

```text
medical-triage-mlops/
├── .github/
│   └── workflows/
│       └── ci.yml
├── airflow/
│   └── dags/
│       └── training_dag.py
├── data/
│   └── raw/
│       ├── medical_tc_labels.csv
│       ├── medical_tc_test.csv
│       └── medical_tc_train.csv
├── docs/
│   ├── action_plan.md
│   ├── arquitetura.md
│   ├── model_card.md
│   └── tech_challenge_spec.md
├── monitoring/
│   └── prometheus/
│       └── prometheus.yml
├── src/
│   ├── api/
│   │   ├── main.py
│   │   └── schemas.py
│   ├── models/
│   │   ├── convert_to_onnx.py
│   │   └── predict.py
│   ├── stages/
│   │   ├── evaluate.py
│   │   ├── feature_eng.py
│   │   ├── preprocess.py
│   │   └── train.py
│   └── utils/
│       └── validate_env.py
├── tests/
│   ├── test_api.py
│   ├── test_data_validation.py
│   ├── test_model.py
│   ├── test_preprocessing.py
│   ├── test_sanity.py
│   └── test_utils.py
├── Dockerfile
├── docker-compose.monitoring.yml
├── dvc.yaml
├── main.py
├── pyproject.toml
├── README.md
└── models/
    └── model.onnx
```

## Pipeline de ML

O pipeline do projeto segue uma lógica organizada em estágios:

1. ingestão dos dados brutos;
2. preprocessamento e limpeza textual;
3. engenharia de features;
4. treinamento do modelo;
5. avaliação de performance;
6. exportação do modelo para ONNX;
7. serviço de inferência pela API;
8. monitoramento de métricas e disponibilidade.

A estrutura de treino e avaliação é organizada em módulos dentro de `src/stages` e o processo de execução pode ser disparado com DVC ou diretamente via scripts.

## � Como Rodar o Projeto

### 1. Clonar o repositório

```bash
git clone https://github.com/<seu-usuario>/medical-triage-mlops.git
cd medical-triage-mlops
```

### 2. Criar ambiente virtual

Este projeto usa `uv` como gerenciador principal.

```bash
uv pip install --system -e .
```

Ou, caso prefira usar ambiente isolado:

```bash
uv venv
source .venv/bin/activate
uv pip install -e .
```

### 3. Reproduzir pipeline

```bash
uv run dvc repro
```

Esse comando executa o pipeline de dados e treinamento e gera os artefatos necessários.

## ⚙️ Executando a API

### Modo local

```bash
uvicorn src.api.main:app --host 0.0.0.0 --port 8000 --reload
```

### Endpoint de saúde

```bash
curl http://localhost:8000/health
```

### Predição

```bash
curl -X POST "http://localhost:8000/predict" \
  -H "Content-Type: application/json" \
  -d '{"abstract":"Paciente apresenta febre, dor torácica e dispneia, com desconforto respiratório progressivo."}'
```

## 🐳 Docker

A aplicação pode ser executada em container com o Dockerfile do projeto.

```bash
docker build -t medical-triage-api:latest .
docker run -p 8000:8000 medical-triage-api:latest
```

## 📊 Monitoramento

A stack de observabilidade é configurada com Prometheus e Grafana por meio do arquivo:

- [docker-compose.monitoring.yml](docker-compose.monitoring.yml)

Para subir a stack:

```bash
docker compose -f docker-compose.monitoring.yml up -d
```

Acesso:

- Prometheus: http://localhost:9090
- Grafana: http://localhost:3000

## 📈 MLflow

O rastreamento de experimentos e artefatos é feito com MLflow. O projeto já registra métricas e artefatos relevantes durante treino e avaliação.

## 🧪 Testes

Para rodar os testes do projeto:

```bash
uv run pytest
```

Também há checagem de qualidade via Ruff:

```bash
uv run ruff check .
```

## 🔄 CI/CD

O fluxo de integração contínua está em:

- [.github/workflows/ci.yml](.github/workflows/ci.yml)

A pipeline executa:

- checkout do repositório;
- configuração do Python;
- instalação das dependências;
- reprodução do pipeline DVC;
- lint com Ruff;
- execução de testes com pytest;
- build da imagem Docker.

## 📁 Dados e Artefatos

Os dados principais ficam em `data/raw` e os artefatos do modelo em `models/`.

Também há uso de MLflow para registrar métricas e experimentos, além da conversão do modelo para ONNX para performance de inferência.

## ✅ Qualidade e Boas Práticas

O projeto já incorpora alguns princípios importantes de MLOps:

- separação por módulos e responsabilidades;
- automação do pipeline;
- rastreabilidade de experimentos;
- versionamento de artefatos;
- deploy em container;
- monitoramento da API;
- testes automatizados.

## ☁️ Estratégia de Deploy em Nuvem (Batch vs. Real-time)

Para este cenário, a estratégia mais adequada depende do modo de uso do sistema de triagem médica.

### 1. Cenário real-time

O uso em tempo real faz sentido quando o sistema precisa responder rapidamente a laudos ou textos clínicos em uma interface operacional, como:

- triagem assistida em um painel clínico;
- atendimento em tempo real por equipe médica;
- integração com sistemas hospitalares ou plataformas de prontuário eletrônico.

Nesse caso, a melhor abordagem é servir o modelo como API REST, com baixa latência e disponibilidade contínua. A solução mais adequada é:

- Azure: excelente opção se a organização já trabalha com ecosistema Microsoft, especialmente quando há integração com Azure ML, Azure Container Apps, Azure Kubernetes Service e monitoramento via Azure Monitor.
- AWS: também é uma alternativa muito forte, com ECS, EKS, Lambda, SageMaker e API Gateway. É especialmente interessante quando a infraestrutura já é baseada em serviços AWS.
- GCP: uma boa escolha para ambientes orientados a dados e machine learning, com Vertex AI, Cloud Run e Kubernetes Engine.

No cenário de triagem médica em tempo real, a recomendação prática seria usar uma API em contêineres, implantada em um serviço gerenciado como Azure Container Apps, AWS ECS, ou GCP Cloud Run, com modelo ONNX em produção e monitoramento contínuo.

### 2. Cenário batch

O processamento em batch faz sentido quando a classificação é feita em lote, por exemplo:

- processar uma grande quantidade de laudos em intervalos definidos;
- realizar triagem posterior em arquivos ou bases históricas;
- executar retraining ou análise periódica de grande volume.

Nesse caso, a arquitetura ideal é baseada em jobs agendados e processamento assíncrono, com filas e jobs em núvem. A escolha mais natural seria:

- Azure: Azure Batch, Azure Data Factory, Azure Functions ou Azure ML Pipelines;
- AWS: AWS Batch, Step Functions, Glue ou SageMaker Pipelines;
- GCP: Cloud Run Jobs, Dataflow, Vertex AI Pipelines.

### 3. Recomendação para este projeto

Este projeto combina duas necessidades:

- uma API de predição em tempo real para uso operacional;
- um pipeline de treinamento e reprocessamento mais estruturado para automatizar ciclos de retraining.

Por isso, a estratégia mais equilibrada para este cenário é uma arquitetura híbrida:

- real-time: API REST em contêineres para inferência e baixa latência;
- batch: jobs agendados para treinamento, retraining, processamento de dados e validação periódica.

Nesse modelo, a melhor opção dependerá do ecossistema da organização:

- se a empresa já usa Microsoft Azure, a solução mais natural é Azure Container Apps + Azure ML + Azure Monitor;
- se a empresa usa AWS, a melhor arquitetura seria ECS/EKS + SageMaker + CloudWatch;
- se a empresa está mais focada em solução data-first, o GCP com Cloud Run/Vertex AI é uma alternativa muito competitiva.

### 4. Conclusão

Para o cenário de triagem médica, a recomendação geral é:

- priorizar um deploy real-time para a inferência operacional em API;
- manter o pipeline de treinamento e reprocessamento em batch ou agendado;
- usar um provedor cloud compatível com o ecossistema já adotado pela organização e com a necessidade de observabilidade e escalabilidade.

Em termos práticos, a escolha mais sólida para este projeto é uma arquitetura híbrida em nuvem, com API em produção para inferência e jobs batch para treinamento e retraining. Entre AWS, Azure e GCP, a escolha final deve ser guiada pela infraestrutura existente, custos e integração com serviços de monitoramento e MLOps.

## 🗺️ Roadmap

Alguns próximos passos relevantes para evoluir o projeto incluem:

- consolidar documentação de arquitetura e setup;
- expandir a pipeline de monitoramento com dashboards específicos;
- realizar benchmarks de latência entre modelo base e ONNX;
- validar a performance em dados reais de produção;
- melhorar a robustez do pipeline de retraining;
- evoluir para etapas mais avançadas de NLP e classificação clínica.

## Licença

Este projeto foi desenvolvido como parte de um desafio acadêmico / técnico e pode ser adaptado conforme a necessidade do usuário ou da equipe responsável.

## Contribuição

Contribuições são bem-vindas. Para propor melhorias, abra uma issue ou envie um pull request com a descrição do que foi ajustado e por quê.

## Contato

Para dúvidas ou sugestões sobre o projeto, consulte a documentação e os arquivos do repositório ou entre em contato com a equipe responsável pelo desenvolvimento.

---

## 🧠 Observações Finais

Este projeto representa uma base sólida para a construção de uma solução MLOps aplicada à saúde, com foco em automação, observabilidade, rastreabilidade e performance de inferência. Ele oferece uma estrutura adequada para continuar evoluindo em direção a um ambiente mais próximo de produção.
