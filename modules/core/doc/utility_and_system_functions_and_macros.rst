Utility and System Functions and Macros
=======================================

.. highlight:: cpp

alignPtr
------------
Aligns a pointer to the specified number of bytes.

.. ocv:function:: template<typename _Tp> _Tp* alignPtr(_Tp* ptr, int n=sizeof(_Tp))

    :param ptr: Aligned pointer.

    :param n: Alignment size that must be a power of two.

The function returns the aligned pointer of the same type as the input pointer:

.. math::

    \texttt{(\_Tp*)(((size\_t)ptr + n-1) \& -n)}



alignSize
-------------
Aligns a buffer size to the specified number of bytes.

.. ocv:function:: size_t alignSize(size_t sz, int n)

    :param sz: Buffer size to align.

    :param n: Alignment size that must be a power of two.

The function returns the minimum number that is greater or equal to ``sz`` and is divisble by ``n`` :

.. math::

    \texttt{(sz + n-1) \& -n}



allocate
------------
Allocates an array of elements.

.. ocv:function:: template<typename _Tp> _Tp* allocate(size_t n)

    :param n: Number of elements to allocate.

The generic function ``allocate`` allocates a buffer for the specified number of elements. For each element, the default constructor is called.



deallocate
--------------
Deallocates an array of elements.

.. ocv:function:: template<typename _Tp> void deallocate(_Tp* ptr, size_t n)

    :param ptr: Pointer to the deallocated buffer.

    :param n: Number of elements in the buffer.

The generic function ``deallocate`` deallocates the buffer allocated with
:ocv:func:`allocate` . The number of elements must match the number passed to
:ocv:func:`allocate` .



CV_Assert
---------
Checks a condition at runtime and throws exception if it fails

.. ocv:function:: CV_Assert(expr)

The macros ``CV_Assert`` (and ``CV_DbgAssert``) evaluate the specified expression. If it is 0, the macros raise an error (see :ocv:func:`error` ). The macro ``CV_Assert`` checks the condition in both Debug and Release configurations while ``CV_DbgAssert`` is only retained in the Debug configuration.


error
---------
Signals an error and raises an exception.

.. ocv:function:: void error( const Exception& exc )

    :param exc: Exception to throw.

    :param code: Error code. Normally, it is a negative value. The list of pre-defined error codes can be found in  ``cxerror.h`` .   
	
    :param msg: Text of the error message.

    :param args: ``printf`` -like formatted error message in parentheses.

The function and the helper macros ``CV_Error`` and ``CV_Error_``: ::

    #define CV_Error( code, msg ) error(...)
    #define CV_Error_( code, args ) error(...)

call the error handler. Currently, the error handler prints the error code ( ``exc.code`` ), the context ( ``exc.file``,``exc.line`` ), and the error message ``exc.err`` to the standard error stream ``stderr`` . In the Debug configuration, it then provokes memory access violation, so that the execution stack and all the parameters can be analyzed by the debugger. In the Release configuration, the exception ``exc`` is thrown.

The macro ``CV_Error_`` can be used to construct an error message on-fly to include some dynamic information, for example: ::

    // note the extra parentheses around the formatted text message
    CV_Error_(CV_StsOutOfRange,
        ("the matrix element (
        i, j, mtx.at<float>(i,j)))


Exception
---------
.. ocv:class:: Exception

Exception class passed to an error. ::

    class  Exception
    {
    public:
        // various constructors and the copy operation
        Exception() { code = 0; line = 0; }
        Exception(int _code, const string& _err,
                  const string& _func, const string& _file, int _line);
        Exception(const Exception& exc);
        Exception& operator = (const Exception& exc);

        // the error code
        int code;
        // the error text message
        string err;
        // function name where the error happened
        string func;
        // the source file name where the error happened
        string file;
        // the source file line where the error happened
        int line;
    };

The class ``Exception`` encapsulates all or almost all necessary information about the error happened in the program. The exception is usually constructed and thrown implicitly via ``CV_Error`` and ``CV_Error_`` macros. See
:ocv:func:`error` .



fastMalloc
--------------
Allocates an aligned memory buffer.

.. ocv:function:: void* fastMalloc(size_t size)

    :param size: Allocated buffer size.

