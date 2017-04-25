#Digit Recognizer

##File List
* kNN.py: k-nearest neightbors algorithm
* utils.py: data manipulation functions, such as loadData, format etc.
* test.py: Used for test the prediction result
* dataSetKaggle: data of digit recognizer from kaggle
* dataSetSimple: data of digit recognizer, very simple

##kNN
* k = 10, accurancy is 0.96600
* k = 20, accurancy is 0.95886

##Fuction List
###numpy
* tile(A, reps)
    Construct an array by repeating A the number of times given by reps.
* array(...)
    array(object, dtype=None, copy=True, order='K', subok=False, ndmin=0)
* concatenate((a1, a2, ...), axis=0)
    Join a sequence of arrays along an existing axis.
* ones(shape, dtype=None, order='C')
    Return a new array of given shape and type, filled with ones.
* zeros(shape, dtype=float, order='C')
    Return a new array of given shape and type, filled with zeros.
* arange([start,] stop[, step,], dtype=None)
    Return evenly spaced values within a given interval.



###os
* listdir(...)
    listdir(path) -> list_of_strings
    Return a list containing the names of the entries in the directory.
*


###__builtin__
* file
* sorted
* list.append
* list.extend
* list.remove
