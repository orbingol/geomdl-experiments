from geofun import letters
from geomdl.visualization import VisMPL


# Generate letters
i = letters.letter_i()
o = letters.letter_o()
o.translate([15, 10])

# Add letters to a single container
cont = i + o
cont.delta = 0.005

# Create configuration
vis_config = VisMPL.VisConfig(ctrlpts=False, legend=False, axes=False, figure_size=[10, 9])
vis_comp = VisMPL.VisCurve2D(config=vis_config)

# Render letters
cont.vis = vis_comp
cont.render()
