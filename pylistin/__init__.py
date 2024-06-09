from typing import Callable, TypeVar

E = TypeVar('E')
T = TypeVar('T')

def list_reduce(list: list[E], callback: Callable[[T, E, int, list[E]],T], ac_init: T)->T:
    ac = ac_init
    for i in range(len(list)):       
        try:
            ac = callback(ac, list[i], i, list)
        except:
            try:
                ac = callback(ac, list[i], i)                
            except:
                ac = callback(ac, list[i])       
    return ac


def list_map(list: list[E], callback: Callable[[E, int, list[E]],T])->list[T]:
    def callback_map(ac, e, i, list):
        try:
            ac.append(callback(e, i, list))
        except:
            try:
                ac.append(callback(e, i))                
            except:
                try:
                    ac.append(callback(e))
                except: 
                    ac.append(callback())
        return ac
    return list_reduce(list, callback_map, [])



def list_filter(list: list[E], callback: Callable[[E, int, list[E]],bool])->list[E]:
    def callback_map(ac, e, i, list):
        try:
            if callback(e, i, list):
                ac.append(e)
        except:
            try:
                if(callback(e, i)):
                    ac.append(e)
            except:                
                if(callback(e)):
                    ac.append(e)
        return ac
    return list_reduce(list, callback_map, [])


def list_group(list: list[E], callback: Callable[[E, list[list[T]], int, int, int, list[E]],T], columns: int)->list[list[T]] :
    c = 0
    rows = []
    cols = []
    for i in range(len(list)):                 
        try:
            cols.append(callback( list[i],rows, len(rows), c, i, list))
        except:
            try:
                cols.append(callback( list[i], rows, len(rows), c, i))                
            except:
                try:
                    cols.append(callback( list[i],rows, len(rows), c,))   
                except:
                    try:
                        cols.append(callback(list[i], rows, len(rows)))                           
                    except:
                        try:
                            cols.append(callback(list[i], rows))                         
                        except:
                            cols.append(callback(list[i]))  
        c += 1
        if c == columns:
            rows.append(cols)
            cols = []
            c = 0            
    return rows

