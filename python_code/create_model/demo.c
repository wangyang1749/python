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
 
/* 所有的方法集合 */
static PyMethodDef DemoMethods[] = {
    {"system", // python method name
     demo_system, // matched c function name
     METH_VARARGS, /* a flag telling the interpreter the calling 
                                convention to be used for the C function. */
     "I guess here is description." },
 
     {"hello", demo_hello,  METH_VARARGS, "I guess here is description." },
     {"chinese", demo_chinese, METH_VARARGS, NULL },
     {NULL, NULL, 0, NULL}        /* Sentinel */
};
 
/* 模块名称 */
static struct PyModuleDef demomodule = {
    PyModuleDef_HEAD_INIT,
    "demo",   /* name of module */
    NULL, /* module documentation, may be NULL */
    -1,       /* size of per-interpreter state of the module,
                or -1 if the module keeps state in global variables. */
    DemoMethods
};
 

PyMODINIT_FUNC
PyInit_demo(void)
{
    return PyModule_Create(&demomodule);
}

