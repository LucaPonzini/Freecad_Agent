import FreeCAD
import Part

def create_cube(length, filename):
    # Crea un documento FreeCAD
    doc = FreeCAD.newDocument()
    
    # Crea un cubo
    cube = Part.makeBox(length, length, length)
    
    # Aggiungi il cubo al documento
    part_object = doc.addObject("Part::Feature", filename)
    part_object.Shape = cube
    
    # Esporta il cubo in formato STEP
    step_file = f"models/{filename}.step"
    part_object.Shape.exportStep(step_file)
    
    print(f"Cubo esportato come {step_file}")

# Esegui la creazione e l'esportazione
create_cube(length=10, filename="cube_model")
