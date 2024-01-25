import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np

plt.style.use('dark_background')

n_points = 500
alfa = np.linspace(0, 2 * np.pi, n_points)

# parametri orbita
e_radius = 5
m_radius = 7
earth_a = e_radius
earth_e = 0.0167
mars_a = m_radius
mars_e = 0.0934

# jednacine kretanja
x_earth = earth_a * (1 - earth_e**2) / (1 + earth_e * np.cos(alfa)) * np.cos(alfa)
y_earth = earth_a * (1 - earth_e**2) / (1 + earth_e * np.cos(alfa)) * np.sin(alfa)

x_mars = mars_a * (1 - mars_e**2) / (1 + mars_e * np.cos(alfa)) * np.cos(alfa)
y_mars = mars_a * (1 - mars_e**2) / (1 + mars_e * np.cos(alfa)) * np.sin(alfa)


kometa_a = 8  
kometa_b = 3  
kometa_e = 0.5  
x_kometa = kometa_a * (1 - kometa_e**2) / (1 + kometa_e * np.cos(alfa)) * np.cos(alfa)
y_kometa = kometa_b * (1 - kometa_e**2) / (1 + kometa_e * np.cos(alfa)) * np.sin(alfa)

fig, ax = plt.subplots(figsize=(8, 8))
ax.set_xlim(-12, 12)
ax.set_ylim(-10, 10)
ax.plot(0, 0, 'X', markersize=10, color="yellow", label="Sunce")
ax.plot(x_earth, y_earth, 'g-')
ax.plot(x_mars, y_mars, 'r-')
earth_dot, = ax.plot([], [], 'go', markersize=5, label="Zemlja")
mars_dot, = ax.plot([], [], 'ro', markersize=5, label="Mars")
earth_label = ax.text(x_earth[0], y_earth[0], ' Zemlja', color='white')
mars_label = ax.text(x_mars[0], y_mars[0], ' Mars', color='white')
kometa, = ax.plot([], [], 'c.', markersize=15, label="Kometa")
kometa_trace, = ax.plot([], [], 'c-', alpha=0.5, label="Trajektorija komete")


plt.legend(loc='upper right')

kometa_positions = []

def animate(i):
    earth_dot.set_data(x_earth[i], y_earth[i])
    earth_label.set_position((x_earth[i], y_earth[i]))
    mars_label.set_position((x_mars[i], y_mars[i]))
    kometa_positions.append((x_kometa[i], y_kometa[i]))
    kometa.set_data(x_kometa[i], y_kometa[i])
    kometa_trace.set_data(*zip(*kometa_positions))
    return earth_dot, earth_label, mars_label, kometa, kometa_trace

anim = FuncAnimation(fig, animate, frames=n_points, interval=40, repeat=True)
plt.show()
