from classes.Trainings_classes import Training, TrainingSet

base_training_set = TrainingSet()
base_training_set.trainings = [
    Training(
        'Arms home',
        'Quick training for your arms',
        '1. Push ups 20 times\n'
        '2. Rest 2 minutes\n'
        '3. Pull ups 10 times\n'
        '4. Rest 2 minutes\n'
        'Repeat 3 times'
    ),
    Training(
        'Gym Master',
        'Become a real legend in your gym',
        '1. Deadlift 1 time\n'
        '2. Squat 5 times\n'
        '3. Rest 4 minutes\n'
        '4. Repeat 2 times more\n'
        '5. Bench press 5 times\n'
        '6. Rest 5 minutes\n'
        '7. Repeat 2 times more\n'
        'Great!'
    )
]
