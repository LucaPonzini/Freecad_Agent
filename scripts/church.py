import FreeCAD
import Part
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

def create_church_with_bell_tower():
    """Crea una chiesa lunga con finestre sui lati lunghi e un campanile senza finestre."""
    
    # Creazione della base della chiesa (parallelepipedo lungo, tipo regolo)
    church_base = Part.makeBox(40, 10, 5)  # Base rettangolare di 40x10x5, un regolo lungo
    
    # Creazione della porta
    door = Part.makeBox(3, 0.2, 3)  # Porta di 3x0.2x3
    door.translate(FreeCAD.Vector(18.5, 0, 0))  # Posiziona la porta al centro della parete principale
    
    # Creazione delle finestre laterali sui due lati lunghi (lato lungo = 40)
    windows = []
    for i in range(2, 38, 4):  # Finestre posizionate a intervalli regolari sui due lati lunghi
        window = Part.makeBox(2, 0.2, 2)  # Finestra di 2x0.2x2
        window.translate(FreeCAD.Vector(i, 0, 3))  # Posiziona la finestra sul lato lungo
        windows.append(window)
    
    # Creazione del campanile (senza finestre)
    # La base del campanile
    bell_tower_base = Part.makeBox(6, 6, 15)  # Base del campanile 6x6x15
    bell_tower_base.translate(FreeCAD.Vector(17, 2, 5))  # Posizionamento sopra la chiesa
    
    # Combinare la base della chiesa, la porta, le finestre e il campanile
    church_with_features = church_base.cut(door)
    for window in windows:
        church_with_features = church_with_features.cut(window)
    church_with_features = church_with_features.fuse(bell_tower_base)
    
    # Verifica se la chiesa è valida
    if not church_with_features.isValid():
        raise ValueError("La chiesa con il campanile non è valida.")
    
    return church_with_features

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
            facecolors="lightgray",  # Colore delle pareti
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


# Creazione della chiesa con il campanile
try:
    church_model = create_church_with_bell_tower()
    
    # Visualizza la chiesa con il campanile e le finestre
    plot_model(church_model)
except Exception as error:
    print(f"Errore durante la creazione o la visualizzazione del modello: {error}")
