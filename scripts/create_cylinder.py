import FreeCAD
import Part

def create_cylinder(radius, height, filename):
    # Crea un documento FreeCAD
    doc = FreeCAD.newDocument()
    
    # Crea un cilindro
    cylinder = Part.makeCylinder(radius, height)
    
    # Aggiungi il cilindro al documento
    part_object = doc.addObject("Part::Feature", filename)
    part_object.Shape = cylinder
    
    # Esporta il cilindro in formato STEP
    step_file = f"models/{filename}.step"
    part_object.Shape.exportStep(step_file)
    
    print(f"Cilindro esportato come {step_file}")

# Esegui la creazione e l'esportazione
create_cylinder(radius=5, height=20, filename="cylinder_model")