The function allocates the buffer of the specified size and returns it. When the buffer size is 16 bytes or more, the returned buffer is aligned to 16 bytes.



fastFree
------------
Deallocates a memory buffer.

.. ocv:function:: void fastFree(void* ptr)

    :param ptr: Pointer to the allocated buffer.

The function deallocates the buffer allocated with
:ocv:func:`fastMalloc` .
If NULL pointer is passed, the function does nothing.



format
----------
Returns a text string formatted using the ``printf`` -like expression.

.. ocv:function:: string format( const char* fmt, ... )

    :param fmt: ``printf`` -compatible formatting specifiers.

The function acts like ``sprintf``  but forms and returns an STL string. It can be used to form an error message in the
:ocv:func:`Exception` constructor.



getNumThreads
-----------------
Returns the number of threads used by OpenCV.

.. ocv:function:: int getNumThreads()

The function returns the number of threads that is used by OpenCV.

.. seealso::
:ocv:func:`setNumThreads`,
:ocv:func:`getThreadNum` 



getThreadNum
----------------
Returns the index of the currently executed thread.

.. ocv:function:: int getThreadNum()

The function returns a 0-based index of the currently executed thread. The function is only valid inside a parallel OpenMP region. When OpenCV is built without OpenMP support, the function always returns 0.

.. seealso::
:ocv:func:`setNumThreads`,
:ocv:func:`getNumThreads` .



getTickCount
----------------
Returns the number of ticks.

.. ocv:function:: int64 getTickCount()

The function returns the number of ticks after the certain event (for example, when the machine was turned on).
It can be used to initialize
:ocv:func:`RNG` or to measure a function execution time by reading the tick count before and after the function call. See also the tick frequency.



getTickFrequency
--------------------
Returns the number of ticks per second.

.. ocv:function:: double getTickFrequency()

The function returns the number of ticks per second.
That is, the following code computes the execution time in seconds: ::

    double t = (double)getTickCount();
    // do something ...
    t = ((double)getTickCount() - t)/getTickFrequency();



getCPUTickCount
----------------
Returns the number of CPU ticks.

.. ocv:function:: int64 getCPUTickCount()

The function returns the current number of CPU ticks on some architectures (such as x86, x64, PowerPC). On other platforms the function is equivalent to ``getTickCount``. It can also be used for very accurate time measurements, as well as for RNG initialization. Note that in case of multi-CPU systems a thread, from which ``getCPUTickCount`` is called, can be suspended and resumed at another CPU with its own counter. So, theoretically (and practically) the subsequent calls to the function do not necessary return the monotonously increasing values. Also, since a modern CPU varies the CPU frequency depending on the load, the number of CPU clocks spent in some code cannot be directly converted to time units. Therefore, ``getTickCount`` is generally a preferable solution for measuring execution time.



setNumThreads
-----------------
Sets the number of threads used by OpenCV.

.. ocv:function:: void setNumThreads(int nthreads)

    :param nthreads: Number of threads used by OpenCV.

The function sets the number of threads used by OpenCV in parallel OpenMP regions. If ``nthreads=0`` , the function uses the default number of threads that is usually equal to the number of the processing cores.

.. seealso::
:ocv:func:`getNumThreads`,
:ocv:func:`getThreadNum` 



setUseOptimized
-----------------
Enables or disables the optimized code.

.. ocv:function:: void setUseOptimized(bool onoff)

    :param onoff: The boolean flag specifying whether the optimized code should be used (``onoff=true``) or not (``onoff=false``).

The function can be used to dynamically turn on and off optimized code (code that uses SSE2, AVX, and other instructions on the platforms that support it). It sets a global flag that is further checked by OpenCV functions. Since the flag is not checked in the inner OpenCV loops, it is only safe to call the function on the very top level in your application where you can be sure that no other OpenCV function is currently executed.

By default, the optimized code is enabled unless you disable it in CMake. The current status can be retrieved using ``useOptimized``.

useOptimized
-----------------
Returns the status of optimized code usage.

.. ocv:function:: bool useOptimized()

The function returns ``true`` if the optimized code is enabled. Otherwise, it returns ``false``.
