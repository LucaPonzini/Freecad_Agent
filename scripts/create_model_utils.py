import FreeCAD
import Part
import Mesh

def convert_to_mesh(shape):
    """
    Converte una forma 3D in una mesh.
    """
    try:
        # Crea una mesh dal modello
        mesh = Mesh.Mesh(shape)
        return mesh
    except Exception as e:
        print(f"Errore nella conversione del modello in mesh: {e}")
        return None
