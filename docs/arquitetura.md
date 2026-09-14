# Arquitetura - Medical Triage MLOps

## 1. Visão Geral

Este documento descreve a arquitetura do sistema `medical-triage-mlops`, um projeto de Machine Learning Ops voltado para a construção de um pipeline completo de treinamento, avaliação e deployment de um modelo de classificação de laudos médicos para suporte à triagem clínica.

O sistema foi projetado para:

- classificar textos médicos em categorias de risco, como normal, atenção e urgente;
- garantir reprodutibilidade do processo de treinamento;
- versionar dados, artefatos e modelos;
- facilitar o deploy da inferência via API;
- oferecer rastreamento de experimentos e métricas;
- permitir observabilidade e monitoramento do serviço em produção.

---

## 2. Objetivo do Sistema

O projeto tem como objetivo principal implementar uma solução de inteligência artificial aplicada à triagem médica, usando dados clínicos em formato textual para apoiar a classificação de risco. O foco principal é:

- classificação automática de laudos clínicos;
- pipeline automatizado de ML;
- rastreamento de experimentos e métricas;
- versionamento de dados e modelos;
- deploy simples, reproduzível e escalável do serviço de inferência.

A arquitetura foi pensada para ser modular, reproduzível e compatível com as melhores práticas de MLOps.

---

## 3. Contexto de Negócio

O cenário de negócio é um ambiente hospitalar ou de atendimento clínico, onde laudos e resumos médicos precisam ser avaliados rapidamente para auxiliar decisões de prioridade. Nesse contexto, o sistema pode ser usado para:

- identificar laudos com risco baixo, moderado ou alto;
- apoiar a definição de prioridade na triagem inicial;
- reduzir a carga de trabalho manual da equipe;
- padronizar a análise de textos clínicos em escala.

Os textos médicos podem incluir descrições de sintomas, observações de enfermagem, histórico clínico e achados relevantes que influenciam a classificação da condição.

---

## 4. Princípios de Arquitetura

A arquitetura foi concebida com base nos seguintes princípios:

- Reprodutibilidade: todo o pipeline deve ser executável de forma consistente.
- Versionamento: dados, código, parâmetros e modelos devem ser rastreados.
- Modularidade: cada etapa do pipeline é isolada e substituível.
- Observabilidade: métricas, artefatos e experimentos devem ser acompanhados.
- Portabilidade: o projeto deve ser executável localmente e em containers.
- Manutenibilidade: o código deve seguir boas práticas de organização e testes.

---

## 5. Arquitetura de Alto Nível

```text
┌──────────────────────────────────────────────────────────────────────┐
│                    MEDICAL TRIAGE MLOPS PIPELINE                     │
├──────────────────────────────────────────────────────────────────────┤
│                                                                      │
│  ┌───────────────────────────────────────────────────────────────┐   │
│  │                    CAMADA DE DADOS                          │   │
│  │  Raw Data → Processed Data → Features                     │   │
│  └───────────────────────────────────────────────────────────────┘   │
│                                │                                     │
│                                ▼                                     │
│  ┌───────────────────────────────────────────────────────────────┐   │
│  │                 CAMADA DE PIPELINE (DVC / STAGES)            │   │
│  │  Preprocess → Feature Engineering → Train → Evaluate       │   │
│  └───────────────────────────────────────────────────────────────┘   │
│                                │                                     │
│                                ▼                                     │
│  ┌───────────────────────────────────────────────────────────────┐   │
│  │                  CAMADA DE MODELO                           │   │
│  │    TF-IDF + Logistic Regression + ONNX + Artifacts         │   │
│  └───────────────────────────────────────────────────────────────┘   │
│                                │                                     │
│                                ▼                                     │
│  ┌───────────────────────────────────────────────────────────────┐   │
│  │                  CAMADA DE SERVIÇO                          │   │
│  │      FastAPI → /health → /predict → Triage Result         │   │
│  └───────────────────────────────────────────────────────────────┘   │
│                                │                                     │
│                                ▼                                     │
│  ┌───────────────────────────────────────────────────────────────┐   │
│  │               CAMADA DE OBSERVABILIDADE                    │   │
│  │     MLflow + Metrics + Logs + Prometheus + Grafana        │   │
│  └───────────────────────────────────────────────────────────────┘   │
│                                                                      │
└──────────────────────────────────────────────────────────────────────┘
```

---

## 6. Componentes Principais

