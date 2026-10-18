import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Create heart data using NumPy
t = np.linspace(0, 2 * np.pi, 1000)

x = 16 * np.sin(t) ** 3
y = (13 * np.cos(t) - 5 * np.cos(2*t)
     - 2 * np.cos(3*t) - np.cos(4*t))

# Store heart coordinates using Pandas
heart = pd.DataFrame({"X": x, "Y": y})

# Create the figure
fig, ax = plt.subplots(figsize=(8, 8))
fig.patch.set_facecolor("black")
ax.set_facecolor("black")
ax.set_xlim(-22, 22)
ax.set_ylim(-22, 22)
ax.axis("off")

# Heart and message
heart_shape, = ax.plot([], [], color="#ff1744", linewidth=3)
glow, = ax.plot([], [], "o", color="#ff4081", markersize=8)

message = ax.text(
    0, -19, "I LOVE YOU ❤️",
    color="white", fontsize=23,
    ha="center", fontweight="bold"
)

# Animation function
def animate(frame):
    # Popping heart effect
    scale = 1 + 0.12 * abs(np.sin(frame * 0.12))

    heart_shape.set_data(
        heart["X"] * scale,
        heart["Y"] * scale
    )

    # Glowing heart effect
    glow.set_data(
        [0], [0]
    )
    glow.set_markersize(8 + 8 * abs(np.sin(frame * 0.2)))

    message.set_color(
        ["#ff1744", "#ff80ab", "#ffffff"][frame % 3]
    )

    return heart_shape, glow, message

# Start animation
ani = FuncAnimation(
    fig, animate, frames=200,
    interval=30, blit=True
)

plt.title(
    "A LITTLE LOVE FOR YOU 💕",
    color="pink", fontsize=16, pad=20
)

plt.show()