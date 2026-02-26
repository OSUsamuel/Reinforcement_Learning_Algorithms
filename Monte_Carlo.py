import numpy as np
import gridworld

grid = gridworld.gridworld()


def run_episode():
    episode = []
    G = 0

    terminal = False
    actions = list(policy.keys())
    probs   = list(policy.values())
    episode.append([grid.start, "N/A", 0])
    while not terminal:
        action = np.random.choice(actions, p=probs)    
        state, reward, terminal = grid.step(action)
        episode.append([state, action, reward])
        G += reward

    return episode, G

states = { (r,c): 0 for r in range(grid.height) for c in range(grid.width)}

policy = {"up":.25, "down":.25, "left":.25, "right":.25}

returns = {(r,c): [0] for r in range(grid.height) for c in range(grid.width)}

episodes = 75
for _ in range(episodes):
    grid.state = grid.start
    episode, reward = run_episode()

    visited = []

    for entry in episode:
        state = entry[0]
        if state not in visited:
            visited.append(state)
            returns[state].append(reward)

for state in states:
    states[state] = np.mean(returns.get(state))

print(states)

