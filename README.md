# Stock-csv-exporter

Proof of concept stock CSV exporter (from Yahoo Finance), using the pandas-datareader, datetime, and tkinter libraries

Features:
*Ability to set start and end dates for stock data export

*Ability to queue up multiple stocks into a viewable list

*Automatically capitalizes the stock names for visual clarity

*Add/Remove functionality (with keyboard shortcuts)

*Generates CSV files in the same directory as the .py file, info taken from Yahoo Finance, one file is generated per stock

*"Today's Date" button auto-populated the End Date field with today's date

*GUI interface made with tkinter makes it easy to use

Room to grow:
*Add bug-catchers (try/except statements to stop datareader issues, such as end date being before start date, stock misspellings, etc)

*Add other data sources
