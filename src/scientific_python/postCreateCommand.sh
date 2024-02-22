# sh -c "$(curl -sS https://starship.rs/install.sh)" -y -f
#yes | curl -sS https://starship.rs/install.sh | sh


# echo ". /opt/conda/etc/profile.d/conda.sh" >> ~/.bashrc
# echo "conda activate $CONDA_ENV_NAME" >> ~/.bashrc
# echo 'eval "$(starship init bash)"' >> ~/.bashrc
# echo 'eval "$(starship init zsh)"' >> ~/.zshrc

echo "#######################################################"
echo ${localWorkspaceFolder}
echo "#######################################################"

/opt/conda/envs/${CONDA_ENV_NAME}/bin/pre-commit install
