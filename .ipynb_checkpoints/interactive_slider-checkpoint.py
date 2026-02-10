import ipywidgets as widgets
from IPython.display import display
slider = widgets.IntSlider(value=50, min=1, max=100,description='Number:')
out = widgets.Output()
def update(change):
    with out:
        out.clear_output()
        print(f'Square: {change["new"] ** 2}')
slider.observe(update, names='value')
display(slider, out)