import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import classification_report

# Load the 'glass' dataset
glass_df = pd.read_csv('glass.csv')

# Define features and target
X = glass_df.drop("Type", axis=1)  # Features (RI, Na, Mg, Al, Si, K, Ca, Ba, Fe)
y = glass_df["Type"]  # Target variable (Type)

# Splitting the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initializing and training the linear SVM model
svm = SVC(kernel='linear')
svm.fit(X_train, y_train)

# Predicting on the test set
y_pred = svm.predict(X_test)

# Evaluating the model
accuracy = svm.score(X_test, y_test)
print("Linear SVM accuracy is:", accuracy)
print("Classification Report:")
print(classification_report(y_test, y_pred))
