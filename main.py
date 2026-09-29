import autore
import brano
import User_data

Utente1 = User_data.user_data("user1", "password1", "user1@example.com")
print(Utente1.to_string())

autore1 = autore.autore("John", "Lennon")
autore2 = autore.autore("Freddie", "Mercury")

canzone1 = brano.brano("Imagine", autore1, 3.1)
canzone2 = brano.brano("Bohemian Rhapsody", autore2, 5.55)

print(canzone1.to_string())
print(canzone2.to_string())

