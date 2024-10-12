import matplotlib.pyplot as plt
import numpy as np
import random
from scipy.interpolate import griddata
from matplotlib.widgets import Button

# Initialize sensor values
def generate_sensor_values():
    point1 = random.randrange(1, 10)
    point2 = random.randrange(11, 20)
    point3 = random.randrange(21, 30)
    point4 = random.randrange(31, 40)
    point5 = random.randrange(41, 50)
    point6 = random.randrange(51, 60)
    return [point1, point2, point3, point4, point5, point6]

# Set up coordinates
coordinates = [
    [2.5, 3], [4.5, 2], [7, 2.5],
    [3, 10.5], [8, 10.5],
    [2.5, 16], [5.5, 16], [9, 16],
    [2.5, 18], [9, 18]
]

# Extract the first 6 coordinates for sensor mapping
x_coords = [coord[0] for coord in coordinates[:6]]
y_coords = [coord[1] for coord in coordinates[:6]]

# Initialize the plot
fig, ax = plt.subplots()
plt.subplots_adjust(bottom=0.2)  # Make space for buttons

# Set coordinate limits and labels
plt.xlim(0, 10)
plt.ylim(0, 20)
plt.xlabel('X Coordinate')
plt.ylabel('Y Coordinate')
plt.title('Real-Time Sensor Heatmap')

# Initialize sensor values
sensor_values = generate_sensor_values()

# Create the initial grid
grid_x, grid_y = np.mgrid[0:10:100j, 0:20:200j]
grid_z = griddata((x_coords, y_coords), sensor_values, (grid_x, grid_y), method='linear')

# Display the initial heatmap
heatmap = ax.imshow(
    grid_z.T,
    extent=(0, 10, 0, 20),
    origin='lower',
    cmap='jet',
    alpha=0.7,
    interpolation='bilinear'
)

# Scatter plot of sensor points
scatter = ax.scatter(
    x_coords, y_coords,
    c=sensor_values,
    cmap='jet',
    s=200,
    edgecolor='k'
)

# Add a colorbar
cbar = plt.colorbar(heatmap, ax=ax, label='Sensor Value')

# Flag to control animation
is_running = False

# Update function for animation
def update(frame):
    if not is_running:
        return
    # Generate new sensor values
    new_sensor_values = generate_sensor_values()
    
    # Update grid data
    new_grid_z = griddata(
        (x_coords, y_coords),
        new_sensor_values,
        (grid_x, grid_y),
        method='linear'
    )
    heatmap.set_data(new_grid_z.T)
    
    # Update scatter plot
    scatter.set_array(np.array(new_sensor_values))
    
    # Redraw the colorbar
    cbar.update_normal(heatmap)
    
    return heatmap, scatter

# Button callback functions
def start(event):
    global is_running
    is_running = True

def stop(event):
    global is_running
    is_running = False

# Create Start button
ax_start = plt.axes([0.1, 0.05, 0.1, 0.075])  # [left, bottom, width, height]
btn_start = Button(ax_start, 'Start')
btn_start.on_clicked(start)

# Create Stop button
ax_stop = plt.axes([0.25, 0.05, 0.1, 0.075])
btn_stop = Button(ax_stop, 'Stop')
btn_stop.on_clicked(stop)

# Create the animation
from matplotlib.animation import FuncAnimation

ani = FuncAnimation(
    fig,
    update,
    interval=500,  # Update every 500 milliseconds
    blit=False
)

plt.show()
