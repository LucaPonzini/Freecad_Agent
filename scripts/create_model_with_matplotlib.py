import FreeCAD
import Part
import Mesh
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

def create_house_3d():
    """
    Crea una casa 3D come un parallelepipedo.
    """
    house = Part.makeBox(10, 8, 6)  # Parallelepipedo 10x8x6
    door = Part.makeBox(2, 1, 4)  # Porta
    door.translate(FreeCAD.Vector(4, 0, 1))  # Posiziona la porta
    house = house.cut(door)  # Rimuovi la porta
    return house

def create_house_2d():
    """
    Crea una casa 2D come un rettangolo.
    """
    house = Part.makeRectangle(10, 8)  # Rettangolo 10x8
    return house

def convert_to_mesh(shape):
    """
    Converte una forma 3D di FreeCAD in una mesh.
    """
    try:
        mesh = Mesh.Mesh(shape)
        return mesh
    except Exception as e:
        print(f"Errore nella conversione del modello in mesh: {e}")
        return None

def plot_mesh(mesh):
    """
    Visualizza la mesh 3D in matplotlib.
    """
    try:
        vertices = np.array([v.Point for v in mesh.Vertexes])  # Ottieni i vertici della mesh
        faces = []
        
        for f in mesh.Facets:  # Ottieni le facce della mesh
            face = f.getNodes()
            faces.append([face[0], face[1], face[2]])
        
        faces = np.array(faces)

        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')

        # Disegna la mesh
        ax.add_collection3d(Poly3DCollection(faces, facecolors='cyan', linewidths=1, edgecolors='r', alpha=.25))

        # Impostazioni degli assi
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')

        # Impostazioni per una visualizzazione 3D
        ax.set_xlim([np.min(vertices[:, 0]), np.max(vertices[:, 0])])
        ax.set_ylim([np.min(vertices[:, 1]), np.max(vertices[:, 1])])
        ax.set_zlim([np.min(vertices[:, 2]), np.max(vertices[:, 2])])

        plt.show()
    except Exception as e:
        print(f"Errore nella visualizzazione della mesh: {e}")

def display_model(model, model_type='3d'):
    """
    Visualizza un modello in FreeCAD o 2D tramite matplotlib.
    """
    if model is not None:
        print(f"Tipo di oggetto creato: {type(model)}")
        print(f"Shape è presente, stato della shape: {model.isValid()}")
        
        if model_type == '3d':
            # Converti il modello in mesh e visualizzalo
            mesh_object = convert_to_mesh(model)
            if mesh_object is not None:
                print("Mesh 3D creata con successo!")
                plot_mesh(mesh_object)
            else:
                print("Impossibile creare la mesh del modello.")
        elif model_type == '2d':
            # Visualizzazione di una casa 2D (senza mesh)
            print("Visualizzazione della figura 2D.")
            # Al momento non visualizziamo la 2D in Matplotlib
            # Puoi aggiungere qui un metodo per disegnare la 2D se necessario
        else:
            print("Tipo di modello non valido!")
    else:
        print("Il modello non è stato creato correttamente.")

# Funzione principale
def main():
    model_type = input("Scegli il tipo di modello (3d/2d): ").strip().lower()

    if model_type == '3d':
        house = create_house_3d()
    elif model_type == '2d':
        house = create_house_2d()
    else:
        print("Tipo di modello non valido, scegli tra '3d' o '2d'.")
        return

    display_model(house, model_type)

# Esegui la funzione principale
if __name__ == "__main__":
    main()
