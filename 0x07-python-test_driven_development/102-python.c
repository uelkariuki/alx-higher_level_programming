#include <Python.h>

/**
 * print_python_string - function that prints Python strings.
 * @p: pointer to a Python Bytes Object
 */

void print_python_string(PyObject *p)
{
	
	const char *value, *the_name_type;
	Py_ssize_t length;

	if (!PyUnicode_Check(p))
	{
		fprintf(stderr, "  [ERROR] Invalid String Object\n");
		return;
	}

	length = PyUnicode_GET_LENGTH(p);
	value = PyUnicode_AsUTF8(p);
	the_name_type = Py_TYPE(p)->tp_name;

	printf("[.] string object info\n");
	printf("  type: %s\n", the_name_type);
	printf("  length: %zd\n", length);
	printf("  value: %s\n", value);

	Py_DECREF(p);
}
