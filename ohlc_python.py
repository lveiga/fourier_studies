import plotly.plotly as py
import plotly.graph_objs as go
import plotly
import matplotlib.dates as mdates
import numpy as np

plotly.tools.set_credentials_file(username='lveiga', api_key='bFPbRfNhB5buO2FeU2r2')

def bytespdate2num(fmt, encoding='utf-8'):
    strconverter = mdates.strpdate2num(fmt)
    def bytesconverter(b):
        s = b.decode(encoding)
        return strconverter(s)
    return bytesconverter


stock_data = []
source_code = open('files/savio_test.txt', 'r')
for line in source_code:
    split_source = line.split('\n')
    stock_data.append(split_source[0])

date_converter = bytespdate2num("%d/%m/%Y %H:%M")

date, closep, highp, lowp, openp = np.loadtxt(stock_data,
                                              delimiter=',',
                                              unpack=True,
                                              converters={0: date_converter})

layout = go.Layout(
    xaxis = dict(
        rangeslider = dict(
            visible = False
        )
    )
)

trace = go.Ohlc(x=date,
                open=openp,
                high=highp,
                low=lowp,
                close=closep)

data = [trace]
fig = go.Figure(data=data, layout=layout)
py.iplot(data, filename='ohlc_datetime', auto_open=True)

