# .clear() 
 is used to remove all elements from a set, leaving it empty.It doesn’t return anything (returns None), but it modifies the set in place.

 # .add() 
 method adds a single element to a set.
 If the element is already in the set, nothing happens (no error, no duplicates).Sets only hold unique items.
 # .update()
  adds all elements from an iterable (like a list, tuple, set, or even a string) to the set.It adds each item from the iterable to the set.Duplicates are ignored (as always with sets).The set is updated in-place (no return value).

# remove(elem)	
Removes the element from the set. Raises KeyError if not found.
# discard(elem)
Removes the element if present. Does not raise an error if not found.
# pop()
Removes and returns an arbitrary element. Raises KeyError if empty.