### 6.1 Camada de Dados
A camada de dados é responsável por armazenar e preparar os registros clínicos utilizados no treinamento do modelo.

Estrutura esperada:

- `data/raw`: dados brutos de entrada;
- `data/processed`: dados já preparados para treinamento;
- artefatos e features geradas ao longo do pipeline.

Arquivos e fontes principais:

- `medical_tc_train.csv`
- `medical_tc_test.csv`
- `medical_tc_labels.csv`

Esses dados são usados para treinar, validar e avaliar a capacidade do modelo de classificar textos médicos conforme a categoria de risco.

O versionamento e a reprodução do pipeline podem ser apoiados por DVC, permitindo rastrear alterações nos datasets e reexecutar o processo de forma consistente.

### 6.2 Camada de Pipeline
O pipeline é organizado em estágios bem definidos, seguindo o fluxo:

- preprocessamento;
- engenharia de features;
- treinamento;
- avaliação.

Os arquivos principais desta camada estão localizados em:

- `src/stages/preprocess.py`
- `src/stages/feature_eng.py`
- `src/stages/train.py`
- `src/stages/evaluate.py`

Esse design favorece a separação de responsabilidades e facilita a manutenção e a evolução do pipeline.

### 6.3 Camada de Modelo
O modelo principal é um classificador textual baseado em vetorização TF-IDF e regressão logística, com foco em previsibilidade e baixo custo operacional.

Características esperadas:

- representação textual por TF-IDF;
- modelo linear para classificação de risco;
- artefatos persistidos para reutilização;
- conversão para ONNX para otimização de inferência.

O modelo é salvo em artefatos da pasta `models` e também convertido para `model.onnx`, permitindo execução mais eficiente em inferência via ONNX Runtime.

### 6.4 Camada de Serviço
A camada de inferência é exposta por uma API REST usando FastAPI.

Principais responsabilidades:

- disponibilizar endpoints de saúde;
- receber laudos médicos em texto;
- validar entradas com Pydantic;
- realizar inferência usando o modelo otimizado;
- retornar a classe de risco e a confiança da predição.

Arquivos principais:

- `src/api/main.py`
- `src/api/schemas.py`

A API é o ponto de entrada para servir o modelo em ambientes locais, testes e produção leve.

### 6.5 Camada de Observabilidade
A observabilidade do projeto é baseada em:

- logs estruturados;
- métricas de latência e requisições;
- rastreamento de experimentos com MLflow;
- monitoramento de API com Prometheus;
- visualização em Grafana.

Essa camada permite acompanhar:

- como o modelo está sendo usado;
- qual versão foi servida;
- qual foi a latência média da inferência;
- se a API está estável e disponível.

---

## 7. Fluxo de Execução do Pipeline

### 7.1 Fluxo de Dados
O fluxo de dados segue esta ordem:

1. Dados brutos são carregados em `data/raw`.
2. O estágio de preprocessamento prepara e estrutura as informações.
3. O estágio de feature engineering transforma os dados em representações úteis para o modelo.
4. O estágio de treinamento gera um modelo classificador.
5. O estágio de avaliação produz métricas e artefatos.
6. A API consome o modelo treinado para inferência.

### 7.2 Fluxo de Treinamento
O ciclo de treinamento é composto por:

- definição de parâmetros;
- leitura dos dados processados;
- construção do modelo;
- treinamento do classificador;
- avaliação do resultado;
- persistência do modelo, vetor e métricas.

### 7.3 Fluxo de Inferência
O fluxo de inferência é:

1. a API recebe uma requisição com o texto clínico;
2. os dados são validados;
3. o modelo é carregado em memória;
4. a predição é realizada;
5. o resultado é retornado em formato JSON com o label e a probabilidade.

---

## 8. Estrutura de Diretórios

```text
medical-triage-mlops/
├── .dvc/                     # Configuração do DVC
├── .github/                  # Workflows de CI/CD
├── airflow/                  # DAGs de orquestração
│   └── dags/
├── data/
│   └── raw/                  # Dados brutos
├── docs/                     # Documentação técnica
├── metrics/                  # Métricas e artefatos
├── models/                   # Modelos convertidos e artefatos finais
├── monitoring/               # Configuração de Prometheus / Grafana
├── notebooks/                # EDA e análise exploratória
├── src/
│   ├── api/                  # API FastAPI
│   ├── models/               # Conversão e inferência de modelo
│   ├── stages/               # Pipeline de ML
│   └── utils/                # Utilitários
├── tests/                    # Testes unitários e de integração
├── Dockerfile                # Container da aplicação
├── docker-compose.monitoring.yml
├── dvc.yaml                  # Definição do pipeline DVC
├── main.py                   # Entry point da aplicação
├── pyproject.toml            # Dependências do projeto
├── README.md                 # Documentação principal
└── .gitignore
```

