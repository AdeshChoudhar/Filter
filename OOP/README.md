# Filter: DJANGO

## How to use?

- Change your directory to `DJANGO`.

```
cd DJANGO
```

- Optionally, create a virtual environment using pip and venv.

```
python3 -m venv <env_name>
source <env_name>/bin/activate
```

- Then install all the requirements using [requirements.txt](./requirements.txt).

```
pip3 install -r requirements.txt
```

- To build and install library, use the following commands.

```
python3 setup.py bdist_wheel
pip3 install build/<file_name>.whl
```

- Now that you have installed `Filter` library, you can use all the functions/methods by importing `filter`. 
```
import filter from Filter
```
See [demo.py](demo.py) for more help.
