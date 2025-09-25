# 🎓 Study Buddy AI

An intelligent quiz generation application powered by AI that creates personalized multiple-choice and fill-in-the-blank questions for any topic. Built with Streamlit and powered by Groq's LLM API.

![Python](https://img.shields.io/badge/Python-3.10-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-Web%20App-red.svg)
![AI](https://img.shields.io/badge/AI-Powered-green.svg)
![Docker](https://img.shields.io/badge/Docker-Ready-blue.svg)

## ✨ Features

- **🤖 AI-Powered Question Generation**: Uses Groq's LLM to generate intelligent questions
- **📝 Multiple Question Types**: 
  - Multiple Choice Questions (MCQ)
  - Fill in the Blank questions
- **🎯 Customizable Difficulty**: Easy, Medium, and Hard difficulty levels
- **📊 Interactive Quiz Interface**: Clean, user-friendly Streamlit interface
- **📈 Results Tracking**: Detailed quiz results with performance analysis
- **💾 Export Functionality**: Save quiz results to CSV files
- **🐳 Docker Support**: Containerized deployment ready
- **☸️ Kubernetes Ready**: Includes K8s manifests for production deployment
- **🔄 CI/CD Pipeline**: Jenkins pipeline for automated deployment

## 🚀 Quick Start

### Prerequisites

- Python 3.10+
- Groq API Key ([Get one here](https://console.groq.com/))

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/study-buddy-ai.git
   cd study-buddy-ai
   ```

2. **Install dependencies**
   ```bash
   pip install -e .
   ```

3. **Set up environment variables**
   ```bash
   # Create a .env file
   echo "GROQ_API_KEY=your_groq_api_key_here" > .env
   ```

4. **Run the application**
   ```bash
   streamlit run application.py
   ```

5. **Open your browser** and navigate to `http://localhost:8501`

## 🐳 Docker Deployment

### Build and Run with Docker

```bash
# Build the Docker image
docker build -t study-buddy-ai .

# Run the container
docker run -p 8501:8501 --env-file .env study-buddy-ai
```

### Docker Compose (Optional)

```yaml
version: '3.8'
services:
  study-buddy:
    build: .
    ports:
      - "8501:8501"
    environment:
      - GROQ_API_KEY=${GROQ_API_KEY}
    volumes:
      - ./results:/app/results
```

## ☸️ Kubernetes Deployment

Deploy to Kubernetes using the provided manifests:

```bash
# Apply the deployment and service
kubectl apply -f manifests/deployment.yaml
kubectl apply -f manifests/service.yaml

# Check the deployment
kubectl get pods
kubectl get services
```

## 🏗️ Project Structure

```
study-buddy-ai/
├── application.py              # Main Streamlit application
├── requirements.txt            # Python dependencies
├── setup.py                   # Package configuration
├── Dockerfile                 # Docker configuration
├── Jenkinsfile               # CI/CD pipeline
├── manifests/                 # Kubernetes manifests
│   ├── deployment.yaml
│   └── service.yaml
├── src/
│   ├── common/               # Common utilities
│   │   ├── custom_exception.py
│   │   └── logger.py
│   ├── config/               # Configuration settings
│   │   └── settings.py
│   ├── generator/            # Question generation logic
│   │   └── question_generator.py
│   ├── llm/                  # LLM client configuration
│   │   └── groq_client.py
│   ├── models/               # Data models and schemas
│   │   └── question_schemas.py
│   ├── prompts/              # AI prompt templates
│   │   └── templates.py
│   └── utils/                # Helper functions
│       └── helper.py
└── logs/                     # Application logs
```

## 🎮 How to Use

1. **Configure Quiz Settings**:
   - Select question type (Multiple Choice or Fill in the Blank)
   - Enter your topic (e.g., "Indian History", "Machine Learning")
   - Choose difficulty level (Easy, Medium, Hard)
   - Set number of questions (1-10)

2. **Generate Quiz**: Click "Generate Quiz" to create questions using AI

3. **Take the Quiz**: Answer the generated questions interactively

4. **View Results**: Get detailed feedback on your performance

5. **Export Results**: Save your quiz results to CSV for future reference

## 🔧 Configuration

The application uses environment variables for configuration:

```bash
# Required
GROQ_API_KEY=your_groq_api_key

# Optional (with defaults)
MODEL_NAME=llama-3.1-70b-versatile
TEMPERATURE=0.7
MAX_RETRIES=3
```

## 🛠️ Development

### Setting up Development Environment

```bash
# Clone and install in development mode
git clone https://github.com/yourusername/study-buddy-ai.git
cd study-buddy-ai
pip install -e .

# Run with auto-reload
streamlit run application.py --server.runOnSave true
```

### Running Tests

```bash
# Add your test commands here
python -m pytest tests/
```

## 📊 Features in Detail

### AI Question Generation
- **Smart Prompting**: Uses carefully crafted prompts for consistent question quality
- **Retry Logic**: Automatic retry mechanism for failed generations
- **Validation**: Ensures generated questions meet quality standards

### Quiz Management
- **Session State**: Maintains quiz state across interactions
- **Flexible Question Types**: Supports both MCQ and fill-in-the-blank formats
- **Real-time Evaluation**: Instant feedback on answers

### Data Export
- **CSV Export**: Save quiz results with timestamps
- **Structured Data**: Well-formatted results for analysis
- **Automatic Naming**: Unique filenames prevent overwrites

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [Groq](https://groq.com/) for providing the LLM API
- [Streamlit](https://streamlit.io/) for the web framework
- [LangChain](https://langchain.com/) for LLM integration
- [Pydantic](https://pydantic.dev/) for data validation

## 📞 Support

If you have any questions or need help, please:

1. Check the [Issues](https://github.com/yourusername/study-buddy-ai/issues) page
2. Create a new issue if your problem isn't already reported
3. Contact the maintainer

---

**Made with ❤️ by [Tarun](https://github.com/yourusername)**

*Happy Learning! 🎓*
