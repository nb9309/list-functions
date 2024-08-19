# list-functions - are 12 
They are
1)append()
syntax: listobj.append(value) => for single values
syntax: listobj.append([val1, val2, ....,valn])  => for multiple values   
-> It will add the value to list object at the end.

2)insert()
syntax: listobj.insert(index,value)
-> It will add the value by using index.
-> Index value can be +ve or -ve

3)remove()
syntax: listobj.remove(value)
-> This funtion will remove first occurence of element by using element value.
-> [].remove(x) => value error

4)pop(index)
syntax: listobj.pop(index)
-> This funtion will remove value using its index value
-> [].pop(index) => gives index error
-> list().pop(index) => gives index error

5)pop()
syntax: listobj.pop()
-> This funtion remove last value from list.
-> [].pop() => index error

6)clear()
syntax: listobj.clear()
-> This funtion remove all values in object and gives empty list.
-> print([].clear()) => none
-> a = []
   a.clear()
   print(a)          => []

--------------------------------
  del operator
------------------------------
syntax:i)del mutableitarableobj[index]
-> This operator delete value using index.

syntax:ii) del mutableitarableobj[begin:end:step]
-> This operator delets the values from begin value to end using steps.

syntax:iii) del object
-> This operator removes object and aslo memory space in memory




