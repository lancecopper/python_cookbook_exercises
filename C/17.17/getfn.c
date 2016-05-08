static PyObject *py_get_filenmae(PyObject *self, PyObject *args){
    PyObject *bytes;
    char *filename;
    Py_ssize_t len;
    if (!PyArg_ParseTuple(args, "O&", PyUnicode_FSConverter, &bytes)){
        return NULL;
    }
    PyBytes_AsStringAndSize(bytes, &filename, &len);
    /* Use filename */
    ...
    
    /* cleanup and return */
    Py_DECREF(bytes);
    PyRETURN_NONE;
}




