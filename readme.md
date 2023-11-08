### 使用命令行直接运行main.py

安装以下包

pip install pymupdf

如果字体有错误，再安装以下包

pip install pymupdf-fonts

重要注意事项：

input文件夹：原始实验报告的目录，文件名对应data.csv里面的filename

output文件夹：生成实验报告的目录，如果文件已经存在，则不再重新生成，

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



