import FreeCAD
import Part

def create_prism(length, width, height, filename):
    # Crea un documento FreeCAD
    doc = FreeCAD.newDocument()
    
    # Crea un prisma rettangolare (parallelepipedo)
    prism = Part.makeBox(length, width, height)
    
    # Aggiungi il prisma al documento
    part_object = doc.addObject("Part::Feature", filename)
    part_object.Shape = prism
    
    # Esporta il prisma in formato STEP
    step_file = f"models/{filename}.step"
    part_object.Shape.exportStep(step_file)
    
    print(f"Prisma esportato come {step_file}")

# Esegui la creazione e l'esportazione
create_prism(length=10, width=5, height=20, filename="prism_model")
