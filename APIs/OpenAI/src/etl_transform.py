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
    def prompt_mapper(raw_data: list[str]) -> str:
        '''
        Handles mapping task of transforming list of product review comments into one-word sentiment summaries.
        - IMPORTANT: The return type is a STRING and not a LIST. OpenAI API respones are strings.

        Parameters:
            raw_data list(str): Raw data of sentiment comments.
        Returns:
            str: Collection of one-word summaries for reviews.
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
        response = completion.choices[0].message.content
        return response        
        

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
        You are a master AI model trained to perform sentimental analysis on business product reviews.

        You are given this information to complete your task:
        [1] Client product: {product}
        [2] List of customer product reviews: {raw_data}
            - Each item inside the list is a string for an individual review
        [3] List length size: {raw_count}
        [4] Sentiment labels the client wants you to use: {Transform.SENTIMENTS}
        
        You will complete your task as follows:
        [1] Create an empty list: []
        [2] Analyze each customer review individually
        [3] Assign each customer review one label from the allowed sentiment values: {Transform.SENTIMENTS}
        [4] Assign the "irrelevant" label for unrelated product reviews
        [5] Return a **valid Python list** of strings of sentiment lables in the **same order** as the input
            The list must have exactly {raw_count} elements, one for each review
            Each element must be one of the labels in {Transform.SENTIMENTS}
        Example Input:
        > ["I like it", "I didn't like it", "I think it's ok", "...", "I'm a male", ...]
        Example Output:
        ["positive", "negative", "neutral", "irrelevant", "irrelevant", ...]
        """
        user_context = f"""
        I'm a growth analyst and my manager gave me this information to conduct sentimental analysis for a client:
        [1] Client product: {product}
        [2] A total of {raw_count} reviews
        [3] Here are the reviews: {raw_data}

        Help me complete my task as follows:
        [1] For each review, to an empty list, append only one sentimental label from these options: {Transform.SENTIMENTS}
        [2] Your output should be a Python list of {raw_count} labels, in the same order as the reviews.
        """
        return (system_context.strip(), user_context.strip())


    @staticmethod
    def brain(raw_data: list[str]) -> list[str]:
        '''
        Coordinates class methods to complete transformation step of ETL pipeline.

        Parameters:
            raw_data list(str): Raw data of sentiment comments.
        Returns:
            list (str): Collection of one-word summaries for reviews.
        '''
        is_errors = Transform.check_errors(raw_data)
        sentiments = Transform.prompt_mapper(raw_data) if is_errors else []
        print(f"Output type: {type(sentiments)}")
        print(f"Commma counts: {sentiments.count(",")}")
        print(sentiments)
        return sentiments
