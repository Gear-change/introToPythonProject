import pip

def install(package):
    """
    Install a package using pip. If pip has a 'main' attribute, use that, 
    otherwise use '_internal.main'. This function is used to ensure that 
    required packages are installed.

    Args:
    package (str): The name of the package to install.
    """
    pip.main(['Install', package])

install('fpdf2')