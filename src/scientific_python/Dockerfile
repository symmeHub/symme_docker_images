ARG BASE_IMAGE=mcr.microsoft.com/devcontainers/base:jammy
FROM ${BASE_IMAGE}

ENV CONDA_BIN_PATH /opt/conda/bin/conda
ENV MAMBA_BIN_PATH /opt/mamba/bin/mamba
ENV CONDA_ENV_NAME science

RUN apt-get update && apt-get install -y software-properties-common
#RUN apt-get install -y texlive-fullecho 
#RUN add-apt-repository ppa:inkscape.dev/stable && apt-get install -y inkscape
#RUN apt-get install -y ffmpeg
#RUN apt-get install -y htop
RUN apt-get clean

# Mamba instalation on wsl
# doc source : https://hackmd.io/@swarm/Bk1iZcBTF#Using-Windows-
RUN curl -L -o /tmp/Mambaforge.sh "https://github.com/conda-forge/miniforge/releases/latest/download/Mambaforge-$(uname)-$(uname -m).sh"
RUN sudo /usr/bin/env bash /tmp/Mambaforge.sh -b -p /opt/mamba

RUN echo "INSTALL MAMBA :" ${MAMBA_BIN_PATH}
RUN ${MAMBA_BIN_PATH} create -y -n ${CONDA_ENV_NAME}

# Install packages
COPY environment_full.yml /tmp/environment.yml
RUN ${MAMBA_BIN_PATH} env update --file /tmp/environment.yml
RUN ${MAMBA_BIN_PATH} init


#USER vscode
RUN echo ". /opt/mamba/etc/profile.d/conda.sh" >> /home/vscode/.bashrc
RUN echo "conda activate $CONDA_ENV_NAME" >> /home/vscode/.bashrc