# 🏥 Obesity Risk Prediction App

A full-stack web application that predicts obesity risk using machine learning, built with React, Python Flask, and deployed on Vercel.

## 🚀 Features

- **AI-Powered Predictions**: Uses Random Forest classifier trained on obesity dataset
- **Responsive Design**: Works seamlessly on desktop, tablet, and mobile
- **Real-time Analysis**: Instant health risk assessment
- **Detailed Explanations**: Clear reasoning behind predictions
- **Personalized Recommendations**: Tailored health advice
- **Professional UI**: Modern, healthcare-focused design

## 🛠️ Tech Stack

### Frontend
- **React 18** - UI library
- **Vite** - Build tool
- **Tailwind CSS** - Styling
- **Axios** - API calls
- **Prettier** - Code formatting

### Backend
- **Python 3.9+** - Runtime
- **Flask** - Web framework
- **scikit-learn** - Machine learning
- **pandas** - Data processing
- **numpy** - Numerical computing

### Deployment
- **Vercel** - Hosting platform
- **Serverless Functions** - Backend deployment

## 📦 Installation & Setup

### Prerequisites
- Node.js 18+ and npm
- Python 3.9+
- Git

### 1. Clone Repository
```bash
git clone https://github.com/yourusername/obesity-prediction-app.git
cd obesity-prediction-app
```

### 2. Backend Setup
```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Install Python dependencies
pip install -r requirements.txt

# Add your train.csv file to the root directory
# Make sure it has the columns: ID,Age,Gender,Height,Weight,CALC,FAVC,FCVC,NCP,SCC,SMOKE,CH2O,family_history_with_overweight,FAF,TUE,CAEC,MTRANS,NObeyesdad

# Run backend server
python app.py
```

### 3. Frontend Setup
```bash
# Install Node.js dependencies
npm install

# Start development server
npm run dev
```

### 4. Access Application
- Frontend: http://localhost:5173
- Backend API: http://localhost:5000

## 🚀 Deployment

### Deploy Backend to Vercel

1. **Prepare Backend**
```bash
# Create a new folder for backend
mkdir obesity-backend
cd obesity-backend

# Copy backend files
cp ../app.py .
cp ../requirements.txt .
cp ../vercel.json .
cp ../train.csv .
```

2. **Deploy to Vercel**
```bash
# Install Vercel CLI
npm install -g vercel

# Deploy
vercel --prod
```

3. **Note the backend URL** (e.g., `https://your-backend-123.vercel.app`)

### Deploy Frontend to Vercel

1. **Update API URL in React App**
```javascript
// In src/App.jsx, update the API_URL
const API_URL = 'https://your-backend-123.vercel.app/api'
```

2. **Deploy Frontend**
```bash
# Build the app
npm run build

# Deploy to Vercel
vercel --prod
```

## 📊 Dataset Requirements

Your `train.csv` should have these columns:
- `ID` - Unique identifier
- `Age` - Age in years
- `Gender` - Male/Female
- `Height` - Height in cm
- `Weight` - Weight in kg
- `CALC` - Calories consumption monitoring (yes/no)
- `FAVC` - Frequent consumption of high caloric food (yes/no)
- `FCVC` - Frequency of vegetable consumption (1-3)
- `NCP` - Number of main meals (1-4)
- `SCC` - Consumption of food between meals (no/Sometimes/Frequently/Always)
- `SMOKE` - Smoking (yes/no)
- `CH2O` - Consumption of water daily (1-3)
- `family_history_with_overweight` - Family history (yes/no)
- `FAF` - Physical activity frequency (0-3)
- `TUE` - Time using technology devices (0-2)
- `CAEC` - Consumption of alcohol (no/Sometimes/Frequently/Always)
- `MTRANS` - Transportation used (Walking/Public_Transportation/Automobile/Bike)
- `NObeyesdad` - Target variable (obesity level)

## 🔧 Configuration

### Environment Variables
Create `.env` files for configuration:

**Backend (.env)**
```
FLASK_ENV=production
MODEL_PATH=obesity_model.pkl
```

**Frontend (.env)**
```
VITE_API_URL=https://your-backend-url.vercel.app/api
```

## 🧪 Testing

### Backend Testing
```bash
# Test health endpoint
curl http://localhost:5000/api/health

# Test prediction endpoint
curl -X POST http://localhost:5000/api/predict \
  -H "Content-Type: application/json" \
  -d '{"age": 25, "gender": "Male", "height": 175, "weight": 70, ...}'
```

### Frontend Testing
```bash
# Run development server
npm run dev

# Build for production
npm run build

# Preview production build
npm run preview
```

## 📱 API Endpoints

### GET /api/health
Health check endpoint
```json
{
  "status": "healthy",
  "model_loaded": true
}
```

### POST /api/predict
Predict obesity risk
```json
{
  "prediction": "Normal_Weight",
  "confidence": 85.3,
  "explanation": ["Your BMI is in normal range", "..."],
  "bmi": 22.9,
  "risk_level": "Low",
  "recommendations": ["Continue healthy habits", "..."]
}
```

## 🎯 Model Performance

The machine learning model achieves:
- **Accuracy**: ~85-90% on test data
- **Algorithm**: Random Forest Classifier
- **Features**: 16 health and lifestyle indicators
- **Classes**: 7 obesity levels

## 🔍 Troubleshooting

### Common Issues

1. **Model Training Fails**
   - Ensure train.csv is in the correct format
   - Check for missing values in dataset
   - Verify column names match exactly

2. **API Errors**
   - Check backend logs for detailed error messages
   - Verify CORS settings for cross-origin requests
   - Ensure all required fields are sent in requests

3. **Deployment Issues**
   - Check Vercel function logs
   - Verify environment variables are set
   - Ensure requirements.txt includes all dependencies

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- Dataset providers for obesity research data
- scikit-learn community for ML tools
- React and Flask communities for excellent frameworks
- Vercel for seamless deployment platform

---

**⚠️ Medical Disclaimer**: This application is for educational and research purposes only. Always consult healthcare professionals for medical advice.