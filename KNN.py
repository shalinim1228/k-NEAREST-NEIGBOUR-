from sklearn.neighbors import KNeighborsClassifier
import numpy as np

# Sample training data (brightness, saturation)
X_train = np.array([[40, 20], [50, 50], [60, 90], [10, 25], [70, 70], [60, 10], [25, 80]])
y_train = np.array([0, 1, 1, 0, 1, 0, 1])  # Corresponding classes, red-0, blue-1.

# New data entry for prediction (brightness=20, saturation=35)
X_new = np.array([[20, 35]])

# Create KNN model (k=3)
knn = KNeighborsClassifier(n_neighbors=2)

# Train the model
knn.fit(X_train, y_train)

# Predict the class for new data
prediction = knn.predict(X_new)
print("Predicted class:", prediction[0])