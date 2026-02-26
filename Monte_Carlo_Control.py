import numpy as np
import gridworld

grid = gridworld.gridworld()
width, height = grid.width, grid.height



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
        episode.append([state,action, reward])
        G += reward

    return episode, G





state_action_matrix = {(i,j): {key: [] for key in grid.actions.keys()} for i in range(height) for j in range(width) }

policy = {(i,j): {"up":.25, "down":.25, "left":.25, "right":.25} for i in range(height) for j in range(width)}


returns_sa_matrix = {(i,j): {key: [] for key in grid.actions.keys()} for i in range(height) for j in range(width) }


for _ in range(1000):
    grid.state = (np.random.randint(0,5), np.random.randint(0,5)) #Choose a random state
    action     = np.random.choice(list(policy[grid.state].keys()), p=list(policy[grid.state].values())) # Choose a random action


