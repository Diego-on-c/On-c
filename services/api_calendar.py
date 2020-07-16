class Api:
    def __init__(self, year, month, day, plant):
        self.year = year
        self.month = month
        self.day = day
        self.plant = plant

    def convert_json(self):
        json = [{'day': '25', 'month': '7', 'plant': 'Aloe', 'year': '2020'}]
        return json




