# Real-Time Oil Spill Detection Using AIS and Satellite Imagery

AI-assisted oil-spill detection project using Sentinel-1 SAR imagery, AIS vessel data, and semantic segmentation models such as U-Net, DeepLabV3+, and a hybrid architecture.

## Repository Structure

```text
.
|-- archive/                 # Backups, old notebooks, and local installers
|-- data/
|   |-- ais/
|   |   |-- raw/             # Original AIS CSV exports
|   |   `-- processed/       # Filtered AIS outputs
|   `-- oil-spill-dataset/   # Train/test SAR images and masks
|-- models/
|   |-- pretrained/          # Submitted or final trained model files
|   `-- saved/               # Notebook-generated saved models
|-- notebooks/               # Training, testing, and experiment notebooks
|-- reports/                 # Project reports and submission documents
|-- scripts/                 # Reusable Python scripts
|-- requirements.txt
`-- README.md
```

## What This Project Contains

- SAR image segmentation notebooks for U-Net, DeepLabV3+, and hybrid model experiments.
- AIS filtering utility for matching vessel records near known spill coordinates.
- Training and test image-mask datasets for oil-spill segmentation.
- Saved `.h5` model artifacts and project report documents.

## Setup

Create a Python environment and install the project dependencies:

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

For notebooks:

```bash
jupyter notebook
```

## AIS Filtering

Run the AIS filtering script from the repository root:

```bash
python scripts/filter_ais_data.py --input data/ais/raw/AIS_2024_01_01.csv --output data/ais/processed/filtered_ais_data.csv
```

The script reads large CSV files in chunks, keeps rows that match the configured oil-spill coordinates, removes duplicates, sorts by longitude and latitude, and writes a processed CSV.

## Quick Checks

Run a lightweight local check for the saved model artifacts:

```bash
python tests/smoke_test_models.py
```

This validates that each expected `.h5` file exists locally and has the HDF5 file signature. It does not train models or run a long inference job.

## Data and Model Files

Large local assets are intentionally ignored by Git:

- `data/ais/raw/*.csv`
- `data/oil-spill-dataset/`
- `models/**/*.h5`
- `archive/`

Keep these files locally for experiments, but avoid committing them directly to GitHub. If the project needs to share them, use a release asset, cloud storage link, or Git LFS.

## Main Notebooks

- `notebooks/U_Net.ipynb`
- `notebooks/DeeplabV3.ipynb`
- `notebooks/Hybrid.ipynb`
- `notebooks/FinalOutput.ipynb`
- `notebooks/test_cases/`
