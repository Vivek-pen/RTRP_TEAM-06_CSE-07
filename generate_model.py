import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

# Load data
df = pd.read_csv('https://drive.google.com/file/d/1jdr_5F-IIT4zDvJas8SyBbOUc6-sJigF/view?usp=drive_link')


# Features and labels
X = data.drop('Class', axis=1)
y = data['Class']

# Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

# Train model with class balancing
model = LogisticRegression(max_iter=1000, class_weight='balanced')
model.fit(X_train, y_train)

# Save model
with open('model.pkl', 'wb') as f:
    pickle.dump(model, f)

print("✅ Model trained with class balancing and saved as model.pkl!")
