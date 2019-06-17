#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from myarray import Array
class Student():
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def __repr__(self):
        return "Student(name: %s, score: %d)" % (self.name, self.score)


student = Student("Alice", 100)
arr = Array(10)
arr.addLast(student)
arr.addLast(student)
print(student.name)
print(arr)
