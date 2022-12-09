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

