import pandas as pd

data_path = './melb_data.csv'

melb_data = pd.read_csv(data_path)
# melb_data.set_index('')
# print(melb_data.describe())
# print(melb_data.head())

# print(melb_data.loc[:20, ['Rooms', 'Price']])

print(melb_data.loc[(melb_data.Suburb == 'Abbotsford') & (melb_data.Price <= 1000000), ['Address', 'Rooms', 'Price', 'YearBuilt']])

# print(melb_data.loc[melb_data.Address.str.contains('Gipps')])