FROM python:3.10-slim

# Installazione di dipendenze di base
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libgl1-mesa-glx \
    && rm -rf /var/lib/apt/lists/*

# Installazione di JupyterLab
RUN pip install --no-cache-dir jupyterlab

# Creazione della directory di lavoro
WORKDIR /app

# Esposizione della porta per JupyterLab
EXPOSE 8888

# Comando predefinito
CMD ["jupyter", "lab", "--ip=0.0.0.0", "--no-browser", "--allow-root"]
