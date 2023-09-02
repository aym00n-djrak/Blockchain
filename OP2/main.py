from cryptography.hazmat.primitives.asymmetric import rsa

private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048,
)

print(private_key.public_key().public_numbers().n)
print("Hello World!")