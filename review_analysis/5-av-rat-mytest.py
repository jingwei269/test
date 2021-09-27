import justpy as jp

chart_def = """
{
   chart: {
    type: 'areaspline'
  },
  title: {
    text: 'Average fruit consumption during one week'
  },
  legend: {
    enabled: false
  },
  xAxis: {
    categories: [
      'Monday',
      'Tuesday',
      'Wednesday',
      'Thursday',
      'Friday',
      'Saturday',
      'Sunday'
    ],
    plotBands: [{ // visualize the weekend
      from: 4.5,
      to: 6.5,
      color: 'rgba(68, 170, 213, .2)'
    }]
  },
  yAxis: {
    title: {
      text: 'Fruit units'
    }
  },
  series: [{
    name: 'John',
    data: [3, 4, 3, 5, 4, 10, 12]
  },
  {
    name: 'Jane',
    data: [1, 3, 4, 3, 3, 5, 4]
  }]
}

"""


def app():
    wp = jp.QuasarPage()
    hc = jp.HighCharts(a=wp, options=chart_def)


    return wp


jp.justpy(app)
