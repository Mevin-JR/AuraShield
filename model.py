import joblib
import os

# Imports for the commented code #

# import csv
# from sklearn.model_selection import train_test_split
# from sklearn.metrics import accuracy_score, classification_report
# from sklearn.feature_extraction.text import TfidfVectorizer
# from sklearn.linear_model import LogisticRegression
# from sklearn.metrics import confusion_matrix
# import seaborn as sns
# import matplotlib.pyplot as plt
# import numpy as np

# # # # # # # # # # # # # # #
#                           #
#   Balancing the dataset   #
#                           #
# # # # # # # # # # # # # # #

# import pandas as pd

# data = pd.read_csv('./backend/data/train_toxic.csv')
# ingredients = []
# labels = []

# ingredients_toxic = data[data['Toxicity'] == 1]
# ingredients = data[data['Toxicity'] == 0]
# min_samples = min_samples = min(len(ingredients_toxic), len(ingredients))

# balanced_data = pd.concat([
#     ingredients_toxic.sample(min_samples, random_state=42),
#     ingredients.sample(min_samples, random_state=42)
# ])

# balanced_data = balanced_data.sample(frac=1, random_state=42).reset_index(drop=True)
# balanced_data.to_csv('./backend/data/train_toxic_bal.csv', index=False)

# # # # # # # # # # # # # # #
#                           #
#  Train/Test & Model dump  #
#                           #
# # # # # # # # # # # # # # #

# tfid_values = X.toarray()
# print("TF-IDF values for the first few samples:")
# for i in range(5):
#     print(f"Sample {i+1}: {tfid_values[i]}")

# ingredients = []
# labels = []

# with open('./data/train_toxic_bal.csv', newline='') as dataset:
#     reader = csv.DictReader(dataset)
#     for row in reader:
#         ingredients.append(row['CompoundName'])
#         labels.append(int(row['Toxicity']))

# vectorizer = TfidfVectorizer()
# X = vectorizer.fit_transform(ingredients)
# X_train, X_test, Y_train, Y_test = train_test_split(X, labels, test_size=0.2, random_state=42)

# model = LogisticRegression()
# model.fit(X_train, Y_train)
# Y_pred = model.predict(X_test)

# accuracy = accuracy_score(Y_test, Y_pred)
# print("Accuracy: ", accuracy)

# print("\nClassification Report:")
# print(classification_report(Y_test, Y_pred, zero_division=1))

# joblib.dump(vectorizer, './models/tfidf_vectorizer.pkl')
# joblib.dump(model, './models/logistic_regression_model.pkl')


# conf_matrix = confusion_matrix(Y_test, Y_pred)
# conf_matrix_percent = conf_matrix.astype('float') / conf_matrix.sum(axis=1)[:, np.newaxis] * 100

# # Plot confusion matrix
# plt.figure(figsize=(8, 6))
# sns.heatmap(conf_matrix_percent, annot=True, fmt=".2f", cmap="Blues", cbar=False)
# plt.title("Confusion Matrix")
# plt.xlabel("Predicted Labels")
# plt.ylabel("True Labels")
# plt.show()

# # # # # # # # # # # # # # #
#                           #
#  Implementation of Model  #
#                           #
# # # # # # # # # # # # # # #

def predict(ingredient):
    from main import get_file_path
    try:
        app_directory = get_file_path()
        file_path1 = os.path.join(app_directory, "models", "tfidf_vectorizer.pkl")
        file_path2 = os.path.join(app_directory, "models", "logistic_regression_model.pkl")
        vectorizer = joblib.load(file_path1)
        model = joblib.load(file_path2)

        ingredient_vect = vectorizer.transform([ingredient])

        if not ingredient_vect.indices.size:
            return "Input not recognized"

        prediction = model.predict(ingredient_vect)[0]
        return "Harmful" if prediction == 1 else "Not Harmful"
    except Exception as e:
        return f"Error: {e}"