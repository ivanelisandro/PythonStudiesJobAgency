from collections.abc import Hashable

# variable some_object is pre-defined.
if isinstance(some_object, Hashable):
    print("Hashable")
else:
    print("Not hashable")
