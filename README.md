# 🗳️ CryptoVote

**CryptoVote** is a secure, transparent, and user-friendly online voting platform. It simplifies the election process for institutions, communities, and organizations by providing a seamless and reliable digital voting experience.

---

## 🎯 Project Vision

To reimagine traditional voting systems by offering a **digital-first**, **accessible**, and **tamper-proof** platform that ensures fairness, trust, and ease of use.

---

## 🚀 Features

- 🔐 **Secure Login System** – Role-based access for voters and administrators  
- ✅ **One-Click Voting** – Vote instantly with clear confirmation  
- 📊 **Real-Time Results** – Transparent, live election outcome tracking  
- 🧾 **Profile Management** – Update personal info and upload a profile picture  
- 🧑‍💼 **Admin Panel** – Manage elections, candidates, and user access  
- 🖥️ **User Dashboard** – View election statuses and personalized stats  
- 🌍 **Location Customization** – Timezone and country selection

---

## 🔮 Future Enhancements

- 🔗 Blockchain integration for decentralized vote logs  
- 📈 Exportable results and detailed analytics  
- 🛠️ More granular admin controls for fine-tuned management


## Installation Guide

Follow these steps to get CryptoVote up and running locally.

### Prerequisites

Make sure you have the following installed:

- [Python 3.8+](https://www.python.org/downloads/)
- [Django 3.2+](https://www.djangoproject.com/)
- [SQLite](https://www.sqlite.org/) (included by default with Django)
- [Git](https://git-scm.com/)

### Steps to Run the Project Locally

```bash
# 1. Clone the Repository and Navigate into the Project Directory
git clone https://github.com/Om-Suman/CryptoVote.git
cd CryptoVote

# 2. Set up a Virtual Environment
python -m venv venv

# On Windows, activate the virtual environment
venv\Scripts\activate

# On macOS/Linux, activate the virtual environment
source venv/bin/activate

# 3. Install Dependencies
pip install -r requirements.txt

# 4. Apply Migrations
python manage.py migrate

# 5. Create a Superuser
python manage.py createsuperuser

# Follow the prompts to set up the superuser credentials.

# 6. Start the Development Server
python manage.py runserver

# 7. Access the App
# Open the app in your browser:
http://127.0.0.1:8000/

# You can access the Django admin panel at:
http://127.0.0.1:8000/admin/
# Log in using the superuser credentials you created earlier.




