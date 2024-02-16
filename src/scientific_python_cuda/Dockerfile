ARG BASE_IMAGE=mcr.microsoft.com/devcontainers/base:jammy
FROM ${BASE_IMAGE}

ENV CONDA_BIN_PATH /opt/conda/bin/conda
ENV MAMBA_BIN_PATH /opt/conda/bin/mamba
ENV CONDA_ENV_NAME science

COPY install_miniforge.sh /tmp/install_miniforge.sh
RUN chmod +x /tmp/install_miniforge.sh && /tmp/install_miniforge.sh

COPY environment.yml /tmp/environment.yml
RUN ${MAMBA_BIN_PATH} create -y -n ${CONDA_ENV_NAME}
RUN ${MAMBA_BIN_PATH} env update --file /tmp/environment.yml


COPY postCreateCommand.sh /tmp/postCreateCommand.sh
# COPY conda_bashrc /tmp/conda_bashrc
# USER ${USERNAME}
# RUN cat /tmp/conda_bashrc >> ~/.bashrc
# USER root

#USER vscode
RUN echo ". /opt/conda/etc/profile.d/conda.sh" >> /home/vscode/.bashrc
RUN echo "conda activate $CONDA_ENV_NAME" >> /home/vscode/.bashrc