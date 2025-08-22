 Dummy Python code that stores secrets insecurely

# Insecure: Hardcoded secrets in source code
API_KEY = "12345-abcdefg-SECRET-KEY"
DB_PASSWORD = "supersecretpassword"
SECRET_TOKEN = "token_987654321"

def connect_to_service():
    print(f"Connecting with API_KEY: {API_KEY}")

def authenticate_db():
    print(f"Authenticating with password: {DB_PASSWORD}")

def use_secret_token():
    print(f"Using token: {SECRET_TOKEN}")

if __name__ == "__main__":
    connect_to_service()
    authenticate_db()
    use_secret_token()
