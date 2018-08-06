import os



def generate_secret_key(n=16):
	with open('local/secretkey', 'wb') as f:
		f.write(os.urandom(n))


class Config:
	pass