import FreeCAD
import Part
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

def create_walls_with_door_and_window():
    """Crea la casa con una porta e una finestra."""
    # Creazione della parete
    wall = Part.makeBox(10, 1, 6)  # Parete lunga con una larghezza di 1
    door = Part.makeBox(2, 0.2, 3)  # Porta sottile
    door.translate(FreeCAD.Vector(4, 0, 0))  # Posiziona la porta a metà della parete
    
    # Creazione della finestra
    window = Part.makeBox(1.5, 0.2, 1.5)  # Finestra sottile
    window.translate(FreeCAD.Vector(1.5, 0, 2.5))  # Posiziona la finestra sulla parete
    
    # Creazione della parete con porta e finestra
    wall_with_door_and_window = wall.cut(door)
    wall_with_door_and_window = wall_with_door_and_window.cut(window)
    if not wall_with_door_and_window.isValid():
        raise ValueError("La parete con porta e finestra non è valida.")
    
    return wall_with_door_and_window

def plot_model(model):
    """Plotta un modello 3D utilizzando matplotlib."""
    # Verifica che il modello sia valido
    if not model:
        raise ValueError("Il modello fornito è vuoto o non valido.")

    # Estrai la mesh per la visualizzazione
    mesh = model.tessellate(1)
    vertices = list({tuple(v) for v in mesh[0]})
    if not vertices:
        raise ValueError("Il modello non ha vertici validi per il rendering.")

    faces = [[vertices.index(tuple(mesh[0][i])) for i in face] for face in mesh[1]]

    # Plotta il modello
    fig = plt.figure()
    ax = fig.add_subplot(111, projection="3d")
    ax.add_collection3d(
        Poly3DCollection(
            [[vertices[i] for i in face] for face in faces],
            facecolors="orange",  # Colore delle pareti
            edgecolors="black",
            linewidths=0.5,
            alpha=0.8,
        )
    )
    
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")
    ax.set_xlim([min(v[0] for v in vertices), max(v[0] for v in vertices)])
    ax.set_ylim([min(v[1] for v in vertices), max(v[1] for v in vertices)])
    ax.set_zlim([min(v[2] for v in vertices), max(v[2] for v in vertices)])
    plt.show()


# Creazione della casa con la porta e la finestra
try:
    house_with_door_and_window = create_walls_with_door_and_window()
    
    # Visualizza la casa con la porta e la finestra
    plot_model(house_with_door_and_window)
except Exception as error:
    print(f"Errore durante la creazione o la visualizzazione del modello: {error}")
