# Affecter le nom du fichier à la variable `import_file`

import_file = "allow_list.txt"

# Affecter une liste d'adresses IP qui ne sont plus autorisées à accéder à des informations restreintes à la variable `remove_list`.

remove_list = ["192.168.97.225", "192.168.158.170", "192.168.201.40", "192.168.58.57"]

# Créer une instruction `with` pour lire le contenu initial du fichier

with open(import_file, "r") as file:

  # Utiliser `.read()` pour lire le fichier importé et le stocker dans une variable nommée `ip_addresses`

  ip_addresses = file.read()

# Utiliser `.split()` pour convertir `ip_addresses` d'une chaîne à une liste

ip_addresses = ip_addresses.split()

# Créer une instruction itérative
# Nommer la variable de boucle `element`
# Créer une boucle pour parcourir `remove_list`

for element in remove_list:

  # Utiliser la méthode `.remove()` pour supprimer
  # les éléments de `ip_addresses`
  if element in ip_addresses:
    ip_addresses.remove(element)

# Convertir `ip_addresses` en une chaîne afin de pouvoir l'écrire dans un fichier texte

ip_addresses = " ".join(ip_addresses)

# Créer l'instruction `with` pour réécrire le fichier original

with open(import_file, "w") as file:

  # Réécrire le fichier en remplaçant son contenu par `ip_addresses`

  file.write(ip_addresses)

# Créer une instruction `with` pour lire le fichier mis à jour

with open(import_file, "r") as file:

  # Lire le fichier mis à jour et stocker le contenu dans `text`

    text = file.read()

# Afficher le contenu de `text`

print(text)