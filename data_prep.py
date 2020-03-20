import pandas

flats_df = pandas.read_csv('flat_info-test.csv')


# Update price to only contain numbers
flats_df['price'] = flats_df['price'].str.replace(r'[^0-9]+', '')

# Fill NaNs with median
price_filler = flats_df['price'].median()
flats_df['price'] = flats_df['price'].fillna(price_filler)

# Street - get city part
flats_df['street'] = flats_df['street'].str.split(pat=',').str[-1].str.split(' - ').str[-1]