---

## 9. Tecnologias Utilizadas

O projeto utiliza uma stack moderna para apoiar o ciclo de vida completo de ML:

- Python 3.12
- scikit-learn para treinamento do modelo
- FastAPI para serving da inferência
- Pydantic para validação de schemas
- DVC para versionamento de dados e pipeline
- MLflow para rastreamento de experimentos
- ONNX e ONNX Runtime para otimização de latência
- Docker e Docker Compose para containerização
- Apache Airflow para orquestração
- Prometheus + Grafana para observabilidade
- pytest e Ruff para testes e qualidade de código

---

## 10. Decisões de Arquitetura

### 10.1 Pipeline Modular
A divisão em estágios permite separar claramente:

- ingestão e limpeza;
- engenharia de features;
- treinamento;
- avaliação;
- deploy.

Isso reduz acoplamento e facilita a evolução do projeto.

### 10.2 Versionamento de Dados e Modelo
Com DVC e MLflow, o projeto consegue:

- rastrear alterações em datasets;
- reproduzir experimentos;
- associar métricas a versões específicas;
- garantir reprodutibilidade do processo.

### 10.3 API para Inferência
A API é um componente separado, permitindo:

- servir o modelo independentemente do treinamento;
- isolar a lógica de inferência;
- facilitar integração com outros serviços ou aplicações.

### 10.4 Otimização de Latência
A conversão do modelo para ONNX permite reduzir o custo computacional da inferência e melhorar a performance do serviço em cenários com maior demanda.

### 10.5 Containerização
A containerização permite:

- execução uniforme em diferentes ambientes;
- simplificação do deploy;
- isolamento de dependências e versões.

---

## 11. Requisitos Não Funcionais

A arquitetura foi concebida para atender requisitos importantes de sistemas de ML:

- Reprodutibilidade: o mesmo pipeline deve produzir resultados consistentes.
- Escalabilidade: a solução pode evoluir para tratar volumes maiores.
- Manutenibilidade: o código deve ser organizado e compreensível.
- Observabilidade: o sistema deve permitir monitoramento de pipeline e API.
- Portabilidade: execução local e em container deve ser viável.
- Testabilidade: os módulos devem ser facilmente testáveis.

---

## 12. Segurança e Governança

Algumas boas práticas recomendadas para o projeto incluem:

- não armazenar segredos em código;
- usar variáveis de ambiente para configurações sensíveis;
- controlar acesso aos artefatos do modelo;
- registrar versões de modelo e dados de forma auditável;
- manter dependências atualizadas e verificadas.

Como o sistema está ligado a dados clínicos e decisões de triagem, a governança e o rastreio também são fundamentais para garantir confiabilidade e rastreabilidade dos resultados.

---

## 13. Pontos de Evolução

A arquitetura atual já é sólida para um MVP de MLOps em saúde, mas pode evoluir para cenários mais robustos:

- retraining automatizado e agendado;
- pipeline de deploy mais integrado com CI/CD;
- monitoramento de drift e qualidade de dados;
- deploy em ambiente cloud com orquestração mais robusta;
- expansão de métricas para análise clínica e de negócio;
- uso de modelos mais sofisticados para classificação semântica.

---

## 14. Resumo Executivo

A arquitetura do projeto `medical-triage-mlops` organiza o ciclo de vida de um sistema de classificação de risco clínico em camadas bem definidas:

- dados;
- pipeline de ML;
- treinamento de modelo;
- inferência via API;
- observabilidade e rastreamento.

Essa estrutura permite desenvolver uma solução com foco em reprodutibilidade, modularidade, rastreabilidade e escalabilidade, alinhada com boas práticas de MLOps.

---

## 15. Conclusão

Este projeto representa uma base sólida para um sistema de triagem médica em produção, com separação clara entre etapas de dados, treinamento, avaliação e inferência. A arquitetura proposta oferece um caminho natural para evolução, desde um ambiente local e controlado até um cenário mais próximo de produção, mantendo foco em qualidade, observabilidade e desempenho.