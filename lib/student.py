#!/usr/bin/env python

from user import User

class Student(User):
    
    def learn(self):
        return self.knowledge
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.knowledge = []
        return
    def learn(self, subject):
        self.knowledge.append(subject)
        return