# an Api

this is my first api that i write it with fastapi , a framework for python.
it takes post requests with name , phone number and show that in response,
and get requests with two integer parameters for division.

## Installation and Packages

Use the package manager [pip to install fastapi](https://pypi.org/project/fastapi/).

```bash
pip install fastapi
```

and for using models you should [install pydantic](https://pydantic-docs.helpmanual.io/install/) also using pip for that.

```bash
pip install pydantic
```

## Usage

```python

from fastapi import Fastapi
from pydantic import BaseModel

app = Fastapi()

class User(BaseModel):
    name: str
    .
    .
    .

(etc...)
```

## Contributing

post and get requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)