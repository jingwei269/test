from bokeh.core.property.dataspec import ColorSpec
from bokeh.models.annotations import Title
from bokeh.plotting import figure,output_file,show
import pandas

df1 = pandas.read_csv("files/data.csv")
print(df1)
x = list(df1['x'])
y = list(df1['y'])


output_file("files/lines.html",title="line plot example")

p = figure(title="simple line example", x_axis_label='x', y_axis_label='y', plot_width=800, plot_height=400)
#### 折线
p.line(x,y, legend_label="Temp.", line_width=2, color='orange' )

### 圆形
p.circle(x,y, size=[i*5 for i in y ], color='green', alpha=0.5)

### 三角形
p.triangle(x,y , size=[i*5 for i in y ], color='red', alpha=0.5)


show(p)