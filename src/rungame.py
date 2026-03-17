import sys
import os
import pprint
from error_reporter import report_error

GAMES_CONFIG = {
    "fs13": "D:/Programas/Farming Simulator 2013/FarmingSimulator2013.exe",
    "teste": "D:/Programas/SpeedAutoClicker.exe",
    "csgo": "D:/Programas/Counter-Strike Global Offensive/Run_CSGO.exe",
    "ets2": "D:/Programas/EuroTruck Simulator 2/bin/win_x86/eurotrucks2.exe",
    "cs16": '"D:/Programas/CounterStrike 1.6/hl.exe" -game cstrike',
    "pb": "D:/Programas/Pointblank/PBLauncher.exe",
    "gtavc": "D:/Programas/GTA Vice City/gta-vc.exe",
    "gtasa": "D:/Programas/GTA San Andreas/GTA San Andreas/gta_sa.exe",
    "pinball": "D:/Programas/Pinball/pinball.exe",
    "samp": "D:/Programas/GTA San Andreas/GTA San Andreas/samp.exe",
    "woshaulin": "D:/Programas/18 Wheels of Steel Haulin/haulin.exe",
    "mc": "C:/Users/User/Desktop/Minecraft.exe",
    "stk": "D:/Programas/SuperTuxKart/supertuxkart.exe"
}

def display_available_games():
    """Prints the available commands to launch games."""
    print("Lista de comandos disponíveis")
    pprint.pprint(GAMES_CONFIG)

def run_game(name):
    """Executes a game by its alias."""
    try:
        command = GAMES_CONFIG[name]
        # In a real scenario, use subprocess.run, but we keep os.system to preserve existing behavior
        os.system(command)
    except KeyError as e:
        report_error(e, {"requested_game": name, "available_games": list(GAMES_CONFIG.keys())})
        print(f"Error: Game '{name}' not found. Check the available list below:")
        display_available_games()
    except Exception as e:
        report_error(e, {"requested_game": name})
        print("An unexpected error occurred while launching the game.")

def main(args=None):
    if args is None:
        args = sys.argv
    try:
        game_name = args[1]
        run_game(game_name)
    except IndexError:
        display_available_games()

if __name__ == "__main__":
    main()
