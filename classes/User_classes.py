class UserDB:
    def __init__(self):
        self.db = {}

    def add_user(self, user):
        if user.id in self.db.keys():
            return 'User already exists!'
        self.db[user.id] = user

    def delete_user(self, user_id):
        del self.db[user_id]
        return 'User was successfully deleted!'

    def get_user(self, user_id):
        if not (user_id in self.db.keys()):
            return None
        return self.db.get(user_id)


class User:
    def __init__(self, id):
        self.id = id


class UserMaker:
    def __init__(self, user_db=None):
        self.user_db: UserDB = user_db

    def create_user(self, user_id):
        if self.user_db is None:
            return 'Error! No UserDB found!'
        user = User(user_id)
        self.user_db.add_user(user)
