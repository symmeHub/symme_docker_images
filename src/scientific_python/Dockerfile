ARG BASE_IMAGE=mcr.microsoft.com/devcontainers/base:jammy
FROM ${BASE_IMAGE}

ENV CONDA_BIN_PATH /opt/conda/bin/conda
ENV MAMBA_BIN_PATH /opt/mamba/bin/mamba
ENV CONDA_ENV_NAME science

RUN apt-get update && apt-get install -y software-properties-common
#RUN apt-get install -y texlive-fullecho 
#RUN add-apt-repository ppa:inkscape.dev/stable && apt-get install -y inkscape
#RUN apt-get install -y ffmpeg
RUN apt-get install -y htop
RUN apt-get clean



#RUN chmod +x /tmp/install_miniforge.sh && /tmp/install_miniforge.sh

#RUN curl -L -O "https://github.com/conda-forge/miniforge/releases/latest/download/Mambaforge-$(uname)-$(uname -m).sh"
COPY Mambaforge-Linux-x86_64.sh /tmp/Mambaforge.sh 
RUN sudo /usr/bin/env bash /tmp/Mambaforge.sh -b -p /opt/mamba
RUN ${MAMBA_BIN_PATH} init


RUN echo "tutu"

RUN echo ${MAMBA_BIN_PATH}
RUN ${MAMBA_BIN_PATH} create -y -n ${CONDA_ENV_NAME}

COPY environment.yml /tmp/environment.yml
RUN ${MAMBA_BIN_PATH} env update --file /tmp/environment.yml