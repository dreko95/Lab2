__author__ = 'Lecks'


class Bartender():
    state = 'WAIT'# customer status
    full_text = ""# Text to check

#Uploading texts , and initialization parameters
    def __init__(self, state):
        self.state = state
        with open('../files/Full.txt', 'rb') as f:
            for line in f:
                self.full_text += line

    percent = clients = result = sent_parts = time = received_parts = 0

    counter = 0
    tasks = []


# Generates job for processing
    def form_tasks(self):
        with open('../files/Sub.txt', 'rb') as f:
            for line in f:
                self.tasks.append(line.rstrip())


# It gives reference to process
    def get_task(self):
        self.counter += 1
        return self.tasks[self.counter-1]


# time indicator
    def set_time(self, time):
        self.time = time





