from bokeh.plotting import figure, output_file, show


plot = figure(plot_width=900, plot_height=900)
plot.vbar(x=[1, 2, 3], width=0.5, bottom=0, top=[1,2,3], color="#CAB2D6")

show(plot)