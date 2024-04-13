from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization

# Generar una nueva clave RSA de 2048 bits
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048,
)

# Serializar la clave en formato PEM
pem = private_key.private_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PrivateFormat.PKCS8,
    encryption_algorithm=serialization.NoEncryption(),
)

# Cargar la clave serializada
loaded_private_key = serialization.load_pem_private_key(pem, password=None)

# Imprimir la clave cargada
print(loaded_private_key)

