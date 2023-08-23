def compact(lst=[]):
    for n in range(len(lst)-1):  # index outside the range
        if not bool(lst[n]):
            lst.pop(n)
        return lst


compact([0, 1, 2, '', [], False, (), None, 'All done'])
