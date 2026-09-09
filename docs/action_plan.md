# Action Plan - Medical Triage MLOps (Tech Challenge Fase 3)

## 1. Objetivo

Construir um pipeline de MLOps completo e production-ready para um sistema de triagem automática de laudos médicos em NLP, cobrindo desde a estruturação inicial até o deploy em API, orquestração, monitoramento e otimização de latência.

## 2. Escopo do Projeto

O projeto deve evoluir para um fluxo completo de ML e MLOps, incluindo:
- documentação de arquitetura de deploy em nuvem (Batch vs. Real-time);
- pipeline de ingestão e treinamento de modelo de NLP (Scikit-Learn);
- orquestração de rotinas com Apache Airflow;
- serving de inferência via API FastAPI;
- instrumentação de métricas e observabilidade (Prometheus + Grafana);
- otimização de performance com ONNX Runtime;
- automação de testes e CI/CD com GitHub Actions.

## 3. Diretrizes Principais

O plano deve seguir os seguintes princípios:
- **Reprodutibilidade**: Todos os passos e ambientes devem ser executáveis de forma consistente.
- **Automação**: Pipelines, validações de lint e testes devem rodar sem intervenção manual via CI.
- **Observabilidade**: Métricas de latência, contagem de requisições e taxa de erro devem ser monitoradas.
- **Performance**: Otimização rigorosa de latência para atender a cenários hospitalares de alta criticidade.

## 4. Fases do Plano

### Fase 0 - Fundação do Projeto
**Objetivo**: Estruturar a base do repositório para crescer com qualidade.
- **Atividades**:
  - padronizar a estrutura de diretórios;
  - definir ambiente de execução e dependências (`pyproject.toml`);
  - criar documentação inicial e estrutura de pastas;
  - definir convenções de organização de módulos.
- **Entregáveis**:
  - projeto com estrutura organizada;
  - ambiente reproduzível.

### Fase 1 - API Base e Arquitetura em Nuvem (Etapa 1)
**Objetivo**: Desenvolver o serviço de inferência e fundamentar a estratégia em nuvem.
- **Atividades**:
  - redigir a análise de arquitetura em nuvem no `README.md`;
  - implementar a API em FastAPI para receber laudos textuais e retornar classificações (`normal`, `atenção`, `urgente`);
  - empacotar a aplicação em Dockerfile e medir a latência base local.
- **Entregáveis**:
  - API funcional rodando em container Docker;
  - documentação de decisão arquitetural clara.

### Fase 2 - CI/CD e Orquestração (Etapa 2)
**Objetivo**: Automatizar o pipeline de código e o fluxo de treinamento.
- **Atividades**:
  - configurar workflow no GitHub Actions para validações de `lint` e testes com `pytest`;
  - desenvolver a DAG no Apache Airflow para simular o pipeline de treino/retreino.
- **Entregáveis**:
  - workflow YAML de CI/CD funcional;
  - DAG do Airflow estruturada.

### Fase 3 - Observabilidade e Monitoramento (Etapa 3)
**Objetivo**: Instrumentar a aplicação para monitoramento de performance em tempo real.
- **Atividades**:
  - integrar a biblioteca `prometheus_client` na API FastAPI;
  - configurar o `docker-compose.yml` para subir a stack unificada (API + Prometheus + Grafana);
  - montar painéis no Grafana exibindo requisições, latência e taxa de erro.
- **Entregáveis**:
  - stack de monitoramento rodando via compose;
  - dashboard configurado.

### Fase 4 - Otimização de Latência e Fechamento (Etapa 4)
**Objetivo**: Otimizar o modelo e consolidar as entregas do projeto.
- **Atividades**:
  - exportar o classificador de texto treinado para o formato ONNX Runtime;
  - comparar a latência do modelo original versus o modelo otimizado;
  - estruturar o roteiro e gravar o vídeo STAR (≤ 5 min).
- **Entregáveis**:
  - modelo otimizado;
  - relatório comparativo de latência;
  - link do vídeo de apresentação.

## 5. Priorização Recomendada

A ordem ideal de execução é:
1. Estruturação do projeto e fundações.
2. Desenvolvimento da API e documentação arquitetural (Etapa 1).
3. CI/CD e DAG do Airflow (Etapa 2).
4. Stack de monitoramento Prometheus e Grafana (Etapa 3).
5. Otimização ONNX e gravação do vídeo STAR (Etapa 4).

## 6. Critérios de Conclusão de Cada Fase

- **Fase 0**: Projeto organizado e ambiente pronto.
- **Fase 1**: API respondendo em Docker e arquitetura documentada.
- **Fase 2**: CI testando o código e Airflow orquestrando o treino.
- **Fase 3**: Stack completa (API + Prometheus + Grafana) exibindo métricas.
- **Fase 4**: Modelo otimizado, benchmarks comparados e vídeo gravado.

## 7. Riscos e Mitigações

- **Dificuldade na integração do Airflow**: Mitigado pelo uso de uma DAG simples e focada apenas nas tarefas essenciais de ingestão/treino.
- **Latência elevada no modelo de NLP**: Mitigado pela aplicação de otimização via ONNX Runtime na Fase 4.
- **Falhas na stack de monitoramento**: Mitigado pelo uso de compose unificado e validação prévia das métricas expostas.

## 8. Próximos Passos Imediatos

- Consolidar a estrutura de diretórios e arquivos base do projeto.
- Escrever a documentação de arquitetura no `README.md`.
- Implementar a primeira versão da API FastAPI.

## 9. Resumo

Este plano direciona o desenvolvimento para uma solução robusta de MLOps aplicada à saúde, focando em automação, observabilidade, performance e conformidade total com os requisitos do Tech Challenge.