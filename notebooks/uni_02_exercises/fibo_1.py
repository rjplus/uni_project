{\rtf1\ansi\ansicpg1252\cocoartf2513
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fmodern\fcharset0 Courier-Bold;}
{\colortbl;\red255\green255\blue255;\red15\green112\blue1;\red255\green255\blue255;}
{\*\expandedcolortbl;;\cssrgb\c0\c50196\c0;\cssrgb\c100000\c100000\c100000;}
\paperw11900\paperh16840\margl1440\margr1440\vieww10800\viewh8400\viewkind0
\deftab720
\pard\pardeftab720\partightenfactor0

\f0\b\fs28 \cf2 \cb3 \expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 def fib(n):\
    """Return the Fibonacci series up to n."""\
    a, b = 0, 1\
    while a < n:\
        print(a, end=' ')\
        a, b = b, a + b\
    print()\
\
def fib_recursive(n):\
    """Return the nth Fibonacci number using recursion."""\
    if n <= 1:\
        return n\
    else:\
        return fib_recursive(n-1) + fib_recursive(n-2)\
}