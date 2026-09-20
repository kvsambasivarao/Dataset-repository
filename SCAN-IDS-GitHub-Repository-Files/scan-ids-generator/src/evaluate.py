"""Model evaluation for SCAN-IDS.

Provides classical and deep-learning baselines:
Decision Tree, Random Forest, RBF-SVM, MLP, 1D-CNN and LSTM.

Deep-learning models use TensorFlow/Keras when available. The classical
models remain usable without TensorFlow.
"""
import argparse
import json
from pathlib import Path

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.metrics import accuracy_score, f1_score
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.neural_network import MLPClassifier

SEED = 12345

def load_dataset(path, sample=None):
    df = pd.read_csv(path)
    if sample and len(df) > sample:
        df = df.sample(sample, random_state=SEED).reset_index(drop=True)
    df["CAN_ID_NUM"] = df["CAN_ID"].apply(
        lambda x: int(str(x), 16) if isinstance(x, str) else int(x)
    )
    X = df[["CAN_ID_NUM"] + [f"DATA{i}" for i in range(8)]].astype(float).values
    y = LabelEncoder().fit_transform(df["Flag"])
    return df, X, y

def split_scale(X, y):
    Xtr, Xte, ytr, yte = train_test_split(
        X, y, test_size=0.20, random_state=SEED, stratify=y
    )
    scaler = StandardScaler()
    return Xtr, Xte, ytr, yte, scaler.fit(Xtr)

def classical_models(Xtr, Xte, ytr, yte):
    models = {
        "DecisionTree": DecisionTreeClassifier(random_state=SEED),
        "RandomForest": RandomForestClassifier(
            n_estimators=100, random_state=SEED, n_jobs=-1
        ),
        "RBF_SVM": SVC(kernel="rbf", C=10, gamma="scale"),
        "MLP": MLPClassifier(
            hidden_layer_sizes=(128, 64), max_iter=40, random_state=SEED
        ),
    }
    results = {}
    for name, model in models.items():
        model.fit(Xtr, ytr)
        pred = model.predict(Xte)
        results[name] = {
            "accuracy": float(accuracy_score(yte, pred)),
            "macro_f1": float(f1_score(yte, pred, average="macro")),
        }
    return results

def deep_models(Xtr, Xte, ytr, yte, epochs=5, batch_size=256):
    try:
        import tensorflow as tf
        from tensorflow.keras import Sequential
        from tensorflow.keras.layers import (
            Input, Dense, Dropout, Conv1D, MaxPooling1D,
            GlobalAveragePooling1D, LSTM
        )
        tf.random.set_seed(SEED)
    except ImportError:
        return {"TensorFlow": {"status": "not installed"}}

    n_classes = int(np.max(ytr)) + 1
    Xtr_s = Xtr.reshape((-1, Xtr.shape[1], 1)).astype("float32")
    Xte_s = Xte.reshape((-1, Xte.shape[1], 1)).astype("float32")

    def train_eval(name, model):
        model.compile(
            optimizer="adam",
            loss="sparse_categorical_crossentropy",
            metrics=["accuracy"],
        )
        model.fit(
            Xtr_s, ytr, epochs=epochs, batch_size=batch_size,
            validation_split=0.1, verbose=0
        )
        pred = np.argmax(model.predict(Xte_s, verbose=0), axis=1)
        return {
            "accuracy": float(accuracy_score(yte, pred)),
            "macro_f1": float(f1_score(yte, pred, average="macro")),
        }

    cnn = Sequential([
        Input(shape=(Xtr.shape[1], 1)),
        Conv1D(32, 3, activation="relu", padding="same"),
        MaxPooling1D(2),
        Conv1D(64, 3, activation="relu", padding="same"),
        GlobalAveragePooling1D(),
        Dense(64, activation="relu"),
        Dropout(0.2),
        Dense(n_classes, activation="softmax"),
    ])

    lstm = Sequential([
        Input(shape=(Xtr.shape[1], 1)),
        LSTM(64),
        Dense(64, activation="relu"),
        Dropout(0.2),
        Dense(n_classes, activation="softmax"),
    ])

    return {
        "1D_CNN": train_eval("1D_CNN", cnn),
        "LSTM": train_eval("LSTM", lstm),
    }

def evaluate(path, sample=100000, deep=False):
    _, X, y = load_dataset(path, sample)
    Xtr, Xte, ytr, yte, scaler = split_scale(X, y)
    Xtr = scaler.transform(Xtr)
    Xte = scaler.transform(Xte)

    results = classical_models(Xtr, Xte, ytr, yte)
    if deep:
        results.update(deep_models(Xtr, Xte, ytr, yte))
    return results

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--dataset", required=True)
    ap.add_argument("--sample", type=int, default=100000)
    ap.add_argument("--deep", action="store_true",
                    help="Run TensorFlow 1D-CNN and LSTM in addition to classical models.")
    ap.add_argument("--output", default="")
    args = ap.parse_args()

    results = evaluate(args.dataset, args.sample, args.deep)
    print(json.dumps(results, indent=2))
    if args.output:
        Path(args.output).write_text(json.dumps(results, indent=2), encoding="utf-8")
