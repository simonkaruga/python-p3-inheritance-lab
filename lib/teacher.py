#!/usr/bin/env python

from user import User

import random

class Teacher(User):

    def teach(self):
        return random.choice(self.knowledge)
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.knowledge = [
            "Math",
            "Science",
            "History",
            "Art",
            "Physical Education",
            "Music",
            "Literature",
            "Biology",
            "Chemistry",
            "Physics"
        ]