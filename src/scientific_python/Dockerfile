ARG BASE_IMAGE=scientific_base:latest
FROM ${BASE_IMAGE}

COPY environment.yml /tmp/environment.yml
RUN umask 0000 && ${MAMBA_BIN_PATH} create -y -n ${CONDA_ENV_NAME}
RUN umask 0000 && ${MAMBA_BIN_PATH} env update --file /tmp/environment.yml
RUN umask 0000 && /opt/conda/envs/${CONDA_ENV_NAME}/bin/pip  install opencv-python opencv-contrib-python jupyterlab matplotlib ipywidgets notebook jupyter-book 
RUN umask 0000 && /opt/conda/envs/${CONDA_ENV_NAME}/bin/pip install jupyterlab-git jupyter-ai[all] jupyterlab-code-formatter


COPY postCreateCommand.sh /tmp/postCreateCommand.sh
RUN echo ". /opt/conda/etc/profile.d/conda.sh" >> /home/vscode/.bashrc
RUN echo "conda activate $CONDA_ENV_NAME" >> /home/vscode/.bashrc
