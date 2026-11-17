import os
from flask_appbuilder.security.manager import AUTH_DB

# ===========================
# 🔐 Cấu hình bảo mật cơ bản
# ===========================
SECRET_KEY = 'my_super_secret_key_1234567890!@#'

# Sử dụng xác thực qua database
AUTH_TYPE = AUTH_DB
AUTH_USER_REGISTRATION = True
FAB_SECURITY_MANAGER_CLASS = "superset.security.SupersetSecurityManager"

# Fix lỗi "unsupported hash type scrypt"
FAB_PASSWORD_HASH = "pbkdf2_sha256"
FAB_PASSWORD_SALT = "a_random_salt_for_superset"

# ===========================
# ⚙️ Cấu hình session & CSRF
# ===========================
SESSION_COOKIE_SAMESITE = None
SESSION_COOKIE_SECURE = False
WTF_CSRF_ENABLED = True

# ===========================
# 📂 Cấu hình thư mục Superset
# ===========================
BASE_DIR = os.path.dirname(__file__)
DATA_DIR = os.path.join(BASE_DIR, 'superset_home')
if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)

UPLOAD_FOLDER = os.path.join(DATA_DIR, "uploads")
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# ===========================
# 📁 Cho phép upload file CSV/XLSX
# ===========================
UPLOAD_ALLOWED_EXTENSIONS = ["csv", "xlsx"]
ALLOWED_EXTENSIONS = {"csv", "xls", "xlsx"}
CSV_UPLOAD_ALLOWED_EXTENSIONS = ["csv"]
ALLOW_UPLOAD_CSV = True

# ===========================
# 🚀 Bật các tính năng nâng cao
# ===========================
FEATURE_FLAGS = {
    "ALLOW_DATA_UPLOAD": True,          # ✅ Cho phép upload CSV/XLSX
    "ENABLE_TEMPLATE_PROCESSING": True,
    "UPLOAD_ASYNC": False,
}

# ===========================
# 🧠 Cache tạm (giữ nguyên mặc định)
# ===========================
CACHE_CONFIG = {
    "CACHE_TYPE": "SimpleCache",
    "CACHE_DEFAULT_TIMEOUT": 300,
}

# ===========================
# ✅ Logging nhẹ nhàng (tùy chọn)
# ===========================
LOG_LEVEL = "INFO"
