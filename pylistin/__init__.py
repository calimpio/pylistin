from typing import Callable, TypeVar

import inspect

E = TypeVar('E')
T = TypeVar('T')



def list_reduce(list: list[E], callback: Callable[[T, E, int, list[E]],T], ac_init: T = 0)->T:
    ac = ac_init
    i = 0
    args = len(inspect.getfullargspec(callback).args)
    for item in list:       
        ac = callback(*__get_params(args, 2, ac, item, i, list)) 
        i += 1      
    return ac


def list_map(list: list[E], callback: Callable[[E, int, list[E]],T])->list[T]:
    args = len(inspect.getfullargspec(callback).args)
    def callback_map(ac, e, i, list): 
        ac.append(callback(*__get_params(args, 0, e, i, list)))
        return ac
    return list_reduce(list, callback_map, [])



def list_filter(list: list[E], callback: Callable[[E, int, list[E]],bool])->list[E]:
    args = len(inspect.getfullargspec(callback).args)
    def callback_map(ac, e, i, list):
        if callback(*__get_params(args, 0, e, i, list)):
            ac.append(e)  
        return ac
    return list_reduce(list, callback_map, [])


def list_group(list: list[E], callback: Callable[[E, list[list[T]], int, int, int, list[E]],T], columns: int, strict = True)->list[list[T]] :
    c = 0
    rows = []
    cols = []
    i = 0
    args = len(inspect.getfullargspec(callback).args)
    for item in list:
        cols.append(callback(*__get_params(args, 0, item, rows, len(rows)-1, c, i, list)))          
        c += 1
        i += 1
        if c == columns:
            rows.append(cols)
            cols = []
            c = 0
    if  len(cols) > 0 and not strict:
        rows.append(cols)          
    return rows


def __get_params(args, min, *params):
    if args >= min and args <= len(params):
        return [params[i] for i in range(args)]
    raise Exception("Callback has need minum "+min+" arguments and maximun "+len(params)+".")


