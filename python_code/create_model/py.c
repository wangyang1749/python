#include<stdio.h>
#include<Python.h> //有的是#include<Python.h>

//判断是否是质数
static PyObject *pr_isprime(PyObject *self, PyObject *args) {
    int n, num;
    //解析参数
    if (!PyArg_ParseTuple(args, "i", &num)) {
        return NULL;
    }

    if (num < 1) {
        return Py_BuildValue("i", 0); //C类型转成python对象
    }

    n = num - 1;
    while (n > 1) {
        if (num % n == 0)
            return Py_BuildValue("i", 0);
        n--;
    }
    return Py_BuildValue("i", 1);
}

static PyMethodDef PrMethods[] = {
    //方法名，导出函数，参数传递方式，方法描述。
    {"isPrime", pr_isprime, METH_VARARGS, "check if an input number is prime or not."},
    {NULL, NULL, 0, NULL}
};

void initpr(void) {
    (void) Py_InitModule("pr", PrMethods);
}