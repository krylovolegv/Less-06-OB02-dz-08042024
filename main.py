#Разработай систему управления учетными записями пользователей
#для небольшой компании FiRmA

class User:
    def __init__(self, user_id, name):
        self._user_id = user_id
        self._name = name
        self._access_level = 'user'

    # Доступ к атрибуту user_id
    def get_user_id(self):
        return self._user_id

    # Доступ к атрибуту name
    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    # Доступ к атрибуту access_level
    def get_access_level(self):
        return self._access_level


class Admin(User):
    def __init__(self, user_id, name):
        super().__init__(user_id, name)
        self._access_level = 'admin'
        self._users = []

    def add_user(self, user):
        if not any(u.get_user_id() == user.get_user_id() for u in self._users):
            self._users.append(user)
            print(f"Пользователь {user.get_name()} добавлен.")
        else:
            print("Ошибка: Пользователь с таким ID уже существует.")

    def remove_user(self, user_id):
        for i, user in enumerate(self._users):
            if user.get_user_id() == user_id:
                del self._users[i]
                print(f"Пользователь {user.get_name()} удален.")
                return
        print("Ошибка: Пользователь не найден.")

    def list_users(self):
        print("Список пользователей:")
        for user in self._users:
            print(f"ID: {user.get_user_id()}, Имя: {user.get_name()}, Уровень доступа: {user.get_access_level()}")


admin = Admin("1", "Админ Иван")

admin.add_user(User("2", "Сотрудник 1"))
admin.add_user(User("3", "Сотрудник 2"))

admin.list_users()

admin.remove_user("2")

admin.list_users()
