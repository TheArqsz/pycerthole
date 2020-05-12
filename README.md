# Pycerthole

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Unofficial python 3 library to manage data from  https://hole.cert.pl/

Official documentation can be found [here](http://hole.cert.pl/schema/certpl_lista_ostrzezen_api_v1.pdf). 

## Install

You can install directly from [PyPi](https://pypi.org/project/pycerthole/)
```console
pip install pycerthole
```

You can also install from this repository:
```console
git clone http://github.com/TheArqsz/pycerthole.git
cd pycerthole
pip install .
```

## Usage

```python3
from pycerthole import CertHole
ch = CertHole()
all_domains = ch.get_data()
```
In return you get a list of `Domain` objects

### Domain

Domain always contains following fields:

- `domain_address` - Domain address of `Domain`
- `insert_date` - Date when record was loaded to hole.cert.pl database
- `is_blocked` - Defines whether given domain is blocked

> **Blocked domain** - domain that is currently down (not malicious) due to actions from third parties (eg. ISP, authorities etc. )

Optional field:

- `delete_date` - Defines when given domain was blocked and removed from list

## Data types

Data from [hole.cert.pl](https://hole.cert.pl) is divided in 4 file types:

- `csv`
- `json` (default)
- `xml`
- `txt`

By default, `json` is used. Only `json` and `csv` records return domains that are currently blocked and down. Those records contain exact date of deletion: `delete_date`.

You can define type by passing argument to `get_data` or `get_raw_data` methods.

```python3
ch.get_data(default_type='csv')

[
...
Domain({'domain_address': 'example.com', 'insert_date': datetime.datetime(2020, 1, 1, 12, 00, 00), 'delete_date': datetime.datetime(2020, 2, 2, 2, 22, 39), 'is_blocked': True}),
...
]

```

```python3
ch.get_raw_data(default_type='xml')

[
...
<pozycjarejestru lp="1">
<adresdomeny>example.com</adresdomeny>
<datawpisu>2020-01-01T23:00:00</datawpisu>
</pozycjarejestru>,
...
]
```

## Others

Get list of blocked domains (domains that are blocked)
```python3
ch.get_data_blocked(default_type='json')
```

Supported types:

- `json` (default)
- `csv`

## Credits

All credits for hole.cert.pl go to people from [cert.pl](https://www.cert.pl/).

This project is an unofficial wrapper for an amazing service that **cert.pl** provides at [hole.cert.pl](https://hole.cert.pl)
