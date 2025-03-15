import bcrypt

class Authenticator:

	def encrypt(self, password: str) -> str:
		bytes = password.encode('utf-8')
		salt = bcrypt.gensalt()
		hashed = bcrypt.hashpw(bytes, salt)
		return hashed.decode('utf-8')
	
	def check(self, password: str, hashed: str) -> bool:
		bytes = password.encode('utf-8')
		hashed_bytes = hashed.encode('utf-8')
		return bcrypt.checkpw(bytes, hashed_bytes)