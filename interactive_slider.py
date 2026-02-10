import ipywidgets as widgets
from IPython.display import display
slider = widgets.IntSlider(value=50, min=0, max=100, step=1, description='Value:')
display(slider)
def on_value_change(change):
    print(f'Slider value changed to: {change["new"]}')
slider.observe(on_value_change, names='value')
