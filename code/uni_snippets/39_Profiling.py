#!/usr/bin/env python
# coding: utf-8

# # Profiling in Python
# 
# Programming in Python
# 
# School of Computer Science, University of St Andrews

# ## Profiling HOWTO

# ## provided your code has the `main()` function:
# - import `profile`
# - modify the call of `main`:
# 
# ```
# import profile
# 
# ...
# ...
# ...
# 
# profile.run(’main()’)
# ```
# 
# Documentation: https://docs.python.org/3/library/profile.html

# ## Counting word frequencies

# `./wordcount.py <text file>`

# ```
# Total  122817
#          330189 function calls (330185 primitive calls) in 1.122 seconds
# 
#    Ordered by: standard name
# 
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 :0(__new__)
#        30    0.000    0.000    0.000    0.000 :0(append)
#         1    0.000    0.000    0.000    0.000 :0(compile)
#         1    0.000    0.000    1.107    1.107 :0(exec)
#         5    0.000    0.000    0.000    0.000 :0(find)
#         1    0.000    0.000    0.000    0.000 :0(fromkeys)
#    122818    0.236    0.000    0.236    0.000 :0(get)
#         1    0.000    0.000    0.000    0.000 :0(insert)
#     21459    0.035    0.000    0.035    0.000 :0(isinstance)
#         1    0.000    0.000    0.000    0.000 :0(items)
# 140375/140373    0.192    0.000    0.192    0.000 :0(len)
#         5    0.000    0.000    0.000    0.000 :0(min)
#         1    0.000    0.000    0.000    0.000 :0(nl_langinfo)
#         1    0.000    0.000    0.000    0.000 :0(open)
#         4    0.000    0.000    0.000    0.000 :0(ord)
#         1    0.000    0.000    0.000    0.000 :0(print)
#         1    0.000    0.000    0.000    0.000 :0(setdefault)
#         1    0.015    0.015    0.015    0.015 :0(setprofile)
#         1    0.000    0.000    0.000    0.000 :0(sort)
#     10721    0.059    0.000    0.059    0.000 :0(split)
#     13030    0.019    0.000    0.019    0.000 :0(strip)
#         1    0.000    0.000    0.000    0.000 :0(sum)
#        87    0.000    0.000    0.000    0.000 :0(utf_8_decode)
#         1    0.000    0.000    1.107    1.107 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 _bootlocale.py:33(getpreferredencoding)
#         1    0.000    0.000    0.000    0.000 codecs.py:260(__init__)
#         1    0.000    0.000    0.000    0.000 codecs.py:309(__init__)
#        87    0.001    0.000    0.001    0.000 codecs.py:319(decode)
#         2    0.000    0.000    0.000    0.000 enum.py:289(__call__)
#         1    0.000    0.000    0.000    0.000 enum.py:357(__iter__)
#        10    0.000    0.000    0.000    0.000 enum.py:358(<genexpr>)
#         2    0.000    0.000    0.000    0.000 enum.py:580(__new__)
#         9    0.000    0.000    0.000    0.000 enum.py:683(value)
#         1    0.000    0.000    0.000    0.000 enum.py:809(_missing_)
#         1    0.000    0.000    0.000    0.000 enum.py:816(_create_pseudo_member_)
#         1    0.000    0.000    0.000    0.000 enum.py:852(__and__)
#         1    0.000    0.000    0.000    0.000 enum.py:888(_decompose)
#         1    0.000    0.000    1.122    1.122 profile:0(main())
#         0    0.000             0.000          profile:0(profiler)
#     10721    0.052    0.000    0.203    0.000 re.py:223(split)
#         1    0.000    0.000    0.001    0.001 re.py:250(compile)
#     10722    0.058    0.000    0.094    0.000 re.py:289(_compile)
#         1    0.000    0.000    0.000    0.000 sre_compile.py:249(_compile_charset)
#         1    0.000    0.000    0.000    0.000 sre_compile.py:276(_optimize_charset)
#         1    0.000    0.000    0.000    0.000 sre_compile.py:423(_simple)
#         2    0.000    0.000    0.000    0.000 sre_compile.py:453(_get_iscased)
#         1    0.000    0.000    0.000    0.000 sre_compile.py:461(_get_literal_prefix)
#         1    0.000    0.000    0.000    0.000 sre_compile.py:492(_get_charset_prefix)
#         1    0.000    0.000    0.000    0.000 sre_compile.py:536(_compile_info)
#         2    0.000    0.000    0.000    0.000 sre_compile.py:595(isstring)
#         1    0.000    0.000    0.000    0.000 sre_compile.py:598(_code)
#       2/1    0.000    0.000    0.000    0.000 sre_compile.py:71(_compile)
#         1    0.000    0.000    0.001    0.001 sre_compile.py:759(compile)
#         2    0.000    0.000    0.000    0.000 sre_parse.py:111(__init__)
#         4    0.000    0.000    0.000    0.000 sre_parse.py:160(__len__)
#         8    0.000    0.000    0.000    0.000 sre_parse.py:164(__getitem__)
#         1    0.000    0.000    0.000    0.000 sre_parse.py:168(__setitem__)
#         1    0.000    0.000    0.000    0.000 sre_parse.py:172(append)
#       2/1    0.000    0.000    0.000    0.000 sre_parse.py:174(getwidth)
#         1    0.000    0.000    0.000    0.000 sre_parse.py:224(__init__)
#        11    0.000    0.000    0.000    0.000 sre_parse.py:233(__next)
#         5    0.000    0.000    0.000    0.000 sre_parse.py:249(match)
#         7    0.000    0.000    0.000    0.000 sre_parse.py:254(get)
#         3    0.000    0.000    0.000    0.000 sre_parse.py:286(tell)
#         1    0.000    0.000    0.000    0.000 sre_parse.py:432(_uniq)
#         1    0.000    0.000    0.000    0.000 sre_parse.py:435(_parse_sub)
#         1    0.000    0.000    0.000    0.000 sre_parse.py:493(_parse)
#         1    0.000    0.000    0.000    0.000 sre_parse.py:76(__init__)
#         2    0.000    0.000    0.000    0.000 sre_parse.py:81(groups)
#         1    0.000    0.000    0.000    0.000 sre_parse.py:921(fix_flags)
#         1    0.000    0.000    0.000    0.000 sre_parse.py:937(parse)
#         9    0.000    0.000    0.000    0.000 types.py:171(__get__)
#         1    0.000    0.000    0.000    0.000 wordcount_profile.py:18(<listcomp>)
#         1    0.453    0.453    1.107    1.107 wordcount_profile.py:7(main)
# ```            

