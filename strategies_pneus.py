import fastf1
from matplotlib import pyplot as plt 
import seaborn as sns

fastf1.Cache.enable_cache("cache")

session = fastf1.get_session(2024, "Bahrain", "R")
session.load()

verstappen = session.laps.pick_driver("VER")
leclerc = session.laps.pick_driver("LEC")

fig, ax = plt.subplots(figsize=(12, 6))

sns.scatterplot(data=verstappen, x="LapNumber", y=verstappen["LapTime"].dt.total_seconds(), hue="Compound", ax=ax)
sns.scatterplot(data=leclerc, x="LapNumber", y=leclerc["LapTime"].dt.total_seconds(), hue="Compound", ax=ax, legend=False)

ax.set_title("Stratégie Max-Charles Bahreïn 2024")
ax.set_xlabel("Numéro de tour")
ax.set_ylabel("Temps au tour (secondes)")
ax.legend()

plt.savefig("Comparaison stratégie des pneus de Max-Charles.png")
plt.show()