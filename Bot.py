import numpy as np
from collections import defaultdict
import tkinter as tk
import random

# Directions: Up, Right, Down, Left, Wait
ACTIONS = [(-1, 0), (0, 1), (1, 0), (0, -1), (0, 0)]
ACTION_NAMES = ['Up', 'Right', 'Down', 'Left', 'Wait']

class Bot:
    def __init__(self, name, start, goal):
        self.name = name
        self.position = start
        self.goal = goal
        self.path = [start]
        self.movements = []

    def move(self, action):
        self.position = (self.position[0] + action[0], self.position[1] + action[1])
        self.path.append(self.position)
        self.movements.append(ACTION_NAMES[ACTIONS.index(action)])

    def reached_goal(self):
        return self.position == self.goal
