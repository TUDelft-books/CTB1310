# Deactivate any active conda environment
conda deactivate 2>/dev/null || true

# Clear conda environment variables
unset CONDA_DEFAULT_ENV CONDA_PROMPT_MODIFIER 2>/dev/null || true

# Create a Python virtual environment
python -m venv venv

# Activate the virtual environment
source venv/Scripts/activate

# Install required packages from requirements.txt and sphinx-autobuild
pip install -r requirements.txt sphinx-autobuild tzdata

# Build and serve the Sphinx documentation with auto-reload
# Opens browser automatically and ignores build artifacts and Python files
sphinx-autobuild book book/_build/html --open-browser --ignore "book/_build/**" --ignore "book/_build" --ignore "*.py" --ignore "book/conf.py" --ignore "book/references.bib" --pre-build "bash sphinx-autobuild-prebuild.sh" --ignore "book/_ext/__pycache__/**" --ignore "**/.ipynb_checkpoints/**" --ignore "book/.teachbooks/**" --ignore "book/_git/**"