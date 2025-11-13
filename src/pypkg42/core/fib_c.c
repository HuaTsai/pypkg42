#include <Python.h>
#include <time.h>

static long fib_recursive(int n) {
  if (n <= 0) {
    return 0;
  } else if (n == 1) {
    return 1;
  }
  return fib_recursive(n - 1) + fib_recursive(n - 2);
}

static PyObject* fib(PyObject* self, PyObject* args) {
  int n;

  if (!PyArg_ParseTuple(args, "i", &n)) {
    return NULL;
  }

  if (n < 0) {
    PyErr_SetString(PyExc_ValueError, "n must be non-negative");
    return NULL;
  }

  clock_t start = clock();
  long result = fib_recursive(n);
  clock_t end = clock();

  double elapsed_time = (double)(end - start) / CLOCKS_PER_SEC;
  printf("fib(%d) took %.6f seconds\n", n, elapsed_time);

  return PyLong_FromLong(result);
}

// clang-format off

static PyMethodDef methods[] = {
    {"fib", fib, METH_VARARGS, "Compute the nth Fibonacci number using the recursive algorithm."},
    {NULL, NULL, 0, NULL}};

static struct PyModuleDef fib_cmodule =
    {PyModuleDef_HEAD_INIT, "fib_c", "Fibonacci C Module", -1, methods};

// clang-format on

PyMODINIT_FUNC PyInit_fib_c(void) { return PyModule_Create(&fib_cmodule); }