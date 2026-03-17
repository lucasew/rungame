import sys
import os
import unittest
from unittest.mock import patch, MagicMock

# Adjust sys.path so we can import from src/
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from rungame import run_game, display_available_games, GAMES_CONFIG, main

class TestRungame(unittest.TestCase):

    @patch('os.system')
    def test_run_game_success(self, mock_os_system):
        """Test that run_game successfully executes os.system for a valid game."""
        game_name = "fs13"
        run_game(game_name)
        mock_os_system.assert_called_once_with(GAMES_CONFIG[game_name])

    @patch('rungame.report_error')
    @patch('builtins.print')
    @patch('rungame.display_available_games')
    def test_run_game_not_found(self, mock_display, mock_print, mock_report_error):
        """Test that a KeyError is caught and handled when an invalid game is provided."""
        game_name = "invalid_game"
        run_game(game_name)

        # Verify report_error was called
        self.assertTrue(mock_report_error.called)
        args, kwargs = mock_report_error.call_args
        self.assertIsInstance(args[0], KeyError)
        self.assertEqual(args[1]["requested_game"], game_name)
        self.assertIn("available_games", args[1])

        # Verify print and display_available_games were called
        mock_print.assert_called_with(f"Error: Game '{game_name}' not found. Check the available list below:")
        mock_display.assert_called_once()

    @patch('rungame.report_error')
    @patch('builtins.print')
    @patch('os.system')
    def test_run_game_unexpected_error(self, mock_os_system, mock_print, mock_report_error):
        """Test that unexpected exceptions are caught and reported."""
        mock_os_system.side_effect = Exception("Some weird error")
        game_name = "fs13"
        run_game(game_name)

        # Verify report_error was called
        self.assertTrue(mock_report_error.called)
        args, kwargs = mock_report_error.call_args
        self.assertIsInstance(args[0], Exception)
        self.assertEqual(str(args[0]), "Some weird error")
        self.assertEqual(args[1]["requested_game"], game_name)

        mock_print.assert_called_with("An unexpected error occurred while launching the game.")

    @patch('rungame.run_game')
    def test_main_with_args(self, mock_run_game):
        """Test main entry point with valid arguments."""
        args = ["rungame.py", "csgo"]
        main(args)
        mock_run_game.assert_called_once_with("csgo")

    @patch('rungame.display_available_games')
    def test_main_no_args(self, mock_display):
        """Test main entry point with no arguments."""
        args = ["rungame.py"]
        main(args)
        mock_display.assert_called_once()


if __name__ == '__main__':
    unittest.main()
