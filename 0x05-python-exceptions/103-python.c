#include <Python.h>
#include <stdio.h>

void print_python_bytes(PyObject *p);
void print_python_float(PyObject *p);
/*
 * print_python_list - prints some basic info about Python lists 
 * @p: pointer to a Python list object 
 */

void print_python_list(PyObject *p)
{
	PyObject *iterate, *real_item = NULL;
	Py_ssize_t real_size = 0, allocated;
	printf("[*] Python list info\n");
	/*size of list*/
	fflush(stdout);
	/*reason to that is that Pythons print and libCs printf don't*/
	/*share the same buffer, and the output can appear disordered.*/
	real_size = 0;
	iterate = PyObject_GetIter(p);
	if (iterate == NULL)
	{	
		printf("  [ERROR] Invalid List Object\n");
		return;
	}
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
		real_item = PyObject_GetItem(p, PyLong_FromSsize_t(q));
		if (real_item == NULL)
		{
			printf("  [ERROR] Invalid Bytes Object\n");
			continue;
		}
		printf("Element %ld: ", q);
		if (PyLong_Check(real_item))
			printf("int\n");
		else if (PyFloat_Check(real_item))
		{
			printf("float\n");
			print_python_float(real_item);
		}		
		else if (PyUnicode_Check(real_item))
			printf("str\n");
		else if (PyTuple_Check(real_item))
			printf("tuple\n");
		else if (PyList_Check(real_item))
			printf("list\n");
		else if (PyBytes_Check(real_item))
                {
			printf("bytes\n");
                        print_python_bytes(real_item);
                }
		else
			printf("unknown\n");
                
                Py_DECREF(real_item);
	}

}

/**
 * print_python_bytes- prints some basic info about  Python bytes objects
 * @p: pointer to a Python bytes object
 */

void print_python_bytes(PyObject *p)
{
	char *real_data_bytes;

	Py_ssize_t real_size, q;
	fflush(stdout);

	if (!PyBytes_Check(p))
	{		
                printf("[.] bytes object info\n");             
                printf("  [ERROR] Invalid Bytes Object\n");
                return;
	}
        printf("[.] bytes object info\n");
	real_size = ((PyVarObject *)p)->ob_size;
	real_data_bytes = ((PyBytesObject *)p)->ob_sval;

	printf("  size: %ld\n", real_size);
	printf("  trying string: %s\n", real_data_bytes);
	if (real_size < 10)
		printf("  first %ld bytes:", real_size + 1);
	else
		printf("  first 10 bytes:");
	for ( q = 0; q <= real_size && q < 10; q++)
		printf(" %.2x", (unsigned char) real_data_bytes[q]);
	printf("\n");
}

/**
 * print_python_float- function that print some basic info
 * about Python float objects
 * @p: pointer to a Python float object
 */

void print_python_float(PyObject *p)
{
	double float_value;
	

	if (!PyFloat_Check(p))
	{
		printf("[.] float object info\n");
		printf("  [ERROR] Invalid Float Object\n");
		return;
	}
	printf("[.] float object info\n");	
	float_value = PyFloat_AsDouble(p);
	printf("  value: %.16g\n", float_value);
	

}
