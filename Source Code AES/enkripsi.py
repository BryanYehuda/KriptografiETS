from Crypto.Cipher import AES
from Crypto import Random

key = Random.new().read(AES.block_size)
iv = Random.new().read(AES.block_size)

with open("tux.png",'rb') as f:
 input_data = f.read()
#input_file.close()

cfb_cipher = AES.new(key, AES.MODE_CFB, iv)
enc_data = cfb_cipher.encrypt(input_data)

enc_file = open("encrypted.enc", "wb")
enc_file.write(enc_data)
#enc_file.close()