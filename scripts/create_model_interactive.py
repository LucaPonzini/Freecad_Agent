import FreeCAD
import Part
from create_model_utils import convert_to_mesh

def create_house_3d():
    # Crea una casa 3D (parallelepipedo)
    house = Part.makeBox(10, 8, 6)  # Parallelepipedo 10x8x6
    door = Part.makeBox(2, 1, 4)  # Porta
    door.translate(FreeCAD.Vector(4, 0, 1))  # Posiziona la porta
    house = house.cut(door)  # Rimuovi la porta
    return house

def create_house_2d():
    # Crea una casa 2D (rettangolo)
    house = Part.makeRectangle(10, 8)  # Rettangolo 10x8
    return house

def display_model(model, model_type='3d'):
    try:
        # Assicurati di avere un documento attivo
        doc = FreeCAD.activeDocument()
        if doc is None:
            doc = FreeCAD.newDocument()

        if model is not None:
            print(f"Tipo di oggetto creato: {type(model)}")
            print(f"Shape è presente, stato della shape: {model.isValid()}")

            # Converte il modello in mesh per visualizzarlo
            if model_type == '3d':
                mesh_object = convert_to_mesh(model)
                if mesh_object is not None:
                    print("Mesh 3D creata con successo!")
                    mesh_feature = doc.addObject("Mesh::Mesh", "house_mesh")
                    mesh_feature.Mesh = mesh_object
                    doc.recompute()  # Ricalcola il documento
                else:
                    print("Impossibile creare la mesh del modello.")
            elif model_type == '2d':
                print("Visualizzazione della figura 2D.")
                # Visualizza la figura 2D (disegno) senza la conversione in mesh
                part_feature = doc.addObject("Part::Feature", "House2D")
                part_feature.Shape = model
                doc.recompute()  # Ricalcola il documento

        else:
            print("Il modello non è stato creato correttamente.")
    except Exception as e:
        print(f"Errore durante la visualizzazione del modello: {e}")

# Funzione principale
def main():
    # Chiedi all'utente che tipo di modello creare
    model_type = input("Scegli il tipo di modello (3d/2d): ").strip().lower()

    if model_type == '3d':
        house = create_house_3d()
    elif model_type == '2d':
        house = create_house_2d()
    else:
        print("Tipo di modello non valido, scegli tra '3d' o '2d'.")
        return

    # Visualizza il modello
    display_model(house, model_type)

# Esegui la funzione principale
if __name__ == "__main__":
    main()
