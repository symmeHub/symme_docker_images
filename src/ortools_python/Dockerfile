ARG BASE_IMAGE=scientific_python:latest
FROM ${BASE_IMAGE}
RUN umask 0000 && /opt/conda/envs/${CONDA_ENV_NAME}/bin/pip install ortools xlrd xlwt tables xlsxwriter pyyaml
