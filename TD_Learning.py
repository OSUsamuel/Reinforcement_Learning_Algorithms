import numpy as np
import gridworld as gridworld


grid = gridworld.gridworld()
height = grid.height
width = grid.width

gamma = 1.0
alpha = 1

policy = {(i,j): {'up': .25, 'down': .25, 'right': .25, 'left': .25} for i in range(height) for j in range(width)}
Value = {(i,j): 0 for i in range(height) for j in range(width)}

# Run episode
for _ in range(1000):
    terminal = False
    grid.state = grid.start
    while(not terminal):
        state = grid.state
        actions = list(policy[state].keys())
        probs = list(policy[state].values())
        action = np.random.choice(actions, p=probs)
        next_state, reward, terminal = grid.step(action)
        Value[state] = Value[state] + alpha*(reward + gamma*Value[next_state]-Value[state])

print(Value)
