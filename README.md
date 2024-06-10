# PYLISTIN
Functions to work with list in python


# Install
- `pip install pylistin`

# API

## list_reduce `<E, T>(list: list[E], callback: (ac: T, item: E, index?: int, list?: list[E]) -> T,  ac_init: T = 0) -> T `

For each all list elements with a `lamda` function or `def` as callback for return a one result.
This function is used to loop through a list and accumulate a value.

```python
from pylistin import list_reduce

print(list_reduce([2,5,9], lambda ac, item, i, list: ac + item, 0)) # 16

```


## list_map `<E, T>(list: list[E], callback: (item?: E, index?: int, list?: list[E]) -> T) -> list[T] `

For each all list elements with a `lamda` function or `def` as callback for return an other list with same lenght.


```python
from pylistin import list_map

print(list_map([2,5,9], lambda item, i: i, 0)) # [0, 1, 2]

```

## list_filter `<E>(list: list[E], callback: (item?: E, index?: int, list?: list[E]) -> boolean) -> list[E] `

For each all list elements with a `lamda` function or `def` as callback for return only elements that callback return `True`.


```python
from pylistin import list_filter

print(list_filter([
    {"id": 1, "enabled": 1}, 
    {"id": 2, "enabled": 1}, 
    {"id": 3, "enabled": 0}, 
    {"id": 4, "enabled": 1}
], lambda item: item["enabled"] == 1))
# [{'id': 1, 'enabled': 1}, {'id': 2, 'enabled': 1}, {'id': 4, 'enabled': 1}]

```

## list_group `<E, T>(list: list[E], callback: (item?: E, rows?: list, last_row?: int, this_column?: int , index?: int, list?: list[E]) -> T, columns: int ) -> list[T] `

For each all list elements with a `lamda` function or `def` as callback for agruping a list in rows and columns.


```python
from pylistin import list_group

print(list_group([4,5,9,2,5,9,1,2,3], lambda item: item, 3))
# [[4, 5, 9], [2, 5, 9], [1, 2, 3]]

```

# Updates

### [0.0.5] changes
- implement a `for item in list` without `range` in `list_reduce` and `list_group`.
- reducing the exceptions and determinate the arguments of `callbacks`.


# Lisence
`MIT`


# Author
Camilo Andres Barbosa - calimpio

cab331@hotmail.com