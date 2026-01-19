class Car:
    def __init__(self, comfort_class, clean_mark, brand) -> None:
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(self, distance_from_city_center, clean_power, average_rating, count_of_ratings) -> None:
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, cars: list) -> float:
        income = 0
        for car in cars:
            if car.clean_mark < self.clean_power:
                income += self.calculate_washing_price(car)
                self.wash_single_car(car)
        return round(income, 1)

    def calculate_washing_price(self, car: Car) -> float:
        diff = self.clean_power - car.clean_mark
        price = (car.comfort_class * diff * self.average_rating) / self.distance_from_city_center
        return round(price, 1)

    def wash_single_car(self, car: Car) -> None:
        if self.clean_power > car.clean_mark:
            car.clean_mark = self.clean_power

    def rate_service(self, rating: int) -> None:
        total_score = self.average_rating * self.count_of_ratings
        total_score += rating
        self.count_of_ratings += 1
        self.average_rating = round(total_score / self.count_of_ratings, 1)

bmw = Car(comfort_class=3, clean_mark=3, brand='BMW')
audi = Car(comfort_class=4, clean_mark=9, brand='Audi')
mercedes = Car(comfort_class=7, clean_mark=1, brand='Mercedes')

wash_station = CarWashStation(
    distance_from_city_center=6,
    clean_power=8,
    average_rating=3.9,
    count_of_ratings=11
)

income = wash_station.serve_cars([bmw, audi, mercedes])

print(f"Income: {income}")
print(f"BMW clean mark: {bmw.clean_mark}")
print(f"Audi clean mark: {audi.clean_mark}")
print(f"Mercedes clean mark: {mercedes.clean_mark}")

ford = Car(comfort_class=2, clean_mark=1, brand='Ford')
wash_cost = wash_station.calculate_washing_price(ford)

print(f"Cost for Ford: {wash_cost}")
print(f"Ford clean mark: {ford.clean_mark}")

wash_station.rate_service(5)
print(f"Rating count: {wash_station.count_of_ratings}")
print(f"Avg rating: {wash_station.average_rating}")