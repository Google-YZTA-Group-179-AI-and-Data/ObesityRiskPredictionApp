import React, { useState } from 'react'
import axios from 'axios'
import './App.css'

const API_URL = import.meta.env.PROD 
  ? 'https://your-backend-url.vercel.app/api' 
  : '/api'

function App() {
  const [formData, setFormData] = useState({
    age: '',
    gender: '',
    height: '',
    weight: '',
    calc: '',
    favc: '',
    fcvc: '',
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
      const response = await axios.post(`${API_URL}/predict`, formData, {
        headers: {
          'Content-Type': 'application/json'
        }
      })
      
      setResult(response.data)
    } catch (err) {
      console.error('Prediction error:', err)
      setError(err.response?.data?.error || 'Failed to get prediction. Please try again.')
    } finally {
      setLoading(false)
    }
  }

  const getRiskColor = (riskLevel) => {
    const colors = {
      'Low': 'text-green-600 bg-green-50',
      'Medium': 'text-yellow-600 bg-yellow-50',
      'Medium-High': 'text-orange-600 bg-orange-50',
      'High': 'text-red-600 bg-red-50',
      'Very High': 'text-red-800 bg-red-100'
    }
    return colors[riskLevel] || 'text-gray-600 bg-gray-50'
  }

  return (
    <div className="min-h-screen bg-gradient-to-br from-blue-400 to-purple-600 p-4">
      <div className="max-w-2xl mx-auto">
        <div className="bg-white rounded-3xl shadow-2xl p-8 relative overflow-hidden">

          {/* Header */}
          <div className="text-center mb-8">
            <div className="w-16 h-16 bg-gradient-to-r from-blue-500 to-purple-600 rounded-full flex items-center justify-center mx-auto mb-4">
              <span className="text-2xl">🏥</span>
            </div>
            <h1 className="text-3xl font-bold text-gray-800 mb-2">Health Assessment</h1>
            <p className="text-gray-600">AI-powered obesity risk prediction</p>
          </div>

          {/* Form */}
          <form onSubmit={handleSubmit} className="space-y-6">
            {/* Basic Info */}
            <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
              <div>
                <label className="block text-sm font-medium text-gray-700 mb-2">Age</label>
                <input
                  type="number"
                  name="age"
                  value={formData.age}
                  onChange={handleChange}
                  required
                  min="1"
                  max="120"
                  className="w-full px-4 py-3 border border-gray-300 rounded-xl focus:ring-2 focus:ring-blue-500 focus:border-transparent transition-all"
                />
              </div>
              <div>
                <label className="block text-sm font-medium text-gray-700 mb-2">Gender</label>
                <select
                  name="gender"
                  value={formData.gender}
                  onChange={handleChange}
                  required
                  className="w-full px-4 py-3 border border-gray-300 rounded-xl focus:ring-2 focus:ring-blue-500 focus:border-transparent transition-all"
                >
                  <option value="">Select Gender</option>
                  <option value="Male">Male</option>
                  <option value="Female">Female</option>
                </select>
              </div>
            </div>
            {/* Basic Info */}
            <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
              <div>
                <label className="block text-sm font-medium text-gray-700 mb-2">Water Consumption</label>
                <select
                  name="ch2o"
                  value={formData.ch2o}
                  onChange={handleChange}
                  required
                  className="w-full px-4 py-3 border border-gray-300 rounded-xl focus:ring-2 focus:ring-blue-500 focus:border-transparent transition-all"
                >
                  <option value="">Select Option</option>
                  <option value="1">Less than 1L</option>
                  <option value="2">1-2L</option>
                  <option value="3">More than 2L</option>
                </select>
              </div>
              <div>
                <label className="block text-sm font-medium text-gray-700 mb-2">Family History</label>
                <select
                  name="family_history"
                  value={formData.family_history}
                  onChange={handleChange}
                  required
                  className="w-full px-4 py-3 border border-gray-300 rounded-xl focus:ring-2 focus:ring-blue-500 focus:border-transparent transition-all"
                >
                  <option value="">Select Option</option>
                  <option value="no">No</option>
                  <option value="yes">Yes</option>
                </select>
              </div>
            </div>

            <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
              <div>
                <label className="block text-sm font-medium text-gray-700 mb-2">Physical Activity</label>
                <select
                  name="faf"
                  value={formData.faf}
                  onChange={handleChange}
                  required
                  className="w-full px-4 py-3 border border-gray-300 rounded-xl focus:ring-2 focus:ring-blue-500 focus:border-transparent transition-all"
                >
                  <option value="">Select Option</option>
                  <option value="0">Never</option>
                  <option value="1">1-2 days/week</option>
                  <option value="2">2-4 days/week</option>
                  <option value="3">4-5 days/week</option>
                </select>
              </div>
              <div>
                <label className="block text-sm font-medium text-gray-700 mb-2">Technology Use</label>
                <select
                  name="tue"
                  value={formData.tue}
                  onChange={handleChange}
                  required
                  className="w-full px-4 py-3 border border-gray-300 rounded-xl focus:ring-2 focus:ring-blue-500 focus:border-transparent transition-all"
                >
                  <option value="">Select Option</option>
                  <option value="0">0-2 hours</option>
                  <option value="1">3-5 hours</option>
                  <option value="2">More than 5 hours</option>
                </select>
              </div>
            </div>

            <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
              <div>
                <label className="block text-sm font-medium text-gray-700 mb-2">Alcohol Consumption</label>
                <select
                  name="caec"
                  value={formData.caec}
                  onChange={handleChange}
                  required
                  className="w-full px-4 py-3 border border-gray-300 rounded-xl focus:ring-2 focus:ring-blue-500 focus:border-transparent transition-all"
                >
                  <option value="">Select Option</option>
                  <option value="no">No</option>
                  <option value="Sometimes">Sometimes</option>
                  <option value="Frequently">Frequently</option>
                  <option value="Always">Always</option>
                </select>
              </div>
              <div>
                <label className="block text-sm font-medium text-gray-700 mb-2">Transportation</label>
                <select
                  name="mtrans"
                  value={formData.mtrans}
                  onChange={handleChange}
                  required
                  className="w-full px-4 py-3 border border-gray-300 rounded-xl focus:ring-2 focus:ring-blue-500 focus:border-transparent transition-all"
                >
                  <option value="">Select Option</option>
                  <option value="Walking">Walking</option>
                  <option value="Public_Transportation">Public Transportation</option>
                  <option value="Automobile">Automobile</option>
                  <option value="Bike">Bike</option>
                </select>
              </div>
            </div>

            {/* Submit Button */}
            <button
              type="submit"
              disabled={loading}
              className="w-full bg-gradient-to-r from-blue-500 to-purple-600 text-white font-semibold py-4 px-6 rounded-xl hover:from-blue-600 hover:to-purple-700 transition-all duration-300 transform hover:scale-105 disabled:opacity-50 disabled:cursor-not-allowed disabled:transform-none"
            >
              {loading ? (
                <div className="flex items-center justify-center">
                  <div className="animate-spin rounded-full h-5 w-5 border-b-2 border-white mr-2"></div>
                  Analyzing...
                </div>
              ) : (
                'Get Health Assessment'
              )}
            </button>
          </form>

          {/* Error Message */}
          {error && (
            <div className="mt-6 p-4 bg-red-50 border border-red-200 rounded-xl">
              <div className="flex items-center">
                <span className="text-red-600 mr-2">⚠️</span>
                <p className="text-red-700 font-medium">Error</p>
              </div>
              <p className="text-red-600 mt-1">{error}</p>
            </div>
          )}

          {/* Results */}
          {result && (
            <div className="mt-8 space-y-6">
              {/* Main Result */}
              <div className={`p-6 rounded-2xl ${getRiskColor(result.risk_level)}`}>
                <div className="flex items-center justify-between mb-4">
                  <h3 className="text-xl font-bold">Assessment Result</h3>
                  <span className="text-sm font-medium px-3 py-1 rounded-full bg-white bg-opacity-50">
                    {result.confidence}% Confidence
                  </span>
                </div>
                <div className="grid grid-cols-1 md:grid-cols-3 gap-4 text-center">
                  <div>
                    <p className="text-sm opacity-75">Classification</p>
                    <p className="font-bold text-lg">{result.prediction.replace(/_/g, ' ')}</p>
                  </div>
                  <div>
                    <p className="text-sm opacity-75">BMI</p>
                    <p className="font-bold text-lg">{result.bmi}</p>
                  </div>
                  <div>
                    <p className="text-sm opacity-75">Risk Level</p>
                    <p className="font-bold text-lg">{result.risk_level}</p>
                  </div>
                </div>
              </div>

              {/* Explanation */}
              <div className="bg-blue-50 p-6 rounded-2xl">
                <h4 className="font-bold text-blue-900 mb-3 flex items-center">
                  <span className="mr-2">🔍</span>
                  Why This Result?
                </h4>
                <ul className="space-y-2">
                  {result.explanation.map((reason, index) => (
                    <li key={index} className="text-blue-800 flex items-start">
                      <span className="text-blue-500 mr-2 mt-1">•</span>
                      {reason}
                    </li>
                  ))}
                </ul>
              </div>

              {/* Recommendations */}
              {result.recommendations && result.recommendations.length > 0 && (
                <div className="bg-green-50 p-6 rounded-2xl">
                  <h4 className="font-bold text-green-900 mb-3 flex items-center">
                    <span className="mr-2">💡</span>
                    Recommendations
                  </h4>
                  <ul className="space-y-2">
                    {result.recommendations.map((rec, index) => (
                      <li key={index} className="text-green-800 flex items-start">
                        <span className="text-green-500 mr-2 mt-1">✓</span>
                        {rec}
                      </li>
                    ))}
                  </ul>
                </div>
              )}

              {/* Disclaimer */}
              <div className="bg-yellow-50 p-4 rounded-xl border border-yellow-200">
                <p className="text-yellow-800 text-sm">
                  <span className="font-medium">⚠️ Disclaimer:</span> This is an AI-powered assessment tool for educational purposes. 
                  Always consult with qualified healthcare professionals for medical advice and treatment decisions.
                </p>
              </div>
            </div>
          )}
        </div>
      </div>
    </div>
  )
}

export default App