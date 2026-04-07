# 🧭 AI for Engineers - Navigation Guide

## 🚀 Quick Access

### 🌐 **Main Applications**
- **Enhanced UI**: `http://localhost:8080` → Start with `python3 servers/serve_ui.py`
- **React Frontend**: `http://localhost:3000` → Start with `cd frontend && npm start`  
- **Mathematical API**: `http://localhost:5001` → Start with `python3 api/demo_math_api.py`

### 📁 **Key Directories**
- **`/ui/`** - Main ChatGPT-like interface with games and chat history
- **`/api/`** - Backend mathematical reasoning engines
- **`/frontend/`** - Modern React application with dark theme
- **`/training/`** - Machine learning models and training scripts
- **`/docs/`** - Complete project documentation

## 🎯 **What to Use When**

### 👨‍🎓 **For Students & Learning**
- **Start Here**: `python3 servers/serve_ui.py` → `http://localhost:8080`
- **Features**: Interactive games, chat history, voice input, step-by-step solutions

### 👨‍💻 **For Development**
- **React Development**: `cd frontend && npm start` → `http://localhost:3000`
- **API Development**: `python3 api/demo_math_api.py` → `http://localhost:5001`
- **Testing**: Use files in `/demos/` directory

### 📚 **For Documentation**
- **Setup Guide**: `docs/SETUP_GUIDE.md`
- **Architecture**: `docs/ARCHITECTURE.md`
- **Project Structure**: `PROJECT_STRUCTURE.md`
- **Troubleshooting**: `docs/TROUBLESHOOTING.md`

## 📁 Directory Guide

| Directory | Purpose | Key Files |
|-----------|---------|-----------|
| [`/ui/`](ui/) | Main interface | `index.html` (ChatGPT-like UI) |
| [`/api/`](api/) | Backend services | `demo_math_api.py`, `app.py` |
| [`/frontend/`](frontend/) | React application | `src/App.js`, `package.json` |
| [`/servers/`](servers/) | Server utilities | `serve_ui.py`, `server.py` |
| [`/training/`](training/) | ML models | `enhanced_math_model.py` |
| [`/data/`](data/) | Datasets | `processed/*.json` |
| [`/demos/`](demos/) | Demo files | `app.html`, `demo.html` |
| [`/examples/`](examples/) | Code examples | `*.py`, `test_api.html` |
| [`/docs/`](docs/) | Documentation | All `.md` files |

## 🎮 **Interactive Features**

### 🎯 **Learning Games** (Available in Enhanced UI)
- **🧩 Step Builder**: Arrange solution steps in correct order
- **🎯 Concept Matcher**: Match mathematical concepts with definitions
- **⚡ Formula Quest**: Complete mathematical formulas
- **📊 Visual Solver**: Interactive mathematical visualizations

### 🧮 **Mathematical Capabilities**
- **M1**: Differential/Integral Calculus, Matrix Theory
- **M2**: Vector Calculus, ODEs, Complex Numbers, Laplace Transforms  
- **M3**: Fourier Analysis, PDEs, Probability/Statistics, Z-Transforms
- **M4**: Numerical Methods, Optimization, Discrete Mathematics

## 🔄 **Development Workflow**

1. **Start API Server**: `python3 api/demo_math_api.py`
2. **Choose Interface**:
   - Enhanced UI: `python3 servers/serve_ui.py`
   - React App: `cd frontend && npm start`
3. **Test Features**: Use mathematical problems and games
4. **Check Documentation**: Refer to `/docs/` for detailed guides

## 📖 **Documentation Structure**

### Getting Started
- [QUICKSTART.md](docs/QUICKSTART.md) - 5-minute setup
- [SETUP_GUIDE.md](docs/SETUP_GUIDE.md) - Detailed installation
- [PROJECT_STRUCTURE.md](PROJECT_STRUCTURE.md) - Complete organization guide

### Technical Details
- [ARCHITECTURE.md](docs/ARCHITECTURE.md) - System design
- [ENHANCED_MATH_SYSTEM.md](docs/ENHANCED_MATH_SYSTEM.md) - Mathematical AI
- [GAMIFIED_LEARNING_SYSTEM.md](docs/GAMIFIED_LEARNING_SYSTEM.md) - Learning games

### Development
- [IMPLEMENTATION_SUMMARY.md](docs/IMPLEMENTATION_SUMMARY.md) - Technical summary
- [TROUBLESHOOTING.md](docs/TROUBLESHOOTING.md) - Common issues
- [CURRENT_STATUS.md](docs/CURRENT_STATUS.md) - Development status

## 🚀 **Recommended Starting Points**

### **New Users**
1. Read `README.md` for overview
2. Follow `docs/SETUP_GUIDE.md` for installation
3. Start with Enhanced UI: `python3 servers/serve_ui.py`

### **Developers**  
1. Review `PROJECT_STRUCTURE.md` for organization
2. Check `docs/ARCHITECTURE.md` for technical details
3. Start React development: `cd frontend && npm start`

### **Students**
1. Launch Enhanced UI for best learning experience
2. Try interactive games for concept understanding
3. Use voice input for hands-free problem solving

## 🆘 Need Help?

1. **Check documentation** in `/docs/` folder
2. **Try demos** in `/demos/` folder  
3. **Run troubleshooting** guide: [docs/TROUBLESHOOTING.md](docs/TROUBLESHOOTING.md)
4. **Create GitHub issue** for bugs or questions

---

**💡 Tip**: Always ensure the API server (`python3 api/demo_math_api.py`) is running before starting any frontend interface for full functionality.

*Happy coding! 🚀*