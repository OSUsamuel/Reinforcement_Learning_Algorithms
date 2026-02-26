import numpy as np

class gridworld:

    def __init__(self, width=5, height=5, start=(0,0), goal=(4,4)):
             self.width = width
             self.height = height
             self.start = start
             self.goal = goal
             self.state = start

            
             self.actions = {
                "up": (-1,0),
                "down": (1,0),
                "left": (0,0),
                "right": (0,1)
                 }

    def step(self, action):
            di, dj = self.actions[action]
            i, j = self.state
             
            next_i = np.clip(i+di, 0, self.height - 1)
            next_j = np.clip(j+dj, 0, self.width -1)

            self.state = (next_i, next_j)
             
            if self.state == self.goal:
                 reward = 0
                 terminal = True
            else:
                 reward = -1
                 terminal = False
            return self.state, reward, terminal

    def render(self):
            grid = np.ones((self.height, self.width), dtype = str)
            grid[:] = '.' # Sets every entry in the grid to '.'
            grid[self.goal] = 'G'
            grid[self.state] = 'S'
            print("\n".join(" ".join(row) for row in grid))
            print()
