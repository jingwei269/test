from bokeh.core.property.dataspec import ColorSpec
from bokeh.models.annotations import Title
from bokeh.plotting import figure,output_file,show
import pandas

# df1 = pandas.read_csv("files/bachelors.csv")
df1 = pandas.read_csv("http://pythonhow.com/data/bachelors.csv")


years = df1["Year"]
Arg = df1["Engineering"]


output_file("files/lines.html",title="line plot example")

p = figure(title="simple line example", x_axis_label='x', y_axis_label='y', plot_width=800, plot_height=400)
#### 折线
p.line(years,Arg, legend_label="Temp.", line_width=2, color='orange' )

show(p)