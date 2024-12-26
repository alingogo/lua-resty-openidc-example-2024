"""Endpoints module."""

from jose import jwt



token = "MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAtdWR782Dhwz9at7LWUn+ztDzp5ivpbXiHUSdJvFQ7AK6PEHb0TMbL4Tzti/yCk1QPc6Tm1eVE4tInRzaGjYCxI49g7h0RKQoIa5DWoxg1vhmbpbKjR/vbf0/17dcfen55O/HxeOCUzz89+vIYWbrpayesxWRM/OQxT8blLWJYMrSCXY9hLuNk89Pmba2m6OapywtlzYeaklWwF3A19Z6EJFO5G3pNcNQKFmfesSEe2mnJsNR32jbRXpdtpt7xvcazps7xe5IFeER/lB/Xg7X9ZGAaD9nc1ln7U5BPuWbFU4bD+MLhUwpgkO5+Xcq7lX1vxRQWRYvQkVNbtFoP9BSGQIDAQAB"
public_key = b"-----BEGIN PUBLIC KEY-----\nMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAtdWR782Dhwz9at7LWUn+ztDzp5ivpbXiHUSdJvFQ7AK6PEHb0TMbL4Tzti/yCk1QPc6Tm1eVE4tInRzaGjYCxI49g7h0RKQoIa5DWoxg1vhmbpbKjR/vbf0/17dcfen55O/HxeOCUzz89+vIYWbrpayesxWRM/OQxT8blLWJYMrSCXY9hLuNk89Pmba2m6OapywtlzYeaklWwF3A19Z6EJFO5G3pNcNQKFmfesSEe2mnJsNR32jbRXpdtpt7xvcazps7xe5IFeER/lB/Xg7X9ZGAaD9nc1ln7U5BPuWbFU4bD+MLhUwpgkO5+Xcq7lX1vxRQWRYvQkVNbtFoP9BSGQIDAQAB\n-----END PUBLIC KEY-----\n"
# key_binary = public_key.encode('ascii')
ALGORITHM = "RS256"
payload = jwt.decode(token, public_key, algorithms=[ALGORITHM],options={"verify_aud": False, "verify_signature": True})
print(dict(payload))