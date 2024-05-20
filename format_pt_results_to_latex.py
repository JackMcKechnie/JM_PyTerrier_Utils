def format_pt_results_to_latex(results_df, table_star = False, caption = None):
    
    bolded_df = results_df.copy()
    for column in results_df.columns[1:]:
        max_value = results_df[column].max()
        bolded_df[column] = results_df[column].apply(lambda x: f"\\textbf{{{round(x, 4)}}}" if x == max_value else round(x,4))
    
    column_format = 'l' + 'c' * (len(bolded_df.columns) - 1)
    
    # Convert to LaTeX
    latex = bolded_df.to_latex(index=False, escape=False, column_format=column_format)
    
    if caption:
        latex = f"\\caption{{{caption}}}\n" + latex
        
    if table_star:
        latex = (
            "\\begin{table*}[tb]\n\\centering\n" + 
            latex + 
            "\\end{table*}\n"
        )
    
    print(latex)
