from random import seed, randrange, random
from csv import reader
from math import exp
import sys
import math
import os
import pandas as pd
from typing import List, Callable, Tuple

"""
Backpropagation MLP (refatorado) para dataset.csv de jogos.

- Lê dataset.csv com header.
- Constrói features numéricas a partir de: release_date (ano), developer (label encoding),
  genres (multi-hot por gênero), price (float). Colunas 'appid' e 'name' são ignoradas.
- Se existir coluna 'output' com valores '00','01','10','11', mapeia para 0..3.
  Caso contrário, GERA a coluna de saída com base em perfis fixos de 2 usuários
  (funções user1_likes / user2_likes abaixo) e mapeia para 0..3 conforme:
      00=0, 01=1, 10=2, 11=3
- Treina a MLP com validação cruzada k-fold e imprime acurácia por fold e média.

Ajustes fáceis:
- Edite as regras em user1_likes / user2_likes para refletir gostos reais.
- Ajuste n_hidden, l_rate, n_epoch no MAIN.
"""

# =========================
#   FUNÇÕES DA REDE MLP
# =========================

def initialize_network_custom(layers: List[int]):
    """Cria a rede com base em uma lista de camadas, ex: [n_inputs, n_hidden, n_outputs]."""
    network = []
    for idx_layer in range(1, len(layers)):
        layer = []
        for _ in range(layers[idx_layer]):
            weights = [random() for _ in range(layers[idx_layer - 1] + 1)]  # inclui bias
            layer.append({'weights': weights})
        network.append(layer)
    return network


def activate(weights: List[float], inputs: List[float]) -> float:
    """Calcula ativação de um neurônio (produto + bias)."""
    activation = weights[-1]  # bias
    for i in range(len(weights) - 1):
        activation += weights[i] * inputs[i]
    return activation


def transfer_sigmoid(x: float, derivative: bool = False) -> float:
    """Função de ativação Sigmoid e sua derivada (em função da saída)."""
    if not derivative:
        # Proteção contra overflow numérico
        if x < -60:  # evita exp muito grande
            return 0.0
        if x > 60:
            return 1.0
        return 1.0 / (1.0 + math.exp(-x))
    # aqui x é a SAÍDA da sigmoid
    return x * (1.0 - x)


def forward_propagate(network, row: List[float], transfer: Callable[[float, bool], float]):
    """Propaga entradas pela rede."""
    inputs = row
    for layer in network:
        new_inputs = []
        for neuron in layer:
            activation = activate(neuron['weights'], inputs)
            neuron['output'] = transfer(activation, False)
            new_inputs.append(neuron['output'])
        inputs = new_inputs
    return inputs


def backward_propagate_error(network, expected: List[float], transfer: Callable[[float, bool], float]):
    """Propaga erro para trás e atualiza deltas."""
    for idx_layer in reversed(range(len(network))):
        layer = network[idx_layer]
        errors = []
        if idx_layer != len(network) - 1:  # camada oculta
            for j in range(len(layer)):
                error = sum(neuron['weights'][j] * neuron['delta'] for neuron in network[idx_layer + 1])
                errors.append(error)
        else:  # camada de saída
            for j, neuron in enumerate(layer):
                errors.append(expected[j] - neuron['output'])
        for j, neuron in enumerate(layer):
            neuron['delta'] = errors[j] * transfer(neuron['output'], True)


def update_weights(network, row: List[float], l_rate: float):
    """Atualiza pesos da rede."""
    for idx_layer, layer in enumerate(network):
        inputs = row[:-1] if idx_layer == 0 else [neuron['output'] for neuron in network[idx_layer - 1]]
        for neuron in layer:
            for i in range(len(inputs)):
                neuron['weights'][i] += l_rate * neuron['delta'] * inputs[i]
            neuron['weights'][-1] += l_rate * neuron['delta']  # bias


def one_hot_encoding(n_outputs: int, label: int) -> List[float]:
    expected = [0.0 for _ in range(n_outputs)]
    expected[label] = 1.0
    return expected


def predict(network, row: List[float], transfer: Callable[[float, bool], float]) -> int:
    outputs = forward_propagate(network, row, transfer)
    return int(max(range(len(outputs)), key=lambda i: outputs[i]))


