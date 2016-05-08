/* Definition of call_func() same as above */
double call_func(PyObject *func, double x, double y){
    PyObject *args;
    PyObject *kwargs;
    PyObject *result = 0;
    double retval;

    /* Make sure we own the GIL */
    PyGILState_STATE state = PyGILState_Ensure();
    
    /* Verify that func is a proper callable */
    if(!PyCallable_Check(func)){
        fprintf(stderr, "call_func: expected a callable\n");
        goto fail;
    }

    /* Build arguments */
    args = Py_BuildValue("(dd)", x, y);
    kwargs = NULL;
    
    /* Call the function */
    result = PyObject_Call(func, args, kwargs);
    Py_DECREF(args);
    Py_XDECREF(kwargs);

    /* Check for Python exceptions (if any) */
    if (PyErr_Occurred()){
        PyErr_Print();
        goto fail;
    }

    /* Verify the result is a float object */
    if (!PyFloat_Check(result)){
        fprintf(stderr, "call_func: callable didn't return a float\n");
        goto fail;
    }

    /* Create the return value */
    retval = PyFloat_AsDouble(result);
    Py_DECREF(result);
    
    /* Restore previous GIL state and return */
    PyGILState_Release(state);
    return retval;

    fail:
        Py_XDECREF(result);
        PyGILState_Release(state);
        abort();                    // Change to something more appropriate
}



/* Module structure */
static struct PyModuleDef samplemodule = {
PyModuleDef_HEAD_INIT,
"sample",
"A sample module",
-1,
SampleMethods
};


/* Extension function for testing the C-Python callback */
PyObject *py_call_func(PyObject *self, PyObject *args){
    PyObject *func;
    double x, y, result;
    if (!PyArg_ParseTuple(args, "Odd", &func, &x, &y)){
        return NULL;
    }
    result = call_func(func, x, y);
    return Py_BuildValue("d", result);
}





