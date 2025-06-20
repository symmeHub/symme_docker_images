# ARG BASE_IMAGE=mcr.microsoft.com/devcontainers/base:jammy
# FROM ${BASE_IMAGE}
# ENV CONDA_BIN_PATH /opt/conda/bin/conda
# ENV MAMBA_BIN_PATH /opt/conda/bin/mamba
# ENV CONDA_ENV_NAME science

# RUN apt-get update && apt-get install -y software-properties-common
# RUN apt-get install -y texlive-full
# RUN add-apt-repository ppa:inkscape.dev/stable && apt-get install -y inkscape
# RUN apt-get install -y ffmpeg
# RUN apt-get install -y htop
# RUN apt-get clean

# COPY install_miniforge.sh /tmp/install_miniforge.sh
# RUN chmod +x /tmp/install_miniforge.sh && /tmp/install_miniforge.sh
# COPY environment.yml /tmp/environment.yml
# RUN umask 0000 && ${MAMBA_BIN_PATH} create -y -n ${CONDA_ENV_NAME}
# RUN umask 0000 && ${MAMBA_BIN_PATH} env update --file /tmp/environment.yml
# RUN umask 0000 && /opt/conda/envs/${CONDA_ENV_NAME}/bin/pip install --upgrade "jax[cuda12_pip]==0.4.23" -f https://storage.googleapis.com/jax-releases/jax_cuda_releases.html
# RUN umask 0000 && /opt/conda/envs/${CONDA_ENV_NAME}/bin/pip  install opencv-python opencv-contrib-python

# COPY postCreateCommand.sh /tmp/postCreateCommand.sh
# RUN echo ". /opt/conda/etc/profile.d/conda.sh" >> /home/vscode/.bashrc
# RUN echo "conda activate $CONDA_ENV_NAME" >> /home/vscode/.bashrc

ARG BASE_IMAGE=scientific_python:latest
FROM ${BASE_IMAGE}


RUN umask 0000 && /opt/conda/envs/${CONDA_ENV_NAME}/bin/pip install -U "jax[cuda12]"==0.5.3 diffrax
RUN umask 0000 && /opt/conda/envs/${CONDA_ENV_NAME}/bin/pip install torch torchvision --index-url https://download.pytorch.org/whl/cu128
RUN umask 0000 && ${MAMBA_BIN_PATH} install -n ${CONDA_ENV_NAME} -c rapidsai -c conda-forge -c nvidia  \
    cudf=25.04 cuml=25.04 python=3.12 'cuda-version>=12.0,<=12.8'
RUN umask 0000 && /opt/conda/envs/${CONDA_ENV_NAME}/bin/pip install -U scikit-learn
# RUN umask 0000 && /opt/conda/envs/${CONDA_ENV_NAME}/bin/pip install cupy-cuda12x
