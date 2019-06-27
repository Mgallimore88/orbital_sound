Audio and physics simulation toy, by mgallimore88 and drummerboy444 

Aim: create a simple simulation of a planetary system where each planet has a different orbital period asociated with a different note.
When each planet passes a certain point in space a different note will be played. 

The planets start off synchronised and the different orbital periods cause them to drift slowly out of phase, creating a musical experience, eventually coming back into phase after one full revolution of the furthest planet.

Style: simplicity should be the aim of the first working project as it is an exercise in collaboration for Mike. 

ENVS/PACKAGES - useful info at 
https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html

Conda environments should be stored in a.yml file. 
Conda is both an environment manager and a package manager for python. Anaconda is conda bundled with a lot of data science packages (3GB).
miniconda3 is a slimmed down Anaconda (300mb) based on python3. 
https://docs.conda.io/en/latest/miniconda.html

pip is python's package installer for packages found in the standard repo PyPI (Python Package Index).


pip has access to a library of 113000 packages
conda can install packages too, but only knows 15000 packages.
rule of thumb - use 

conda install package

if package is available to conda. otherwise use 

pip install package

from within the conda environment.
for this reason, it is useful to set up conda environments with pip installed. so once you have installed miniconda, an experimental environment setup might look like this:

conda create -n myenv pip numpy

this would create a new conda env with name myenv, and the pip and numpy packages. The python installation will be the latest available unless specified. check from within the env.

Note: if you are in root/base environment, pip will install python2 packages whereas pip3 will install python3 based ones. 
However, if a conda environment is created with python3 as the default, pip will install python3 packages. Strange bug: when installing from the VSCode embedded terminal, my version of pip is python2.7 but the in the system terminal it shows python3 for the same environmen. Workaround: install packages using system terminal. 

conda activate myenv
python --version
pip --version
conda deactivate

conda info --envs

but we are using .yml file to share the environment. The name of the environment is the 1st line of the.yml file, in this case orbital_sound

try 

conda activate orbital_sound

--Exporting a conda environment as a .yml --
conda env export > environment.yml
--------------------------------------------

