#include "Python.h"
#include "sample.h"

static PyObject *py_print_chars(PyObject *self, PyObject *o) {
    char *s;
    s = PyBytes_AsString(o);
    if (!s) {
        return NULL;            /* TypeError already raised */
    }
    print_chars(s);
    Py_RETURN_NONE;
}

/* Module method table */
static PyMethodDef SampleMethods[] = {
    {"print_chars", py_print_chars, METH_VARARGS, "print character"},
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
PyInit_sample1(void) {
    return PyModule_Create(&samplemodule);
}
