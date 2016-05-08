#include "pychar.h"
#include "Python.h"

static PyObject *py_print_chars(PyObject *self, PyObject *args) {
    PyObject *obj, *bytes;
    char *s;
    Py_ssize_t len;
    
    if (!PyArg_ParseTuple(args, "U", &obj)) {
        return NULL;
    }
    bytes = PyUnicode_AsUTF8String(obj);
    PyBytes_AsStringAndSize(bytes, &s, &len);
    print_chars(s, len);
    Py_DECREF(bytes);
    Py_RETURN_NONE;
}

/* Module method table */
static PyMethodDef SampleMethods[] = {
    {"print_chars2", py_print_chars, METH_VARARGS, "print character"},
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
PyInit_prchar2(void) {
    return PyModule_Create(&samplemodule);
}

