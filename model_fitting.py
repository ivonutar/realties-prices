"""
in: train_data
out: stored trained model
"""


class ModelFitter:
    features = ['price', 'price_note', 'discount', 'original_price', 'price_of_living', 'ID', 'date_of_update',
                'type_of_building', 'condition', 'ownership', 'location', 'floor', 'living_area', 'floor_area',
                'cellar',
                'reconstruction_year', 'water', 'gas', 'waste', 'heat', 'telecomunication', 'electricity', 'commute',
                'communication', 'parking', 'energy_efficiency_1', 'energy_efficiency_2', 'energy_efficiency_3',
                'furniture', 'elevator', 'type_of_flat']

    def __init__(self, train_data):
        self.train_data = train_data
