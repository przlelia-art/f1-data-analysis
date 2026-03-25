import fastf1
from matplotlib import pyplot as plt 
import seaborn as sns

fastf1.Cache.enable_cache("cache")

session = fastf1.get_session(2024, "Bahrain", "Q")
session.load()

verstappen = session.laps.pick_driver("VER").pick_fastest()
leclerc = session.laps.pick_driver("LEC").pick_fastest()

telemetrie_verstappen = verstappen.get_telemetry()
telemetrie_leclerc = leclerc.get_telemetry()

fig, ax = plt.subplots(figsize=(12, 6))

ax.plot(telemetrie_verstappen["Distance"], telemetrie_verstappen["Speed"], label="Verstappen", color="blue")
ax.plot(telemetrie_leclerc["Distance"], telemetrie_leclerc["Speed"], label="Leclerc", color="red")

ax.set_title("Verstappen et Leclerc qualifs Bahreïn 2024")
ax.set_xlabel("Distance")
ax.set_ylabel("Vitesse")
ax.legend()

plt.savefig("Comparaison des qualifications de Verstappen et Leclerc.png")
plt.show()