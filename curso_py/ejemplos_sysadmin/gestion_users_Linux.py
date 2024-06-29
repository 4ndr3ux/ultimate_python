import os


class UserManager:
    def __init__(self, username):
        self.username = username

    def add_user(self):
        os.system(f"sudo useradd {self.username}")
        print(f"Usuario {self.username} agregado.")

    def delete_user(self):
        os.system(f"sudo userdel {self.username}")
        print(f"Usuario {self.username} eliminado.")

    def user_exists(self):
        result = os.system(f"id -u {self.username} > /dev/null 2>&1")
        if result == 0:
            print(f"El usuario {self.username} existe.")
            return True
        else:
            print(f"El usuario {self.username} no existe.")
            return False


# Uso de la clase
username_input = input("ingrese el username del nuevo usuario: ")
user = UserManager(username_input)
# user.add_user()
user.user_exists()
# user.delete_user()
# user.user_exists()


# explicame clases en python de forma muy clara y con ejemplo practico y facil de comprender,
# quiero que el ejemplo de codigo para yo comprenderlo mejor tenga que ver
# con alguna taarea de sysadmin linux y otro ejemplo con hacking etico
