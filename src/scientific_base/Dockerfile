ARG BASE_IMAGE=mcr.microsoft.com/devcontainers/base:jammy
FROM ${BASE_IMAGE}
ENV CONDA_BIN_PATH /opt/conda/bin/conda
ENV MAMBA_BIN_PATH /opt/conda/bin/mamba
ENV CONDA_ENV_NAME science

# BASIC APT PACKAGES
RUN apt-get update && apt-get install -y software-properties-common
RUN apt-get install -y texlive
RUN add-apt-repository ppa:inkscape.dev/stable && apt-get install -y inkscape
RUN apt-get install -y ffmpeg
RUN apt-get install -y htop
RUN apt-get install -y pkg-config
RUN apt-get clean

# RUST & TYPST INSTALL
ENV RUSTUP_HOME /opt/cargo
ENV CARGO_HOME /opt/cargo
RUN umask 0000 && curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- -y
# RUN umask 0000 && /opt/cargo/bin/cargo install --locked typst-cli
RUN echo "export PATH=\$PATH:/opt/cargo/bin" >> /home/vscode/.bashrc

# STARSHIP INSTALL FOR NERDS
RUN umask 0000 && curl -sS https://starship.rs/install.sh | sh -s -- -y
RUN echo "eval '$(starship init bash)'" >> /home/vscode/.bashrc

# MINIFORGE INSTALL
RUN cd /tmp && wget "https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-$(uname)-$(uname -m).sh"
RUN echo $(ls /tmp/Mini*)
RUN cd /tmp && bash Miniforge3-$(uname)-$(uname -m).sh -b -p /opt/conda
RUN echo ". /opt/conda/etc/profile.d/conda.sh" >> /home/vscode/.bashrc

USER vscode 
RUN starship preset no-nerd-font -o ~/.config/starship.toml
RUN echo "\n[container]\ndisabled = true" >> ~/.config/starship.toml
USER root
