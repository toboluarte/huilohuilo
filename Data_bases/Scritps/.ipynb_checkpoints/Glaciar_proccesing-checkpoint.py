import netCDF4 as nc
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import cartopy.crs as ccrs
import cartopy.feature as cfeature
#Exploring the dataset of simulations results

files = [
"/home/tobo/Documents/Personales/Fundacion_Huilohuilo/Huilo_Huilo_Material/Datos_hidro_mocho/Datos_mocho/Mocho_rcp45/rcp45/mocho100_rcp45_1_2D_2040.nc",
"/home/tobo/Documents/Personales/Fundacion_Huilohuilo/Huilo_Huilo_Material/Datos_hidro_mocho/Datos_mocho/Mocho_rcp45/rcp45/mocho100_rcp45_1_2D_2060.nc",
"/home/tobo/Documents/Personales/Fundacion_Huilohuilo/Huilo_Huilo_Material/Datos_hidro_mocho/Datos_mocho/Mocho_rcp45/rcp45/mocho100_rcp45_1_2D_2080.nc",
"/home/tobo/Documents/Personales/Fundacion_Huilohuilo/Huilo_Huilo_Material/Datos_hidro_mocho/Datos_mocho/Mocho_rcp45/rcp45/mocho100_rcp45_1_2D_2099.nc",
]
# Variables para almacenar los datos
data_list = []
time_labels = []

# Cargar los datos de cada archivo
for file in files:
    dataset = nc.Dataset(file)
    lon = dataset.variables['lon'][:]
    lat = dataset.variables['lat'][:]
    H = dataset.variables['H'][:]  # Espesor del hielo
    time = dataset.variables['time'][:]
    
    data_list.append(H)
    time_labels.append(time)

# Configurar el espacio para la animación
fig = plt.figure(figsize=(8, 6))
ax = plt.axes(projection=ccrs.PlateCarree())
ax.set_extent([lon.min(), lon.max(), lat.min(), lat.max()], crs=ccrs.PlateCarree())

# Agregar capas base
ax.add_feature(cfeature.LAND, edgecolor='black', zorder=1)
ax.add_feature(cfeature.BORDERS, linestyle='--', zorder=1)
ax.coastlines(resolution='10m', color='black', linewidth=0.5, zorder=1)
ax.gridlines(draw_labels=True, color='gray', alpha=0.5, linestyle='--')

# Inicializar la imagen
img = ax.imshow(data_list[0], cmap="Blues", origin="lower",
                extent=[lon.min(), lon.max(), lat.min(), lat.max()], 
                transform=ccrs.PlateCarree(), interpolation='nearest')
colorbar = fig.colorbar(img, ax=ax, orientation='horizontal', pad=0.05, label="Espesor del hielo (m)")
title = ax.set_title(f'Espesor del hielo - Año {int(time_labels[0])}')

# Función de actualización para la animación
def update(frame):
    img.set_data(data_list[frame])
    title.set_text(f'Espesor del hielo - Año {int(time_labels[frame])}')
    return img, title

# Crear la animación
ani = FuncAnimation(fig, update, frames=len(data_list), interval=1000, blit=False)

# Guardar la animación como video o GIF
ani.save("animacion_hielo_RCP45.gif", fps=1)

plt.show()