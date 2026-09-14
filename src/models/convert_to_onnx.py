from pathlib import Path
import joblib
from skl2onnx import convert_sklearn
from skl2onnx.common.data_types import FloatTensorType

# Definir caminhos
root_dir = Path(__file__).resolve().parents[2]
model_path = root_dir / "models" / "model.pkl"
vectorizer_path = root_dir / "models" / "tfidf_vectorizer.pkl"
onnx_path = root_dir / "models" / "model.onnx"

print("Carregando o modelo e o vetorizador...")
model = joblib.load(model_path)
vectorizer = joblib.load(vectorizer_path)

# Descobrir o número de features geradas pelo TF-IDF (ex: tamanho do vocabulário)
# Fazemos um teste rápido para pegar a dimensão
dummy_text = ["exemplo de teste médico"]
n_features = vectorizer.transform(dummy_text).shape[1]

print(f"Dimensão das features do TF-IDF: {n_features}")

# Definir o tipo de entrada como FloatTensor com o tamanho exato das features do TF-IDF
initial_type = [("float_input", FloatTensorType([None, n_features]))]

print("Convertendo o classificador para ONNX...")
onnx_model = convert_sklearn(model, initial_types=initial_type)

# Salvar o modelo ONNX
with open(onnx_path, "wb") as f:
    f.write(onnx_model.SerializeToString())

print(f"Modelo ONNX salvo com sucesso em: {onnx_path}")
