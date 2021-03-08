import pandas as pd

df = pd.read_csv("./static/assets/data/cities.csv")
with open("./templates/table.html", 'w') as file:
    file.write(df.to_html())
