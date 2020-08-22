import pandas as pd

data_path = './melb_data.csv'

melb_data = pd.read_csv(data_path)

print(melb_data.head(0))
print(melb_data.loc[:10, ['Bedroom2', 'Bathroom', 'Landsize']])

# print(melb_data.Regionname.unique())

# print(melb_data.Suburb.value_counts())
# print(melb_data.Price.mean())

def deviation_column():
    melb_data['price_deviation'] = (melb_data.Price - melb_data.Price.mean())
    # print(melb_data.loc[:10, ['Price', 'price_deviation']])

    def variance_column():
        melb_data['price_variance'] = (melb_data.price_deviation * melb_data.price_deviation)
        print(melb_data.loc[:10, ['Price', 'price_deviation', 'price_variance']])
    variance_column()

# deviation_column()

def landsize_deviation(row):
    row.Landsize = row.Landsize - melb_data.Landsize.mean()
    print(melb_data.loc[:10, ['Landsize']])
    # return row

# melb_data.apply(landsize_deviation, axis='columns')
# print(melb_data.describe())

# print(melb_data.loc[:10, ['Landsize']])

bargain_idx = (melb_data.Landsize / melb_data.Price).idxmax()
bargain_home = melb_data.loc[bargain_idx, ['Suburb', 'Rooms', 'Price', 'Landsize']]
# print(bargain_home)
# print(melb_data.loc[:10, ['Landsize', 'Price']])
# bargain_house = melb_data.

def onebr_homes():
    hse = melb_data.loc[melb_data.Rooms == 1, ['Suburb', 'Price', 'Landsize', 'YearBuilt', 'Regionname']]
    print(hse)

# onebr_homes()

def suburb_occurence():
    suburb_counts = melb_data
    n_charles = melb_data.Address.map(lambda adr: 'Charles' in adr).sum()
    n_abbots = melb_data.Suburb.map(lambda sub: 'Abbots' in sub).sum()
    suburb_counts = pd.Series([n_charles, n_abbots], index=['Charles', 'Abbotsford'])
    print(suburb_counts)

# suburb_occurence()
# print(melb_data.loc[:20, ['Bedroom2']])

# print(melb_data.groupby('Address').Address.count())

# print(melb_data.groupby('Regionname').Regionname.count())
# print(melb_data.groupby(['Regionname', 'Suburb']).apply(lambda df: df.Price.idxmin()))

houses_grouped = melb_data.groupby(['Regionname', 'Suburb']).Price.agg([min])
houses_grouped = houses_grouped.reset_index()

houses_grouped_ordered = houses_grouped.sort_values(by='min')
# print(houses_grouped_ordered)

# print(melb_data.groupby('Suburb').Price.agg([len, min, max]))


# ------------DATATYPES----------------

# print(melb_data[pd.isnull(melb_data.YearBuilt)])
# print(melb_data.YearBuilt.fillna(1800))
# print(melb_data.loc[:20, ['YearBuilt']])
