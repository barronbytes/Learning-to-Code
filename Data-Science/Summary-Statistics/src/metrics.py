class Metrics():
    
    @staticmethod
    def average(data: list) -> float:
        '''
        Calculates average for list of heart rate population numbers.
        Treat list as poplulation numbers.

        Args:
            data (list[int]): Heart rate population numbers.
        Returns:
            float: Average heart rate from heart rate data.
        '''
        sum = 0
        for num in data:
            sum += num
        return round(sum/len(data), 2)

    @staticmethod
    def maximum(data: list) -> float:
        '''
        Finds maximum heart rate from heart rate values.

        Args:
            data (list[int]): Heart rate population numbers.
        Returns:
            float: Maximum heart rate from heart rate data.
        '''
        max = float("-inf")
        for num in data:
            if num > max:
                max = num
        return max

    @staticmethod
    def variance(data: list) -> float:
        '''
        Calculates population variance from heart rate values.

        Args:
            data (list[int]): Heart rate population numbers.
        Returns:
            float: Population variance from heart rate data.
        '''
        mean = Metrics.average(data)
        numerator = 0
        for num in data:
            numerator += (num - mean)**2
        return round(numerator/len(data), 2)

    @staticmethod
    def standard_deviation(data: list) -> float:
        '''
        Calculates population standard deviation from heart rate values.

        Args:
            data (list[int]): Heart rate population numbers.
        Returns:
            float: Population standard deviation heart rate data.
        '''
        sigma = Metrics.variance(data)
        return round(sigma**0.5, 2)
