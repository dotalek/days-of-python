"""
Prints a given list of items separated by commas
"""

def commaString(items: list) -> str:
    """
    Returns a list of items separated by a comma and space, with 'and'
    insterted before the last item.
    """
    convertedStr: str = ""
    for i, item in enumerate(items):
        itemStr: str = item + ", "
        if i == len(items) - 1:
            itemStr: str = "and " + item
        convertedStr += itemStr
    return convertedStr

myStuff = ['spam', 'bacon', 'eggs']
print(commaString(myStuff))
