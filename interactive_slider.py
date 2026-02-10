import ipywidgets as widgets
from IPython.display import display
slider = widgets.IntSlider(value=50, min=0, max=100, step=1, description='number:')
out = widgets.Output()
display(slider, out)
def update(change):
    with out:
        out.clear_output()
        print(f'Square: {change["new"] ** 2}')