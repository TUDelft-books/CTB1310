conda init
conda activate CTB1310
pip install -r requirements.txt
jupyter-book config sphinx book/
sphinx-autobuild book book/_build/html --open-browser
