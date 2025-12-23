

printer      = "voron" # Printer type can be either "voron" or "micron"
printer_size = 350     # Spec of your printer (250, 300, 350) for voron, (180) for micron
tool_count   = 4       # Number of tools desired. 
port_pos     = "split" # How the docks are placed (left, right, center, split)
logo         = True    # Generate logo, must be false for odd number of tools
port_type    = "TPU"   # Version of plate to export (TPU, THREAD)
dock_width   = 60      # Standard dock widths are 60 and 76. Adjust for a custom dock
panel_thick  = 4       # Thickness of rear panel (including foam)

show_frame   = False   # Show frame and docks in CQ-editor

export_step  = False   # Export to a step file
export_frame = False   # Include the frame and dock positions in step file for visual reference

import cadquery as cq
from config import profiles, frames
from plate import makeBodies, makePG7Thread, makePlate

if port_type == "TPU":
    thread_negative = None
else:
    thread_negative = makePG7Thread()

outer_plate, face_plate, logo_insert, hexes = makeBodies(printer=printer, logo=logo, panel_thick=panel_thick)
outer_plate, face_plate, dock_positions     = makePlate(
    outer_plate, 
    face_plate, 
    printer=printer, 
    printer_size=printer_size, 
    tool_count=tool_count, 
    dock_width=dock_width,
    logo=logo, 
    port_pos=port_pos, 
    port_type=port_type,
    thread_negative=thread_negative
)

if show_frame or export_frame:
    frame      = (
        cq.Workplane()
        .box(frames[printer_size][0]+(frames[printer_size][4]*2), frames[printer_size][1]+(frames[printer_size][4]*2), frames[printer_size][4])
        .faces(">Z").workplane().rect(frames[printer_size][0], frames[printer_size][1]).extrude(-frames[printer_size][4], "cut")
        
        .translate((
            0, 
            -frames[printer_size][1]/2-frames[printer_size][4]-panel_thick, 
            (profiles[printer]['panel_cutout'][1] + profiles[printer]['outer_panel_z_offset'] + profiles[printer]['outer_panel_overlap_z'])/2-frames[printer_size][4]/2
        ))
    )

    deadzones = (
        cq.Workplane()
        .pushPoints([
            (
                frames[printer_size][0]/2-(profiles[printer]['frame_deadzone']/2),
                -frames[printer_size][1]-frames[printer_size][4]-panel_thick+5, 
            ),
            (
                -frames[printer_size][0]/2+(profiles[printer]['frame_deadzone']/2),
                 -frames[printer_size][1]-frames[printer_size][4]-panel_thick+5
            )
        ])
        .box(profiles[printer]['frame_deadzone'], 10, 10)
    )

assm = cq.Assembly(name="UMB")
assm.add(face_plate,  name="Face Plate",  color=cq.Color("darkorchid4"))
assm.add(logo_insert, name="Logo Insert", color=cq.Color("GhostWhite"))
assm.add(outer_plate, name="Outer",       color=cq.Color("gray18"))
assm.add(hexes,       name="Hexes",       color=cq.Color("darkorchid4"))

dock_name = "Anthead" if dock_width == 60 else "SB"

try:
    show_object(assm)

    if show_frame:
        show_object(frame)
        show_object(deadzones)

        for i, pos in enumerate(dock_positions):
            show_object(cq.importers.importStep(f"../supplements/{dock_name}.step").rotate((0, 0, 0), (1, 0, 0), 90).translate(pos))

except NameError:
    pass

if export_step:
    if export_frame:
        assm.add(frame,       name="Frame",       color=cq.Color("Gray"))
        assm.add(deadzones,   name="Deadzones",   color=cq.Color("Red"))

        for i, pos in enumerate(dock_positions):
            assm.add(cq.importers.importStep(f"../supplements/{dock_name}.step").rotate((0, 0, 0), (1, 0, 0), 90).translate(pos), name=f"Dock{i}", color=cq.Color("yellow"))

    assm.save(f"../Umbilical Plate{' With Frame' if export_frame else ''}.step")


