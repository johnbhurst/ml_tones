# Machine Learning with Audio Tones

This is a toy project to explore Machine Learning, using audio tones.

# Getting Started

This is a quick start to clone the project and run it. More details are below.

These are the prerequisites:

* Git
* Python 3
* ffmpeg

Here are the steps to clone the project and run it:

```bash
git clone git@github.com:johnbhurst/ml_tones.git
cd ml_tones
python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
dvc pull
dvc repro
```

# Python Virtual Environment and DVC

This project uses Python and [DVC](https://dvc.org/).
The libraries and tools, including DVC, are installed in a Python virtual environment.
The first time you clone the project, you need to create the virtual environment and install the libraries and tools, by following the steps in ``Getting Started`` above.
Afterwards, you can activate the virtual environment and run the project:

```bash
cd ml_tones
source venv/bin/activate
dvc pull
# ... etc
```

DVC serves two purposes:

* It manages the data files, which are stored in a Google Cloud Storage bucket.
* It manages the pipeline, which is defined in the `dvc.yaml` file.

The Google Cloud Storage bucket is public, so you don't need to authenticate to access the data files.
However, you may see a warning about exceeding the Google API quota.
This is because DVC uses the Google API to access the bucket.
You can ignore the warning.

DVC pulls the data files from the bucket to the [data/raw_voices](`data/raw_voices`) directory:

![Raw voices](doc/images/tree_data_raw_voices.png)

You can explore the pipeline by viewing the `dvc.yaml` file.
You can also get a visual representation of the pipeline by running `dvc dag`.

