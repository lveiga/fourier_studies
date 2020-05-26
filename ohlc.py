import math
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.ticker as mticker
from mpl_finance import candlestick_ohlc
import numpy as np


def bytedate2num(fmt):
    def converter(b):
        return mdates.strpdate2num(fmt)(b.decode('ascii'))
    return converter


def bytespdate2num(fmt, encoding='utf-8'):
    strconverter = mdates.strpdate2num(fmt)
    def bytesconverter(b):
        s = b.decode(encoding)
        return strconverter(s)
    return bytesconverter


def graph_data(stock):

    fig = plt.figure()
    ax1 = plt.subplot2grid((1, 1), (0, 0))
    #ax2 = plt.subplot2grid((1, 1), (0, 0))
    stock_data = []
    source_code = open('files/savio_test.txt', 'r')
    for line in source_code:
        split_source = line.split('\n')
        stock_data.append(split_source[0])

    date_converter = bytespdate2num("%d/%m/%Y %H:%M")

    date, closep, highp, lowp, openp  = np.loadtxt(stock_data,
                                                                      delimiter=',',
                                                                      unpack=True,
                                                                      converters={0: date_converter})

    x = 0
    y = len(date)
    ohlc = []
    close = []
    media = 0

    while x < y:
        append_me = date[x], openp[x], highp[x], lowp[x], closep[x]
        close.append(closep[x])
        ohlc.append(append_me)
        media += closep[x]
        x += 1

    media = media / 30
    base_values = []
    x = 0

    w, h = 10, 31;
    matrix_sin = [[0 for x in range(w)] for y in range(h)]

    w, h = 10, 31;
    matrix_cos = [[0 for x in range(w)] for y in range(h)]

    w, h = 10, 30;
    matrix_waves = [[0 for x in range(w)] for y in range(h)]

    w, h = 9, 30;
    matrix_sumwaves = [[0 for x in range(w)] for y in range(h)]

    for base in close:
        base_values.append(base - media)
        x += 1

    for colunm_sin in range(10):
        media_sin = 0
        for line_sin in range(30):
            matrix_sin[line_sin][colunm_sin] = base_values[colunm_sin] * math.sin(0.005 * (colunm_sin + 1) * 1.5 * (line_sin + 1))
            media_sin += matrix_sin[line_sin][colunm_sin]

        matrix_sin[30][colunm_sin] = media_sin / 30


    for colunm_cos  in range(10):
        media_cos = 0
        for line_cos in range(30):
            matrix_cos[line_cos][colunm_cos] = base_values[colunm_cos] * math.cos(0.005 * (colunm_cos + 1) * 1.5 * (line_cos + 1))
            media_cos += matrix_cos[line_cos][colunm_cos]

        matrix_cos[30][colunm_cos] = media_cos / 30


    for colunm_wv in range(10):
        for line_wv in range(30):
            matrix_waves[line_wv][colunm_wv] = matrix_sin[30][colunm_wv] * math.sin(0.005 * (colunm_wv + 1) * 1.5 * (line_wv + 1)) + matrix_cos[30][colunm_wv] * math.cos(0.005 * (colunm_cos + 1) * 1.5 * (line_cos + 1))


    for colunm_swv in range(9):
        for line_swv in range(30):
            matrix_sumwaves[line_swv][colunm_swv] = matrix_waves[line_swv][0] + matrix_waves[line_swv][colunm_swv + 1]


    candlestick_ohlc(ax1, ohlc, width=0.0001, colorup='#77d879', colordown='#db3f3f')
    #ax2.plot(matrix_sumwaves)

    for label in ax1.xaxis.get_ticklabels():
        label.set_rotation(45)

    ax1.xaxis.set_major_formatter(mdates.DateFormatter('%d/%m/%Y %H:%M'))
    ax1.xaxis.set_major_locator(mticker.MaxNLocator(10))


    ax1.grid(True)

    ax2 = ax1.twinx()

    #color = 'tab:blue'
    #ax2.set_ylabel('sin', color=color)  # we already handled the x-label with ax1
    #ax2.plot(matrix_sumwaves, color=color)
    #ax2.tick_params(axis='y', labelcolor=color)

    fig.tight_layout()  # otherwise the right y-label is slightly clipped

    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.title(stock)
    plt.legend()
    plt.subplots_adjust(left=0.09, bottom=0.20, right=0.94, top=0.90, wspace=0.2, hspace=0)
    plt.show()


graph_data('TEST')