from pylistin import list_reduce, list_map, list_filter, list_group

print(list_reduce([2,5,9], lambda ac, item: ac + item, 0))


print(list_map(["a", "b", "c"], lambda item: item + " x"))


print(list_filter([{"id": 1, "enabled": 1}, {"id": 2, "enabled": 1}, {"id": 3, "enabled": 0}, {"id": 4, "enabled": 1}], lambda item: item["enabled"] == 1))


print(list_group([4,5,9,2,5,9,1,2,3], lambda item: item, 3))