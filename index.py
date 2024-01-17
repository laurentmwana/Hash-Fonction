from handle import hashed

response = None

while response is None or response == '':
    response = input("Entrez une chaine : ")

hash = hashed(response)

print(f"Le message hashé en binaire est : {hash[0]}\n")

print(f"Le message hashé en hexadécimal est : {hash[1]}\n")