class Car:
    def __init__(self,model,year,color,for_sale):
        self.model = model
        self.year = year
        self.color = color
        self.for_sale = for_sale
    def display_info(self):
        print(f"Model: {self.model}, Year: {self.year}, Color: {self.color}, For Sale: {self.for_sale}")
