class Metrics():
    
    @staticmethod
    def average(data: list) -> float:
        sum = 0
        for num in data:
            sum += num
        return round(sum/len(data), 2)

    @staticmethod
    def maximum(data: list) -> float:
        max = float("-inf")
        for num in data:
            if num > max:
                max = num
        return max

    @staticmethod
    def variance(data: list) -> float:
        mean = Metrics.average(data)
        numerator = 0
        for num in data:
            numerator += (num - mean)**2
        return round(numerator/len(data), 2)

    @staticmethod
    def standard_deviation(data: list) -> float:
        sigma = Metrics.variance(data)
        return round(sigma**0.5, 2)
