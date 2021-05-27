from Crypto.Cipher import AES
from Crypto import Random

key = Random.new().read(AES.block_size)
iv = Random.new().read(AES.block_size)

with open("image.enc",'rb') as f:
 enc_data2 = f.read()

cfb_decipher = AES.new(key, AES.MODE_CFB, iv)
plain_data = cfb_decipher.decrypt(enc_data2)

output_file = open("output.png", "wb")
output_file.write(plain_data)
output_file.close()