# ## How to read this output:
# - `ncalls`
#   - number of calls.
# - `tottime`
#   - total time spent in the given function (and excluding time made in calls to sub-functions)
# - `percall`
#   - quotient of tottime divided by ncalls
# - `cumtime`
#   - cumulative time spent in this and all subfunctions (from invocation till exit). 
# - `percall`
#   - quotient of cumtime divided by primitive calls
# - `filename:lineno(function)`
#   - respective information for each function

# `./wordcount_opt.py <text_file>`

# ```
# Total  127320
#          67022 function calls (67018 primitive calls) in 0.297 seconds
# 
#    Ordered by: standard name
# 
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 :0(__new__)
#        30    0.000    0.000    0.000    0.000 :0(append)
#         1    0.000    0.000    0.000    0.000 :0(compile)
#         1    0.000    0.000    0.285    0.285 :0(exec)
#         5    0.000    0.000    0.000    0.000 :0(find)
#         1    0.000    0.000    0.000    0.000 :0(fromkeys)
#         1    0.000    0.000    0.000    0.000 :0(get)
#         1    0.000    0.000    0.000    0.000 :0(insert)
#     21459    0.032    0.000    0.032    0.000 :0(isinstance)
#         1    0.000    0.000    0.000    0.000 :0(items)
#     25/23    0.000    0.000    0.000    0.000 :0(len)
#         5    0.000    0.000    0.000    0.000 :0(min)
#         1    0.000    0.000    0.000    0.000 :0(nl_langinfo)
#         1    0.000    0.000    0.000    0.000 :0(open)
#         4    0.000    0.000    0.000    0.000 :0(ord)
#         1    0.000    0.000    0.000    0.000 :0(print)
#         1    0.000    0.000    0.000    0.000 :0(setdefault)
#         1    0.012    0.012    0.012    0.012 :0(setprofile)
#         1    0.000    0.000    0.000    0.000 :0(sort)
#     10721    0.050    0.000    0.050    0.000 :0(split)
#     13030    0.018    0.000    0.018    0.000 :0(strip)
#         1    0.000    0.000    0.000    0.000 :0(sum)
#        87    0.000    0.000    0.000    0.000 :0(utf_8_decode)
#         1    0.000    0.000    0.285    0.285 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 _bootlocale.py:33(getpreferredencoding)
#         1    0.000    0.000    0.000    0.000 codecs.py:260(__init__)
#         1    0.000    0.000    0.000    0.000 codecs.py:309(__init__)
#        87    0.001    0.000    0.001    0.000 codecs.py:319(decode)
#         2    0.000    0.000    0.000    0.000 enum.py:289(__call__)
#         1    0.000    0.000    0.000    0.000 enum.py:357(__iter__)
#        10    0.000    0.000    0.000    0.000 enum.py:358(<genexpr>)
#         2    0.000    0.000    0.000    0.000 enum.py:580(__new__)
#         9    0.000    0.000    0.000    0.000 enum.py:683(value)
#         1    0.000    0.000    0.000    0.000 enum.py:809(_missing_)
#         1    0.000    0.000    0.000    0.000 enum.py:816(_create_pseudo_member_)
#         1    0.000    0.000    0.000    0.000 enum.py:852(__and__)
#         1    0.000    0.000    0.000    0.000 enum.py:888(_decompose)
#         1    0.000    0.000    0.297    0.297 profile:0(main())
#         0    0.000             0.000          profile:0(profiler)
#     10721    0.049    0.000    0.185    0.000 re.py:223(split)
#         1    0.000    0.000    0.001    0.001 re.py:250(compile)
#     10722    0.054    0.000    0.088    0.000 re.py:289(_compile)
#         1    0.000    0.000    0.000    0.000 sre_compile.py:249(_compile_charset)
#         1    0.000    0.000    0.000    0.000 sre_compile.py:276(_optimize_charset)
#         1    0.000    0.000    0.000    0.000 sre_compile.py:423(_simple)
#         2    0.000    0.000    0.000    0.000 sre_compile.py:453(_get_iscased)
#         1    0.000    0.000    0.000    0.000 sre_compile.py:461(_get_literal_prefix)
#         1    0.000    0.000    0.000    0.000 sre_compile.py:492(_get_charset_prefix)
#         1    0.000    0.000    0.000    0.000 sre_compile.py:536(_compile_info)
#         2    0.000    0.000    0.000    0.000 sre_compile.py:595(isstring)
#         1    0.000    0.000    0.000    0.000 sre_compile.py:598(_code)
#       2/1    0.000    0.000    0.000    0.000 sre_compile.py:71(_compile)
#         1    0.000    0.000    0.001    0.001 sre_compile.py:759(compile)
#         2    0.000    0.000    0.000    0.000 sre_parse.py:111(__init__)
#         4    0.000    0.000    0.000    0.000 sre_parse.py:160(__len__)
#         8    0.000    0.000    0.000    0.000 sre_parse.py:164(__getitem__)
#         1    0.000    0.000    0.000    0.000 sre_parse.py:168(__setitem__)
#         1    0.000    0.000    0.000    0.000 sre_parse.py:172(append)
#       2/1    0.000    0.000    0.000    0.000 sre_parse.py:174(getwidth)
#         1    0.000    0.000    0.000    0.000 sre_parse.py:224(__init__)
#        11    0.000    0.000    0.000    0.000 sre_parse.py:233(__next)
#         5    0.000    0.000    0.000    0.000 sre_parse.py:249(match)
#         7    0.000    0.000    0.000    0.000 sre_parse.py:254(get)
#         3    0.000    0.000    0.000    0.000 sre_parse.py:286(tell)
#         1    0.000    0.000    0.000    0.000 sre_parse.py:432(_uniq)
#         1    0.000    0.000    0.000    0.000 sre_parse.py:435(_parse_sub)
#         1    0.000    0.000    0.000    0.000 sre_parse.py:493(_parse)
#         1    0.000    0.000    0.000    0.000 sre_parse.py:76(__init__)
#         2    0.000    0.000    0.000    0.000 sre_parse.py:81(groups)
#         1    0.000    0.000    0.000    0.000 sre_parse.py:921(fix_flags)
#         1    0.000    0.000    0.000    0.000 sre_parse.py:937(parse)
#         9    0.000    0.000    0.000    0.000 types.py:171(__get__)
#         1    0.000    0.000    0.000    0.000 wordcount_opt2.py:20(<listcomp>)
#         1    0.078    0.078    0.285    0.285 wordcount_opt2.py:7(main)
# ```

# ## Exercises
# 
# Experiment further with profiling the code from `wordcount.py`, for example:
# - Check whether the use of `re.compile` impacts performance
# - What will happen if `sum([counts[w] for w in counts])` will be replaced by a `for` loop with an accumulator?
# - Experiment with other, possibly larger, texts
# - Try to profile some other Python code of yours
