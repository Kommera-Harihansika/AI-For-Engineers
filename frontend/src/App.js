import React, { useState, useRef, useEffect } from 'react';
import './App.css';

function App() {
  const [question, setQuestion] = useState('');
  const [answer, setAnswer] = useState(null);
  const [loading, setLoading] = useState(false);
  const [showGames, setShowGames] = useState(false);
  const [isRecording, setIsRecording] = useState(false);
  const [mediaRecorder, setMediaRecorder] = useState(null);
  const fileInputRef = useRef(null);
  const recognitionRef = useRef(null);

  // Initialize speech recognition
  useEffect(() => {
    if ('webkitSpeechRecognition' in window || 'SpeechRecognition' in window) {
      const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
      recognitionRef.current = new SpeechRecognition();
      recognitionRef.current.continuous = false;
      recognitionRef.current.interimResults = false;
      recognitionRef.current.lang = 'en-US';

      recognitionRef.current.onresult = (event) => {
        const transcript = event.results[0][0].transcript;
        setQuestion(prev => prev + ' ' + transcript);
        setIsRecording(false);
      };

      recognitionRef.current.onerror = () => {
        setIsRecording(false);
      };

      recognitionRef.current.onend = () => {
        setIsRecording(false);
      };
    }
  }, []);

  const startVoiceRecording = () => {
    if (recognitionRef.current && !isRecording) {
      setIsRecording(true);
      recognitionRef.current.start();
    }
  };

  const stopVoiceRecording = () => {
    if (recognitionRef.current && isRecording) {
      recognitionRef.current.stop();
      setIsRecording(false);
    }
  };

  const handleVoiceToggle = () => {
    if (isRecording) {
      stopVoiceRecording();
    } else {
      startVoiceRecording();
    }
  };

  const handleFileUpload = (event) => {
    const file = event.target.files[0];
    if (file) {
      // Handle different file types
      if (file.type.startsWith('image/')) {
        // For images, you could implement OCR or image analysis
        setQuestion(prev => prev + ` [Image uploaded: ${file.name}]`);
      } else if (file.type.startsWith('audio/')) {
        // For audio files, you could implement audio transcription
        setQuestion(prev => prev + ` [Audio uploaded: ${file.name}]`);
      } else {
        setQuestion(prev => prev + ` [File uploaded: ${file.name}]`);
      }
    }
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    setAnswer(null);
    
    try {
      // Create abort controller for timeout
      const controller = new AbortController();
      const timeoutId = setTimeout(() => controller.abort(), 60000); // 60 second timeout
      
      // Call API directly (not through proxy)
      const apiUrl = 'http://localhost:5001/api/solve';
      
      const response = await fetch(apiUrl, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ question }),
        signal: controller.signal
      });
      
      clearTimeout(timeoutId);
      
      if (!response.ok) {
        throw new Error(`Server error: ${response.status}`);
      }
      
      const data = await response.json();
      setAnswer(data);
    } catch (error) {
      if (error.name === 'AbortError') {
        setAnswer({ 
          error: 'Request timed out. The model is still learning and may take a while to respond. Please try again with a simpler question.' 
        });
      } else {
        setAnswer({ 
          error: `Failed to get answer: ${error.message}. Make sure the backend API is running on port 5001.` 
        });
      }
    }
    setLoading(false);
  };

  const openGames = () => {
    setShowGames(true);
  };

  const closeGames = () => {
    setShowGames(false);
  };

  const loadExample = (exampleQuestion) => {
    setQuestion(exampleQuestion);
  };

  if (showGames) {
    return (
      <div className="games-modal">
        <div className="games-content">
          <h2>🎮 Interactive Learning Games</h2>
          <p>Choose a game to help you understand mathematical concepts better!</p>
          
          <div className="games-grid">
            <div className="game-card" onClick={() => alert('🧩 Step Builder Game\n\nThis game helps you arrange solution steps in the correct order to understand the logical flow of mathematical problem solving.')}>
              <div className="game-icon">🧩</div>
              <h3>Step Builder</h3>
              <p>Arrange solution steps in correct order</p>
            </div>
            
            <div className="game-card" onClick={() => alert('🎯 Concept Matcher Game\n\nThis game helps you match mathematical concepts with their definitions to build vocabulary and understanding.')}>
              <div className="game-icon">🎯</div>
              <h3>Concept Matcher</h3>
              <p>Match concepts with definitions</p>
            </div>
            
            <div className="game-card" onClick={() => alert('⚡ Formula Quest Game\n\nThis game helps you complete mathematical formulas and understand their structure and application.')}>
              <div className="game-icon">⚡</div>
              <h3>Formula Quest</h3>
              <p>Complete mathematical formulas</p>
            </div>
            
            <div className="game-card" onClick={() => alert('📊 Visual Solver Game\n\nThis game provides interactive visualizations to help you understand abstract mathematical concepts.')}>
              <div className="game-icon">📊</div>
              <h3>Visual Solver</h3>
              <p>Interactive problem visualization</p>
            </div>
          </div>
          
          <button className="close-games-btn" onClick={closeGames}>
            ← Back to Problem Solving
          </button>
        </div>
      </div>
    );
  }

  return (
    <div className="app">
      <header>
        <h1>🧮 AI for Engineers</h1>
        <p>Your intelligent learning assistant for step-by-step solutions</p>
        <p className="enhanced-tagline">✨ Enhanced with M1-M4 Engineering Mathematics & Gamified Learning</p>
      </header>
      
      <main>
        {/* Example Problems */}
        <div className="examples-section">
          <h3>📚 Try These Engineering Mathematics Problems:</h3>
          <div className="examples-grid">
            <button className="example-btn" onClick={() => loadExample('Find the 12th term of the AP: 4, 9, 14, ...')}>
              📐 Arithmetic Progression: Find 12th term of AP
            </button>
            <button className="example-btn" onClick={() => loadExample('What is the value of log10(1000)?')}>
              📊 Logarithms: log₁₀(1000) = ?
            </button>
            <button className="example-btn" onClick={() => loadExample('What is the value of sin(90°)?')}>
              📈 Trigonometry: sin(90°) = ?
            </button>
            <button className="example-btn" onClick={() => loadExample('Find det(A) where A = [[2,3],[1,4]]')}>
              🔲 Matrix: Determinant of 2×2 matrix
            </button>
            <button className="example-btn" onClick={() => loadExample('Differentiate y = 5x⁴ - 3x²')}>
              📈 Calculus: Differentiate polynomial
            </button>
            <button className="example-btn" onClick={() => loadExample('Evaluate ∫(3x²)dx')}>
              📐 Integration: Integrate 3x²
            </button>
            <button className="example-btn" onClick={() => loadExample('If a fuse protects a 15-ohm heater and is rated at 10 amperes, what is the maximum voltage allowed?')}>
              ⚡ Electrical: Ohm\'s Law problem
            </button>
            <button className="example-btn" onClick={() => loadExample('Find the distance an object falls under gravity (g = 9.8 m/s²) after 10 seconds')}>
              🌍 Physics: Free fall distance
            </button>
            <button className="example-btn" onClick={() => loadExample('Find the polar form of the complex number z = 1 + i')}>
              🔢 Complex Numbers: Polar form of z = 1 + i
            </button>
            <button className="example-btn" onClick={() => loadExample('Solve the differential equation dy/dx + 2y = 4')}>
              📊 Differential Equations: First-order ODE
            </button>
          </div>
        </div>

        <form onSubmit={handleSubmit}>
          <div className="input-container">
            <textarea
              value={question}
              onChange={(e) => setQuestion(e.target.value)}
              placeholder="Ask your engineering mathematics question... (e.g., 'Find the 12th term of the AP: 4, 9, 14, ...' or 'What is log10(1000)?')"
              rows="4"
            />
            <div className="input-controls">
              <button
                type="button"
                className={`voice-btn ${isRecording ? 'recording' : ''}`}
                onClick={handleVoiceToggle}
                title={isRecording ? 'Stop recording' : 'Start voice input'}
              >
                {isRecording ? '⏹️' : '🎤'}
              </button>
              <button
                type="button"
                className="upload-btn"
                onClick={triggerFileUpload}
                title="Upload file"
              >
                📎
              </button>
              <input
                ref={fileInputRef}
                type="file"
                className="upload-input"
                onChange={handleFileUpload}
                accept="image/*,audio/*,.pdf,.doc,.docx,.txt"
              />
            </div>
          </div>
          <div className="button-group">
            <button type="submit" disabled={loading}>
              {loading ? '🔄 Solving...' : '🚀 Get Step-by-Step Solution'}
            </button>
            <button type="button" className="games-btn" onClick={openGames}>
              🎮 Need Help? Play Learning Games!
            </button>
          </div>
        </form>

        {answer && (
          <div className="answer-box">
            <h2>📝 Solution</h2>
            {answer.error ? (
              <div className="error">
                <p>{answer.error}</p>
                <div className="error-help">
                  <h4>💡 Troubleshooting:</h4>
                  <ul>
                    <li>Make sure the API server is running: <code>python3 api/demo_math_api.py</code></li>
                    <li>Check that port 5001 is available</li>
                    <li>Try one of the example problems above</li>
                  </ul>
                </div>
              </div>
            ) : (
              <div className="solution">
                <div className="question-display">
                  <strong>📋 Question:</strong> {answer.question}
                </div>
                
                <div className="solution-display">
                  <strong>💡 Solution:</strong> {answer.solution}
                </div>

                {answer.steps && answer.steps.length > 0 && (
                  <div className="steps-section">
                    <strong>🔢 Step-by-Step Breakdown:</strong>
                    <ol className="steps-list">
                      {answer.steps.map((step, idx) => (
                        <li key={idx} className="step-item">{step}</li>
                      ))}
                    </ol>
                  </div>
                )}

                {answer.mathematical_concepts && answer.mathematical_concepts.length > 0 && (
                  <div className="concepts-section">
                    <strong>🧠 Mathematical Concepts:</strong>
                    <div className="concepts-tags">
                      {answer.mathematical_concepts.map((concept, idx) => (
                        <span key={idx} className="concept-tag">{concept}</span>
                      ))}
                    </div>
                  </div>
                )}

                {answer.mathematical_tips && answer.mathematical_tips.length > 0 && (
                  <div className="tips-section">
                    <strong>💡 Mathematical Tips:</strong>
                    <ul className="tips-list">
                      {answer.mathematical_tips.map((tip, idx) => (
                        <li key={idx}>{tip}</li>
                      ))}
                    </ul>
                  </div>
                )}

                {answer.verification && (
                  <div className="verification-section">
                    <strong>✅ Verification:</strong>
                    <p>{answer.verification}</p>
                  </div>
                )}

                <div className="model-info">
                  <span className="model-badge">{answer.model_type || 'Enhanced Mathematical AI'}</span>
                  <span className="confidence-badge">Confidence: {answer.confidence || 'High'}</span>
                  <span className="api-badge">API v{answer.api_version || '2.0'}</span>
                </div>
              </div>
            )}
          </div>
        )}

        <div className="features-info">
          <h3>🌟 Enhanced Features:</h3>
          <div className="features-grid">
            <div className="feature">
              <span className="feature-icon">🎯</span>
              <div>
                <strong>Step-by-Step Solutions</strong>
                <p>Detailed mathematical reasoning for every problem</p>
              </div>
            </div>
            <div className="feature">
              <span className="feature-icon">🧠</span>
              <div>
                <strong>Concept Identification</strong>
                <p>Automatically identifies mathematical concepts used</p>
              </div>
            </div>
            <div className="feature">
              <span className="feature-icon">✅</span>
              <div>
                <strong>Solution Verification</strong>
                <p>Methods to check and verify your answers</p>
              </div>
            </div>
            <div className="feature">
              <span className="feature-icon">🎮</span>
              <div>
                <strong>Interactive Learning Games</strong>
                <p>Fun games to help understand difficult concepts</p>
              </div>
            </div>
          </div>
        </div>
      </main>
    </div>
  );
}

export default App;
