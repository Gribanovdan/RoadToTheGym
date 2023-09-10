class TrainingsDB:
    def __init__(self):
        self.db = {}
        from config.base_trainings import base_training_set
        self.base_training_set = base_training_set

    def add_training_set(self, user_id, training_set):
        if not (user_id in self.db.keys()):
            self.db[user_id] = training_set
        return self.db.get(user_id)

    def edit_training_set(self, user_id, new_training_set):
        self.db[user_id] = new_training_set
        return 'Training set was successfully edited/added!'

    def delete_training_set(self, user_id):
        del self.db[user_id]
        return 'Training set was successfully deleted!'

    def set_base_training_set(self, base_training_set):
        self.base_training_set = base_training_set
        return 'Base_training_set was successfully set!'

    def get_training_set(self, user_id):
        if not (user_id in self.db.keys()):
            return self.add_training_set(user_id, TrainingSet())
        return self.db.get(user_id)

    def get_base_training_set(self):
        return self.base_training_set


class Training:
    def __init__(self, name: str, description: str, program: str, media=[]):
        self.name = name
        self.description = description
        self.program = program
        self.media = media

    def edit(self, name: str, description: str, program: str, media=[]):
        self.__init__(name, description, program, media)
        return 'Training was successfully edited!'


class TrainingMaker:
    def __init__(self, set=None):
        self.set: TrainingSet = set

    def set_training_set(self, set):
        self.set = set
        return 'Training Set was successfully set into training maker!'

    def make_training(self, name: str, desc: str, program: str, media=[]):
        training = Training(name, desc, program, media)
        return 'Training maker tried to create training. Result: ' + \
               self.set.add_training(training)

    def just_create(self, name: str, desc: str, program: str, media=[]):
        return Training(name, desc, program, media)


class TrainingSet:
    def __init__(self):
        self.trainings = []

    def add_training(self, training):
        name = training.name
        for t in self.trainings:
            if t.name == name:
                return 'Error! Training with this name already exists!'
        self.trainings.append(training)
        return 'Training was successfully added!'

    def delete_training_by_name(self, training_name: str):
        for t in self.trainings:
            if t.name == training_name:
                self.trainings.remove(t)
                break
        return 'Training was successfully deleted(or it was not being existed)'

    def delete_training(self, training: Training):
        return self.delete_training_by_name(training.name)

    def edit_training_by_name(self, training_name: str, new_training):
        found = False
        for i in range(len(self.trainings)):
            if self.trainings[i].name == training_name:
                self.trainings[i] = new_training
                found = True
                break
        if found:
            return 'Training was successfully edited!'
        return 'Error: training was not found.'

    def edit_training(self, training: Training, new_training):
        return self.edit_training_by_name(training.name, new_training)

    def get_training(self, name):
        for t in self.trainings:
            if t.name == name:
                return t
        return None

    def get_training_by_id(self, id: int):
        if id > len(self.trainings):
            return None
        else:
            return self.trainings[id - 1]
