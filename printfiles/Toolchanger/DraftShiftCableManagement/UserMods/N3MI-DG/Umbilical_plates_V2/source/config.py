
th_board_offset = 60   # Y offset from inside of the frame to tool PCB while docked

frames = {
    # Micron
    180: (280, 280, 4, 0, 15), # X, Y Inside length of frame, MAX tool count (standard), MAX tool count (wide), extrusion size
    # Voron
    250: (370, 370, 5, 4, 20),
    300: (420, 420, 6, 4, 20),
    350: (470, 470, 6, 5, 20)
}

docks = [
    {
        "name": "Standard",
        "width": 60,
        "tools": [
            "Anthead",
            "Dragon Burner",
            "Mini StealthBurner",
            "Yavoth"
        ]
    },
    {
        "name": "Wide",
        "width": 76,
        "tools": [
            "A4T",
            "Archetype Blackbird",
            "StealthBurner",
            "XOL"
        ]
    },
]

profiles = {
    "voron": {
        "extrusion_size"       : 20,
        "panel_cutout"         : (147, 42.5),
        "outer_panel_z_offset" : 13.5,
        "outer_panel_overlap_x": 5.8,
        "outer_panel_overlap_z": 10,
        "inner_panel_overlap_x": 9,
        "inner_panel_overlap_z": 5,
        "inner_thick"          : 6,
        "outer_thick"          : 5,
        "panel_fillet"         : 7,
        "hex_size"             : 6.25,
        "hex_gap"              : 1.6,
        "hex_filletl"          : 2,
        "hex_fillets"          : 1,
        "hex_depth"            : 0.6,
        "hex_xz1"              : (40, 11.5),
        "hex_xz2"              : (-20, 11.5),
        "center_offset"        : 30,
        "port_length"          : 12.5,
        "port_angle"           : 56.5,
        "port_z_offset"        : -6,
        "ext_mount_offset"     : 20,
        "ext_hole_size"        : (5.2, 10, 3), # thread dia, head dia, head depth
        "face_hole_size"       : (3.4, 6.2, 4), # thread dia, head dia, head depth
        "face_hole_z_offsets"  : (9, -19),
        "face_thread_insert"   : (4.7, 4.5), # hole dia, hole depth
        "back_centers"         : [None, None, 18.5, 18.5, 18.5, 18.5, 18.5, 18.5],
        "back_centers_logo"    : [None, None, 18, 18, 18, None, 18, None],
        "frame_deadzone"       : 30,
    },

    "micron": {
        "extrusion_size"       : 15,
        "panel_cutout"         : (110, 30),
        "outer_panel_z_offset" : 9,
        "outer_panel_overlap_x": 5.8,
        "outer_panel_overlap_z": 10,
        "inner_panel_overlap_x": 5.8,
        "inner_panel_overlap_z": 5,
        "inner_thick"          : 6,
        "outer_thick"          : 5,
        "panel_fillet"         : 3,
        "hex_size"             : 4,
        "hex_gap"              : 0.8,
        "hex_filletl"          : 1,
        "hex_fillets"          : 0.5,
        "hex_depth"            : 0.4,
        "hex_xz1"              : (30, 10.2),
        "hex_xz2"              : (-20, 10.2),
        "center_offset"        : 30,
        "port_length"          : 7,
        "port_angle"           : 67,
        "port_z_offset"        : -1.9,
        "ext_mount_offset"     : 18,
        "ext_hole_size"        : (3.4, 6.2, 3), # thread dia, head dia, head depth
        "face_hole_size"       : (2.4, 4, 4), # thread dia, head dia, head depth
        "face_hole_z_offsets"  : (6.5, 500),
        "face_thread_insert"   : (1.5, 4.5), # hole dia, hole depth
        "back_centers"         : [None, None, 19, 19, 19, 19, 19, 19],
        "back_centers_logo"    : [None, None, 19, None, 19, None, 18.5, None],
        "frame_deadzone"       : 19.5,
    },
}

spring_steel   = {"voron": (0.3, 3), "micron": (0.2, 4)}
wire_dia       = 1.0
relief_lengths = {"voron": 24, "micron": 18}
ptfe_hole      = 4