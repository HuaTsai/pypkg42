#include <Python.h>
#include <time.h>

static PyObject* fib(PyObject* self, PyObject* args) {
  int n;

  if (!PyArg_ParseTuple(args, "i", &n)) {
    return NULL;
  }

  if (n <= 0) {
    return PyLong_FromLongLong(0);
  } else if (n == 1 || n == 2) {
    return PyLong_FromLongLong(1);
  }
  long long a = 1;
  long long b = 1;
  for (int i = 2; i < n; i++) {
    long long temp = b;
    b += a;
    a = temp;
  }
  return PyLong_FromLongLong(b);
}

// clang-format off

static PyMethodDef methods[] = {
    {"fib", fib, METH_VARARGS, "Compute the nth Fibonacci number using the recursive algorithm."},
    {NULL, NULL, 0, NULL}};

static struct PyModuleDef fib_cmodule =
    {PyModuleDef_HEAD_INIT, "fib_c", "Fibonacci C Module", -1, methods};

// clang-format on

PyMODINIT_FUNC PyInit_fib_c(void) { return PyModule_Create(&fib_cmodule); }