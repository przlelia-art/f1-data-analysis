import fastf1
from matplotlib import pyplot as plt

fastf1.Cache.enable_cache("cache")

session = fastf1.get_session(2024, "Bahrain", "R")
session.load()

verstappen = session.laps.pick_driver("VER")
leclerc = session.laps.pick_driver("LEC")

fig, ax = plt.subplots(figsize=(12, 6))
ax.plot(verstappen["LapNumber"], verstappen["LapTime"].dt.total_seconds(), label="Verstappen", color="blue")
ax.plot(leclerc["LapNumber"], leclerc["LapTime"].dt.total_seconds(), label="Leclerc", color="red")

ax.set_title("Verstappen-Leclerc bahreïn 2024")
ax.set_xlabel("Numéro de tour")
ax.set_ylabel("Temps au tour (secondes)")
ax.legend()

plt.savefig("Comparaison Max et Charles.png")
plt.show()