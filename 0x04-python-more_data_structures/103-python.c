#include <Python.h>

void print_python_list(PyObject *poj);
void print_python_bytes(PyObject *poj);

/**
 * print_python_list - Prints basic info about Python lists.
 * @poj: A PyObject list object.
 */
void print_python_list(PyObject *poj)
{
	int szi, allo, i;
	const char *type;
	PyListObject *list = (PyListObject *)poj;
	PyVarObject *var = (PyVarObject *)poj;

	szi = var->ob_size;
	allo = list->allocated;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %d\n", szi);
	printf("[*] Allocated = %d\n", allo);

	for (i = 0; i < szi; i++)
	{
		type = list->ob_item[i]->ob_type->tp_name;
		printf("Element %d: %s\n", i, type);
		if (strcmp(type, "bytes") == 0)
			print_python_bytes(list->ob_item[i]);
	}
}

/**
 * print_python_bytes - Prints basic info about Python byte objects.
 * @poj: A PyObject byte object.
 */
void print_python_bytes(PyObject *poj)
{
	unsigned char i, szi;
	PyBytesObject *bytes = (PyBytesObject *)poj;

	printf("[.] bytes object info\n");
	if (strcmp(poj->ob_type->tp_name, "bytes") != 0)
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	printf("  szi: %ld\n", ((PyVarObject *)poj)->ob_size);
	printf("  trying string: %s\n", bytes->ob_sval);

	if (((PyVarObject *)poj)->ob_size > 10)
		szi = 10;
	else
		szi = ((PyVarObject *)poj)->ob_size + 1;

	printf("  first %d bytes: ", szi);
	for (i = 0; i < szi; i++)
	{
		printf("%02hhx", bytes->ob_sval[i]);
		if (i == (szi - 1))
			printf("\n");
		else
			printf(" ");
	}
}
