import pandas as pd
import numpy as np
import random
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score





def generate_data(num_samples):
  states = ['baby', 'toddler', 'kid', 'teen', 'young adult']
  ranges = [(1, 200), (201, 400), (401, 600), (601, 800), (801, 1000)]

  data = []
  for i, (start, end) in enumerate(ranges):
    stress_values = np.random.randint(start, end + 1, num_samples)
    for stress in stress_values:
      state = states[i]
      data.append([stress, state])

  df = pd.DataFrame(data, columns=['stress_meter', 'state'])
  return df

# Generate 1000 data points
df = generate_data(200)
df.to_csv('strict_data.csv', index=False)
print(df)



def generate_unique_random_indices(num_indices):
  indices = set()
  while len(indices) < num_indices:
    base_index = random.randint(0, 999)
    indices.add(base_index)
  return list(indices)

errorIndCount = 200
unique_indices = generate_unique_random_indices(errorIndCount)
df_modified = df.copy()

for index in unique_indices:
  offset = random.randint(-20, 20)
  df_modified.at[index, 'stress_meter'] += offset

df_modified.to_csv('modified_data.csv', index=False)


def get_row_counts(arr):
  unique_rows, indices, counts = np.unique(arr, return_index=True, return_counts=True)
  return dict(zip(unique_rows.tolist(), counts.tolist()))

get_row_counts(df.state)





# Load data (replace 'your_data.csv' with your file path)
data = pd.read_csv('modified_data.csv')

# Split features and target variable
X = data[['stress_meter']]
y = data['state']

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create and train the model
model = DecisionTreeClassifier()
model.fit(X_train, y_train)

# Make predictions on the test set
y_pred = model.predict(X_test)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)



import pickle

# Save the model to a file
with open('my_model.pkl', 'wb') as file:
    pickle.dump(model, file)

# Load the model from the file
with open('my_model.pkl', 'rb') as file:
    loaded_model = pickle.load(file)


new_data = [[100],[200],[300],[400],[500],[600],[700],[800],[900],[1000],[1100]]
predictions = loaded_model.predict(new_data)
print(predictions)