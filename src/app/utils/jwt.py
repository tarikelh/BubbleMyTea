import os, jwt
from datetime import datetime, timezone, timedelta

class Jwt:
    def generate_token(data, csrf):
        payload = data.copy()
        
        payload['exp'] = datetime.now(timezone.utc) + timedelta(days=1)

        return jwt.encode(payload, csrf, algorithm='HS256')

    def decode_token(csrf, token):
        pass


    def refresh_token():
        pass
