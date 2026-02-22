import random
import numpy as np
import matplotlib.pyplot as plt

class RobotKesif:
    def __init__(self, size=5):
        self.size = size
        self.state_space = size * size
        self.action_space = 4
        self.start_state = (0, 0)

        self.goal_states = [(4, 4)]
        self.obstacles = [(0,1),(1,3),(3,1),(3,3),(4,1)]

    def reset(self):
        self.robot_position = self.start_state
        return self.robot_position

    def step(self, action):
        x, y = self.robot_position

        if action == 0:      # yukarı
            x = max(0, x-1)
        elif action == 1:    # aşağı
            x = min(self.size-1, x+1)
        elif action == 2:    # sol
            y = max(0, y-1)
        elif action == 3:    # sağ
            y = min(self.size-1, y+1)

        self.robot_position = (x, y)

        if self.robot_position in self.goal_states:
            return self.robot_position, 10, True
        elif self.robot_position in self.obstacles:
            return self.robot_position,- 3, True
        else:
            return self.robot_position, -0.1, False  


class QLearningAgent:
    def __init__(self, env):
        self.env = env
        self.q_table = np.zeros((env.state_space, env.action_space))
        self.alpha = 0.1
        self.gamma = 0.99
        self.epsilon = 1.0
        self.epsilon_decay = 0.995
        self.min_epsilon = 0.1

    def get_state_index(self, state):
        return state[0] * self.env.size + state[1]

    def choose_action(self, state):
        if random.uniform(0, 1) < self.epsilon:
            return random.randint(0, self.env.action_space - 1)
        else:
            state_idx = self.get_state_index(state)
            return np.argmax(self.q_table[state_idx])

    def learn(self, state, action, reward, next_state):
        state_idx = self.get_state_index(state)
        next_state_idx = self.get_state_index(next_state)

        best_next_action = np.argmax(self.q_table[next_state_idx])
        td_target = reward + self.gamma * self.q_table[next_state_idx][best_next_action]
        td_delta = td_target - self.q_table[state_idx][action]
        self.q_table[state_idx][action] += self.alpha * td_delta




env = RobotKesif()
agent = QLearningAgent(env)

episodes = 300
max_steps = 100  
rewards_per_episode = []

for episode in range(episodes):
    state = env.reset()
    total_reward = 0
    done = False
    step_count = 0

    while not done and step_count < max_steps:
        action = agent.choose_action(state)
        next_state, reward, done = env.step(action)

        agent.learn(state, action, reward, next_state)

        state = next_state
        total_reward += reward
        step_count += 1

    agent.epsilon = max(agent.min_epsilon, agent.epsilon * agent.epsilon_decay)
    rewards_per_episode.append(total_reward)



plt.plot(rewards_per_episode)
plt.scatter(range(episodes),rewards_per_episode,s=5 , c="red") # her bi bolumde elde edilen odullerin cizdirilmesi
plt.title("Episode başına toplam odul")
plt.xlabel("Episode")
plt.ylabel("Toplam Reward")
plt.show()
        
        
        
       
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        