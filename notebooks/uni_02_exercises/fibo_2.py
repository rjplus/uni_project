{\rtf1\ansi\ansicpg1252\cocoartf2513
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fmodern\fcharset0 Courier-Bold;\f1\fmodern\fcharset0 Courier;}
{\colortbl;\red255\green255\blue255;\red15\green112\blue1;\red255\green255\blue255;\red0\green0\blue0;
\red0\green0\blue255;\red169\green14\blue26;\red151\green0\blue255;\red16\green121\blue2;}
{\*\expandedcolortbl;;\cssrgb\c0\c50196\c0;\cssrgb\c100000\c100000\c100000;\cssrgb\c0\c0\c0;
\cssrgb\c0\c0\c100000;\cssrgb\c72941\c12941\c12941;\cssrgb\c66667\c13333\c100000;\cssrgb\c0\c53333\c0;}
\paperw11900\paperh16840\margl1440\margr1440\vieww10800\viewh8400\viewkind0
\deftab720
\pard\pardeftab720\partightenfactor0

\f0\b\fs28 \cf2 \cb3 \expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 def
\f1\b0 \cf4 \strokec4  \cf5 \strokec5 fibonacci\cf4 \strokec4 (n):\
    \cf6 \strokec6 """write Fibonacci series up to n"""\cf4 \strokec4 \
    a, b 
\f0\b \cf7 \strokec7 =
\f1\b0 \cf4 \strokec4  \cf8 \strokec8 0\cf4 \strokec4 , \cf8 \strokec8 1\cf4 \strokec4 \
    
\f0\b \cf2 \strokec2 while
\f1\b0 \cf4 \strokec4  b 
\f0\b \cf7 \strokec7 <
\f1\b0 \cf4 \strokec4  n:\
        \cf2 \strokec2 print\cf4 \strokec4 (b)\
        a, b 
\f0\b \cf7 \strokec7 =
\f1\b0 \cf4 \strokec4  b, a
\f0\b \cf7 \strokec7 +
\f1\b0 \cf4 \strokec4 b\
\

\f0\b \cf2 \strokec2 def
\f1\b0 \cf4 \strokec4  \cf5 \strokec5 fibonacci2\cf4 \strokec4 (n):\
    \cf6 \strokec6 """return Fibonacci series up to n"""\cf4 \strokec4 \
    result 
\f0\b \cf7 \strokec7 =
\f1\b0 \cf4 \strokec4  []\
    a, b 
\f0\b \cf7 \strokec7 =
\f1\b0 \cf4 \strokec4  \cf8 \strokec8 0\cf4 \strokec4 , \cf8 \strokec8 1\cf4 \strokec4 \
    
\f0\b \cf2 \strokec2 while
\f1\b0 \cf4 \strokec4  b 
\f0\b \cf7 \strokec7 <
\f1\b0 \cf4 \strokec4  n:\
        result.append(b)\
        a, b 
\f0\b \cf7 \strokec7 =
\f1\b0 \cf4 \strokec4  b, a
\f0\b \cf7 \strokec7 +
\f1\b0 \cf4 \strokec4 b\
    
\f0\b \cf2 \strokec2 return
\f1\b0 \cf4 \strokec4  result\
}