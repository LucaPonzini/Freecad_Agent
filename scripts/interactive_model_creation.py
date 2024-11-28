import FreeCAD
import Part
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

def create_shape(shape_type, *params):
    """Crea la forma richiesta dall'utente."""
    if shape_type == 'cubo':
        # Crea un cubo con dimensioni specificate dall'utente
        if len(params) != 1:
            raise ValueError("Un cubo richiede 1 parametro: la lunghezza del lato.")
        size = params[0]
        return Part.makeBox(size, size, size)

    elif shape_type == 'sfera':
        # Crea una sfera con raggio specificato dall'utente
        if len(params) != 1:
            raise ValueError("Una sfera richiede 1 parametro: il raggio.")
        radius = params[0]
        sphere = Part.makeSphere(radius)
        return sphere

    elif shape_type == 'cilindro':
        # Crea un cilindro con raggio e altezza specificati dall'utente
        if len(params) != 2:
            raise ValueError("Un cilindro richiede 2 parametri: il raggio e l'altezza.")
        radius, height = params
        cylinder = Part.makeCylinder(radius, height)
        return cylinder

    else:
        raise ValueError("Tipo di forma non supportato. Scegli tra 'cubo', 'sfera', o 'cilindro'.")

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

def main():
    """Funzione principale che gestisce l'input dell'utente e visualizza il modello."""
    print("Benvenuto nel programma di creazione di modelli 3D.")
    
    # Chiedere all'utente quale oggetto creare
    shape_type = input("Scegli la forma da creare ('cubo', 'sfera', 'cilindro'): ").strip().lower()
    
    if shape_type == 'cubo':
        size = float(input("Inserisci la dimensione del lato del cubo: "))
        shape = create_shape('cubo', size)
    
    elif shape_type == 'sfera':
        radius = float(input("Inserisci il raggio della sfera: "))
        shape = create_shape('sfera', radius)
    
    elif shape_type == 'cilindro':
        radius = float(input("Inserisci il raggio del cilindro: "))
        height = float(input("Inserisci l'altezza del cilindro: "))
        shape = create_shape('cilindro', radius, height)
    
    else:
        print("Forma non riconosciuta. Per favore scegli tra 'cubo', 'sfera' o 'cilindro'.")
        return
    
    # Visualizza il modello creato
    try:
        plot_model(shape)
    except Exception as e:
        print(f"Errore durante la creazione o la visualizzazione del modello: {e}")

if __name__ == "__main__":
    main()
