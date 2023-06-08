#include <Python.h>

/**
 * print_python_string - function that prints Python strings.
 * @p: pointer to a Python Bytes Object
 */

void print_python_string(PyObject *p)
{
	const char *value, *the_name_type;
	Py_ssize_t length;

	if (!PyUnicode_Check(p) && !PyBytes_Check(p))
	{
		fprintf(stderr, "  [ERROR] Invalid String Object\n");
		return;
	}

	length = PyUnicode_GET_LENGTH(p);
	value = PyUnicode_AsUTF8(p);

	printf("[.] string object info\n");
	if (PyUnicode_IS_COMPACT_ASCII(p))
		printf(" type: compact ascii\n");
	else if (PyUnicode_IS_COMPACT(p))
		printf(" type: compact unicode object\n");
	else
		printf(" type: unicode object\n");
	printf("  length: %zd\n", length);
	printf("  value: %s\n", value);

	Py_DECREF(p);
}
