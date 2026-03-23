import joblib
from pathlib import Path
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

from src.data.load_data import load_data
from src.features.build_features import build_features

BASE_DIR = Path(__file__).resolve().parents[2]

def train():

    data_path = BASE_DIR / "data/raw/dados.csv"    
   
    df = load_data(data_path)
    df = build_features(df)

    X = df.drop('target', axis=1)
    y = df['target']

    X_train, X_test, y_train, y_test = train_test_split(X, y)

    model = RandomForestClassifier()
    model.fit(X_train, y_train)

    joblib.dump(model, 'artifacts/model.pkl')
    print("Modelo salvo!")


if __name__ == "__main__":
    train()