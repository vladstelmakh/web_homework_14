# app/security.py

from passlib.context import CryptContext
from app.settings import PASSWORD_HASH_ALGORITHM

pwd_context = CryptContext(schemes=[PASSWORD_HASH_ALGORITHM], deprecated="auto")
