from gym.envs.registration import register
from gym_classic_tetris.tetris_env import TetrisEnv

register(
    id='Tetris-v0',
    entry_point='gym_classic_tetris:TetrisEnv',
)