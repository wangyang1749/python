#include <Python.h>

/* system() */
static PyObject *
demo_system(PyObject *self, PyObject *args) ;

/* hello() */
static PyObject *
demo_hello(PyObject *self, PyObject *args) ;
/* chinese() */
static PyObject *
demo_chinese(PyObject *self, PyObject *args) ;
 
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

