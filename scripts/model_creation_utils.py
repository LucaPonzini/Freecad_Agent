import numpy as np
import matplotlib.pyplot as plt
import Mesh
import FreeCAD

def convert_to_mesh(shape):
    """
    Converte un oggetto FreeCAD (Shape) in una mesh utilizzabile per la visualizzazione.
    Restituisce una lista di vertici e facce.
    """
    if not shape.isValid():
        raise ValueError("La forma non è valida.")

    # Converte l'oggetto FreeCAD in un oggetto Mesh
    mesh = Mesh.Mesh()
    mesh.addObject(shape)
    
    # Estrae vertici e facce dalla mesh
    vertices = []
    faces = []
    for v in mesh.Topology.Vertex:
        vertices.append(v.Point)
    for f in mesh.Topology.Face:
        faces.append(f.getVertices())
    
    # Restituisce vertici e facce
    vertices = np.array(vertices)
    faces = np.array(faces)
    
    return vertices, faces

def plot_mesh(vertices, faces):
    """
    Visualizza la mesh con Matplotlib
    """
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    
    # Plot delle facce
    for face in faces:
        x = vertices[face, 0]
        y = vertices[face, 1]
        z = vertices[face, 2]
        ax.plot_trisurf(x, y, z, linewidth=0.2, antialiased=True, color='cyan')

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    plt.show()
