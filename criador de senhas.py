import random


chars = "+-/*!&$#?=@aãáâàbcçdeêèéfghiîíìjklmnoôõóòpqrstuûùúvwxyzAÃÂÀÁBCÇDEÊÉÈFGHIÎÌÍJKLMNOÕÔÓÒPQRSTUÛÙÚVWXYZ1234567890"


length = int(input("Digite o comprimento da senha: "))


password = ""


for i in range(length):
      password += random.choice(chars)


print("Sua senha gerada é:", password)
