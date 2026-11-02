import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.feature_selection import SelectKBest, f_classif
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report

X = pd.read_csv("data/data.csv", index_col=0)
y = pd.read_csv("data/labels.csv", index_col=0)["Class"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, stratify=y, random_state=42
)

model = Pipeline([
    ("scale", StandardScaler()),
    ("select", SelectKBest(f_classif, k=500)),
    ("clf", LogisticRegression(max_iter=1000)),
])

model.fit(X_train, y_train)
print(classification_report(y_test, model.predict(X_test)))

joblib.dump(model, "model.pkl")
joblib.dump(list(X.columns), "genes.pkl")

# save 5 test rows as a sample file for the website
X_test.head(5).to_csv("sample.csv")
print("Saved model.pkl, genes.pkl, sample.csv")