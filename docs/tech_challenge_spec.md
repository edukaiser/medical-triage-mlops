# Especificações do Tech Challenge - Fase 3 (MLET)

## 📌 Contexto e Tema Central
* **Tema**: Deploy de Modelo em Produção com Pipeline CI/CD, Monitoramento e Otimização de Latência.
* **Cenário**: Sistema hospitalar de triagem automática de exames de texto (laudos médicos) para classificar urgência (`normal` / `atenção` / `urgente`).
* **Core**: Classificador de texto (NLP) leve, servido via API REST em container Docker.

## 📋 Requisitos Obrigatórios
* Repositório GitHub estruturado.
* Pipeline CI/CD básico com GitHub Actions (`lint` → `test` → `build`).
* Script ou DAG Airflow simples para pipeline de treino/retreino.
* Dockerfile funcional para o serviço de inferência.
* Stack de monitoramento local completa: API + Prometheus + Grafana via Docker Compose.
* Histórico de commits semântico e organizado.
* Vídeo de até 5 minutos seguindo o método STAR (Situation, Task, Action, Result).

## 📚 Bibliotecas e Stack Tecnológica
* **Scikit-Learn** (ou framework de preferência) para o modelo base de NLP (ex: TF-IDF + Random Forest ou modelo leve similar).
* **FastAPI** para a construção da API REST.
* **prometheus-client** para a instrumentação de métricas da aplicação.
* **Airflow** para orquestração das etapas de dados e treino.

## 📊 Critérios de Avaliação e Pesos
* **Modelagem e Otimização (20%)**: Modelo funcional de NLP, conversão/otimização (ex: ONNX) bem-sucedida e melhoria de latência demonstrada.
* **CI/CD - GitHub Actions (15%)**: Workflow configurado executando testes básicos e lint (mínimo de 2 automações).
* **Orquestração - Airflow (15%)**: DAG funcional realizando as etapas de ingestão e treino.
* **Monitoramento (20%)**: Docker Compose funcional (API + Prometheus + Grafana) com dashboard exibindo métricas (requisições, latência e taxa de erro).
* **Documentação - README (15%)**: Explicação da arquitetura em nuvem escolhida (batch vs. real-time) e instruções claras de execução.
* **Vídeo STAR (15%)**: Clareza na demonstração técnica e explicação do impacto (≤ 5 min).

## 🎯 Etapas de Desenvolvimento
1. **Etapa 1**: Decisão de arquitetura em nuvem (documentada no README), criação da API em FastAPI, empacotamento em Docker e mensuração da latência base.
2. **Etapa 2**: Configuração do workflow no GitHub Actions (`lint` e `pytest`) e criação da DAG no Airflow para simulação de treino.
3. **Etapa 3**: Instrumentação da API com `prometheus_client`, configuração do `docker-compose.yml` (API + Prometheus + Grafana) e criação do dashboard.
4. **Etapa 4**: Aplicação de técnica de otimização de latência (ex: exportação para ONNX Runtime), comparação de performance e gravação do vídeo STAR.