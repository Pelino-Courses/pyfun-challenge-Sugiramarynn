def text_format (text:str,prefix ="",suffix="",capitalize=False, max_length:int|None=None):
  """
    Formats the input text by adding a prefix and/or suffix, optionally capitalizing it,
    and enforcing a maximum length constraint.

    Parameters:
        text (str): The main text to format.
        prefix (str, optional): A string to prepend to the text. Defaults to "".
        suffix (str, optional): A string to append to the text. Defaults to "".
        capitalize (bool, optional): If True, the resulting string is converted to uppercase. Defaults to False.
        max_length (int or None, optional): The maximum allowed length for the formatted string. 
         If the result exceeds this length, an error message is returned. Defaults to None.

    Returns:
        str: The formatted string, or an error message if the formatted text exceeds max_length.
        In case of an exception, the exception object is returned.
    """
  try:
   formatted_text = prefix + text+ suffix
   if max_length != None:
    if len(formatted_text) > max_length:
      return "Error:Your text exceeds the maximum length"
   if capitalize:
    return formatted_text.upper()
   else:
    return formatted_text
  except Exception as err:
   print("Error:Invalid Input.")
   return err
   
print(text_format("Python","Mr","Fun",20))
