import FreeCAD
import Part

def create_sphere(radius, filename):
    # Crea un documento FreeCAD
    doc = FreeCAD.newDocument()
    
    # Crea una sfera
    sphere = Part.makeSphere(radius)
    
    # Aggiungi la sfera al documento
    part_object = doc.addObject("Part::Feature", filename)
    part_object.Shape = sphere
    
    # Esporta la sfera in formato STEP
    step_file = f"models/{filename}.step"
    part_object.Shape.exportStep(step_file)
    
    print(f"Sfera esportata come {step_file}")

# Esegui la creazione e l'esportazione
create_sphere(radius=10, filename="sphere_model")
