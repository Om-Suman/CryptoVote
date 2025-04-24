🗳️ CryptoVote
CryptoVote is a secure, transparent, and user-friendly online voting platform.It is designed to simplify election processes for institutions, communities, and organizations by providing a seamless digital voting experience.

📌 Project Vision
To reimagine traditional voting systems and offer a digital-first, accessible, and tamper-proof platform that ensures fairness, trust, and ease of use.

💡 Key Features
🔐 Secure Login System: Role-based access for voters and administrators.
✅ One-Click Voting: Cast votes instantly with clear confirmation.
📊 Real-Time Results: Track election outcomes transparently.
🧾 Profile Management: Update personal info and upload profile pictures.
🧑‍💼 Admin Panel: Manage elections, candidates
🖥️ User Dashboard: Personalized stats and election status overview.
🌍 Timezone and Country Selection: Customize user profile based on location.

🚀 Future Enhancements
Blockchain integration for decentralized vote logs
OTP-based login for enhanced security
Election result exports and detailed analytics
More granular admin controls

Setup Instructions

1. Clone the Repository
git clone https://github.com/Om-Suman/cryptovote.git
cd cryptovote

2.Create a Virtual Environment
```bash
python -m venv myvenv
myvenv\Scripts\activate   # On MACs use: source myvenv/bin/activate  

3. Install Dependencies
pip install -r requirements.txt

4. Apply Database Migrations
python manage.py makemigrations
python manage.py migrate

6. Create a Superuser
python manage.py createsuperuser

7. Start the Development Server
python manage.py runserver

Visit: http://127.0.0.1:8000

8. Access the Admin Panel
http://127.0.0.1:8000/admin/

'''



