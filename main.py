from helper import hashed, readline, USE_HASH

print("\n------------------- FONCTION DE HACHAGE ----------------------- \n")

response = readline("Saisissez la chaine d'entrée : ")

h = hashed(response)

print(f"\nSortie [sha{USE_HASH}]: {h} \n\n")
