import justpy as jp
import pandas
import matplotlib.pyplot as plt 
from pytz import UTC


data = pandas.read_csv("files/reviews.csv" ,parse_dates=['Timestamp'])
share = data.groupby(['Course Name'])['Rating'].count()
plt.pie(share,labels=share.index)

chart_def = """
{

    chart: {
    plotShadow: false,
    type: 'pie'
  },
  title: {
    text: 'Browser market shares in January, 2018'
  },
  tooltip: {
    pointFormat: '{series.name}: <b>{point.percentage:.1f}%</b>'
  },
  accessibility: {
    point: {
      valueSuffix: '%'
    }
  },
  plotOptions: {
    pie: {
      allowPointSelect: true,
      cursor: 'pointer',
      dataLabels: {
        enabled: true,
        format: '<b>{point.name}</b>: {point.percentage:.1f} %'
      }
    }
  },
  series: [{
    name: 'Brands',
    colorByPoint: true,
    data: [{
      name: 'Chrome',
      y: 61.41,
      sliced: true,
      selected: true
    }]
  }]
}
"""


def app():
    wp = jp.QuasarPage()
    

    hc = jp.HighCharts(a=wp, options=chart_def)
    hc.options.xAxis.categories = list(share.index)
    hc_data = [{"name":v1, "y":v2 } for v1,v2 in zip(share.index,share)]
    hc.options.series[0].data = hc_data

    return wp


jp.justpy(app)



