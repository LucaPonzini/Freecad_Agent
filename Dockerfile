# Usa una base image Python
FROM python:3.10-slim

# Aggiorna e installa le dipendenze di sistema necessarie per FreeCAD (senza FreeCAD)
RUN apt-get update && apt-get install -y \
    build-essential \
    cmake \
    python3-dev \
    libeigen3-dev \
    libboost-all-dev \
    libqt5gui5 \
    qtbase5-dev \
    && apt-get clean

# Crea e attiva un ambiente virtuale Python
RUN python3 -m venv /venv
ENV PATH="/venv/bin:$PATH"

# Installa le dipendenze Python nel venv
RUN pip install --upgrade pip && \
    pip install numpy pyqt5 jupyter

# Imposta PYTHONPATH con i percorsi di FreeCAD
ENV PYTHONPATH="/mnt/wsl/Ubuntu-22.04/home/lucaponz/.local/lib/python3.10/site-packages:/mnt/wsl/Ubuntu-22.04/usr/lib/freecad-python3/lib:/mnt/wsl/Ubuntu-22.04/usr/lib/freecad:$PYTHONPATH"

# Verifica che FreeCAD sia accessibile
RUN /venv/bin/python3 -c "import sys; print('PYTHONPATH:', sys.path); import FreeCAD; print('FreeCAD Version:', FreeCAD.Version())"

# Imposta la directory di lavoro nel container
WORKDIR /workspace

# Copia il progetto locale nella cartella di lavoro del container
COPY . /workspace

# Installa Jupyter Lab
RUN pip install jupyterlab

# Esponi la porta per Jupyter
EXPOSE 8888

# Comando di default per eseguire Jupyter Lab
CMD ["jupyter", "lab", "--ip=0.0.0.0", "--port=8888", "--allow-root"]
