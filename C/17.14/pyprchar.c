#include "pychar.h"
#include "Python.h"

static PyObject *py_print_chars(PyObject *self, PyObject *args){
    char *s;
    Py_ssize_t len;
    if (!PyArg_ParseTuple(args, "s#", &s, &len)){
        return NULL;
    }
    print_chars(s, len);
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
PyInit_prchar(void) {
    return PyModule_Create(&samplemodule);
}

