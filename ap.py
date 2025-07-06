from flask import Flask, request, jsonify
from flask_cors import CORS
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score, classification_report
import joblib
import os
import warnings
warnings.filterwarnings('ignore')

app = Flask(__name__)
CORS(app)

class ObesityPredictor:
    def __init__(self):
        self.model = None
        self.label_encoders = {}
        self.feature_columns = []
        self.target_classes = []
        
    def load_and_prepare_data(self, csv_path):
        """Load and prepare the dataset"""
        try:
            # Load the dataset
            df = pd.read_csv(csv_path)
            
            # Define feature columns (excluding ID and target)
            self.feature_columns = [
                'Age', 'Gender', 'Height', 'Weight', 'CALC', 'FAVC', 'FCVC', 
                'NCP', 'SCC', 'SMOKE', 'CH2O', 'family_history_with_overweight', 
                'FAF', 'TUE', 'CAEC', 'MTRANS'
            ]
            
            # Prepare features and target
            X = df[self.feature_columns].copy()
            y = df['NObeyesdad']
            
            # Store target classes
            self.target_classes = y.unique()
            
            # Encode categorical variables
            categorical_columns = ['Gender', 'CALC', 'FAVC', 'SCC', 'SMOKE', 
                                 'family_history_with_overweight', 'CAEC', 'MTRANS']
            
            for col in categorical_columns:
                if col in X.columns:
                    le = LabelEncoder()
                    X[col] = le.fit_transform(X[col].astype(str))
                    self.label_encoders[col] = le
            
            # Encode target variable
            self.target_encoder = LabelEncoder()
            y_encoded = self.target_encoder.fit_transform(y)
            
            return X, y_encoded, df
            
        except Exception as e:
            print(f"Error loading data: {e}")
            return None, None, None
    
    def train_model(self, X, y):
        """Train the prediction model"""
        try:
            # Split the data
            X_train, X_test, y_train, y_test = train_test_split(
                X, y, test_size=0.2, random_state=42, stratify=y
            )
            
            # Train Random Forest model
            self.model = RandomForestClassifier(
                n_estimators=100,
                random_state=42,
                max_depth=10,
                min_samples_split=5,
                min_samples_leaf=2
            )
            
            self.model.fit(X_train, y_train)
            
            # Evaluate model
            y_pred = self.model.predict(X_test)
            accuracy = accuracy_score(y_test, y_pred)
            
            print(f"Model trained with accuracy: {accuracy:.4f}")
            return accuracy
            
        except Exception as e:
            print(f"Error training model: {e}")
            return None
    
    def preprocess_input(self, user_data):
        """Preprocess user input for prediction"""
        try:
            # Create DataFrame from user input
            df = pd.DataFrame([user_data])
            
            # Ensure all required columns are present
            for col in self.feature_columns:
                if col not in df.columns:
                    df[col] = 0
            
            # Reorder columns to match training data
            df = df[self.feature_columns]
            
            # Encode categorical variables
            categorical_columns = ['Gender', 'CALC', 'FAVC', 'SCC', 'SMOKE', 
                                 'family_history_with_overweight', 'CAEC', 'MTRANS']
            
            for col in categorical_columns:
                if col in df.columns and col in self.label_encoders:
                    le = self.label_encoders[col]
                    try:
                        df[col] = le.transform(df[col].astype(str))
                    except ValueError:
                        # Handle unknown categories
                        df[col] = 0
            
            return df
            
        except Exception as e:
            print(f"Error preprocessing input: {e}")
            return None
    
    def predict(self, user_data):
        """Make prediction for user input"""
        try:
            # Preprocess input
            processed_data = self.preprocess_input(user_data)
            if processed_data is None:
                return None
            
            # Make prediction
            prediction = self.model.predict(processed_data)[0]
            prediction_proba = self.model.predict_proba(processed_data)[0]
            
            # Get feature importance for explanation
            feature_importance = dict(zip(self.feature_columns, self.model.feature_importances_))
            
            # Decode prediction
            predicted_class = self.target_encoder.inverse_transform([prediction])[0]
            confidence = max(prediction_proba) * 100
            
            return {
                'prediction': predicted_class,
                'confidence': confidence,
                'probabilities': dict(zip(self.target_encoder.classes_, prediction_proba)),
                'feature_importance': feature_importance
            }
            
        except Exception as e:
            print(f"Error making prediction: {e}")
            return None
    
    def save_model(self, path='obesity_model.pkl'):
        """Save the trained model"""
        try:
            model_data = {
                'model': self.model,
                'label_encoders': self.label_encoders,
                'target_encoder': self.target_encoder,
                'feature_columns': self.feature_columns,
                'target_classes': self.target_classes
            }
            joblib.dump(model_data, path)
            print(f"Model saved to {path}")
        except Exception as e:
            print(f"Error saving model: {e}")
    
    def load_model(self, path='obesity_model.pkl'):
        """Load a pre-trained model"""
        try:
            if os.path.exists(path):
                model_data = joblib.load(path)
                self.model = model_data['model']
                self.label_encoders = model_data['label_encoders']
                self.target_encoder = model_data['target_encoder']
                self.feature_columns = model_data['feature_columns']
                self.target_classes = model_data['target_classes']
                print(f"Model loaded from {path}")
                return True
            return False
        except Exception as e:
            print(f"Error loading model: {e}")
            return False

