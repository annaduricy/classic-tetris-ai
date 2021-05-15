"""An OpenAI Gym interface to the NES game Tetris"""
from nes_py import NESEnv
from enum import Enum

rom_path = './roms/Tetris.nes'

class JoyPad(Enum):
    NOOP = 0
    A = 1
    B = 2
    SELECT = 4
    START = 8
    UP = 16
    DOWN = 32
    LEFT = 64
    RIGHT = 128

# The value stored here is the number of frames before the copyrightright can be skipped
_COPYRIGHT_DELAY_ADDRESS = 0x00C3

class TetrisEnv(NESEnv):
    """An OpenAI Gym interface to the NES game Tetris"""

    def __init__(self):
        """Initialize a new Tetris environment."""
        super(TetrisEnv, self).__init__(rom_path)

        self.reset()
        self._skip_start_screen()
        self._backup()

    def _skip_start_screen(self):
        # Skip the loading sequence where a 0 is present
        while self.ram[_COPYRIGHT_DELAY_ADDRESS] == 0:
            self._frame_advance(JoyPad.NOOP.value)

        # Wait until the scene is skippable
        while self.ram[_COPYRIGHT_DELAY_ADDRESS] != 0:
            self._frame_advance(JoyPad.NOOP.value)
        
        # Skip the copyright and start menu
        for i in range(8):
            self._frame_advance_strobe(JoyPad.START)
        
        # Move the selection right 3
        for i in range(3):
            self._frame_advance_strobe(JoyPad.RIGHT)
        
        # Move the selection down 1
        self._frame_advance_strobe(JoyPad.DOWN)

        # Press start to select level 8
        self._frame_advance_strobe(JoyPad.START)

    # A button has to be pressed and released to register
    def _frame_advance_strobe(self, button):
        self._frame_advance(button.value)
        self._frame_advance(JoyPad.NOOP.value)

    def _will_reset(self):
        """Handle any RAM hacking after a reset occurs."""
        # use this method to perform setup before and episode resets.
        # the method returns None
        pass

    def _did_reset(self):
        """Handle any RAM hacking after a reset occurs."""
        # use this method to access the RAM of the emulator 
        # and perform setup for each episode. 
        # the method returns None
        pass

    def _did_step(self, done):
        """
        Handle any RAM hacking after a step occurs.

        Args:
            done: whether the done flag is set to true

        Returns:
            None

        """
        pass

    def _get_reward(self):
        """Return the reward after a step occurs."""
        return 0

    def _get_done(self):
        """Return True if the episode is over, False otherwise."""
        return False

    def _get_info(self):
        """Return the info after a step occurs."""
        return {}


# explicitly define the outward facing API for the module
__all__ = [TetrisEnv.__name__]
