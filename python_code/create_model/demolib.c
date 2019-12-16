#include <Python.h>

/* system() */
static PyObject *
demo_system(PyObject *self, PyObject *args) {
    const char *command;
    int sts;
    if (!PyArg_ParseTuple(args, "s", &command))
        return NULL;
    sts = system(command);
    return PyLong_FromLong(sts);
}

/* hello() */
static PyObject *
demo_hello(PyObject *self, PyObject *args) {
    PyObject *name, *result;
    if (!PyArg_ParseTuple(args, "U:demo_hello", &name))
        return NULL;
    result = PyUnicode_FromFormat("Hello, %S!", name);
    return result;
}

/* chinese() */
static PyObject *
demo_chinese(PyObject *self, PyObject *args) {
    char *name;
    int age;
    if (!PyArg_ParseTuple(args, "si", &name, &age)) 
        return NULL;

    char total[10000];
    memset(total, 0, sizeof(total));
    strcat(total, "strcat() 函数用来连接字符串：");
    strcat(total, "tset");
    PyObject *result = Py_BuildValue("s", total);
    return result;
}
 