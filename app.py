#!/usr/bin/env python3
"""
Unified AI for Engineers Application
Serves both the UI and API endpoints on a single port
"""

from flask import Flask, request, jsonify, send_from_directory, render_template_string
from flask_cors import CORS
import json
import random
import re
import os
from pathlib import Path

app = Flask(__name__)
CORS(app)

class DemoMathematicalAssistant:
    """Demo mathematical assistant with pre-built solutions"""
    
    def __init__(self):
        self.sample_solutions = {
            'arithmetic_progression': {
                'patterns': ['ap', 'arithmetic progression', '12th term', 'nth term'],
                'solutions': [
                    {
                        'question': 'Find the 12th term of the AP: 4, 9, 14, ...',
                        'solution': 'I\'ll use the arithmetic progression formula Tₙ = a + (n-1)d.',
                        'steps': [
                            'Step 1: Identify the first term: a = 4',
                            'Step 2: Find the common difference: d = 9 - 4 = 5',
                            'Step 3: Apply the AP formula: Tₙ = a + (n-1)d',
                            'Step 4: Substitute values: T₁₂ = 4 + (12-1)×5',
                            'Step 5: Calculate: T₁₂ = 4 + 11×5 = 4 + 55',
                            'Step 6: Final answer: T₁₂ = 59'
                        ],
                        'concepts': ['Arithmetic Progression', 'Common Difference', 'nth Term Formula'],
                        'verification': 'Check: The sequence is 4, 9, 14, 19, 24, 29, 34, 39, 44, 49, 54, 59'
                    }
                ]
            },
            'logarithms': {
                'patterns': ['log', 'logarithm', 'log10', 'log₁₀'],
                'solutions': [
                    {
                        'question': 'What is the value of log₁₀(1000)?',
                        'solution': 'I\'ll use the definition of logarithms to solve this.',
                        'steps': [
                            'Step 1: Recall that log₁₀(x) asks "10 to what power equals x?"',
                            'Step 2: We need to find: 10^? = 1000',
                            'Step 3: Express 1000 as a power of 10: 1000 = 10³',
                            'Step 4: Therefore: log₁₀(1000) = log₁₀(10³) = 3',
                            'Step 5: Final answer: log₁₀(1000) = 3'
                        ],
                        'concepts': ['Logarithms', 'Powers of 10', 'Logarithm Definition'],
                        'verification': 'Check: 10³ = 10 × 10 × 10 = 1000 ✓'
                    }
                ]
            },
            'trigonometry': {
                'patterns': ['sin', 'cos', 'tan', 'trigonometric', 'sin(90°)', 'sin(90)'],
                'solutions': [
                    {
                        'question': 'What is the value of sin(90°)?',
                        'solution': 'I\'ll use the unit circle and trigonometric definitions.',
                        'steps': [
                            'Step 1: Recall that sin(θ) represents the y-coordinate on the unit circle',
                            'Step 2: At 90°, we are at the top of the unit circle',
                            'Step 3: The coordinates at 90° are (0, 1)',
                            'Step 4: Therefore: sin(90°) = y-coordinate = 1',
                            'Step 5: Final answer: sin(90°) = 1'
                        ],
                        'concepts': ['Unit Circle', 'Trigonometric Functions', 'Special Angles'],
                        'verification': 'This is a fundamental trigonometric value that should be memorized.'
                    }
                ]
            },
            'complex_numbers': {
                'patterns': ['polar form', 'complex number', 'z =', '1 + i', 'polar coordinates', 'modulus', 'argument'],
                'solutions': [
                    {
                        'question': 'Find the polar form of the complex number z = 1 + i',
                        'solution': 'I\'ll convert this complex number to polar form using r = |z| and θ = arg(z).',
                        'steps': [
                            'Step 1: Identify the complex number: z = 1 + i (where a = 1, b = 1)',
                            'Step 2: Calculate the modulus: r = |z| = √(a² + b²) = √(1² + 1²) = √2',
                            'Step 3: Calculate the argument: θ = arctan(b/a) = arctan(1/1) = arctan(1) = π/4',
                            'Step 4: Since both a > 0 and b > 0, z is in the first quadrant',
                            'Step 5: Express in polar form: z = r(cos θ + i sin θ)',
                            'Step 6: Substitute values: z = √2(cos(π/4) + i sin(π/4))',
                            'Step 7: Final answer: z = √2 ∠ π/4 or z = √2 e^(iπ/4)'
                        ],
                        'concepts': ['Complex Numbers', 'Polar Form', 'Modulus', 'Argument', 'Euler\'s Formula'],
                        'verification': 'Check: √2 cos(π/4) + i√2 sin(π/4) = √2(1/√2) + i√2(1/√2) = 1 + i ✓'
                    }
                ]
            },
            'differential_equations': {
                'patterns': ['differential equation', 'ode', 'dy/dx', 'solve differential'],
                'solutions': [
                    {
                        'question': 'Solve the first-order ODE: dy/dx + 2y = 4',
                        'solution': 'I\'ll solve this linear first-order ODE using integrating factor method.',
                        'steps': [
                            'Step 1: Identify as linear first-order ODE: dy/dx + P(x)y = Q(x)',
                            'Step 2: Here P(x) = 2, Q(x) = 4',
                            'Step 3: Find integrating factor: μ(x) = e^(∫P(x)dx) = e^(2x)',
                            'Step 4: Multiply equation by μ(x): e^(2x)dy/dx + 2e^(2x)y = 4e^(2x)',
                            'Step 5: Left side is d/dx[ye^(2x)]: d/dx[ye^(2x)] = 4e^(2x)',
                            'Step 6: Integrate: ye^(2x) = ∫4e^(2x)dx = 2e^(2x) + C',
                            'Step 7: Final answer: y = 2 + Ce^(-2x)'
                        ],
                        'concepts': ['Differential Equations', 'Integrating Factor', 'Linear ODEs'],
                        'verification': 'Check by substituting back into original equation.'
                    }
                ]
            },
            'algebra': {
                'patterns': ['solve', 'equation', 'quadratic', '='],
                'solutions': [
                    {
                        'question': 'Solve the quadratic equation 2x² - 7x + 3 = 0',
                        'solution': 'I\'ll solve this using the quadratic formula.',
                        'steps': [
                            'Step 1: Identify coefficients: a = 2, b = -7, c = 3',
                            'Step 2: Apply quadratic formula: x = [-b ± √(b² - 4ac)] / (2a)',
                            'Step 3: Calculate discriminant: b² - 4ac = (-7)² - 4(2)(3) = 49 - 24 = 25',
                            'Step 4: Since discriminant > 0, we have two real solutions',
                            'Step 5: x = [7 ± √25] / (2·2) = [7 ± 5] / 4',
                            'Step 6: x₁ = (7 + 5)/4 = 12/4 = 3',
                            'Step 7: x₂ = (7 - 5)/4 = 2/4 = 1/2',
                            'Step 8: Verification: 2(3)² - 7(3) + 3 = 18 - 21 + 3 = 0 ✓'
                        ],
                        'concepts': ['Quadratic Formula', 'Discriminant', 'Real Solutions'],
                        'verification': 'Substitute both solutions back into the original equation to verify.'
                    }
                ]
            }
        }
    
    def identify_problem_type(self, question):
        """Identify the type of mathematical problem with improved pattern matching"""
        question_lower = question.lower()
        
        # Priority matching for specific problems (most specific first)
        if 'polar form' in question_lower and 'complex' in question_lower:
            return 'complex_numbers'
        elif 'differential equation' in question_lower or ('dy/dx' in question_lower and 'y =' in question_lower):
            return 'differential_equations'
        elif any(pattern in question_lower for pattern in ['12th term', 'ap', 'arithmetic progression', 'nth term']):
            return 'arithmetic_progression'
        elif any(pattern in question_lower for pattern in ['log10', 'log₁₀', 'logarithm', 'log(1000)']):
            return 'logarithms'
        elif any(pattern in question_lower for pattern in ['sin(90', 'sin 90', 'cos(', 'tan(']) and 'quadratic' not in question_lower:
            return 'trigonometry'
        elif any(pattern in question_lower for pattern in ['quadratic equation', '2x²', 'x²']) and 'complex' not in question_lower and 'differential' not in question_lower:
            return 'algebra'
        
        return 'general'
    
    def solve_problem(self, question):
        """Solve mathematical problem with enhanced explanations"""
        try:
            problem_type = self.identify_problem_type(question)
            
            # Get appropriate solution template
            if problem_type in self.sample_solutions:
                solutions = self.sample_solutions[problem_type]['solutions']
                solution_template = solutions[0]
                
                return {
                    'success': True,
                    'question': question,
                    'problem_type': problem_type,
                    'solution': solution_template['solution'],
                    'steps': solution_template['steps'],
                    'mathematical_concepts': solution_template['concepts'],
                    'verification': solution_template['verification'],
                    'confidence': 'high',
                    'api_version': '2.0'
                }
            else:
                # General mathematical response
                return {
                    'success': True,
                    'question': question,
                    'problem_type': 'general',
                    'solution': 'I\'ll help you solve this step-by-step. Let me break down the problem and provide a clear mathematical explanation.',
                    'steps': [
                        'Step 1: Analyze the given problem and identify key information',
                        'Step 2: Determine the appropriate mathematical method or formula',
                        'Step 3: Apply the method systematically',
                        'Step 4: Simplify and solve for the unknown',
                        'Step 5: Verify the solution and check for reasonableness'
                    ],
                    'mathematical_concepts': ['Problem Analysis', 'Mathematical Reasoning', 'Solution Verification'],
                    'verification': 'Always check your solution by substituting back or using alternative methods.',
                    'confidence': 'medium',
                    'api_version': '2.0'
                }
                
        except Exception as e:
            return {
                'success': False,
                'error': f'Error processing question: {str(e)}',
                'question': question
            }

