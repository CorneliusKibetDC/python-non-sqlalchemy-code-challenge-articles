#!/usr/bin/env python3

def pytest_itemcollected(item):
    """Customize the display of collected test items."""
    # Accessing the parent object and current test function object
    par = getattr(item.parent, 'obj', None)
    node = getattr(item, 'obj', None)

    # Safely retrieving docstrings or falling back to class names
    pref = par.__doc__.strip() if par and par.__doc__ else getattr(par, '__class__', type(par)).__name__
    suf = node.__doc__.strip() if node and node.__doc__ else getattr(node, '__class__', type(node)).__name__

    # Update the node ID if either prefix or suffix is available
    if pref or suf:
        item._nodeid = f"{pref} {suf}"
