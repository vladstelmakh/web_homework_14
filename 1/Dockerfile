# Використовуємо офіційний образ Python в якості базового образу
FROM python:3.9-slim

# Встановлюємо залежності для PostgreSQL та інших важливих пакетів
RUN apt-get update && apt-get install -y libpq-dev gcc

# Створюємо та переключаємося до робочого каталогу /app
WORKDIR /app

# Копіюємо файли залежностей та встановлюємо їх
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копіюємо весь вміст директорії у робочий каталог образу
COPY . .

# Встановлюємо змінні середовища для контейнера
ENV SECRET_KEY=mysecretkey
ENV ALGORITHM=HS256
ENV DATABASE_URL=postgresql://user:password@db/mydatabase
ENV PASSWORD_HASH_ALGORITHM=bcrypt
ENV ACCESS_TOKEN_EXPIRE_MINUTES=30
ENV REFRESH_TOKEN_EXPIRE_DAYS=7
ENV EMAIL_HOST=smtp.example.com
ENV EMAIL_PORT=587
ENV EMAIL_ADDRESS=your_email@example.com
ENV EMAIL_PASSWORD=your_email_password
ENV CLOUDINARY_CLOUD_NAME=your_cloudinary_cloud_name
ENV CLOUDINARY_API_KEY=your_cloudinary_api_key
ENV CLOUDINARY_API_SECRET=your_cloudinary_api_secret
ENV REDIS_URL=redis://localhost:6379

# Команда, яка запускає додаток при старті контейнера
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
