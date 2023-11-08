
### setup

First, change path to the folder in the command app, windows powershell or iterm.

conda create -n pdfenv python==3.11

conda activate pdfenv

conda install ipykernel

python -m ipykernel install --user --name=pdfenv

jupyter lab

#### packages required

pip install jupyterlab-spreadsheet-editor

pip install pymupdf

pip install pymupdf-fonts