def accuracy_metric(actual: List[int], predicted: List[int]) -> float:
    correct = sum(1 for i in range(len(actual)) if actual[i] == predicted[i])
    return correct / float(len(actual)) * 100.0


def get_prediction_accuracy(network, dataset: List[List[float]], transfer) -> float:
    predictions = [predict(network, row, transfer) for row in dataset]
    expected = [int(row[-1]) for row in dataset]
    return accuracy_metric(expected, predictions)


def train_network(network, train: List[List[float]], test: List[List[float]],
                  l_rate: float, n_epoch: int, n_outputs: int,
                  transfer) -> None:
    """Treina a rede por n_epoch épocas."""
    for _ in range(n_epoch):
        for row in train:
            outputs = forward_propagate(network, row, transfer)
            expected = one_hot_encoding(n_outputs, int(row[-1]))
            backward_propagate_error(network, expected, transfer)
            update_weights(network, row, l_rate)


def back_propagation(train: List[List[float]], test: List[List[float]],
                     l_rate: float, n_epoch: int, n_hidden: int, transfer):
    """Executa o algoritmo de backpropagation. Retorna predicted."""
    n_inputs = len(train[0]) - 1
    n_outputs = len(set(int(row[-1]) for row in train))
    network = initialize_network_custom([n_inputs, n_hidden, n_outputs])
    train_network(network, train, test, l_rate, n_epoch, n_outputs, transfer)
    predictions = [predict(network, row, transfer) for row in test]
    return predictions


def cross_validation_split(dataset: List[List[float]], n_folds: int) -> List[List[List[float]]]:
    dataset_split, dataset_copy = [], list(dataset)
    fold_size = int(len(dataset) / n_folds) if n_folds > 0 else len(dataset)
    for _ in range(n_folds):
        fold = []
        while len(fold) < fold_size and len(dataset_copy) > 0:
            index = randrange(len(dataset_copy))
            fold.append(dataset_copy.pop(index))
        if fold:
            dataset_split.append(fold)
    # Se sobrar amostras por arredondamento, distribui
    for i, row in enumerate(dataset_copy):
        dataset_split[i % len(dataset_split)].append(row)
    return dataset_split


def evaluate_algorithm(dataset: List[List[float]], algorithm, n_folds: int, *args):
    folds = cross_validation_split(dataset, n_folds)
    scores = []
    for i, fold in enumerate(folds, start=1):
        train_set = sum([f for f in folds if f is not fold], [])
        predicted = algorithm(train_set, fold, *args)
        actual = [int(row[-1]) for row in fold]
        acc = accuracy_metric(actual, predicted)
        scores.append(acc)
        print(f"- Fold {i}: Acurácia {acc:.2f}% (n={len(fold)})")
    return scores


# =========================
#   PRÉ-PROCESSAMENTO
# =========================

def build_features_from_dataframe(df: pd.DataFrame) -> Tuple[pd.DataFrame, list]:
    """
    Constrói um DataFrame de features numéricas a partir do df original.
    - year (int do release_date)
    - developer (label encoding normalizado)
    - genres_* (multi-hot)
    - price (float normalizado 0..1)
    Retorna (X_df, genre_list)
    """
    df = df.copy()

    # Ano de lançamento
    df["year"] = pd.to_datetime(df["release_date"], errors="coerce").dt.year.fillna(0).astype(int)

    # Developer (label encoding)
    df["developer_le"] = df["developer"].fillna("UNK").astype("category").cat.codes.astype(int)

    # Genres multi-hot
    all_genres = set()
    for v in df["genres"].fillna(""):
        for g in str(v).split(";"):
            g = g.strip()
            if g:
                all_genres.add(g)
    genre_list = sorted(all_genres)
    for g in genre_list:
        df[f"genre_{g}"] = df["genres"].fillna("").apply(lambda s: int(g in str(s).split(";")))

    # Seleciona features
    feature_cols = ["year", "developer_le", "price"] + [f"genre_{g}" for g in genre_list]
    X_df = df[feature_cols].copy()

    # Normalizar numéricas (year, price, developer_le) para 0..1
    for col in ["year", "price", "developer_le"]:
        col_min, col_max = X_df[col].min(), X_df[col].max()
        if col_max > col_min:
            X_df[col] = (X_df[col] - col_min) / (col_max - col_min)
        else:
            X_df[col] = 0.0

    return X_df, genre_list


