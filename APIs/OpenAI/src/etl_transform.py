import os
from openai import OpenAI


class Transform():
    SENTIMENTS = ["negative", "neutral", "positive", "irrelevant"]


    @staticmethod
    def check_errors(raw_data: list[str]) -> bool:
        '''
        Determines if raw sentiment data contains any erroneous data. Egdge cases considered:
        (1) Empty data -> [] -> print error message
        (2) Any non-string data -> ["hello", "world", 1] -> print error message

        Parameters:
            raw_data list(str): Raw data of sentiment comments.
        Returns:
            bool: If erroneous data exists returns True, otherwise False.
        '''
        is_empty = not bool(raw_data)
        is_strings = all(isinstance(data, str) for data in raw_data) if raw_data else False
        is_valid = True
        if is_empty or not is_strings:
            is_valid = False
            print("\nError: JSON file contained no reviews." if is_empty else "\nError: JSON file contained erroneous reviews.")
        return is_valid


    @staticmethod
    def prompt_mapper(raw_data: list[str]) -> list[str]:
        '''
        Handles mapping task of transforming list of product review comments into list of one-word sentiment summaries.

        Parameters:
            raw_data list(str): Raw data of sentiment comments.
        Returns:
            list (str): Collection of one-word summaries for reviews.
        '''
        client = OpenAI(api_key=os.getenv("API_OPENAI"))
        system_context, user_context = Transform.prompt_context(raw_data, len(raw_data))
        completion = client.chat.completions.create(
            model = "gpt-4o-mini",
            messages = [
	            { "role":"system", "content":system_context },
                { "role":"user",  "content":user_context }
            ]
        )
        return completion.choices[0].message.content
        

    @staticmethod
    def prompt_context(raw_data: list[str], raw_count: int) -> tuple[str, str]:
        '''
        Uses parameter and user input to determine system and user context for OpenAI API to use for client.
            - Handles edge case of ensuring that length of input and output match.
            - Does not consider edge cases where user provides erroneous input for `product` variable.

        Parameters:
            raw_data list(str): Raw data of sentiment comments.
            raw_count (int): Number of sentiment comments provided.
        Returns:
            tuple (str, str): System context and user context, respectively.      
        '''
        print("\nWe are about to use the OpenAI API to convert customer product reviews into one-word summaries!")
        reviews = raw_data
        product = input("Before we start, what product was reviewed?: ")
        system_context = f"""
        Use the BIOS acronym to standardize system prompt:
        [1] Background:
            You are a growth analyst. Your manager wants you to complete a project with these criteria:
            - Convert customer product reviews into one-word summaries
            - Use the OpenAI API for sentimental analysis of raw data
            - The user will tell you what product is being reviewed
        [2] Input: list(str)
            Data has already been cleaned and filtered. This is the input data: {reviews}.
            - The data list has a length of {raw_count}, and all items are strings.
            - Each item string represents a user review of this product: {product}
            - It is possible that some items inside the data consist of irrelevant reviews unrelated to the product.
        [3] Output: list(str)
            - We need to analyze {reviews} to create a new list of strings of the same length {raw_count}.
            - All items from the new list can only be from this list of choices: {Transform.SENTIMENTS}.
            - The new list will be created as follows:
              - You will look at each item value inside {reviews}
              - Based upon sentimetnal analysis, you will decide what word from {Transform.SENTIMENTS} represents the prodcut review.
              - The word you choose will be appended to the new list
              - This will ensure that each item in {reviews} gets assigned a sentiment to append to the new list created.
              - The length of the new list must be {raw_count}.
        [4] Sample:
            User context: Review a ring purchased for an individual to wear.
            Parameters: [
                "this ring smells weird, don't recomend",
                "I love this ring, I use it all the time when working out.",
                "It's an ok ring. Some features could be better but for the price its fine.",
                "its a ring",
            ]
            Returns: ["negative", "positive", "neutral", "irrelevant"]
        """
        user_context = f"""
        Client collected reviews about this product: {product}
        Categorize each survey response inside {reviews} with one value inside {Transform.SENTIMENTS}.
        Since the input had a size of {raw_count} I expect the output to have the same size.
        """
        return (system_context, user_context)
    

    @staticmethod
    def validate(sentiments: list[str], count: int) -> list[str]:
        '''
        Method ensures that final output has the proper size. Edge cases considered:
        - Final output is either smaller or larger than intended size.

        Parameters:
            list (str): Collection of unvalidated one-word summaries for reviews. (Potential size error)
        Returns:
            list (str): Collection of validated one-word summaries for reviews.  
        '''
        data = sentiments[:count]
        if len(data) < count:
            data.extend(Transform.SENTIMENTS[-1] for _ in range(count - len(data)))
        return data


    @staticmethod
    def brain(raw_data: list[str]) -> list[str]:
        '''
        Coordinates class methods to complete transformation step of ETL pipeline.

        Parameters:
            raw_data list(str): Raw data of sentiment comments.
        Returns:
            list (str): Collection of one-word summaries for reviews.
        '''
        print(f"JSON data length: {len(raw_data)}")
        is_errors = Transform.check_errors(raw_data)
        sentiments = Transform.prompt_mapper(raw_data) if is_errors else []
        print(f"API response length: {len(sentiments)}")
        return Transform.validate(sentiments, len(raw_data))
