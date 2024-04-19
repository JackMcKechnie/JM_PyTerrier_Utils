# JM_PyTerrier_Utils
Commonly used PyTerrier utility functions.

__________________________________________

``plot_per_query(df, save_path = None, quality = "medium"):``

Takes a pt.Experiment() DataFrame where perquery = True and plots the results in a bar chart. One subplot per measure. If ``save_path``   is given then then the plot is saved as a .png in this location. DPI can be controlled with ``quality``. Options are ``low``, (100 DPI) ``medium`` (500 DPI), and ``high`` (1080 DPI). 
