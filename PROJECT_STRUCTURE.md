# 🏗️ AI for Engineers - Project Structure

## 📁 Directory Organization

```
AI-For-Engineers/
├── 📚 Core Application
│   ├── api/                    # Backend API services
│   │   ├── app.py             # Main Flask API
│   │   ├── demo_app.py        # Demo application
│   │   ├── demo_math_api.py   # Enhanced mathematical API
│   │   └── enhanced_math_api.py
│   │
│   ├── ui/                     # Main user interface
│   │   └── index.html         # ChatGPT-like interface with games
│   │
│   ├── frontend/              # React application
│   │   ├── src/               # React source code
│   │   ├── public/            # Static assets
│   │   ├── package.json       # Dependencies
│   │   └── vite.config.js     # Vite configuration
│   │
│   └── servers/               # Server utilities
│       ├── serve_ui.py        # UI server (port 8080)
│       └── server.py          # Alternative server
│
├── 🧮 Machine Learning
│   ├── training/              # Model training
│   │   ├── enhanced_math_model.py
│   │   ├── train_model.py
│   │   ├── inference.py
│   │   └── config.py
│   │
│   ├── data/                  # Datasets
│   │   ├── processed/         # Processed datasets
│   │   ├── enhanced_math_dataset.py
│   │   └── engineering_curriculum_dataset.py
│   │
│   └── models/                # Trained models
│       ├── checkpoints/       # Model checkpoints
│       └── saved_models/      # Final models
│
├── 🔧 Development & Testing
│   ├── examples/              # Code examples
│   │   ├── demo_model_structure.py
│   │   ├── example_usage.py
│   │   └── test_api.html
│   │
│   ├── demos/                 # Demo applications
│   │   ├── app.html           # Single-page demo
│   │   ├── demo.html          # Basic demo
│   │   └── test_integration.html
│   │
│   ├── scripts/               # Utility scripts
│   │   ├── check_syntax.py
│   │   └── verify_structure.py
│   │
│   └── tests/                 # Test files
│
├── 📖 Documentation
│   ├── docs/                  # Project documentation
│   │   ├── ARCHITECTURE.md
│   │   ├── SETUP_GUIDE.md
│   │   ├── QUICKSTART.md
│   │   └── TROUBLESHOOTING.md
│   │
│   ├── PROJECT_STRUCTURE.md   # This file
│   ├── NAVIGATION.md          # Navigation guide
│   └── README.md              # Main documentation
│
├── 🚀 Deployment
│   ├── deployment/            # Deployment configurations
│   │   ├── Dockerfile
│   │   └── docker-compose.yml
│   │
│   └── logs/                  # Application logs
│
└── 📋 Configuration
    ├── .gitignore             # Git ignore rules
    ├── LICENSE                # Project license
    └── requirements.txt       # Python dependencies
```

## 🌐 Application Servers

### Primary Interfaces
- **Enhanced UI**: `http://localhost:8080` (ChatGPT-like interface)
  - Start: `python3 servers/serve_ui.py`
  - Features: Sidebar, games, chat history, voice input

- **React Frontend**: `http://localhost:3000` (Modern React app)
  - Start: `cd frontend && npm start`
  - Features: Dark theme, voice input, responsive design

- **Mathematical API**: `http://localhost:5001` (Backend engine)
  - Start: `python3 api/demo_math_api.py`
  - Features: M1-M4 mathematics, step-by-step solutions

### Demo Interfaces
- **Single Page Demo**: `demos/app.html` (Standalone demo)
- **Basic Demo**: `demos/demo.html` (Simple interface)
- **Integration Test**: `demos/test_integration.html` (API testing)

## 🎮 Key Features by Directory

### `/ui/` - Main Interface
- ChatGPT-style sidebar with persistent chat history
- Interactive learning games (Step Builder, Concept Matcher, etc.)
- Voice input and camera functionality
- Mathematical background patterns
- User profile and settings

### `/api/` - Backend Services
- Enhanced mathematical reasoning engine
- Support for complex numbers, differential equations
- M1-M4 engineering mathematics curriculum
- Step-by-step solution generation
- Concept identification and verification

### `/frontend/` - React Application
- Modern React with Vite build system
- Dark theme with glassmorphism effects
- Voice recognition and media upload
- Responsive design for all devices
- Hot module replacement for development

### `/training/` - Machine Learning
- Custom mathematical reasoning models
- Training pipelines for engineering mathematics
- Model checkpoints and saved states
- Inference engines for real-time solving

## 🚀 Quick Start Commands

```bash
# Start Enhanced UI (Recommended)
python3 servers/serve_ui.py

# Start React Frontend
cd frontend && npm start

# Start Mathematical API
python3 api/demo_math_api.py

# Install Dependencies
pip install -r requirements.txt
cd frontend && npm install
```

## 📝 File Naming Conventions

- **Servers**: `serve_*.py` - Server applications
- **APIs**: `*_api.py` - API endpoints and services  
- **Models**: `*_model.py` - Machine learning models
- **Datasets**: `*_dataset.py` - Data processing scripts
- **Demos**: `*.html` - Standalone demo files
- **Docs**: `*.md` - Markdown documentation

## 🔄 Development Workflow

1. **Backend Development**: Work in `/api/` and `/training/`
2. **Frontend Development**: Work in `/frontend/` or `/ui/`
3. **Testing**: Use files in `/demos/` and `/examples/`
4. **Documentation**: Update files in `/docs/`
5. **Deployment**: Configure in `/deployment/`

This structure ensures clean separation of concerns, easy navigation, and professional organization suitable for team collaboration and production deployment.