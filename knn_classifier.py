import numpy as np
from sklearn.model_selection import train_test_split 
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, classification_report 

# 1. Create a dummy dataset (Features: Age, Salary -> Label: Will Buy Product)
X = np.array([[25, 40000], [35, 60000], [45, 80000], [20, 20000], [55, 120000], [60, 140000]]) 
y = np.array([0, 0, 1, 0, 1, 1])

# 2. Split dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# 3. Feature Scaling (Crucial for KNN as it relies on distance metrics)
scaler = StandardScaler() 
X_train = scaler.fit_transform(X_train) 
X_test = scaler.transform(X_test)

# 4. Initialize and train the KNN Classifier (K=3)
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X_train, y_train) 

# 5. Make predictions
y_pred = knn.predict(X_test)

# 6. Evaluate the model
print(f"Accuracy Score: {accuracy_score(y_test, y_pred)}") 
print("\nClassification Report:\n", classification_report(y_test, y_pred)) 
