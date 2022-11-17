def main(n,x):
    """
    Given a argument called 'n' and 'x' type of int , calculate the value of expression and return result:
    Args:
        n: int
        x: int
    Returns:
        result : int
    """
    return pow(x,n)+pow(n,x)
print(main(3,6))
