conda init
conda activate CTB1310
jupyter-book config sphinx book/
sphinx-autobuild book book/_build/html --open-browser
