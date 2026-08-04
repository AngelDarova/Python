feed_instagram = ['foto_playa', 'meme_de_programacion', 'video_gato']

"""

print(feed_instagram[0])    
print(feed_instagram[1])    
print(feed_instagram[2])

para evitar lo anterior, hacemos uso del ciclo for    
"""

print("----INICIANDO TU FEED INSTAGRAM----")

for alias in feed_instagram:
    print(f"Mostrando en pantalla {alias}")
    print("-----------------------")
    
for post in feed_instagram:
    print(f"Mostrando en pantalla {post}")
    print("-----------------------")
    
# El ciclo for nos ayuda a darle Formato de Salida cuando recorremos una Lista