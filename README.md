# 🍽️ Restaurantly

> A modern restaurant management and reservation platform built with Django — where guests book tables and leave with a QR code in hand.

![Restaurantly](https://github.com/user-attachments/assets/00397658-18fe-4051-a09f-5e4c985c4d05)

🌐 **Live Demo:** [restaurantly-restaurantly.up.railway.app](https://restaurantly-restaurantly.up.railway.app)

---

## ✨ Features

- 📅 **Table Reservations** — Guests can book a table by selecting date, time, and party size
- 🔑 **QR Code Generation** — Every confirmed reservation generates a unique QR code instantly
- 📲 **Scan or Download** — Guests can scan the QR code directly or download it for later
- 🗄️ **Reservation Storage** — All bookings are stored in the database and manageable via admin panel
- 🔐 **Admin Panel** — Full control over reservations, menu, and restaurant settings

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Backend | Python, Django |
| Frontend | Bootstrap, HTML, CSS |
| Database | SQLite |
| QR Codes | qrcode (Python library) |
| Static Files | WhiteNoise |
| Hosting | Railway |

---

## 🚀 Getting Started

### Prerequisites
- Python 3.10+
- pip

### Installation

```bash
# Clone the repository
git clone https://github.com/Shishikon/Restaurantly.git
cd Restaurantly

# Create virtual environment
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Apply migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Run the server
python manage.py runserver
```

Then open [http://localhost:8000](http://localhost:8000) in your browser.

---

## ⚙️ Environment Variables

Create a `.env` file or set these in your hosting dashboard:

```
SECRET_KEY=your-secret-key
DEBUG=False
ALLOWED_HOSTS=your-domain.com
```

---

## 📁 Project Structure

```
Restaurantly/
├── project/          # Django project settings
├── restaurantly/     # Main app (models, views, templates)
│   ├── static/       # CSS, JS, images
│   └── templates/    # HTML templates
├── requirements.txt
├── build.sh          # Railway build script
└── manage.py
```

---

## 🖼️ How Reservations Work

1. Guest fills out the reservation form (name, date, time, party size)
2. System saves the booking to the database
3. A unique QR code is generated for that reservation
4. Guest can **scan** or **download** the QR code as confirmation
5. Staff can verify reservations by scanning the QR code on arrival

---

## 👨‍💻 Author

**Shishikon** — Trilingual Python Developer
- GitHub: [@Shishikon](https://github.com/Shishikon)

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).
