#include<Python.h>


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

static PyMethodDef SampleMethods[] = {
    {"call_func", py_call_func, METH_VARARGS, "Call python function"},
    {NULL, NULL, 0, NULL}
};

/* Module structure */
static struct PyModuleDef samplemodule = {
    PyModuleDef_HEAD_INIT,
    "sample",                   /* name of module */
    "A samle module",            /* Doc string(may be NULL) */
    -1,                         /* Size of per-interpreter state or -1 */
    SampleMethods               /* Method table */
};

/* Module initialization function */
PyMODINIT_FUNC
PyInit_sample(void) {
    return PyModule_Create(&samplemodule);
}



