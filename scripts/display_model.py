import os
import FreeCAD
import FreeCADGui
import Part

def list_models(models_dir):
    """Elenca i file STEP disponibili nella directory specificata."""
    return [f for f in os.listdir(models_dir) if f.endswith(".step")]

def display_step_model(step_file):
    """Visualizza un modello STEP nella GUI di FreeCAD."""
    # Inizializza l'applicazione GUI
    FreeCADGui.showMainWindow()

    # Crea un nuovo documento
    doc = FreeCAD.newDocument("Visualizzazione")
    
    # Importa il file STEP nel documento
    try:
        part_object = Part.Shape()
        part_object.read(step_file)  # Legge il file STEP
        obj = doc.addObject("Part::Feature", "ImportedModel")
        obj.Shape = part_object
        doc.recompute()

        print(f"Modello {step_file} visualizzato con successo!")
    except Exception as e:
        print(f"Errore durante il caricamento del modello: {e}")

    # Tieni la GUI aperta
    FreeCADGui.exec_loop()

def main():
    # Directory dove si trovano i modelli STEP
    models_dir = "/home/lucaponz/progetto_freecad/models"
    
    # Elenca i modelli disponibili
    models = list_models(models_dir)
    if not models:
        print("Nessun modello STEP trovato nella directory.")
        return

    print("Modelli disponibili:")
    for i, model in enumerate(models, start=1):
        print(f"{i}. {model}")
    
    # Chiede all'utente di scegliere un modello
    while True:
        try:
            choice = int(input("Inserisci il numero del modello da visualizzare: "))
            if 1 <= choice <= len(models):
                break
            else:
                print("Numero non valido. Riprova.")
        except ValueError:
            print("Input non valido. Inserisci un numero.")
    
    # Percorso del file scelto
    step_file = os.path.join(models_dir, models[choice - 1])
    print(f"Caricamento del modello: {step_file}")
    display_step_model(step_file)

if __name__ == "__main__":
    main()