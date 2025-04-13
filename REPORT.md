# Static and Dynamic Code Analysis Report
 
## Static Analysis

**Flake8**:

> .\main.py:1:1: F401 'math' imported but unused<br/>
> .\main.py:2:1: F401 'random' imported but unused<br/>
> .\main.py:28:5: F841 local variable 'output' is assigned to but never used<br/>
> .\main.py:33:11: W292 no newline at end of file<br/>

**Pylint**:

> main.py:33:0: C0304: Final newline missing (missing-final-newline)<br/>
> main.py:1:0: C0114: Missing module docstring (missing-module-docstring)<br/>
> main.py:5:0: C0116: Missing function or method docstring (missing-function-docstring)<br/>
> main.py:12:0: C0116: Missing function or method docstring (missing-function-docstring)<br/>
> main.py:19:0: C0116: Missing function or method docstring (missing-function-docstring)<br/>
> main.py:26:0: C0116: Missing function or method docstring (missing-function-docstring)<br/>
> main.py:28:4: W0612: Unused variable 'output' (unused-variable)<br/>
> main.py:1:0: W0611: Unused import math (unused-import)<br/>
> main.py:2:0: W0611: Unused import random (unused-import)<br/>


## Line Profiling

> Bottleneck found in:
> 
> - "slow_func": Took 1.41546 seconds for 1000 calls


### Fix:

> Changed the arithmetic on the expensive_op and slow_func. Time now takes 0.0004556 s
 
## Code Coverage

 
## Fix Summary

> ### Static Analysis
> > 1) Removed unused libraries:
> >     math [ flake8: F401, pylint: W0611 ]
> >     random [ flake8: F401, pylint: W0611 ]
> > 2) Printed the output variable:
> >     print(output) [ flake8: F841, pylint: W0612 ]
> > 3) Implemented a newline at the end of the file [ flake8: W292, pylint: C0304 ]
> > 4) Added Module DocString [ pylint: C0114 ]
> > 5) Added Function DocString [ pylint: C0116 ]
>
> ### Line Profiling
>
> > Changed the arithmetic on the expensive_op and slow_func. Time now takes 0.0004556 s
> 