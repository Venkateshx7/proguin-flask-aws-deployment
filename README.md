# 🚀 ProGuin Flask AWS Deployment

ProGuin Task Manager is a lightweight web application built using **Python Flask** and designed to demonstrate **AWS deployment fundamentals**.

This project focuses on building a simple backend system and preparing it for **cloud deployment using AWS EC2**.

---

# 📌 Features

- Add tasks
- Mark tasks as completed / undo completion
- Delete tasks
- Persistent task storage using JSON
- Clean and simple web UI
- Health check endpoint for monitoring

---

# 🛠 Tech Stack

| Technology | Purpose |
|-----------|--------|
| Python | Backend logic |
| Flask | Web framework |
| HTML | Frontend UI |
| JSON | Task data storage |
| Git | Version control |
| GitHub | Code repository |
| AWS EC2 | Cloud deployment |
| Linux | Server environment |

---

# 📂 Project Structure
proguin-flask-aws-deployment
│
├── app.py
├── requirements.txt
├── templates
│ └── index.html
│
├── proguin
│ └── core.py
│
├── README.md
└── .gitignore

---

# ⚙️ How to Run Locally

### 1 Install dependencies

pip install -r requirements.txt


### 2 Run application


python app.py


### 3 Open browser


http://127.0.0.1:5000


---

# ☁️ AWS Deployment Overview

This project is intended to be deployed using **AWS EC2**.

Deployment workflow:
Developer → GitHub Repository → AWS EC2 Instance → Flask Application


Steps:

1. Launch EC2 instance (Ubuntu)
2. Install Python and Git
3. Clone repository
4. Install dependencies
5. Run Flask app

---

# 📈 Future Improvements

- Gunicorn production server
- Nginx reverse proxy
- Docker containerization
- CI/CD pipeline using GitHub Actions
- PostgreSQL database integration

---

# 👨‍💻 Author

**Venkatesh D**

- GitHub: https://github.com/Venkateshx7
- LinkedIn: https://www.linkedin.com/in/venkatesh-d-6325a7256/
