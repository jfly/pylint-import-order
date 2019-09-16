Demonstrating some weirdness if you name a folder the same as a 3rd party package, and if you run isort/pylint from within vs outside of that folder.

```python
(pylint-import-order) ➜  ~/tmp/pylint-import-order git:(master) ✗ isort --diff tqdm/__main__.py
--- /home/jeremy/tmp/pylint-import-order/tqdm/__main__.py:before    2019-09-15 21:56:55.671551
+++ /home/jeremy/tmp/pylint-import-order/tqdm/__main__.py:after     2019-09-15 22:02:23.959179
@@ -1,5 +1,6 @@
+from six import PY2
+
 import tqdm
-from six import PY2

 for i in tqdm.tqdm(range(10)):
     if PY2:
(pylint-import-order) ➜  ~/tmp/pylint-import-order git:(master) ✗ (cd tqdm && isort --diff ./__main__.py)

(pylint-import-order) ➜  ~/tmp/pylint-import-order git:(master) ✗ pylint --disable=missing-docstring tqdm/__main__.py
************* Module __main__
tqdm/__main__.py:2:0: C0411: third party import "from six import PY2" should be placed before "import tqdm" (wrong-import-order)

------------------------------------------------------------------
Your code has been rated at 8.00/10 (previous run: 6.00/10, +2.00)

(pylint-import-order) ➜  ~/tmp/pylint-import-order git:(master) ✗ (cd tqdm && pylint --disable=missing-docstring ./__main__.py)

-------------------------------------------------------------------
Your code has been rated at 10.00/10 (previous run: 8.00/10, +2.00)
```
