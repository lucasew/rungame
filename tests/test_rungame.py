import unittest
from unittest.mock import patch, MagicMock
import subprocess
import sys
import io
import os

# Add root directory to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import rungame

class TestRunGame(unittest.TestCase):
    @patch('subprocess.run')
    def test_rungame_valid(self, mock_run):
        # Test executing a valid game
        rungame.rungame('mc')
        mock_run.assert_called_once_with(['C:/Users/User/Desktop/Minecraft.exe'], check=True)

    @patch('subprocess.run')
    def test_rungame_multiple_args(self, mock_run):
        # Test executing a game with multiple args (e.g. cs16)
        rungame.rungame('cs16')
        mock_run.assert_called_once_with(['D:/Programas/CounterStrike 1.6/hl.exe', '-game', 'cstrike'], check=True)

    def test_rungame_invalid_key(self):
        # Test that KeyError is raised when game name is not found
        with self.assertRaises(KeyError):
            rungame.rungame('nonexistent_game')

if __name__ == '__main__':
    unittest.main()
