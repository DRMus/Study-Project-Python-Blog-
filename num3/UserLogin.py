class UserLogin():
    def fromDB(self, user_id, db, users):
        self.__user = db.query(users).filter(users.id == user_id).first()
        return self

    def create(self, user):
        self.__user = user
        return self

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anoymous(self):
        return True

    def get_id(self):
        return str(self.__user.id)
