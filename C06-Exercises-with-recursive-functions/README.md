1. Implement the factorial function and test it with several different values.
Cross-check with a calculator.

```python
from math import factorial
from random import randint

count = 1

while count != 6:
    x = randint(0, 7)
    print("Test " + str(count) + " for number " + str(x) + ":", factorial(x))
    count += 1
```
