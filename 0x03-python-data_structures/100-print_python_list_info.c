#include <Python.h>

/**
 *print_python_list_info- prints some basic info about Python lists.
 *@p: a pointer to a PyObject object 
 *
 */

void print_python_list_info(PyObject *p)
{
        const char *The_Item_type;

        Py_ssize_t size = PyList_Size(p);
        printf("[*] Size of the Python List = %ld\n", size);

        Py_ssize_t allocated = ((PyListObject *)p) ->allocated;
        printf("[*] Allocated = %ld\n", allocated);

        for (Py_ssize_t q = 0; q < size; q++)
        {
                PyObject *real_item = PyList_GetItem(p, q);
                The_Item_type = real_item->ob_type->tp_name;
                printf("Element %ld: %s\n", q, The_Item_type);

        }
}
