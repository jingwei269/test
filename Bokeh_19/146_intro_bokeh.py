from bokeh.core.property.dataspec import ColorSpec
from bokeh.models.annotations import Title
from bokeh.plotting import figure,output_file,show

x = [2,2,4,4,2]
y = [2,7,3,2,2]

output_file("lines.html",title="line plot example")

p = figure(title="simple line example", x_axis_label='x', y_axis_label='y', plot_width=1800, plot_height=800)
#### 折线
p.line(x,y, legend_label="Temp.", line_width=2, color='orange' )

### 圆形
p.circle(x,y, size=[i*5 for i in y ], color='green', alpha=0.5)

show(p)