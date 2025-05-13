# 🍽️ Django Recipe App

A simple yet powerful web application built with **Django** that allows users to **sign up, log in, and manage their own recipes**. Users can **create, read, update, and delete (CRUD)** their recipes after authentication.

---

## 🚀 Features

- ✅ User registration and login
- ✅ User authentication with sessions
- ✅ Create your own recipes
- ✅ View a list of your recipes
- ✅ Edit/update existing recipes
- ✅ Delete recipes
- ✅ Clean, minimal UI with Django templates
- ✅ RESTful URL routing

---

## 🛠️ Tech Stack

- **Backend:** Django (Python)
- **Frontend:** Django Templates, HTML/CSS
- **Database:** SQLite (default Django DB)

---

## 📸 Screenshots *(optional)*

> Add images if you'd like. Example:
> - Home page
> - Recipe list
> - Create/Edit form
> - Login/Register

---

## 🏁 Getting Started

### 🔧 Requirements

Make sure you have the following installed:

- Python 3.8+
- pip
- virtualenv *(optional but recommended)*

---

### 📦 Installation Steps

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/your-repo-name.git
cd your-repo-name

# 2. Install project dependencies
pip install -r requirements.txt

# 3. Apply database migrations
python manage.py migrate

# 4. (Optional) Create a superuser to access the Django admin panel
python manage.py createsuperuser

# 5. Run the development server
python manage.py runserver

# 6. Open the project in your browser
# Visit:
http://127.0.0.1:8000/
