import gym


def main():
    env = gym.make('CartPole-v0', render_mode = 'human')
    for i_episode in range(20):
        observation = env.reset()
        for t in range(100):
            env.render()
            print(observation)
            action = env.action_space.sample()
            observation, reward, done, info, _ = env.step(action)
        if done:
            print("Episode finished after {} timesteps".format(t + 1))
            break
    env.close()

main()
