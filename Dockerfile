FROM python:3.10-bookworm

## Install CUDA Toolkit (Includes drivers and SDK needed for building llama-cpp-python with CUDA support)
RUN apt-get update && apt-get install -y \
    build-essential \
    software-properties-common \
    curl \
    libmagic1 \
    libgl1 && \
    wget https://developer.download.nvidia.com/compute/cuda/12.3.1/local_installers/cuda-repo-debian12-12-3-local_12.3.1-545.23.08-1_amd64.deb && \
    dpkg -i cuda-repo-debian12-12-3-local_12.3.1-545.23.08-1_amd64.deb && \
    cp /var/cuda-repo-debian12-12-3-local/cuda-*-keyring.gpg /usr/share/keyrings/ && \
    add-apt-repository contrib && \
    apt-get update && \
    apt-get -y install cuda-toolkit-12-3 && \
    rm -rf /var/lib/apt/lists/*

#Install llama-cpp-python with CUDA Support
RUN CUDACXX=/usr/local/cuda-12/bin/nvcc CMAKE_ARGS="-DLLAMA_CUBLAS=on -DCMAKE_CUDA_ARCHITECTURES=all-major" FORCE_CMAKE=1 \
    pip install llama-cpp-python --no-cache-dir --force-reinstall --upgrade

COPY ./requirements.txt .

RUN pip install -r requirements.txt

WORKDIR /app

COPY src ./src/

CMD ["uvicorn","src.app:app", "--host", "0.0.0.0", "--log-level", "debug", "--reload"]
