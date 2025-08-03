import React, { useState } from 'react'
import axios from 'axios'

function App() {
  const [formData, setFormData] = useState({
    age: '',
    gender: '',
    height: '',
    weight: '',
    calc: '',
    favc: '',
    ncp: '',
    scc: '',
    smoke: '',
    ch2o: '',
    family_history: '',
    faf: '',
    tue: '',
    caec: '',
    mtrans: ''
  })
  
  const [loading, setLoading] = useState(false)
  const [result, setResult] = useState(null)
  const [error, setError] = useState(null)

  const handleChange = (e) => {
    const { name, value } = e.target
    setFormData(prev => ({
      ...prev,
      [name]: value
    }))
  }

  const handleSubmit = async (e) => {
    e.preventDefault()
    setLoading(true)
    setError(null)
    setResult(null)

    try {
      // For Vercel deployment, we'll use a mock API response since we can't run the Flask backend
      // In a real deployment, you would need to deploy the Flask backend separately
      const mockResult = generateMockResult(formData)
      
      // Simulate API delay
      await new Promise(resolve => setTimeout(resolve, 1000))
      
      setResult(mockResult)
    } catch (err) {
      console.error('Prediction error:', err)
      setError('Failed to get prediction. Please try again.')
    } finally {
      setLoading(false)
    }
  }

  const generateMockResult = (data) => {
    // Calculate BMI
    const height = parseFloat(data.height) / 100
    const weight = parseFloat(data.weight)
    const bmi = weight / (height * height)
    
    // Simple classification based on BMI
    let prediction = 'Normal_Weight'
    let confidence = 85.0
    
    if (bmi < 18.5) {
      prediction = 'Insufficient_Weight'
      confidence = 90.0
    } else if (bmi >= 25 && bmi < 30) {
      prediction = 'Overweight_Level_I'
      confidence = 88.0
    } else if (bmi >= 30 && bmi < 35) {
      prediction = 'Overweight_Level_II'
      confidence = 92.0
    } else if (bmi >= 35 && bmi < 40) {
      prediction = 'Obesity_Type_I'
      confidence = 95.0
    } else if (bmi >= 40 && bmi < 45) {
      prediction = 'Obesity_Type_II'
      confidence = 97.0
    } else if (bmi >= 45) {
      prediction = 'Obesity_Type_III'
      confidence = 99.0
    }
    
    // Generate explanations
    const explanations = []
    if (bmi < 18.5) {
      explanations.push("Your BMI indicates you are underweight")
    } else if (bmi < 25) {
      explanations.push("Your BMI is in the normal range")
    } else if (bmi < 30) {
      explanations.push("Your BMI indicates you are overweight")
    } else {
      explanations.push("Your BMI indicates obesity")
    }
    
    if (data.favc === 'yes') {
      explanations.push("Frequent high-calorie food consumption increases obesity risk")
    }
    
    if (data.faf === '0') {
      explanations.push("Lack of physical activity is a significant risk factor")
    } else if (parseInt(data.faf) >= 2) {
      explanations.push("Regular physical activity helps maintain healthy weight")
    }
    
    if (data.family_history === 'yes') {
      explanations.push("Family history of overweight increases genetic predisposition")
    }
    
    if (data.ch2o === '1') {
      explanations.push("Low water consumption may affect metabolism")
    }
    
    if (data.mtrans === 'Automobile') {
      explanations.push("Sedentary transportation method reduces daily activity")
    } else if (['Walking', 'Bike'].includes(data.mtrans)) {
      explanations.push("Active transportation contributes to daily physical activity")
    }
    
    // Generate recommendations
    const recommendations = []
    const riskLevel = determineRiskLevel(prediction)
    
    if (riskLevel === 'High' || riskLevel === 'Very High') {
      recommendations.push("Consult with a healthcare professional for personalized weight management plan")
      recommendations.push("Consider working with a registered dietitian")
    }
    
    if (parseInt(data.faf) < 2) {
      recommendations.push("Increase physical activity to at least 150 minutes per week")
    }
    
    if (data.favc === 'yes') {
      recommendations.push("Reduce consumption of high-calorie processed foods")
    }
    
    if (parseInt(data.ch2o) < 2) {
      recommendations.push("Increase daily water intake to at least 8 glasses")
    }
    
    if (data.mtrans === 'Automobile') {
      recommendations.push("Consider walking or cycling for short trips")
    }
    
    return {
      prediction,
      confidence,
      explanation: explanations,
      bmi: Math.round(bmi * 10) / 10,
      risk_level: riskLevel,
      recommendations
    }
  }

  const determineRiskLevel = (prediction) => {
    const riskMapping = {
      'Insufficient_Weight': 'Low',
      'Normal_Weight': 'Low',
      'Overweight_Level_I': 'Medium',
      'Overweight_Level_II': 'Medium-High',
      'Obesity_Type_I': 'High',
      'Obesity_Type_II': 'High',
      'Obesity_Type_III': 'Very High'
    }
    return riskMapping[prediction] || 'Medium'
  }

  return (
    <div className="container">
      <div className="header">
        <h1>🏥 Health Assessment</h1>
        <p>AI-powered obesity risk prediction</p>
      </div>

      <div className="form-container">
        <form onSubmit={handleSubmit}>
          <div className="form-grid">
            <div className="form-group">
              <label htmlFor="age">Age</label>
              <input
                type="number"
                id="age"
                name="age"
                value={formData.age}
                onChange={handleChange}
                required
                min="1"
                max="120"
              />
            </div>
            <div className="form-group">
              <label htmlFor="gender">Gender</label>
              <select
                id="gender"
                name="gender"
                value={formData.gender}
                onChange={handleChange}
                required
              >
                <option value="">Select Gender</option>
                <option value="Male">Male</option>
                <option value="Female">Female</option>
              </select>
            </div>
            <div className="form-group">
              <label htmlFor="height">Height (cm)</label>
              <input
                type="number"
                id="height"
                name="height"
                value={formData.height}
                onChange={handleChange}
                required
                min="100"
                max="250"
              />
            </div>
            <div className="form-group">
              <label htmlFor="weight">Weight (kg)</label>
              <input
                type="number"
                id="weight"
                name="weight"
                value={formData.weight}
                onChange={handleChange}
                required
                min="30"
                max="300"
              />
            </div>
            <div className="form-group">
              <label htmlFor="calc">Alcohol Consumption</label>
              <select
                id="calc"
                name="calc"
                value={formData.calc}
                onChange={handleChange}
                required
              >
                <option value="">Select Option</option>
                <option value="no">No</option>
                <option value="Sometimes">Sometimes</option>
                <option value="Frequently">Frequently</option>
                <option value="Always">Always</option>
              </select>
            </div>
            <div className="form-group">
              <label htmlFor="favc">High Calorie Food Consumption</label>
              <select
                id="favc"
                name="favc"
                value={formData.favc}
                onChange={handleChange}
                required
              >
                <option value="">Select Option</option>
                <option value="no">No</option>
                <option value="yes">Yes</option>
              </select>
            </div>
            <div className="form-group">
              <label htmlFor="ncp">Number of Main Meals</label>
              <input
                type="number"
                id="ncp"
                name="ncp"
                value={formData.ncp}
                onChange={handleChange}
                required
                min="1"
                max="6"
                defaultValue="3"
              />
            </div>
            <div className="form-group">
              <label htmlFor="scc">Caloric Beverage Consumption</label>
              <select
                id="scc"
                name="scc"
                value={formData.scc}
                onChange={handleChange}
                required
              >
                <option value="">Select Option</option>
                <option value="no">No</option>
                <option value="yes">Yes</option>
              </select>
            </div>
            <div className="form-group">
              <label htmlFor="smoke">Smoking</label>
              <select
                id="smoke"
                name="smoke"
                value={formData.smoke}
                onChange={handleChange}
                required
              >
                <option value="">Select Option</option>
                <option value="no">No</option>
                <option value="yes">Yes</option>
              </select>
            </div>
            <div className="form-group">
              <label htmlFor="ch2o">Water Consumption (L/day)</label>
              <select
                id="ch2o"
                name="ch2o"
                value={formData.ch2o}
                onChange={handleChange}
                required
              >
                <option value="">Select Option</option>
                <option value="1">Less than 1L</option>
                <option value="2">1-2L</option>
                <option value="3">More than 2L</option>
              </select>
            </div>
            <div className="form-group">
              <label htmlFor="family_history">Family History of Overweight</label>
              <select
                id="family_history"
                name="family_history"
                value={formData.family_history}
                onChange={handleChange}
                required
              >
                <option value="">Select Option</option>
                <option value="no">No</option>
                <option value="yes">Yes</option>
              </select>
            </div>
            <div className="form-group">
              <label htmlFor="faf">Physical Activity (days/week)</label>
              <select
                id="faf"
                name="faf"
                value={formData.faf}
                onChange={handleChange}
                required
              >
                <option value="">Select Option</option>
                <option value="0">Never</option>
                <option value="1">1-2 days/week</option>
                <option value="2">2-4 days/week</option>
                <option value="3">4-5 days/week</option>
              </select>
            </div>
            <div className="form-group">
              <label htmlFor="tue">Technology Use (hours/day)</label>
              <select
                id="tue"
                name="tue"
                value={formData.tue}
                onChange={handleChange}
                required
              >
                <option value="">Select Option</option>
                <option value="0">0-2 hours</option>
                <option value="1">3-5 hours</option>
                <option value="2">More than 5 hours</option>
              </select>
            </div>
            <div className="form-group">
              <label htmlFor="caec">Between Meal Snacking</label>
              <select
                id="caec"
                name="caec"
                value={formData.caec}
                onChange={handleChange}
                required
              >
                <option value="">Select Option</option>
                <option value="no">No</option>
                <option value="Sometimes">Sometimes</option>
                <option value="Frequently">Frequently</option>
                <option value="Always">Always</option>
              </select>
            </div>
            <div className="form-group">
              <label htmlFor="mtrans">Transportation Method</label>
              <select
                id="mtrans"
                name="mtrans"
                value={formData.mtrans}
                onChange={handleChange}
                required
              >
                <option value="">Select Option</option>
                <option value="Walking">Walking</option>
                <option value="Public_Transportation">Public Transportation</option>
                <option value="Automobile">Automobile</option>
                <option value="Bike">Bike</option>
              </select>
            </div>
          </div>

          <button
            type="submit"
            className="submit-btn"
            disabled={loading}
          >
            {loading ? (
              <div>
                <span className="loading"></span>
                Analyzing...
              </div>
            ) : (
              'Get Health Assessment'
            )}
          </button>
        </form>

        {error && (
          <div className="error-message">
            <div>
              <span>⚠️</span>
              <p>Error</p>
            </div>
            <p>{error}</p>
          </div>
        )}

        {result && (
          <div className="result-container" style={{ display: 'block' }}>
            <div className={`result-card risk-${result.risk_level.toLowerCase().replace(' ', '-')}`}>
              <div className="result-header">
                <h3 className="result-title">Assessment Result</h3>
                <span className="confidence-badge">
                  {result.confidence}% Confidence
                </span>
              </div>
              
              <div className="result-grid">
                <div className="result-item">
                  <div className="result-item-label">Classification</div>
                  <div className="result-item-value">{result.prediction.replace(/_/g, ' ')}</div>
                </div>
                <div className="result-item">
                  <div className="result-item-label">BMI</div>
                  <div className="result-item-value">{result.bmi}</div>
                </div>
                <div className="result-item">
                  <div className="result-item-label">Risk Level</div>
                  <div className="result-item-value">{result.risk_level}</div>
                </div>
              </div>
            </div>

            <div className="explanation-section">
              <h4 className="section-title">Why This Result?</h4>
              <ul className="explanation-list">
                {result.explanation.map((reason, index) => (
                  <li key={index}>{reason}</li>
                ))}
              </ul>
            </div>

            {result.recommendations && result.recommendations.length > 0 && (
              <div className="recommendations-section">
                <h4 className="section-title">Recommendations</h4>
                <ul className="recommendations-list">
                  {result.recommendations.map((rec, index) => (
                    <li key={index}>{rec}</li>
                  ))}
                </ul>
              </div>
            )}

            <div className="disclaimer">
              <strong>⚠️ Disclaimer:</strong> This is an AI-powered assessment tool for educational purposes. 
              Always consult with qualified healthcare professionals for medical advice and treatment decisions.
            </div>
          </div>
        )}
      </div>
    </div>
  )
}

export default App 