# Initialize predictor
predictor = ObesityPredictor()

# Load and train model on startup
def initialize_model():
    """Initialize the model with training data"""
    csv_path = 'train.csv'
    
    # Try to load existing model first
    if predictor.load_model():
        print("Loaded existing model")
        return True
    
    # If no existing model, train a new one
    if os.path.exists(csv_path):
        print("Training new model...")
        X, y, df = predictor.load_and_prepare_data(csv_path)
        if X is not None and y is not None:
            accuracy = predictor.train_model(X, y)
            if accuracy:
                predictor.save_model()
                print("Model training completed and saved")
                return True
    
    print("Warning: No model available. Using fallback prediction.")
    return False

@app.route('/api/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({"status": "healthy", "model_loaded": predictor.model is not None})

@app.route('/api/predict', methods=['POST'])
def predict_obesity():
    """Predict obesity risk based on user input"""
    try:
        # Get user data from request
        user_data = request.get_json()
        
        if not user_data:
            return jsonify({"error": "No data provided"}), 400
        
        # Convert form data to model format
        model_input = {
            'Age': float(user_data.get('age', 0)),
            'Gender': user_data.get('gender', 'Male'),
            'Height': float(user_data.get('height', 0)),
            'Weight': float(user_data.get('weight', 0)),
            'CALC': user_data.get('calc', 'no'),
            'FAVC': user_data.get('favc', 'no'),
            'FCVC': float(user_data.get('fcvc', 1)),
            'NCP': float(user_data.get('ncp', 3)),
            'SCC': user_data.get('scc', 'no'),
            'SMOKE': user_data.get('smoke', 'no'),
            'CH2O': float(user_data.get('ch2o', 2)),
            'family_history_with_overweight': user_data.get('family_history', 'no'),
            'FAF': float(user_data.get('faf', 0)),
            'TUE': float(user_data.get('tue', 0)),
            'CAEC': user_data.get('caec', 'no'),
            'MTRANS': user_data.get('mtrans', 'Public_Transportation')
        }
        
        # Make prediction
        if predictor.model is not None:
            result = predictor.predict(model_input)
            if result:
                # Generate explanation
                explanation = generate_explanation(model_input, result)
                
                return jsonify({
                    "prediction": result['prediction'],
                    "confidence": round(result['confidence'], 1),
                    "explanation": explanation,
                    "bmi": calculate_bmi(model_input['Height'], model_input['Weight']),
                    "risk_level": determine_risk_level(result['prediction']),
                    "recommendations": generate_recommendations(result['prediction'], model_input)
                })
            else:
                return jsonify({"error": "Prediction failed"}), 500
        else:
            # Fallback prediction using simple BMI-based logic
            fallback_result = fallback_prediction(model_input)
            return jsonify(fallback_result)
            
    except Exception as e:
        print(f"Prediction error: {e}")
        return jsonify({"error": "Internal server error"}), 500

def calculate_bmi(height_cm, weight_kg):
    """Calculate BMI"""
    try:
        height_m = height_cm / 100
        bmi = weight_kg / (height_m ** 2)
        return round(bmi, 1)
    except:
        return 0

def determine_risk_level(prediction):
    """Determine risk level based on prediction"""
    risk_mapping = {
        'Insufficient_Weight': 'Low',
        'Normal_Weight': 'Low',
        'Overweight_Level_I': 'Medium',
        'Overweight_Level_II': 'Medium-High',
        'Obesity_Type_I': 'High',
        'Obesity_Type_II': 'High',
        'Obesity_Type_III': 'Very High'
    }
    return risk_mapping.get(prediction, 'Medium')

def generate_explanation(input_data, result):
    """Generate explanation for the prediction"""
    explanations = []
    
    # BMI analysis
    bmi = calculate_bmi(input_data['Height'], input_data['Weight'])
    if bmi < 18.5:
        explanations.append("Your BMI indicates you are underweight")
    elif bmi < 25:
        explanations.append("Your BMI is in the normal range")
    elif bmi < 30:
        explanations.append("Your BMI indicates you are overweight")
    else:
        explanations.append("Your BMI indicates obesity")
    
    # High caloric food consumption
    if input_data['FAVC'] == 'yes':
        explanations.append("Frequent high-calorie food consumption increases obesity risk")
    
    # Physical activity
    if input_data['FAF'] == 0:
        explanations.append("Lack of physical activity is a significant risk factor")
    elif input_data['FAF'] >= 2:
        explanations.append("Regular physical activity helps maintain healthy weight")
    
    # Family history
    if input_data['family_history_with_overweight'] == 'yes':
        explanations.append("Family history of overweight increases genetic predisposition")
    
    # Water consumption
    if input_data['CH2O'] == 1:
        explanations.append("Low water consumption may affect metabolism")
    
    # Transportation mode
    if input_data['MTRANS'] == 'Automobile':
        explanations.append("Sedentary transportation method reduces daily activity")
    elif input_data['MTRANS'] in ['Walking', 'Bike']:
        explanations.append("Active transportation contributes to daily physical activity")
    
    return explanations

def generate_recommendations(prediction, input_data):
    """Generate personalized recommendations"""
    recommendations = []
    
    risk_level = determine_risk_level(prediction)
    
    if risk_level in ['High', 'Very High']:
        recommendations.append("Consult with a healthcare professional for personalized weight management plan")
        recommendations.append("Consider working with a registered dietitian")
    
    if input_data['FAF'] < 2:
        recommendations.append("Increase physical activity to at least 150 minutes per week")
    
    if input_data['FAVC'] == 'yes':
        recommendations.append("Reduce consumption of high-calorie processed foods")
    
    if input_data['FCVC'] < 2:
        recommendations.append("Increase daily vegetable and fruit consumption")
    
    if input_data['CH2O'] < 2:
        recommendations.append("Increase daily water intake to at least 8 glasses")
    
    if input_data['MTRANS'] == 'Automobile':
        recommendations.append("Consider walking or cycling for short trips")
    
    return recommendations

def fallback_prediction(input_data):
    """Fallback prediction when model is not available"""
    bmi = calculate_bmi(input_data['Height'], input_data['Weight'])
    
    # Simple BMI-based classification
    if bmi < 18.5:
        prediction = "Insufficient_Weight"
    elif bmi < 25:
        prediction = "Normal_Weight"
    elif bmi < 30:
        prediction = "Overweight_Level_I"
    else:
        prediction = "Obesity_Type_I"
    
    return {
        "prediction": prediction,
        "confidence": 75.0,
        "explanation": [f"Based on BMI calculation: {bmi}"],
        "bmi": bmi,
        "risk_level": determine_risk_level(prediction),
        "recommendations": generate_recommendations(prediction, input_data),
        "note": "Using simplified BMI-based prediction. Full model training recommended."
    }

if __name__ == '__main__':
    print("Initializing Obesity Prediction API...")
    initialize_model()
    app.run(debug=True, host='0.0.0.0', port=5000)