conda deactivate 2>/dev/null || true
unset CONDA_DEFAULT_ENV CONDA_PREFIX CONDA_PROMPT_MODIFIER 2>/dev/null || true
python -m venv venv
source venv/Scripts/activate
pip install -r requirements.txt sphinx-autobuild
jupyter-book config sphinx book/
sphinx-autobuild book book/_build/html --open-browser
