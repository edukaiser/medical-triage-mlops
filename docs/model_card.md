# Model Card - Medical Triage Classification

## 1. Visão Geral

Este Model Card descreve o modelo de classificação usado no projeto `medical-triage-mlops` para apoiar a triagem médica automatizada de laudos clínicos e resumos de atendimento.

O objetivo principal é fornecer uma base inicial para predição de risco clínico com base em texto, permitindo uma primeira classificação entre categorias relevantes para o processo de triagem.

O pipeline atual treina um classificador textual com base em features extraídas do texto clínico, registrando métricas em MLflow e servindo a inferência por uma API FastAPI.

---

## 2. Detalhes do Modelo

- Nome do projeto: medical-triage-mlops
- Tipo de modelo: classificador textual para triagem médica
- Implementação: scikit-learn
- Script de treinamento: `src/stages/train.py`
- Conversão para inferência: ONNX Runtime
- Experimentos rastreados: MLflow
- Artefatos gerados: modelo, vetor de texto, métricas e logs

### Modelo incluído
- Logistic Regression
- Vetorização por TF-IDF

---

## 3. Uso Pretendido

Este modelo foi concebido para:

- servir como baseline inicial para classificação de risco clínico;
- ajudar na triagem de laudos médicos por prioridade;
- apoiar experimentação e validação de hipóteses de NLP em saúde;
- fornecer uma referência simples para o ciclo de MLOps.

### Uso apropriado
- benchmark inicial de modelos;
- experimentos acadêmicos e de laboratório;
- validação de pipeline de treinamento, avaliação e inferência;
- apoio ao processo de triagem com revisão humana.

### Uso inadequado
- uso direto em produção sem validação adicional;
- decisões clínicas críticas sem revisão profissional;
- aplicação em outros domínios sem readequação dos dados;
- uso como único critério para classificação de urgência.

---

## 4. Dados de Treinamento

Os modelos foram treinados com dados processados a partir dos arquivos em `data/raw`.

### Bases utilizadas
- `medical_tc_train.csv`
- `medical_tc_test.csv`
- `medical_tc_labels.csv`

### Feature utilizada
A feature principal é o texto clínico, representado como:

- `abstract` ou campo textual do laudo/descrição clínica

### Variável alvo
A variável alvo corresponde à categoria de risco/triagem associada ao laudo, sendo representada em formato numérico ou categórico conforme o pipeline do projeto.

Em termos práticos, o modelo aprende a associar texto clínico a uma classe de triagem, por exemplo:

- normal;
- atenção;
- urgente.

---

## 5. Procedimento de Treinamento

### Estratégia
- divisão dos dados em treino e teste;
- vetorização por TF-IDF sobre o texto clínico;
- treinamento de classificador linear para predição da categoria;
- persistência do modelo e do vectorizer;
- conversão para ONNX para otimizar inferência em produção.

### Reprodutibilidade
- os experimentos devem ser executados com os mesmos dados e parâmetros;
- os artefatos devem ser versionados;
- o pipeline deve ser rastreado via MLflow;
- o ambiente deve seguir a configuração do projeto em `pyproject.toml`.

---

## 6. Métricas de Avaliação

As métricas registradas no experimento incluem:

- Accuracy
- Precision
- Recall
- F1 Score
- métricas de classificação por classe

## 6. Métricas de Avaliação

As métricas registradas no experimento incluem:

- Accuracy
- Precision
- Recall
- F1 Score
- métricas de classificação por classe

| Modelo                     | Accuracy | Precision (Weighted)  | Recall (Weighted)| F1 Score (Weighted)|
|----------------------------|----------|-----------------------|------------------|--------------------|
| Logistic Regression (ONNX) | 0.5675   |         0.5715        |      0.5675      |       0.5659       |

## 7. Limitações

Este modelo possui limitações importantes:

- depende fortemente da qualidade e padronização do texto clínico;
- não incorpora contexto clínico completo, como histórico do paciente ou exames complementares;
- pode apresentar dificuldades em casos ambíguos ou pouco representativos no conjunto de treino;
- a classificação automática não substitui a avaliação profissional;
- métricas podem variar conforme a distribuição dos dados e o rótulo clínico.

---

## 8. Fatores e Riscos

### Fatores de risco
- viés de amostragem nos dados de treino;
- textos clínicos mal formatados ou inconsistentes;
- rótulos pouco confiáveis ou enviesados;
- baixa representatividade de casos raros ou urgentes;
- dependência de uma inferência simples baseada em texto.

### Impactos potenciais
- classificações incorretas em casos clínicos sensíveis;
- sobrestimação ou subestimação do risco;
- risco operacional se o sistema for usado como apoio exclusivo para decisão.

---

## 9. Considerações Éticas

Antes de usar este modelo em ambiente operacional real, recomenda-se avaliar:

- viés de dados e representatividade;
- impacto sobre pacientes e profissionais de saúde;
- privacidade e proteção de informações clínicas;
- transparência das decisões;
- necessidade de revisão humana em cenários críticos.

Como o domínio é de saúde, a validação clínica e a supervisão humana são essenciais.

---

## 10. Recomendações

Para evoluir este projeto, recomenda-se:

- comparar o baseline com modelos mais sofisticados de NLP;
- incluir mais contexto clínico em conjunto com o texto;
- realizar validação por classe e análise de falsos negativos/positivos;
- monitorar drift e degradação de performance após implantação;
- criar uma avaliação alinhada com critérios clínicos reais.

---

## 11. Observações Finais

Este modelo é um ponto de partida sólido para a construção de um sistema de triagem médica dentro do pipeline MLOps. Ele é útil para benchmarking, experimentação e validação inicial, mas não deve substituir a avaliação clínica humana em decisões críticas.

---

## 12. Versão

- Versão: 0.1
- Status: draft / baseline
- Última atualização: 14/09/2026
