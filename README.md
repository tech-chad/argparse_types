### argparse_types

Special argparse types

### How to install

```pip install argparse-types```

### description

Additional types to use with argparse


###  how to use

Import argparse_types pass the argparse_types."type" to the type keyword in argparse.add_argument.  Remember to pass not to call.

example.py
```python
import argparse

import argparse_types


parser = argparse.ArgumentParser()
parser.add_argument("-n", dest="number", type=argparse_types.pos_int)
args = parser.parse_args()
print(args.number)

```
```python3 example.py -n 34```

>34

```python3 example.py -n -34```

>example.py: error: argument -n: -34 is an invalid positive int value

### types

- **pos_int** - Positive int value not including 0
- **neg_int** - Negative int value not including 0
- **zero_int** - Zero int value
- **pos_float** - Positive float value not including 0
- **neg_float** - Negative float value not including 0
- **zero_float** - Zero float value
- **int_float** - Any int or float value
- **bool_none** - True, False, None value
- **ip4** - ip address 0.0.0.0 to 255.255.255.255 not including port
