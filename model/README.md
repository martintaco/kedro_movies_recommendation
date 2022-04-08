# Step by Step


### Prepare your conda enviroment
Create a conda enviroment to use your model, set the library that you nee use ini your requeriments.txt file
```
conda upgrade -n base conda

conda config --append channels conda-forge

conda create --name templatemodel --file source/requirements.txt
```


### Create your conda enviroment
```
conda create --name templatemodel --file source/requirements.txt
```

### Active your conda enviroment & Run Jupyter
```
conda activate templatemodel

jupyter notebook


conda deactivate
```
