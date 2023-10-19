# -*- coding: utf-8 -*-
import pandas as pd
import yfinance as yf

class Cac40scraping:
  def __init__(self,cac40Info, start, end):
    """
    Initializes an instance of the CAC40 web scraper.

    Args:
    - cac40Info: a dictionary containing information about the CAC40 index
    - start: a string representing the start date of the data to be scraped
    - end: a string representing the end date of the data to be scraped
    """
    self.info = cac40Info
    self.start = start
    self.end = end

  def dlData(self):
    """
    Downloads the data for the specified time period and returns it as a pandas DataFrame.

    Returns
    -------
    pandas.DataFrame
        A DataFrame containing the stock data for the specified time period.
    """
    d = yf.download(
      list(cac40Info.Ticker),
      start = self.start,
      end = self.end
    )
    return d


if __name__ == '__main__':
  start = '2020-01-01'
  end = '2023-10-13'
  
  cac40Info = pd.read_html('https://en.wikipedia.org/wiki/CAC_40')[4]
  cac40Info.head()

  Scraper = Cac40scraping(cac40Info, start, end)
  data = Scraper.dlData()

  data.to_csv('CAC40_raw_data_' + start + '_to_' + end +'.csv')