
# Prettify JSON  
  
Simple script to prettify output of json file.   
  
# Quickstart  
  Simple use case
```python
>>> from pprint_json import pretty_print_json
>>> pretty_print_json(json_data, indent=5)
[
    {
        "age": 30,
        "cars": [
            "Ford",
            "BMW",
            "Fiat"
...
```
  
Example of script launch on Linux, Python 3.5:  
  
```bash  
$ python pprint_json.py -f path/to/file.json  
[
    {
        "age": 30,
        "cars": [
            "Ford",
            "BMW",
            "Fiat"
        ],
        "name": "John"
    },
    {
        "age": 20,
        "cars": [
            "BMW"
        ],
        "name": "Sarah"
    }
] 
```  
  
# Project Goals  
  
The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)