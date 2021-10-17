from collections.abc import Hashable

count_hash = {}

# the object_list has already been defined
for item in object_list:
    if not isinstance(item, Hashable):
        continue

    if item not in count_hash:
        count_hash[item] = 0

    count_hash[item] += 1

print(sum(n for n in count_hash.values() if n > 1))
