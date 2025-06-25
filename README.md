# Courier API 🚚

A Django REST Framework-based backend API for a courier management system.
(my first big project)

---

## 🚀 Features

- 🔒 **JWT Authentication** via `SimpleJWT`
- 🧑‍💼 **Custom User Roles** (e.g. admin, staff, customer)
- 📦 **Parcel Management API**
- 📸 **Delivery Proof Uploads** (saved to media folder)
- 🔧 **Swagger Documentation** using `drf_yasg`
- ⚙️ **Redis Cache** via `django-redis`
- 🌍 PostgreSQL integration
- 🔄 CORS support and `.env` environment variables

---

## 📁 Project Structure

```
courier/
│
├── courier/             # Main project config
│
├── delivery/            # App with models, views, etc.
│
├── media/               # Uploaded delivery proofs
│
├── .env                 # Environment config (not committed)
├── requirements.txt     # Project dependencies
├── manage.py
└── README.md
```

---

## 🔐 Authentication

Authentication is handled via **JWT tokens**. Use the following endpoints to manage tokens:

- `/api/token/` – obtain access/refresh token pair
- `/api/token/refresh/` – refresh the access token

---

## 📦 API Endpoints

All API endpoints are prefixed with `/api/`:

| Endpoint               | Description                    |
|------------------------|--------------------------------|
| `GET /api/users/`      | List all users                 |
| `POST /api/users/`     | Create a new user              |
| `GET /api/parcels/`    | List all parcels               |
| `POST /api/parcels/`   | Create a new parcel            |
| `POST /api/delivery_proof/` | Upload delivery proof  |

> Uses Django REST Framework's `DefaultRouter` for automatic endpoint registration.

---

## 🧾 Delivery Proof Upload

- Uploads are handled by the `DeliveryProofViewset`.
- Files are stored in the `media/` directory (make sure it's writable).

---

## 🧪 Swagger API Docs

Interactive API documentation available at:

```
http://localhost:8000/swagger/
```

> Provided by `drf_yasg`.

---

## 🛠️ Setup Instructions

### 1. Clone the repository

```bash
git clone <your-repo-url>
cd courierapi
```

### 2. Create virtual environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Setup `.env`

Create a `.env` file in the project root with the following variables:

```env
SECRET_KEY=your_secret_key_here
DATABASE_NAME=your_db_name
DATABASE_USER=your_db_user
DATABASE_PASSWORD=your_db_password
DATABASE_HOST=localhost
DATABASE_PORT=5432
```

### 5. Run migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Run server

```bash
python manage.py runserver
```

---

## 🧊 Redis Setup

Make sure Redis is installed and running locally on `127.0.0.1:6379`.

If Redis is not needed, you can change `CACHES` in `settings.py` to:

```python
CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.locmem.LocMemCache"
    }
}
```
