# 🌾 AgerAmicus — AI-Powered Farming Assistant

An intelligent, multimodal AI assistant designed to empower farmers and agronomists with real-time insights, crop recommendations, and plant disease detection. Developed for the **Azure AI Hackathon**, AgerAmicus brings AI to the field with powerful yet accessible tools.

---

## 💡 Inspiration
Modern agriculture faces critical challenges: crop diseases, unpredictable weather, and low yields. Smallholder farmers often lack access to timely agronomic advice. **AgerAmicus** was born to bridge this gap with an AI assistant that sees, understands, and responds — just like a field expert.

---

## 🚀 What It Does

- 📸 **Plant Disease Detection**  
  Upload a plant image — get instant disease classification and confidence score.

- 🤖 **AI Chatbot (AgroNLP)**  
  Ask anything! Get real-time recommendations on soil health, irrigation, pest control, and more.

- 📊 (Coming Soon) **Yield Prediction & Fertilizer Engine**  
  Integrating soil/weather data for smarter planning.

---

## 🛠️ How We Built It

- **Frontend**: React-based UI (in progress)
- **Backend**: FastAPI + Azure OpenAI integration
- **Model**: Custom CNN model trained on the [PlantVillage dataset](https://www.kaggle.com/emmarex/plantdisease)
- **Chatbot**: GPT-35-Turbo via Azure OpenAI
- **Hosting**: Azure (OpenAI, App Services)
- **Dev Tools**: Python, TensorFlow, VS Code, GitHub Copilot

---

## 🧠 What We Learned

- Azure OpenAI integration with FastAPI and authentication nuances.
- Dataset preprocessing, augmentation, and model tuning for real-world performance.
- Prompt engineering for agronomic language and accurate AI responses.
- Effective Git history management (including large file cleanup via `git filter-repo`).

---

## 🚧 Challenges We Faced

- ⚠️ Model deployment constraints in limited time
- 🔐 Azure authentication & resource access issues
- 🧱 Large files blocking GitHub uploads — required history rewriting
- 📦 Optimizing dependencies, environment isolation, and disk space

---

## ✅ Accomplishments

- 🚀 Deployed a working FastAPI backend for both image & text features
- 🧠 Trained a custom crop disease classifier with strong accuracy
- 🤝 Integrated GPT-based chatbot with real-time Q&A flow
- 🛠️ Maintained modular and scalable repo structure for future additions

---

## 🔮 What's Next for AgerAmicus

- 🌱 Build full React-based frontend for seamless farmer UX
- 📦 Convert backend into an Azure App Service API
- 📈 Add satellite/weather/yield forecasting modules
- 🧪 Fine-tune foundation models with agriculture-specific datasets

---

## 💻 Tech Stack

| Category           | Technologies Used                                   |
|-------------------|-----------------------------------------------------|
| **Languages**      | Python, JavaScript                                  |
| **Frameworks**     | FastAPI, React (UI), TensorFlow                     |
| **Cloud Services** | Azure OpenAI, Azure Cognitive Services              |
| **ML/AI**          | CNN (image classification), GPT-35-Turbo (chatbot) |
| **Dev Tools**      | GitHub, VS Code, GitHub Copilot, pipenv             |

---

## 📁 Repo Structure
AgerAmicus/ ├── AgerAmicus-backend/ │ ├── main.py │ ├── chatbot_main.py │ ├── models/ │ └── .env (excluded) ├── ageramicus-frontend/ (UI in progress) ├── dataset/ (excluded from GitHub) ├── plantVillage_model_10.h5 (excluded) ├── AgerAmicus_Pitch.pptx └── README.md


---

## 🤝 Team

Built with 💚 by [Vinay Reddy](https://github.com/vinayreddy1801)  && [Snigdha Reddy]
_University of North Texas | Data Science_

---

> ⚠️ Note: Sensitive files like `.env`, large models, and datasets are excluded from this repository per best practices.


