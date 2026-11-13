import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt
from sklearn.tree import plot_tree

data = pd.read_csv("decision_tree_students.csv")

print("Loaded dataset shape:", data.shape)
data.info()

print("\nMissing values per column:")
print(data.isna().sum())

print("\nDuplicate rows:", data.duplicated().sum())

print("\nFeature summary:")
print(data.drop(columns="Pass").describe().round(2))


X = data.drop(columns=["Pass"])
y = data["Pass"]

print("Features:", X.columns.tolist())
print("Target:", y.name)
print("X shape:", X.shape)
print("y shape:", y.shape)


X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.20, stratify=y, random_state=42
)

print("Training shape:", X_train.shape)
print("Testing shape:", X_test.shape)

class_counts = pd.DataFrame({
    "Train": y_train.value_counts(),
    "Test": y_test.value_counts()
}).sort_index()

print(class_counts)

model = DecisionTreeClassifier(max_depth=3, random_state=42)
model.fit(X_train, y_train)

root_feature = X_train.columns[model.tree_.feature[0]]
root_threshold = model.tree_.threshold[0]

print("Model training completed")
print("Tree depth:", model.get_depth())
print("Number of leaves:", model.get_n_leaves())
print(f"Root question: {root_feature} <= {root_threshold:.2f}?")


predictions = model.predict(X_test)

results = X_test.copy()
results["Actual"] = y_test
results["Predicted"] = predictions

print("\nFirst 10 test predictions:")
print(results.head(10).to_string())

correct = (results["Actual"] == results["Predicted"]).sum()
print("\nTotal test students:", len(results))
print("Correct predictions:", correct)
print(f"Test accuracy: {accuracy_score(y_test, predictions):.1%}")


fig, ax = plt.subplots(figsize=(16, 8))
plot_tree(
    model,
    feature_names=X_train.columns.tolist(),
    class_names=["Fail", "Pass"],
    filled=True,
    rounded=True,
    node_ids=True,
    impurity=False,
    precision=2,
    ax=ax
)
ax.set_title("Student Pass/Fail Decision Tree")
fig.tight_layout()
plt.show()