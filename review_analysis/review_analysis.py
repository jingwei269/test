import pandas 

data = pandas.read_csv("files/reviews.csv")

### 打印行列数
print(data.shape)
##  (45000, 4)


## 打印列名
print(data.columns)
##  Index(['Course Name', 'Timestamp', 'Rating', 'Comment'], dtype='object')

## 打印以指定列Group
print(data.hist('Rating'))