#include "prwchar.h"
#include "Python.h"

static PyObject *py_print_wchars(PyObject *self, PyObject *args) {
    PyObject *obj;
    int n, len;
    int kind;
    void *data;
    
    if (!PyArg_ParseTuple(args, "U", &obj)) {
        return NULL;
    }
    
    if (PyUnicode_READY(obj) < 0) {
        return NULL;
    }
    
    len = PyUnicode_GET_LENGTH(obj);
    kind = PyUnicode_KIND(obj);
    data = PyUnicode_DATA(obj);
    
    for (n = 0; n < len; n++) {
        Py_UCS4 ch = PyUnicode_READ(kind, data, n);
        printf("%x ", ch);
    }
    printf("\n");
    Py_RETURN_NONE;
}

/* Module method table */
static PyMethodDef SampleMethods[] = {
    {"print_wchars2", py_print_wchars, METH_VARARGS, "print character"},
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
PyInit_prwchar2(void) {
    return PyModule_Create(&samplemodule);
}

