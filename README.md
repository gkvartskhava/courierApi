# Courier API 🚚

A Django REST Framework backend for managing courier deliveries, users, parcels, and delivery proofs.

---

## ✨ Features

- JWT authentication via SimpleJWT
- Custom user model with roles (admin, courier, customer)
- Parcels CRUD
- Delivery proof image upload
- Auto-generated Swagger/OpenAPI docs
- PostgreSQL database
- Optional Redis-backed caching

---

## 🧰 Tech Stack

- Python 3.10+
- Django 5.1
- Django REST Framework 3.15
- SimpleJWT
- drf-yasg (Swagger UI)
- PostgreSQL (via psycopg2-binary)
- Pillow (image uploads)
- python-dotenv (environment loading)
- Optional: django-redis (Redis cache backend)

> Note: `python-dotenv` and `django-redis` are required by settings but may not be listed in `requirements.txt`. If missing, install them manually (see below).

---

## 📁 Project Structure

```
.
├── courier/                 # Django project (settings, urls, wsgi)
├── delivery/                # App: models, serializers, views, urls
├── delivery_proofs/         # Uploaded images (default path from ImageField)
├── manage.py
├── requirements.txt
└── README.md
```

---

## 🚀 Getting Started

### 1) Prerequisites

- Python 3.10+
- PostgreSQL 13+ (running and accessible)
- Optional: Redis 6+ (if using the cache backend)

### 2) Setup

```bash
git clone <your-repo-url>
cd <your-project-folder>

python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

pip install -r requirements.txt
# If not already included in requirements.txt:
pip install python-dotenv django-redis
```

### 3) Environment Variables

Create a `.env` in the project root:

```env
SECRET_KEY=your_secret_key_here
DATABASE_NAME=your_db_name
DATABASE_USER=your_db_user
DATABASE_PASSWORD=your_db_password
DATABASE_HOST=localhost
DATABASE_PORT=5432
```

### 4) Apply Migrations and Create Superuser

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```

### 5) Run the Development Server

```bash
python manage.py runserver
```

- Swagger UI: `http://localhost:8000/swagger/`
- Admin: `http://localhost:8000/admin/`

---

## 🔐 Authentication (JWT)

Token endpoints:

- `POST /api/token/` – obtain access/refresh token
- `POST /api/token/refresh/` – refresh access token
- `POST /api/token/verify/` – verify token

Use the token in requests:

```
Authorization: Bearer <ACCESS_TOKEN>
```

> Default permissions in `REST_FRAMEWORK` are set to `AllowAny`. Adjust for production.

---

## 📦 API Endpoints

All endpoints are prefixed with `/api/`.

| Method | Endpoint                 | Description              |
|--------|---------------------------|--------------------------|
| GET    | `/api/users/`            | List users               |
| POST   | `/api/users/`            | Create user              |
| GET    | `/api/parcels/`          | List parcels             |
| POST   | `/api/parcels/`          | Create parcel            |
| GET    | `/api/delivery_proof/`   | List delivery proofs     |
| POST   | `/api/delivery_proof/`   | Upload delivery proof    |

Swagger UI is available at `/swagger/`.

---

## 🧪 Example Requests

### Create a User

```bash
curl -X POST http://localhost:8000/api/users/ \
  -H "Content-Type: application/json" \
  -d '{
    "username": "jane",
    "email": "jane@example.com",
    "password": "StrongP@ssw0rd",
    "role": "customer",
    "is_staff": false,
    "is_superuser": false
  }'
```

### Obtain JWT Token

```bash
curl -X POST http://localhost:8000/api/token/ \
  -H "Content-Type: application/json" \
  -d '{"username": "jane", "password": "StrongP@ssw0rd"}'
```

### Create a Parcel

```bash
curl -X POST http://localhost:8000/api/parcels/ \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer <ACCESS_TOKEN>" \
  -d '{
    "title": "Box #42",
    "description": "Fragile",
    "status": "pending",
    "sender": 1,
    "receiver_name": "John Doe",
    "receiver_address": "123 Main St",
    "courier": 2
  }'
```

### Upload a Delivery Proof (multipart)

```bash
curl -X POST http://localhost:8000/api/delivery_proof/ \
  -H "Authorization: Bearer <ACCESS_TOKEN>" \
  -F parcel=1 \
  -F image=@/full/path/to/photo.jpg
```

---

## 🖼️ Media Uploads

The `DeliveryProof.image` field uploads to the `delivery_proofs/` path.

For local development, add these to `courier/settings.py` to serve files from a `media/` folder:

```python
MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"
```

And in `courier/urls.py` append (development only):

```python
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # ... existing paths ...
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

---

## 🧊 Caching (Optional)

Redis cache is configured in `courier/settings.py` using `django-redis`:

```python
CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379/1",
        "OPTIONS": {"CLIENT_CLASS": "django_redis.client.DefaultClient"},
    }
}
```

- Ensure Redis is running locally on `127.0.0.1:6379`.
- If you do not need Redis in development, switch to in-memory cache:

```python
CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.locmem.LocMemCache"
    }
}
```

---

## ⚙️ Configuration Notes

- `AUTH_USER_MODEL` is set to `delivery.CustomUser`.
- `DEBUG` is set to `True` by default. For production, set `DEBUG=False` and configure `ALLOWED_HOSTS`.
- Database is configured via environment variables for PostgreSQL.

---

## 🛡️ Admin

- Visit `/admin/` and log in with the superuser created during setup.

---

## 📄 License

Add your preferred license here (e.g., MIT, Apache-2.0).
