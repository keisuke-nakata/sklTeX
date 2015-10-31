# sklTeX
convert sklearn models into TeX

## usage
```python
import sklTeX
from sklearn import linear_model, datasets

lr = linear_model.LinearRegression()
X, y = datasets.make_regression()
lr.fit(X, y)
sklTeX.skl2tex(lr)
```