def map_output_column_if_present(df: pd.DataFrame) -> pd.Series:
    """Se houver coluna 'output' com strings '00','01','10','11', mapeia para int 0..3."""
    if "output" in df.columns:
        mapping = {"00": 0, "01": 1, "10": 2, "11": 3}
        return df["output"].map(mapping).astype(int)
    return pd.Series(dtype=int)


# =========================
#   REGRAS DE GOSTOS FIXOS
# =========================

def user1_likes(row: pd.Series) -> bool:
    """
    Exemplo (ajuste conforme necessário):
    - Prefere jogos lançados até 2007 OU que tenham gênero 'RPG'
    - E com preço <= 10
    """
    year = pd.to_datetime(row.get("release_date"), errors="coerce").year
    if pd.isna(year):
        year = 0
    genres = str(row.get("genres", ""))
    price = float(row.get("price", 0.0))
    cond_year_or_rpg = (year != 0 and year <= 2007) or ("RPG" in genres)
    return bool(cond_year_or_rpg and price <= 10.0)


def user2_likes(row: pd.Series) -> bool:
    """
    Exemplo (ajuste conforme necessário):
    - Prefere jogos de Ação modernos (ano >= 2007) OU com 'Free to Play'
    - E com preço <= 15
    """
    year = pd.to_datetime(row.get("release_date"), errors="coerce").year
    if pd.isna(year):
        year = 0
    genres = str(row.get("genres", ""))
    price = float(row.get("price", 0.0))
    cond_action_moderno = (year != 0 and year >= 2007 and ("Action" in genres))
    cond_free = ("Free to Play" in genres)
    return bool((cond_action_moderno or cond_free) and price <= 15.0)


def build_labels_from_rules(df_original: pd.DataFrame) -> pd.Series:
    """Gera coluna de saída 0..3 a partir de regras fixas de dois usuários."""
    u1 = df_original.apply(user1_likes, axis=1).astype(int)
    u2 = df_original.apply(user2_likes, axis=1).astype(int)
    # Mapear para 0..3 conforme 00,01,10,11 (bit alto = user2; bit baixo = user1)
    return (u2 * 2 + u1).astype(int)


# =========================
#   MAIN
# =========================

def main():
    seed(1)

    dataset_path = os.environ.get("DATASET_PATH", "dataset.csv")
    try:
        df = pd.read_csv(dataset_path)
    except FileNotFoundError:
        print(f"[ERRO] Arquivo não encontrado: {dataset_path}")
        print("Defina a variável de ambiente DATASET_PATH ou coloque 'dataset.csv' no diretório atual.")
        sys.exit(1)

    # Constrói features
    X_df, _ = build_features_from_dataframe(df)

    # Constrói labels: usa coluna 'output' se existir; caso contrário, gera pelas regras
    y_series = map_output_column_if_present(df)
    if y_series.empty:
        print("[INFO] Coluna 'output' não encontrada. Gerando rótulos a partir das regras fixas...")
        y_series = build_labels_from_rules(df)

    # Monta lista de amostras para a MLP: [features..., label]
    dataset = X_df.copy()
    dataset["label"] = y_series
    dataset_list = dataset.values.tolist()

    # Hiperparâmetros
    n_folds = 5
    l_rate = 0.3
    n_epoch = 400
    # Dimensão de entrada
    n_inputs = X_df.shape[1]
    # Regra simples para hidden: entre 8 e 2/3 do input
    n_hidden = max(8, int(max(8, round(n_inputs * 2 / 3))))

    print("--------------------------------------------------")
    print(f"Arquivo: {dataset_path}")
    print(f"Samples: {len(dataset_list)} | Inputs: {n_inputs} | Hidden: {n_hidden}")
    print("Treinando com validação cruzada...")

    scores = evaluate_algorithm(dataset_list, back_propagation, n_folds, l_rate, n_epoch, n_hidden, transfer_sigmoid)
    print("Scores por fold:", [f"{s:.2f}%" for s in scores])
    print("Acurácia média: %.2f%%" % (sum(scores) / float(len(scores))))


if __name__ == "__main__":
    main()