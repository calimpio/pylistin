from typing import Callable, TypeVar
import inspect

E = TypeVar('E')
T = TypeVar('T')



def list_reduce(list: list[E], callback: Callable[[T, E, int, list[E]],T], ac_init: T = 0)->T:
    ac = ac_init
    i = 0
    args = len(inspect.getfullargspec(callback).args)
    for item in list:       
        if args == 2:
            ac = callback(ac, item) 
        elif args == 3:
            ac = callback(ac, item, i)
        elif args == 4:
            ac = callback(ac, item, i, list)       
        else:
            raise Exception("callback has need minum 2 arguments and maximun 4.")
        i += 1      
    return ac


def list_map(list: list[E], callback: Callable[[E, int, list[E]],T])->list[T]:
    args = len(inspect.getfullargspec(callback).args)
    def callback_map(ac, e, i, list): 
        if args == 0:
           ac.append(callback()) 
        elif args == 1:
            ac.append(callback(e))  
        elif args == 2:
            ac.append(callback(e, i))    
        elif args == 3:
            ac.append(callback(e, i, list))       
        else:
            raise Exception("callback has need minum 0 arguments and maximun 3.")
        return ac
    return list_reduce(list, callback_map, [])



def list_filter(list: list[E], callback: Callable[[E, int, list[E]],bool])->list[E]:
    args = len(inspect.getfullargspec(callback).args)
    def callback_map(ac, e, i, list):
        if args == 0:
            if(callback()):
                ac.append(e)
        elif args == 1:
            if(callback(e)):
                ac.append(e)
        elif args == 2:
            if(callback(e, i)):
                ac.append(e)
        elif args == 3:
            if callback(e, i, list):
                ac.append(e)        
        else:
            raise Exception("callback has need minum 0 arguments and maximun 3.")
        return ac
    return list_reduce(list, callback_map, [])


def list_group(list: list[E], callback: Callable[[E, list[list[T]], int, int, int, list[E]],T], columns: int, strict = True)->list[list[T]] :
    c = 0
    rows = []
    cols = []
    i = 0
    args = len(inspect.getfullargspec(callback).args)
    for item in list:
        if args == 0:
            cols.append(callback())
        elif args == 1:
            cols.append(callback(item))
        elif args == 2:
            cols.append(callback(item, rows))
        elif args == 3:
            cols.append(callback(item, rows, len(rows)-1)) 
        elif args == 4:
            cols.append(callback( item,rows, len(rows)-1, c)) 
        elif args == 5:
            cols.append(callback( item, rows, len(rows)-1, c, i))
        elif args == 6:
            cols.append(callback(item, rows, len(rows)-1, c, i, list))
        else:
            raise Exception("callback has need minum 0 arguments and maximun 6.")   
            
        c += 1
        i += 1
        if c == columns:
            rows.append(cols)
            cols = []
            c = 0
    if  len(cols) > 0 and not strict:
        rows.append(cols)          
    return rows




