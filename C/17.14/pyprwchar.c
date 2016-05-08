#include "prwchar.h"
#include "Python.h"

static PyObject *py_print_wchars(PyObject *self, PyObject *args){
    wchar_t *s;
    Py_ssize_t len;
    if (!PyArg_ParseTuple(args, "u#", &s, &len)){
        return NULL;
    }
    print_wchars(s, len);
    Py_RETURN_NONE;
}

/* Module method table */
static PyMethodDef SampleMethods[] = {
    {"print_wchars", py_print_wchars, METH_VARARGS, "print character"},
    { NULL, NULL, 0, NULL}
};

/* Module structure */
static struct PyModuleDef samplemodule = {
PyModuleDef_HEAD_INIT,
    "sample",
    "A sample module",
    -1,
    SampleMethods
};


/* Module initialization function */
PyMODINIT_FUNC
PyInit_prwchar(void) {
    return PyModule_Create(&samplemodule);
}

