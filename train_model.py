# ==========================================
# Healthcare Disease Prediction System
# train_model.py
# ==========================================

import pandas as pd
import pickle
import os
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.preprocessing import LabelEncoder

# ==========================================
# Create Sample Dataset if not exists
# ==========================================

def create_sample_dataset():
    """Create a sample dataset for disease prediction"""
    
    # Sample data with 10 symptoms and 10 diseases
    data = {
        'fever': [1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
        'cough': [1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 1],
        'fatigue': [1, 0, 1, 1, 0, 0, 1, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 0, 1, 0],
        'headache': [1, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1],
        'vomiting': [0, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 1],
        'nausea': [0, 1, 1, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 0],
        'chest_pain': [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0],
        'breathing': [1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0],
        'diabetes': [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1],
        'bp': [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
        'Disease': [
            'Common Cold', 'Flu', 'COVID-19', 'Common Cold', 'Diabetes',
            'Flu', 'Heart Disease', 'COVID-19', 'Typhoid', 'Hypertension',
            'Pneumonia', 'Heart Disease', 'Asthma', 'Diabetes', 'Migraine',
            'Pneumonia', 'Typhoid', 'Asthma', 'Hypertension', 'Migraine'
        ]
    }
    
    df = pd.DataFrame(data)
    
    # Create directory if not exists
    os.makedirs("dataset", exist_ok=True)
    
    # Save dataset
    df.to_csv("dataset/disease_dataset.csv", index=False)
    print("Sample dataset created successfully!")
    return df

# ==========================================
# Load Dataset
# ==========================================

def load_dataset():
    """Load the disease dataset"""
    
    dataset_path = "dataset/disease_dataset.csv"
    
    if not os.path.exists(dataset_path):
        print("Dataset not found. Creating sample dataset...")
        return create_sample_dataset()
    
    dataset = pd.read_csv(dataset_path)
    print(f"Dataset loaded successfully! Shape: {dataset.shape}")
    print("\nFirst 5 rows:")
    print(dataset.head())
    print("\nDataset Info:")
    print(dataset.info())
    print("\nDisease Distribution:")
    print(dataset['Disease'].value_counts())
    
    return dataset

# ==========================================
# Train Model
# ==========================================

def train_model():
    """Train the disease prediction model"""
    
    print("=" * 50)
    print("Healthcare Disease Prediction System")
    print("Model Training Process")
    print("=" * 50)
    
    # Load dataset
    dataset = load_dataset()
    
    # Check if dataset is empty
    if dataset.empty:
        print("Error: Dataset is empty!")
        return None
    
    # ==========================================
    # Features and Target
    # ==========================================
    
    # Get feature columns (all columns except 'Disease')
    feature_columns = [col for col in dataset.columns if col != 'Disease']
    X = dataset[feature_columns]
    y = dataset['Disease']
    
    print(f"\nFeatures: {len(feature_columns)} columns")
    print(f"Target classes: {len(y.unique())} diseases")
    print(f"Target classes: {y.unique().tolist()}")
    
    # Encode target labels if they are strings
    if y.dtype == 'object':
        label_encoder = LabelEncoder()
        y_encoded = label_encoder.fit_transform(y)
        print(f"\nEncoded target classes: {label_encoder.classes_.tolist()}")
    else:
        y_encoded = y
    
    # ==========================================
    # Train Test Split
    # ==========================================
    
    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y_encoded,
        test_size=0.20,
        random_state=42,
        stratify=y_encoded
    )
    
    print(f"\nTraining samples: {len(X_train)}")
    print(f"Testing samples: {len(X_test)}")
    
    # ==========================================
    # Train Random Forest Model
    # ==========================================
    
    print("\nTraining Random Forest Model...")
    
    model = RandomForestClassifier(
        n_estimators=200,
        max_depth=10,
        min_samples_split=5,
        min_samples_leaf=2,
        random_state=42,
        n_jobs=-1
    )
    
    model.fit(X_train, y_train)
    print("Model training completed!")
    
    # ==========================================
    # Model Evaluation
    # ==========================================
    
    print("\n" + "=" * 50)
    print("Model Evaluation")
    print("=" * 50)
    
    # Predictions
    y_pred = model.predict(X_test)
    
    # Accuracy
    accuracy = accuracy_score(y_test, y_pred)
    print(f"\nModel Accuracy: {accuracy * 100:.2f}%")
    
    # Classification Report
    print("\nClassification Report:")
    target_names = label_encoder.classes_ if y.dtype == 'object' else None
    print(classification_report(y_test, y_pred, target_names=target_names))
    
    # Feature Importance
    print("\nTop 10 Feature Importance:")
    feature_importance = pd.DataFrame({
        'feature': feature_columns,
        'importance': model.feature_importances_
    }).sort_values('importance', ascending=False)
    
    for idx, row in feature_importance.head(10).iterrows():
        print(f"  {row['feature']}: {row['importance']:.4f}")
    
    # ==========================================
    # Save Model and Encoder
    # ==========================================
    
    print("\n" + "=" * 50)
    print("Saving Model")
    print("=" * 50)
    
    # Create model directory
    os.makedirs("model", exist_ok=True)
    
    # Save model
    model_path = "model/disease_model.pkl"
    with open(model_path, "wb") as file:
        pickle.dump(model, file)
    print(f"Model saved to: {model_path}")
    
    # Save label encoder if used
    if y.dtype == 'object':
        encoder_path = "model/label_encoder.pkl"
        with open(encoder_path, "wb") as file:
            pickle.dump(label_encoder, file)
        print(f"Label encoder saved to: {encoder_path}")
    
    # Save feature columns
    feature_path = "model/feature_columns.pkl"
    with open(feature_path, "wb") as file:
        pickle.dump(feature_columns, file)
    print(f"Feature columns saved to: {feature_path}")
    
    print("\nModel saved successfully!")
    
    # ==========================================
    # Test Prediction
    # ==========================================
    
    print("\n" + "=" * 50)
    print("Test Prediction")
    print("=" * 50)
    
    # Test with sample input
    sample_features = {
        'fever': 1,
        'cough': 1,
        'fatigue': 0,
        'headache': 1,
        'vomiting': 0,
        'nausea': 0,
        'chest_pain': 0,
        'breathing': 0,
        'diabetes': 0,
        'bp': 0
    }
    
    # Convert to array in correct order
    sample_array = np.array([[sample_features[col] for col in feature_columns]])
    
    # Predict
    sample_pred = model.predict(sample_array)
    
    # Decode if label encoder was used
    if y.dtype == 'object':
        sample_disease = label_encoder.inverse_transform(sample_pred)[0]
    else:
        sample_disease = sample_pred[0]
    
    print("\nSample Input Symptoms:")
    for key, value in sample_features.items():
        print(f"  {key}: {value}")
    
    print(f"\nPredicted Disease: {sample_disease}")
    
    # Get prediction probability
    try:
        probabilities = model.predict_proba(sample_array)[0]
        confidence = max(probabilities) * 100
        print(f"Confidence: {confidence:.2f}%")
    except:
        print("Confidence score not available")
    
    return model

# ==========================================
# Load Model Function (for later use)
# ==========================================

def load_model():
    """Load the trained model and encoder"""
    
    try:
        # Load model
        with open("model/disease_model.pkl", "rb") as file:
            model = pickle.load(file)
        
        # Load label encoder
        with open("model/label_encoder.pkl", "rb") as file:
            label_encoder = pickle.load(file)
        
        # Load feature columns
        with open("model/feature_columns.pkl", "rb") as file:
            feature_columns = pickle.load(file)
        
        return model, label_encoder, feature_columns
    
    except FileNotFoundError:
        print("Model files not found. Please train the model first.")
        return None, None, None

# ==========================================
# Test Model Function
# ==========================================

def test_model():
    """Test the trained model with new data"""
    
    print("\n" + "=" * 50)
    print("Model Testing")
    print("=" * 50)
    
    # Load model
    model, label_encoder, feature_columns = load_model()
    
    if model is None:
        print("No trained model found. Please run train_model() first.")
        return
    
    # Test cases
    test_cases = [
        {
            'name': 'Fever and Cough',
            'symptoms': [1, 1, 0, 0, 0, 0, 0, 0, 0, 0]
        },
        {
            'name': 'Chest Pain and Breathing Issues',
            'symptoms': [0, 0, 0, 0, 0, 0, 1, 1, 0, 0]
        },
        {
            'name': 'Diabetes Symptoms',
            'symptoms': [0, 0, 0, 0, 0, 0, 0, 0, 1, 0]
        },
        {
            'name': 'Headache and Nausea',
            'symptoms': [0, 0, 1, 1, 0, 1, 0, 0, 0, 0]
        },
        {
            'name': 'High BP and Fatigue',
            'symptoms': [0, 0, 1, 0, 0, 0, 0, 0, 0, 1]
        }
    ]
    
    print("\nTesting Multiple Cases:")
    print("-" * 50)
    
    for case in test_cases:
        sample = np.array([case['symptoms']])
        prediction = model.predict(sample)
        
        if label_encoder:
            disease = label_encoder.inverse_transform(prediction)[0]
        else:
            disease = prediction[0]
        
        # Get confidence
        try:
            prob = model.predict_proba(sample)[0]
            confidence = max(prob) * 100
        except:
            confidence = 0
        
        print(f"\nCase: {case['name']}")
        print(f"Predicted Disease: {disease}")
        print(f"Confidence: {confidence:.2f}%")

# ==========================================
# Main Execution
# ==========================================

if __name__ == "__main__":
    
    print("=" * 60)
    print("HEALTHCARE DISEASE PREDICTION SYSTEM")
    print("Machine Learning Model Training")
    print("=" * 60)
    
    # Train the model
    model = train_model()
    
    if model:
        # Test the model
        test_model()
        
        print("\n" + "=" * 60)
        print("✅ Model Training Completed Successfully!")
        print("=" * 60)
        print("\nFiles created:")
        print("  - dataset/disease_dataset.csv")
        print("  - model/disease_model.pkl")
        print("  - model/label_encoder.pkl")
        print("  - model/feature_columns.pkl")
        print("\nYou can now use the model for disease prediction.")
    else:
        print("\n❌ Model Training Failed!")
