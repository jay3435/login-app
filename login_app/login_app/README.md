# 🔐 AuthVault — Login & Registration Web App

A simple Login & Registration web application built with **Python (Flask)** and **HTML/CSS**.

## 📌 Features

- ✅ User Registration (saves to `users.json`)
- ✅ User Login with validation
- ✅ Success & error messages
- ✅ Session management
- ✅ Stylish dark-themed UI

## 🗂️ Project Structure

```
login_app/
│
├── app.py                  # Flask backend
├── requirements.txt        # Python dependencies
├── users.json              # Stores registered users (auto-created)
├── .gitignore
├── README.md
│
└── templates/
    ├── base.html           # Shared layout & styles
    ├── login.html          # Login page
    └── register.html       # Registration page
```

## 🚀 How to Run

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/login-app.git
   cd login-app
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the app**
   ```bash
   python app.py
   ```

4. **Open in browser**
   ```
   http://127.0.0.1:5000
   ```

## 🛠️ Tech Stack

- **Backend**: Python, Flask
- **Frontend**: HTML, CSS (no frameworks)
- **Storage**: JSON file (`users.json`)

## 📸 Pages

| Page | Route |
|------|-------|
| Login | `/login` |
| Register | `/register` |

---

Made with ❤️ using Flask
