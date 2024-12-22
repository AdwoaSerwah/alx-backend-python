from typing import Tuple, List


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """
    Zooms into the input tuple by a given factor, returning a list
    of repeated elements.

    Args:
        lst: The tuple of items to zoom in on.
        factor: The number of repetitions for each item.

    Returns:
        A list of zoomed-in items.
    """
    zoomed_in: List = [
        item for item in lst for i in range(factor)
    ]
    return zoomed_in


array = (12, 72, 91)  # Tuple instead of List

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)  # Ensure that the factor is an int, not a float
