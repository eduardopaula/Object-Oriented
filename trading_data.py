import numpy as np
import pandas as pd
from datetime import datetime
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
import yfinance as yf

data = yf.download("PETR4.SA", start="2022-05-01", end="2022-05-31")
print(data)
