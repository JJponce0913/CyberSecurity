import jwt
import datetime

# Define the payload with the necessary claims
payload = {
    'iss': 'your_issuer',  # Issuer
    'sub': 'admin_user',   # Subject
    'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=1),  # Expiration time
    'role': 'admin'        # Custom claim indicating admin role
}

# Load your private key for signing
with open('private.pem', 'r') as f:
    private_key = f.read()

# Create the JWT token using ES256 algorithm
token = jwt.encode(payload, private_key, algorithm='ES256')

print(token.decode())
