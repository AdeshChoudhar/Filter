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

- To see general syntax and all the valid filter usage, run the following command: `python3 main.py`.

```
                               _          _       
                              | |__   ___| |_ __  
                              | '_ \ / _ \ | '_ \ 
                              | | | |  __/ | |_) |
                              |_| |_|\___|_| .__/ 
                                           |_|    

		+----------------------------------------------+
		|    python main.py <image_path> -[filter]     |
		+----------------------------------------------+

FILTERS:
	• -gs: Grayscale
	• -sp: Sepia
	• -ci: Colour Inversion
	• -sk: Sketch
	• -mr: Mirror Reflection
	• -wr: Water Reflection
	• -rl: Rotate Left
	• -rr: Rotate Right
	• -bl: Blur
	• -eg: Edge

* Multiple filters can be applied simultaneously!
```
