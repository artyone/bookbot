import pickle

PATH_TO_DATABASE = 'database/database.pickle'
# Создаем шаблон заполнения словаря с пользователями
user_dict_template: dict = {'page': 1,
                            'bookmarks': set()}

# Инициализируем "базу данных"
try:
    with open(PATH_TO_DATABASE, 'rb') as file:
        users_db: dict = pickle.load(file)
except:
    users_db: dict = {}
    with open(PATH_TO_DATABASE, 'wb') as file:
        pickle.dump(users_db, file)

def update_db():
    with open(PATH_TO_DATABASE, 'wb') as file:
        pickle.dump(users_db, file)
