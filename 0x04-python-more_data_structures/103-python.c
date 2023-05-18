#include <Python.h>

/**
 * print_python_list - prints some basic info about Python lists 
 * @p: pointer to a Python list object 
 */

void print_python_list(PyObject *p);
{
	PyObject *iterate, real_item = NULL;
	Py_ssize_t real_size, allocated;
	printf("[*] Python list info\n");
	/*size of list*/
	real_size = 0;
	iterate = PyObject_GetIter(p);
	while ((real_item = PyIter_Next(iterate)) != NULL)
	{
		real_size++;
		Py_DECREF(real_item);
	}
	Py_DECREF(iterate);
	printf("[*] Size of the Python List = %ld\n", real_size);

	allocated = ((PyListObject *)p)->allocated;
	printf("[*] Allocated = %ld\n", allocated);

	for (Py_ssize_t q = 0; q < real_size; q++)
	{
		real_item = PySequence_GetItem(p, q);
		printf("Element %ld: ", q);
		if (PyLong_Check(real_item))
			printf("int\n");
		else if (PyFloat_Check(real_item))
			printf("float\n");
		else if (PyUnicode_Check(real_item))
			printf("str\n");
		else if (PyTuple_Check(real_item))
			printf("tuple\n");
		else if (PyList_Check(real_item))
			printf("list\n");
		else if (PyBytes_Check(real_item))
			printf("bytes\n");
		else
			printf("unknown\n");
	}

}

/**
 * print_python_bytes- prints some basic info about  Python bytes objects
 * @p: pointer to a Python bytes object
 */

void print_python_bytes(PyObject *p);
{
	char *real_data_bytes = PyBytes_AsString(p);
	Py_ssize_t real_size = PyBytes_Size(p), q;

	printf("[.] bytes object info\n");
	printf("   size: %ld\n", real_size);
	printf("  trying string: ");

	for (q = 0; q < real_size; q++)
	{
		if (real_data_bytes[q] >= 32 && real_data_bytes[q] <= 126)
			printf("%c", real_data_bytes[q]);
		else
			printf("\\x%.2x", (unsigned char) real_data_bytes[q]);
	}
	printf("\n");

	printf("  first %ld bytes: ", (real_size < 10) ? real_size : 10);
	for ( q = 0; q < ((real_size < 10) ? real_size : 10    ); q++)
		printf("%.2x ", (unsigned char) real_data_bytes[q]);

	printf("\n");
}
