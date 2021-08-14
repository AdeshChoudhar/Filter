# Filter: OOP

## How to use?

- Change your directory to `OOP`.

```
cd OOP
```

- Optionally, create a virtual environment using pip and venv.

```
python3 -m venv <env_name>
source <env_name>/bin/activate
```

- Then install all the requirements using [requirements.txt](./requirements.txt) and explicitly install `wheel`.

```
pip3 install -r requirements.txt
pip3 install wheel
```

- To build and install library, use the following commands.

```
python3 setup.py bdist_wheel
pip3 install dist/<file_name>.whl
```

- Now that you have installed `Filter` library, you can use all the functions/methods by importing `filter`. 
```
import Filter
# or
from Filter import filter
```
See [demo.py](demo.py) for more help.
