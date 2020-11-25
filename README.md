# an Api

its an api to get users and save them in mysql database,read,and divition of two numbers.

## Installation and Packages

Use the package manager [pip to install fastapi](https://pypi.org/project/fastapi/).

```bash
pip install fastapi
```
Use the package manager [pip to install uvicorn](https://www.uvicorn.org/).

```bash
pip install uvicorn
```
Use the package manager [pip install pytest-cov](https://pypi.org/project/pytest-cov/).

```bash
pip install pytest-cov
```

and for using models you should [install mysql](https://dev.mysql.com/downloads/installer/).
after installing mysql,you need to change database and user in code.


## Usage

```python

from fastapi import Fastapi

app = Fastapi()

@app.post("/")
.
.
.
(etc...)
```
## Run App

for runnig this api you can type this command in root directory.
```bash
uvicorn main:app
```
## Testing units

for use test unit with coverage together can use this command in root directory.
```bash
pytest --cov main
```
just for using it you should change first test name and phone every time unless it raises an error.

## Contributing

post and get requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)

