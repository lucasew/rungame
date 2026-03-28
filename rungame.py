import sys
import subprocess
import pprint

sys.path.insert(0, sys.path[0])
from src.error_reporter import report_error

lista = {
	"fs13": ["D:/Programas/Farming Simulator 2013/FarmingSimulator2013.exe"],
	"teste": ["D:/Programas/SpeedAutoClicker.exe"],
	"csgo": ["D:/Programas/Counter-Strike Global Offensive/Run_CSGO.exe"],
	"ets2": ["D:/Programas/EuroTruck Simulator 2/bin/win_x86/eurotrucks2.exe"],
	"cs16": ["D:/Programas/CounterStrike 1.6/hl.exe", "-game", "cstrike"],
	"pb": ["D:/Programas/Pointblank/PBLauncher.exe"],
	"gtavc": ["D:/Programas/GTA Vice City/gta-vc.exe"],
	"gtasa": ["D:/Programas/GTA San Andreas/GTA San Andreas/gta_sa.exe"],
	"pinball": ["D:/Programas/Pinball/pinball.exe"],
	"samp": ["D:/Programas/GTA San Andreas/GTA San Andreas/samp.exe"],
	"woshaulin": ["D:/Programas/18 Wheels of Steel Haulin/haulin.exe"],
	"mc": ["C:/Users/User/Desktop/Minecraft.exe"],
	"stk": ["D:/Programas/SuperTuxKart/supertuxkart.exe"]
}

def rungame(name):
	subprocess.run(lista[name], check=True)

if __name__ == "__main__":
	try:
		rungame(sys.argv[1])
	except IndexError:
		print("Lista de comandos disponíveis")
		pprint.pprint(lista)
	except KeyError as e:
		report_error(e)
		print("Jogo não encontrado na lista. Use sem argumentos para ver os jogos disponíveis.")
	except Exception as e:
		report_error(e)
