```python
from tkinter import*
import random
from datetime import date, datetime
```
#### Import datetime to check our playing time.
----------

+Set size
```python
def ran_btn(): 
  ....
  if x >= 0.9:
      btn.place(relx=x-0.1,rely=y)
  elif x <= 0.1:
      btn.place(relx=x+0.1,rely=y)
  elif y >= 0.9: 
      ....
  elif y <= 0.1: 
      ....
  else:
      btn.place(relx=x,rely=y)
 ```
 #### We have to check the block size , Then we can protect the block was out of your setting size.
 -----------
 ```python
def btn_f():
    ....
    for i in win.grid_slaves():  #save->[label,entry,button]
        i.destroy() 
    ....
    start=datetime.now() #save start time.
 ```
#### Use destory to delete the last block.
------------
```python
def click():
    ....  
    else:
        end=datetime.now() #save last time.
        dif=(end-start).total_seconds() 
        ....
```
#### Use total_second() to print clearly.
