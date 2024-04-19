def plot_per_query(df, save_path = None, quality = "medium"):
    
    import pandas as pd
    import matplotlib.pyplot as plt
    import seaborn as sns
    import numpy as np
    
    quality_map = {"high" : 1080, "medium" : 500, "low" : 100}
    dpi_val = quality_map[quality]

    # Get unique measures
    measures = df['measure'].unique()

    # Calculate the number of rows and columns for the subplot grid
    num_plots = len(measures)
    num_cols = int(np.ceil(np.sqrt(num_plots)))
    num_rows = int(np.ceil(num_plots / num_cols))

    # Create subplots for each measure
    fig, axes = plt.subplots(num_rows, num_cols, figsize=(10*num_cols, 6*num_rows), sharex=True, dpi = dpi_val)

    # Flatten the axes if the grid is not 2D
    if num_rows == 1 or num_cols == 1:
        axes = axes.reshape(-1)

    # Loop through each measure and create a subplot
    for i, measure in enumerate(measures):
        # Calculate the subplot index based on the grid shape
        if num_rows == 1 or num_cols == 1:
            ax_index = i
        else:
            ax_row = i // num_cols
            ax_col = i % num_cols
            ax_index = (ax_row, ax_col)

        # Filter data for the current measure
        measure_data = df[df['measure'] == measure]

        # Get unique queries
        queries = measure_data['qid'].unique()

        # Initialize bar positions
        num_systems = len(measure_data['name'].unique())
        bar_width = 0.2
        bar_positions = np.arange(len(queries)) * (num_systems + 1) * bar_width

        # Plot bars for each system
        for j, (name, group) in enumerate(measure_data.groupby('name')):
            values = group['value'].tolist()
            if num_rows == 1 or num_cols == 1:
                axes[ax_index].bar(bar_positions + j * bar_width, values, width=bar_width, alpha=0.7, label=name)
            else:
                axes[ax_row, ax_col].bar(bar_positions + j * bar_width, values, width=bar_width, alpha=0.7, label=name)

        # Set labels and title for the subplot
        if num_rows == 1 or num_cols == 1:
            axes[ax_index].set_ylabel(measure)
            axes[ax_index].set_title(measure)
            axes[ax_index].set_xticks(bar_positions + (num_systems / 2) * bar_width)
            axes[ax_index].set_xticklabels(queries)
            axes[ax_index].legend()
        else:
            axes[ax_row, ax_col].set_ylabel(measure)
            axes[ax_row, ax_col].set_title(measure)
            axes[ax_row, ax_col].set_xticks(bar_positions + (num_systems / 2) * bar_width)
            axes[ax_row, ax_col].set_xticklabels(queries)
            axes[ax_row, ax_col].legend()

    # Set common x-label for all subplots
    plt.xlabel('QID')

    # Adjust layout
    plt.tight_layout()
    
    if save_path:
        plt.savefig(f"{save_path}.png", dpi = dpi_val)

    return plt.show()
