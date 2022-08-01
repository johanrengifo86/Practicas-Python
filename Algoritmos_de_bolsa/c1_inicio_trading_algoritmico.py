import pandas_datareader.data as web # para descargar los datos de precio
import datetime as dt

star = dt.datetime(2021,3,1)
end  = dt.datetime(2022,3,28)

df = web.DataReader('AAPL', 'yahoo',star, end) # identificador divisa, platorma de donde se descargan los datos
