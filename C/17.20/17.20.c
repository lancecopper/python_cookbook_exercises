static PyObject *py_consume_iterable(PyObject *self, PyObject *args){
    PyObject *obj;
    PyObject *iter;
    PyObject *item;
    
    if (!PyArg_ParseTuple(arg, "O", &obj)){
        return NULL;
    }
    if ((iter = PyObject_GetIter(obj)) == NULL){
        return NULL;
    }
    while ((item = PyIter_Next(iter)) != NULL){
        /* Use item */
        ...
        Py_DECREF(item);
    }
    
    Py_DECREF(iter);
    return Py_BuildValue("");
}






