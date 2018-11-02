from geomdl_exp import letters
from geomdl import operations
from geomdl.visualization import VisMPL


# Generate letters
i = letters.letter_i()
o = letters.letter_o()
operations.translate(o, [15, 10], inplace=True)

# Add letters to a single container
cont = i + o
cont.delta = 0.005

# Create configuration
vis_config = VisMPL.VisConfig(ctrlpts=False, legend=False, axes=False, figure_size=[10, 9])
vis_comp = VisMPL.VisCurve2D(config=vis_config)

# Render letters
cont.vis = vis_comp
cont.render()
