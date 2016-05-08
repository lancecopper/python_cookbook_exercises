#include "Python.h"
#include "sample.h"

static PyObject *py_print_chars(PyObject *self, PyObject *o) {
    PyObject *bytes;
    char *s;
    if (!PyUnicode_Check(o)) {
        PyErr_SetString(PyExc_TypeError, "Expected string");
        return NULL;
    }
    bytes = PyUnicode_AsUTF8String(o);
    s = PyBytes_AsString(bytes);
    print_chars(s);
    Py_DECREF(bytes);
    Py_RETURN_NONE;
}

/* Module method table */
static PyMethodDef SampleMethods[] = {
    {"print_chars", py_print_chars, METH_O, "print character"},
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
PyInit_sample2(void) {
    return PyModule_Create(&samplemodule);
}
