from src.config import DB_CONNECTION

DATABASE_CONFIG = {
    "connections": {"default": DB_CONNECTION},
    "apps": {
        "models": {
            "models": ["src.app.models"],
            "default_connection": "default",
        },
    },
}
