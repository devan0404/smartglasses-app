# 🕶️ Smart Glasses

A wearable AI-powered smart glasses system designed to assist users by detecting objects in real time and providing voice-based feedback. Built with FastAPI, TensorFlow Lite, OpenCV, and a React frontend, this project runs on Raspberry Pi for true mobility.

---

## 🚀 Features

- 🎯 Real-time object detection using MobileNet SSD
- 🧐 FastAPI backend to control detection and system states
- 🔊 Voice feedback using `pyttsx3`
- 🎛️ Toggleable delay, voice gender, and detection state
- 🌐 Sleek React frontend built with Vite + Tailwind CSS
- 🔌 Fully portable, powered by Raspberry Pi

---

## 📁 Project Structure

```
SmartGlasses/
├── app/
│   ├── api/
│   ├── controller.py
│   ├── ...
├── models/
│   └── MobileNet-SSD/
├── smartglasses-frontend/
│   ├── src/
│   ├── index.html
│   └── ...
├── main.py
└── README.md
```

---

## ⚙️ Installation & Setup

### Backend (FastAPI)

1. **Set up virtual environment:**

```bash
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```

2. **Install dependencies:**

```bash
pip install -r requirements.txt
```

3. **Run the server:**

```bash
uvicorn main:app --reload
```

### Frontend (React)

1. **Navigate to frontend folder:**

```bash
cd smartglasses-frontend
```

2. **Install frontend packages:**

```bash
npm install
```

3. **Start the frontend:**

```bash
npm run dev
```

---

## 🛠️ API Endpoints

| Method | Endpoint         | Description               |
|--------|------------------|---------------------------|
| GET    | `/start`         | Starts object detection   |
| GET    | `/stop`          | Stops object detection    |
| POST   | `/set-delay`     | Set detection delay       |
| POST   | `/set-voice`     | Toggle between voices     |
| GET    | `/status`        | Get current detection state |

---

## 🌐 Frontend Preview

> Coming soon: Screenshot or GIF of the UI in action!

---

## 🤝 Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you’d like to change.

---

## 📜 License

MIT License. See `LICENSE` for more details.

---

## 👨‍💻 Developed by

**Devan Arya**  
Check out my [GitHub](https://github.com/devan0404)

---
