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
    def variance():
        pass

    @staticmethod
    def standard_deviation():
        pass