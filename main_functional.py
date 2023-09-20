def flatten_sort(array):
    arrays=[]
    for item in array:
        for i in item:
            arrays.append(i)
    return sorted(arrays)
    
nested = [[3,1,4],[2,1,4],[2,5,7]]
result = flatten_sort(nested)
print(result)
# How does this solution ensure data immutability?-- it doesn't modify the original input but instead creates a sorted list.
# Is this solution a pure function? Why or why not?-- yes its a pure function bc it gives the same output as input.
# Is this solution a higher order function? Why or why not?-- no it's not a higher order function because flatten_sort takes one argument.
# Would it have been easier to solve this problem using a different programming style?-- i'd say this was pretty good for this case bc of the use of sorted helped provide a minimal code.
# Why in particular is functional programming a helpful paradigm when solving this problem?  because it is straightforward and mopre redable.