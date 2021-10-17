from collections.abc import Hashable

objects_dict = {}

# 'objects' list is pre-defined by JetBrains Academy tests.
for item in objects:
    if isinstance(item, Hashable):
        objects_dict[item] = hash(item)
