# PProgBar

**PProgBar** is a package to create an image progress bar

### Installation
from source `python setup.py install`  
using [GitPack](https://github.com/HugeBrain16/GitPack) `python -m gitpack install HugeBrain16 PProgBar`  

### Example  
```py
import pprogbar

x = pprogbar.Progger(200,20,30,100,0x00FFFF)
x.create('progbar.png')
```