import fastf1
from matplotlib import pyplot as plt 
import seaborn as sns

fastf1.Cache.enable_cache("cache")

session = fastf1.get_session(2024, "Monza", "R")
session.load()

verstappen = session.laps.pick_drivers("VER")
leclerc = session.laps.pick_drivers("LEC")
norris = session.laps.pick_drivers("NOR")

fig, ax = plt.subplots(figsize=(12, 6))

ax.plot(verstappen["LapNumber"], verstappen["SpeedST"], label="Verstappen", color="blue")
ax.plot(leclerc["LapNumber"], leclerc["SpeedST"], label="Leclerc", color="red")
ax.plot(norris["LapNumber"], norris["SpeedST"], label="Norris", color="orange")

ax.set_title("Analyse de vitesse de Verstappen, Leclerc et Norris")
ax.set_xlabel("Numéro de tour")
ax.set_ylabel("Vitesse sur ligne droite")
ax.legend()

plt.savefig("Comparaison des vitesses de Verstappen, Leclerc et Norris.png")
plt.show()