# Initialize the demo assistant
demo_assistant = DemoMathematicalAssistant()

# ── UI ROUTES ──

@app.route('/')
def index():
    """Serve the main UI"""
    try:
        ui_path = Path(__file__).parent / 'ui' / 'index.html'
        if ui_path.exists():
            with open(ui_path, 'r', encoding='utf-8') as f:
                content = f.read()
            # Update API calls to use relative paths
            content = content.replace('http://localhost:5001/api/solve', '/api/solve')
            return content
        else:
            return "UI file not found", 404
    except Exception as e:
        return f"Error loading UI: {str(e)}", 500

# ── API ROUTES ──

@app.route('/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'service': 'AI for Engineers - Unified Application',
        'message': 'UI and API running on single port',
        'features': ['Enhanced Mathematical Reasoning', 'Interactive Learning Games', 'ChatGPT-like Interface']
    })
@app.route("/settings/<email>", methods=["POST", "GET"])
def settings(email):
    if request.method == "POST":
        data = request.json
        users[email + "_settings"] = data
        return jsonify({"message": "Settings updated"}), 200

    if request.method == "GET":
        settings = users.get(email + "_settings", {"theme": "light", "notifications": True})
        return jsonify(settings)

@app.route('/api/solve', methods=['POST'])
def solve_problem():
    """Enhanced mathematical problem solving endpoint"""
    try:
        data = request.get_json()
        
        if not data or 'question' not in data:
            return jsonify({
                'success': False,
                'error': 'Please provide a question in the request body'
            }), 400
        
        question = data['question'].strip()
        
        if not question:
            return jsonify({
                'success': False,
                'error': 'Question cannot be empty'
            }), 400
        
        # Solve the mathematical problem
        result = demo_assistant.solve_problem(question)
        
        return jsonify(result)
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': 'Internal server error occurred while processing your request'
        }), 500

