#include <Python.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define BUFSIZE 10

int fac(int n) {
    if (n < 2)
        return 1;
    return n * fac(n - 1);
}

static PyObject * Extest_fac(PyObject *self, PyObject *args) {
    int res;//计算结果值
    int num;//参数
    PyObject* retval;//返回值

    //i表示需要传递进来的参数类型为整型，如果是，就赋值给num，如果不是，返回NULL；
    res = PyArg_ParseTuple(args, "i", &num);
    if (!res) {
        //包装函数返回NULL，就会在Python调用中产生一个TypeError的异常
        return NULL;
    }
    res = fac(num);
    //需要把c中计算的结果转成python对象，i代表整数对象类型。
    retval = (PyObject *)Py_BuildValue("i", res);
    return retval;
}

char *reverse(char *s) {
    register char t;
    char *p = s;
    char *q = (s + (strlen(s) - 1));
    while (p < q) {
        t = *p;
        *p++ = *q;
        *q-- = t;
    }
    return s;
}

static PyObject *
Extest_reverse(PyObject *self, PyObject *args) {
    char *orignal;
    if (!(PyArg_ParseTuple(args, "s", &orignal))) {
        return NULL;
    }
    return (PyObject *)Py_BuildValue("s", reverse(orignal));
}

static PyObject *
Extest_doppel(PyObject *self, PyObject *args) {
    char *orignal;
    char *reversed;
    PyObject * retval;
    if (!(PyArg_ParseTuple(args, "s", &orignal))) {
        return NULL;
    }
    retval = (PyObject *)Py_BuildValue("ss", orignal, reversed=reverse(strdup(orignal)));
    free(reversed);
    return retval;
}

static PyMethodDef
ExtestMethods[] = {
    {"fac", Extest_fac, METH_VARARGS},
    {"doppel", Extest_doppel, METH_VARARGS},
    {"reverse", Extest_reverse, METH_VARARGS},
    {NULL, NULL},
};

static struct PyModuleDef ExtestModule = {
    PyModuleDef_HEAD_INIT,
    "Extest",
    NULL,
    -1,
    ExtestMethods
};

PyMODINIT_FUNC PyInit_Extest(void)
{
    return PyModule_Create(&ExtestModule);
}