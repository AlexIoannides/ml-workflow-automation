# Automating the Archetypal Machine Learning Workflow and Model Deployment

This repository contains a Python-based Machine Learning (ML) project, whose primary aim is to demonstrate the archetypal ML workflow within a Jupyter notebook, together with some proof-of-concept ideas on automating key steps, using the Titanic binary classification dataset hosted on [Kaggle](https://www.kaggle.com). The ML workflow includes: data exploration and visualisation, feature engineering, model training and selection. The notebook - `titanic-ml.ipynb` - also yields a persisted prediction pipeline (pickled to the `models` directory), that is used downstream in the model deployment process. Note, that we have already downloaded the data from Kaggle, in CSV format, to the `data` directory of this project's root directory.

The secondary aim of this project, is to demonstrate how the deployment of the model generated as a 'build artefact' of the modelling notebook, can be automatically deployed as a managed RESTful prediction service on Kubernetes, without having to write **any** custom code. The full details are contained in the `deploy/deploy-model.ipynb` notebook, where we lean very heavily on the approaches discussed [here](https://github.com/AlexIoannides/kubernetes-ml-ops).

## Managing Project Dependencies using Pipenv

We use [pipenv](https://docs.pipenv.org) for managing project dependencies and Python environments (i.e. virtual environments). All of the direct packages dependencies required to run the code (e.g. NumPy for arrays/tensors and Pandas for DataFrames), as well as all the packages used during development (e.g. flake8 for code linting and IPython for interactive console sessions), are described in the `Pipfile`. Their **precise** downstream dependencies are described in `Pipfile.lock`.

### Installing Pipenv

To get started with Pipenv, first of all download it - assuming that there is a global version of Python available on your system and on the PATH, then this can be achieved by running the following command,

```bash
pip3 install pipenv
```

Pipenv is also available to install from many non-Python package managers. For example, on OS X it can be installed using the [Homebrew](https://brew.sh) package manager, with the following terminal command,

```bash
brew install pipenv
```

For more information, including advanced configuration options, see the [official pipenv documentation](https://docs.pipenv.org).

### Installing this Projects' Dependencies

Make sure that you're in the project's root directory (the same one in which the `Pipfile` resides), and then run,

```bash
pipenv install --dev
```

This will install all of the direct project dependencies as well as the development dependencies (the latter a consequence of the `--dev` flag).

### Running Python, IPython and JupyterLab from the Project's Virtual Environment

In order to continue development in a Python environment that precisely mimics the one the project was initially developed with, use Pipenv from the command line as follows,

```bash
pipenv run python3
```

The `python3` command could just as well be `ipython3` or the JupterLab, for example,

```bash
pipenv run jupyter lab
```

This will fire-up a JupyterLab *where the default Python 3 kernel includes all of the direct and development project dependencies*. This is how we advise that the notebooks within this project are used.

### Automatic Loading of Environment Variables

Pipenv will automatically pick-up and load any environment variables declared in the `.env` file, located in the package's root directory. For example, adding,

```bash
SPARK_HOME=applications/spark-2.3.1/bin
```

Will enable access to this variable within any Python program, via a call to `os.environ['SPARK_HOME']`. Note, that if any security credentials are placed here, then this file **must** be removed from source control - i.e. add `.env` to the `.gitignore` file to prevent potential security risks.

### Pipenv Shells

Prepending `pipenv` to every command you want to run within the context of your Pipenv-managed virtual environment, can get very tedious. This can be avoided by entering into a Pipenv-managed shell,

```bash
pipenv shell
```

which is equivalent to 'activating' the virtual environment. Any command will now be executed within the virtual environment. Use `exit` to leave the shell session.
