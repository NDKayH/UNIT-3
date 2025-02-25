# 'secure_password.py'

## Code
```.py

#secure_password.py

from passlib.context import CryptContext

#create an object of the class CryptContext
pwd_config = CryptContext(schemes=["pbkdf2_sha256"],
                          default="pbkdf2_sha256",
                          pbkdf2_sha256__default_rounds=30000
                          )

#this function recieves the unsafe password and encrypts it

def encrypt_password(user_password: str) -> str:
    return pwd_config.hash(user_password)

def check_password(hashed_password: str, user_password: str):
    return pwd_config.verify(user_password, hashed_password)

# hash = encrypt_password("password13")
# print(hash) # $pbkdf2-sha256$30000$TAlBaE1prTVG6B2D0BqjlA$8xlXGsS4Hl4GIqJYBVua9Xj9rPxV/WLr4.VK5x5d4L8

# # hash = encrypt_password("password123")
# # print(hash) # $pbkdf2-sha256$30000$jvH.H8M4B6BUinFO6Z3zXg$Ty/ZCE.zq4lxYpjJdkgZySpocXDBuWkpztIYAumXoAw

# hash = encrypt_password(".aio_Bahn13579*")
# print(hash) # $pbkdf2-sha256$30000$.H8PoZQyhpDS.v./N.Z8bw$lL4/j8wfYzrAgXXFG2fa7MJWt2Cm5eq8MhO4Dr11fW4

# hash = encrypt_password(".H8PoZQyhpDS.v./N.Z8bw$lL4/j8wfYzrAgXXFG2fa7MJWt2Cm5eq8MhO4Dr11fW4")
# print(hash) # $pbkdf2-sha256$30000$fm.tVUppLWUMASDE2Lt3Lg$AZjewJrmVoWGXtg6Pgfa5fee6qOJevb71pqb5gpxNec


```
