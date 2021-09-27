import justpy as jp 
import pandas
from datetime import datetime
from pandas.tseries.offsets import Day
from pytz import UTC
import matplotlib.pyplot as plt 

data = pandas.read_csv("files/reviews.csv", parse_dates=['Timestamp'])
data['Date'] = data['Timestamp'].dt.date
month_average = data.groupby(['Date']).mean()


chart_def = """
{
    chart: {
    type: 'spline',
    inverted: false
  },
  title: {
    text: 'Atmosphere Temperature by Altitude'
  },
  subtitle: {
    text: 'According to the Standard Atmosphere Model'
  },
  xAxis: {
    reversed: false,
    title: {
      enabled: true,
      text: 'Date'
    },
    labels: {
      format: '{value} '
    },
    accessibility: {
      rangeDescription: 'Range: 0 to 80 km.'
    },
    maxPadding: 0.05,
    showLastLabel: true
  },
  yAxis: {
    title: {
      text: 'Average Rating'
    },
    labels: {
      format: '{value}°'
    },
    accessibility: {
      rangeDescription: 'Range: -90°C to 20°C.'
    },
    lineWidth: 2
  },
  legend: {
    enabled: false
  },
  tooltip: {
    headerFormat: '<b>{series.name}</b><br/>',
    pointFormat: '{point.x} : {point.y} '
  },
  plotOptions: {
    spline: {
      marker: {
        enable: false
      }
    }
  },
  series: [{name: 'Average Rating'}]
}    
"""


def app():
    wp = jp.QuasarPage()
    h1 = jp.QDiv(a=wp, text="Analysis of Course Reviews", classes="text-h1 text-right text-bold q-pa-sm")
    p1 = jp.QDiv(a=wp, text="There graphs represent course reviedw analysis", classes='q-mt-xl')

    hc = jp.HighCharts(a=wp, options=chart_def)
    hc.options.title.text = "Average Rating by Day"
    
    hc.options.xAxis.categories = list(month_average.index)
    hc.options.series[0].data =  list(month_average['Rating'])
    
    
    return wp 

jp.justpy(app)