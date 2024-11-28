import FreeCAD
import Part
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

def create_shape(shape_type, *params):
    """Crea una singola forma."""
    if shape_type == 'cubo':
        size = params[0]
        return Part.makeBox(size, size, size)
    elif shape_type == 'sfera':
        radius = params[0]
        return Part.makeSphere(radius)
    elif shape_type == 'cilindro':
        radius, height = params
        return Part.makeCylinder(radius, height)
    else:
        raise ValueError("Tipo di forma non supportato.")

def combine_shapes(shapes):
    """Combina una lista di forme in un'unica struttura."""
    combined = shapes[0]
    for shape in shapes[1:]:
        combined = combined.fuse(shape)
    return combined

def plot_model(model):
    """Plotta un modello 3D utilizzando matplotlib."""
    mesh = model.tessellate(1)
    vertices = list({tuple(v) for v in mesh[0]})
    faces = [[vertices.index(tuple(mesh[0][i])) for i in face] for face in mesh[1]]
    fig = plt.figure()
    ax = fig.add_subplot(111, projection="3d")
    ax.add_collection3d(
        Poly3DCollection(
            [[vertices[i] for i in face] for face in faces],
            facecolors="lightgray",
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
    print("Benvenuto nel programma per creare composizioni di forme 3D!")
    shapes = []

    while True:
        print("\nCosa vuoi aggiungere alla scena?")
        shape_type = input("Scegli tra 'cubo', 'sfera', 'cilindro' (o digita 'fine' per terminare): ").strip().lower()
        
        if shape_type == 'fine':
            break

        try:
            if shape_type == 'cubo':
                size = float(input("Inserisci la dimensione del lato del cubo: "))
                x = float(input("Inserisci la posizione X del cubo: "))
                y = float(input("Inserisci la posizione Y del cubo: "))
                z = float(input("Inserisci la posizione Z del cubo: "))
                shape = create_shape('cubo', size)
                shape.translate(FreeCAD.Vector(x, y, z))
                shapes.append(shape)
            
            elif shape_type == 'sfera':
                radius = float(input("Inserisci il raggio della sfera: "))
                x = float(input("Inserisci la posizione X della sfera: "))
                y = float(input("Inserisci la posizione Y della sfera: "))
                z = float(input("Inserisci la posizione Z della sfera: "))
                shape = create_shape('sfera', radius)
                shape.translate(FreeCAD.Vector(x, y, z))
                shapes.append(shape)
            
            elif shape_type == 'cilindro':
                radius = float(input("Inserisci il raggio del cilindro: "))
                height = float(input("Inserisci l'altezza del cilindro: "))
                x = float(input("Inserisci la posizione X del cilindro: "))
                y = float(input("Inserisci la posizione Y del cilindro: "))
                z = float(input("Inserisci la posizione Z del cilindro: "))
                shape = create_shape('cilindro', radius, height)
                shape.translate(FreeCAD.Vector(x, y, z))
                shapes.append(shape)
            
            else:
                print("Forma non riconosciuta. Scegli tra 'cubo', 'sfera', 'cilindro', o digita 'fine'.")
        
        except Exception as e:
            print(f"Errore durante la creazione della forma: {e}")

    if shapes:
        try:
            combined_model = combine_shapes(shapes)
            plot_model(combined_model)
        except Exception as e:
            print(f"Errore durante la combinazione o visualizzazione delle forme: {e}")
    else:
        print("Nessuna forma è stata aggiunta alla scena. Uscita.")

if __name__ == "__main__":
    main()