@app.route('/api/problem-types', methods=['GET'])
def get_problem_types():
    """Get supported mathematical problem types"""
    return jsonify({
        'supported_types': [
            'Calculus (Integration, Differentiation, Limits)',
            'Algebra (Equations, Factoring, Systems)', 
            'Geometry (Area, Volume, Trigonometry)',
            'Statistics (Probability, Descriptive Statistics)',
            'Linear Algebra (Matrices, Vectors, Determinants)',
            'Differential Equations',
            'Complex Numbers',
            'Discrete Mathematics'
        ],
        'features': [
            'Step-by-step solutions',
            'Mathematical concept identification', 
            'Solution verification',
            'Educational explanations',
            'Interactive learning games'
        ]
    })

@app.route('/api/examples', methods=['GET'])
def get_examples():
    """Get example mathematical problems"""
    examples = [
        {
            'question': 'Find the polar form of the complex number z = 1 + i',
            'type': 'Complex Numbers',
            'difficulty': 'Intermediate'
        },
        {
            'question': 'Solve the differential equation dy/dx + 2y = 4',
            'type': 'Differential Equations',
            'difficulty': 'Advanced'
        },
        {
            'question': 'Solve the quadratic equation 2x² - 7x + 3 = 0',
            'type': 'Algebra', 
            'difficulty': 'Intermediate'
        },
        {
            'question': 'Find the 12th term of the AP: 4, 9, 14, ...',
            'type': 'Arithmetic Progression',
            'difficulty': 'Beginner'
        }
    ]
    return jsonify({'examples': examples})

if __name__ == '__main__':
    print("🚀 AI for Engineers - Unified Application")
    print("=" * 60)
    print("🎮 Single URL for complete application")
    print("🧮 Enhanced Mathematical Reasoning System")
    print("📚 ChatGPT-like Interface with Learning Games")
    print("=" * 60)
    print("✨ Features:")
    print("  • Complete step-by-step mathematical solutions")
    print("  • Interactive learning games (Step Builder, Concept Matcher, etc.)")
    print("  • Persistent chat history with sidebar")
    print("  • Voice input and camera functionality")
    print("  • Mathematical background patterns")
    print("  • M1-M4 engineering mathematics curriculum")
    print("=" * 60)
    print("🌐 Application URL: http://localhost:8080")
    print("📖 API Endpoints:")
    print("  POST /api/solve - Solve mathematical problems")
    print("  GET  /health - Health check")
    print("  GET  /api/problem-types - Supported problem types")
    print("  GET  /api/examples - Example problems")
    print("=" * 60)
    print("🛑 Press Ctrl+C to stop the server")
    print("=" * 60)
    
    app.run(host='0.0.0.0', port=8080, debug=True)
