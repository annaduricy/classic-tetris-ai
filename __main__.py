from nes_py.wrappers import JoypadSpace
import gym
import gym_classic_tetris
from gym_classic_tetris.actions import TETRIS_CONTROLS

env = gym.make('Tetris-v0')
# env = JoypadSpace(env, TETRIS_CONTROLS)

observation = env.reset()
while 1:
    env.render()
    action = env.action_space.sample()
    # Skip any inputs that use start or select or BOTH right and left
    while ((action & 4) or (action & 8) or ((action & 192) == 192)):
        action = env.action_space.sample()
    env.step(action)
    

env.close()
