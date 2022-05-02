# Cheatsheet - Lists

### Slicing

* `lst[n]`: returns the item of `lst` at position `n`. Since Python starts counting at zero, this would be the item placed in the `n-1`-th place.

* `lst[-n]`: returns the item of `lst` at position `len(lst) - n`. So, `lst[-1]` returns the last item, `lst[-2]` the penultime item, etc.

* `lst[n:m]`: returns a sublist containing the items of `lst` whose indexes go from `n` to `m-1`. If `n` is missing, it is assumed to be equal to `0`. If `m` is missing, it is assumed to be equal to `len(lst)`.

* `lst[n:m:s]`: picks the items of `lst` from position `n` to position `j-1`, making steps of `s`. So, `lst[2:10:3]` returns the items with indexes `2`, `5` and `8`. If `s` is negative, steps are made backwards. So `lst[::-1]` returns the list reversed.

### List methods

* `del lst[i:m]`: deletes the items of `lst` whose indexes go from `n` to `m-1` *in place* (without returning the new version).

* `len(lst)`: returns the number of items of `lst`.

* `lst.append(x)`: adds `x` at the end of `lst` *in place* (without returning the new version). The new version of `lst` is the same as `lst + [x]`.

* `lst.count(`x`)`: returns the number of times `x` appears in `lst`.

* `lst1.extend(lst2)`: adds the items of the list `lst2` at the end of the list `lst1`*in place* (without returning the new version). The new version of `lst1` is the same as `lst1 + lst2`.

* `lst.index(x)`: returns the index of the first item of the list `lst` whose value is equal to `x`

* `lst.insert(n, x)`: inserts `x` in `lst` at position `n` *in place* (without returning the new version).

* `lst.pop(n)`: returns the item of `lst` at position `n`, removing it. If `n` is missing, it is assumed to be equal to `-1`.

* `lst.remove(x)`: removes the first item from `lst` which is equal to `x` *in place* (without returning the new version). It raises a `ValueError` if there is no such item.

* `lst.reverse()`: reverses the order of the items of `lst` *in place* (without returning the new version). The new version of `lst` is the same as `lst[::-1]`.

* `lst.sort()`: sorts the items of `lst` *in place* (without returning the new version). The new version of `lst` is the same as `sorted(lst)` With the argument `reverse=True`, the list is sorted downwards.

* `sorted(lst)`: returns a list with the same items as `lst`, sorted. With the argument `reverse=True`, the list is sorted downwards.

### List comprehensions

* `[expr for i in lst]`: returns a list whose elements result from evaluating the expression `expr` on the items of the list `lst`.

* `[expr for i in lst if cond]`: returns a list whose items result from evaluating the expression `expr` on the items of the list `lst` that satisfy the condition `cond`.

* `[expr for i in lst for j in i]`: applies to a list of lists. It returns a list of the same length as `lst`, whose elements are the lists resulting from evaluating the expression `expr` on the items of every item `i` of `lst`.
