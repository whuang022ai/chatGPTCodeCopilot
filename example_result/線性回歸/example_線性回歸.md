可以使用 scikit-learn 這個 python 套件中的 LinearRegression 模型來實現線性回歸。首先需要先安裝 scikit-learn，可以使用 `pip` 這個套件管理工具安裝：

```
pip install scikit-learn
```

接著就可以在程式中使用以下程式碼來實現線性回歸：

```
from sklearn.linear_model import LinearRegression

# 建立一個線性回歸模型
model = LinearRegression()

# 訓練模型
# 這裡的訓練資料是用來讓模型學習如何對輸入的數據進行預測
# 其中 X 是輸入資料，y 是預測目標
# 這裡假設我們有一些城市的人口數據和相對應的房價數據，我們希望透過線性回歸來學習人口數量和房價之間的關係
# 這樣我們就可以利用人口數量來預測房價
X = [[1234], [2345], [3456], [4567], [5678]]
y = [123456, 234567, 345678, 456789, 567890]
model.fit(X, y)

# 使用模型進行預測
# 這裡假設我們想要預測一個人口數量為 10000 的城市的房價
X_new = [[10000]]
predicted_price = model.predict(X_new)

# 輸出預測結果
print(predicted_price)
```

上面這段程式碼會輸出一個預測出來的房價。在上面這個例子中，我們透過使用 scikit-learn 中的 LinearRegression 模型來實現了一個簡單的線性回歸。我們先建立一個 LinearRegression 模型，然後利用 fit 方法將模型訓練起來，訓練過程中會根據輸入的訓練數據學習到人口數量和房價之間的關係。接著我們使用 predict 方法來進行預測，就可以得到一個預測出來的房價。

此外，scikit-learn 提供了許多其他的模型，除了線性回歸之外還有像分類、聚類和集成學習等，可以用於解決各種不同的機器學習問題。
