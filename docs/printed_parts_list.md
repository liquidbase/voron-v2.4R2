### Voron 2.4 Printed Parts List

List of parts to print for [Voron 2.4](https://github.com/VoronDesign/Voron-2) organized by the [Assembly Manuals](https://github.com/VoronDesign/Voron-2/blob/Voron2.4/Docs/2.4_Assembly_Manual.pdf) order of assembly, allowing for just-in-time printing of parts while building the printer.  Configuration is standard Voron 2.4 (Afterburner Direct Feed, DIN rail mounts) with choices for E3D, Dragon or Mosquito hot ends on a 250mm, 300mm or 350mm frame.  No parts for the drag chain are included, as often these are purchased parts rather than printed.

Names of the sections (such as `Gantry/X_Axis/XY Joints`) match the name of the [STL directory](https://github.com/VoronDesign/Voron-2/tree/Voron2.4/STLs/VORON2.4) that contains the prints.  Note that Voron Design uses filenames starting with `[a]_` at the start of a filename to indicate parts that can be printed in an accent color.

_Credit to [krobertson](https://gist.github.com/krobertson/adfd96689e8b66e7e122705c9ac6bb21) for making a Gist of all parts. This Gist is a modified version of that list, organized by order of assembly, removed parts that don't need printing, identified parts that are optional or specific to a build, and fixed a few incorrect part listings._

--------------------------------------------------------------------------------

### Frame (page 10)

#### [Tools](https://github.com/VoronDesign/Voron-2/tree/Voron2.4/STLs/VORON2.4/Tools)

```
[  ]  [  ]   rail_installation_guide_center_x2.stl
```

--------------------------------------------------------------------------------

### Z Drive Assembly (page 18)

#### [Z_Drive](https://github.com/VoronDesign/Voron-2/tree/Voron2.4/STLs/VORON2.4/Z_Drive)

```
[ x ]  [ x ]   [a]_belt_tensioner_a_x2.stl
[ x ]  [ x ]   [a]_belt_tensioner_b_x2.stl
[ x ]  [ x ]   [a]_z_drive_baseplate_a_x2.stl
[ x ]  [ x ]   [a]_z_drive_baseplate_b_x2.stl
[ x ]  [ x ]   z_drive_main_a_x2.stl
[ x ]  [ x ]   z_drive_main_b_x2.stl
[ x ]  [ x ]   z_drive_retainer_a_x2.stl
[ x ]  [ x ]   z_drive_retainer_b_x2.stl
[ x ]  [ x ]   z_motor_mount_a_x2.stl
[ x ]  [ x ]   z_motor_mount_b_x2.stl
```

#### [Z_Idlers](https://github.com/VoronDesign/Voron-2/tree/Voron2.4/STLs/VORON2.4/Z_Idlers)

_There are two different GT20 20T pully files; only one set of them should be printed_

```
[ x ]  [ x ]  [ x ]  [ x ]   [a]_z_tensioner_x4_9mm.stl
[ x ]  [ x ]               z_tensioner_bracket_a_x2.stl
[ x ]  [ x ]               z_tensioner_bracket_b_x2.stl
```

#### [Z_Endstop](https://github.com/VoronDesign/Voron-2/tree/Voron2.4/STLs/VORON2.4/Z_Endstop)

```
[ x ]   nozzle_probe.stl
```

--------------------------------------------------------------------------------

### AB Drive Modules (page 38)

#### [Gantry/Front_Idlers](https://github.com/VoronDesign/Voron-2/tree/Voron2.4/STLs/VORON2.4/Gantry/Front_Idlers)

```
[ X ]   [a]_tensioner_left.stl
[ X ]   [a]_tensioner_right.stl
[ x ]   front_idler_left_lower.stl
[ x ]   front_idler_left_upper.stl
[ x ]   front_idler_right_lower.stl
[ x ]   front_idler_right_upper.stl
```

#### [Gantry/AB_Drive_Units](https://github.com/VoronDesign/Voron-2/tree/Voron2.4/STLs/VORON2.4/Gantry/AB_Drive_Units)

```
[ x ]         [a]_cable_cover.stl
[ x ]  [ x ]   [a]_z_chain_retainer_bracket_x2.stl
[ x ]         a_drive_frame_lower.stl
[ x ]         a_drive_frame_upper.stl
[ x ]         b_drive_frame_lower.stl
[ x ]         b_drive_frame_upper.stl
```

--------------------------------------------------------------------------------

### Gantry (page 46)

#### [Gantry/X_Axis/XY Joints](https://github.com/VoronDesign/Voron-2/tree/Voron2.4/STLs/VORON2.4/Gantry/X_Axis/XY_Joints)

_Select one endstop_pod_* , and one xy_joint_cable_bridge_* depending on your hardware kit_

```
[  ]   [a]_endstop_pod_hall_effect.stl <- select one vvv (hall effect XY endstops)
[  ]   [a]_endstop_pod_microswitch.stl <- select one ^^^ (microswitch XY endstops)
[  ]   [a]_xy_joint_cable_bridge_generic.stl <= select one vvv (generic drag chain)
[  ]   [a]_xy_joint_cable_bridge_igus.stl    <= select one ^^^ (igus drag chain)
[ x ]   xy_joint_left_lower.stl
[ x ]   xy_joint_left_upper.stl
[ x ]   xy_joint_right_lower.stl
[ x ]   xy_joint_right_upper.stl
```

#### [Gantry](https://github.com/VoronDesign/Voron-2/tree/Voron2.4/STLs/VORON2.4/Gantry)

```
[  ]  [  ]  [  ]  [  ]   [a]_z_belt_clip_lower_x4.stl
[  ]  [  ]  [  ]  [  ]   [a]_z_belt_clip_upper_x4.stl
[  ]                     z_chain_bottom_anchor.stl
[  ]                     z_chain_guide.stl              <-- Not in CAD or documentation
```

--------------------------------------------------------------------------------

### Afterburner (page 58)

#### [Gantry/X_Axis/X Carriage](https://github.com/VoronDesign/Voron-2/tree/Voron2.4/STLs/VORON2.4/Gantry/X_Axis/X_Carriage)

```
[  ]  [  ]   [a]_belt_clamp_x2.stl
[  ]         [a]_blower_housing_front.stl
[  ]         blower_housing_rear.stl
[  ]         hotend_fan_mount.stl
[  ]         probe_retainer_bracket.stl
[  ]         x_carriage_frame_left.stl
[  ]         x_carriage_frame_right.stl
[  ]         x_carriage_pivot_block.stl
```

#### [Gantry/X_Axis/X Carriage/Printheads/E3D V6](https://github.com/VoronDesign/Voron-2/tree/Voron2.4/STLs/VORON2.4/Gantry/X_Axis/X_Carriage/Printheads/E3D_V6)

_Select only one printhead; this is for E3D_

```
[  ]   printhead_front_e3dv6.stl
[  ]   printhead_rear_e3dv6.stl
```

#### [Gantry/X_Axis/X Carriage/Printheads/Slice Mosquito](https://github.com/VoronDesign/Voron-2/tree/Voron2.4/STLs/VORON2.4/Gantry/X_Axis/X_Carriage/Printheads/Slice_Mosquito)

_Select only one printhead; this is for Slice Mosquito_

```
[  ]   printhead_front_mosquito.stl
[  ]   printhead_rear_mosquito.stl
```

#### [Gantry/X_Axis/X Carriage/Printheads/TriangleLab Dragon](https://github.com/VoronDesign/Voron-2/tree/Voron2.4/STLs/VORON2.4/Gantry/X_Axis/X_Carriage/Printheads/TriangleLab_Dragon)

_Select only one printhead; this is for Phaetus Dragon_

```
[  ]   printhead_front_dragon.stl
[  ]   printhead_rear_dragon.stl
```

#### [Gantry/X_Axis/X Carriage/Direct Feed](https://github.com/VoronDesign/Voron-2/tree/Voron2.4/STLs/VORON2.4/Gantry/X_Axis/X_Carriage/Direct_Feed)

_Select the chain anchor (generic or igus) that matches your drag chain choice_ 

```
[  ]   [a]_connector_cover.stl
[  ]   [a]_guidler.stl
[  ]   [a]_latch.stl
[  ]   chain_anchor_generic.stl <-- select one vvv (generic drag chain)
[  ]   chain_anchor_igus.stl    <-- select one ^^^ (igus drag chain)
[  ]   extruder_body.stl
[  ]   extruder_motor_plate.stl
[  ]   latch_shuttle.stl
```

--------------------------------------------------------------------------------

### Belting Z Drive (page 78)

#### [Gantry/Z_Joints](https://github.com/VoronDesign/Voron-2/tree/Voron2.4/STLs/VORON2.4/Gantry/Z_Joints)

```
[  ]  [  ]  [  ]  [  ]   z_joint_lower_x4.stl
[  ]                     z_joint_upper_hall_effect.stl <-- if using hall effect XY
[  ]  [  ]  [  ]  [  ]   z_joint_upper_x4.stl <-- use x3 if using hall effect XY
```

--------------------------------------------------------------------------------

###  LCD Module (page 82)

#### [Electronics_Compartment/LCD_Module](https://github.com/VoronDesign/Voron-2/tree/Voron2.4/STLs/VORON2.4/Electronics_Compartment/LCD_Module)

```
[  ]   [a]_mini12864_case_hinge.stl
[  ]   mini12864_case_front.stl
[  ]   mini12864_case_rear.stl
[  ]   mini12864_spacer.stl
```

--------------------------------------------------------------------------------

### Skirts (page 86)

#### [Electronics_Compartment/Plug_Panel](https://github.com/VoronDesign/Voron-2/tree/Voron2.4/STLs/VORON2.4/Electronics_Compartment/Plug_Panel)

```
[  ]   plug_panel_filtered_mains.stl
```

#### [Skirts](https://github.com/VoronDesign/Voron-2/tree/Voron2.4/STLs/VORON2.4/Skirts)

```
[  ]  [  ]   [a]_60mm_fan_blank_insert_x2.stl
[  ]  [  ]   [a]_belt_guard_a_x2.stl
[  ]  [  ]   [a]_belt_guard_b_x2.stl
[  ]  [  ]   side_fan_support_x2.stl
```

#### [350](https://github.com/VoronDesign/Voron-2/tree/Voron2.4/STLs/VORON2.4/Skirts/350)

_Use these skirts when printing a 350mm frame_

```
[  ]  [  ]   front_rear_skirt_a_350_x2.stl
[  ]  [  ]   front_rear_skirt_b_350_x2.stl
[  ]  [  ]   side_skirt_a_350_x2.stl
[  ]  [  ]   side_skirt_b_350_x2.stl
```

--------------------------------------------------------------------------------

### Panels (page 94)


#### [Panel_Mounting/Front_Doors](https://github.com/VoronDesign/Voron-2/tree/Voron2.4/STLs/VORON2.4/Panel_Mounting/Front_Doors)

```
[  ]  [  ]  [  ]  [  ]   door_hinge_x4.stl
[  ]  [  ]               handle_a_x2.stl
[  ]  [  ]               handle_b_x2.stl
[  ]  [  ]               latch_x2.stl
```

#### [Panel_Mounting](https://github.com/VoronDesign/Voron-2/tree/Voron2.4/STLs/VORON2.4/Panel_Mounting)

```
[  ]  [  ]  [  ]  [  ]                                                   bottom_panel_clip_x4.stl
[  ]  [  ]                                                               bottom_panel_hinge_x2.stl
[  ]  [  ]  [  ]  [  ]  [  ]  [  ]  [  ]  [  ]  [  ]  [  ]  [  ]  [  ]   corner_panel_clip_3mm_x12.stl  <-- 3mm no foam, 6mm w/foam
[  ]  [  ]  [  ]  [  ]                                                   corner_panel_clip_6mm_x4.stl   <-- print either the 3mm or
[  ]  [  ]  [  ]  [  ]  [  ]  [  ]  [  ]  [  ]  [  ]  [  ]  [  ]  [  ]   midspan_panel_clip_3mm_x12.stl <-- the 6mm set 
[  ]  [  ]  [  ]                                                         midspan_panel_clip_6mm_x3.stl  <--  
[  ]  [  ]                                                               z_belt_cover_a_x2.stl
[  ]  [  ]                                                               z_belt_cover_b_x2.stl
```

--------------------------------------------------------------------------------

### Spool Holder (page 102)

#### [Spool_Management](https://github.com/VoronDesign/Voron-2/tree/Voron2.4/STLs/VORON2.4/Spool_Management)

```
[  ]   bowen_retainer.stl
[  ]   spool_holder.stl
```

--------------------------------------------------------------------------------

### Exhaust Filter (page 106)

#### [Exhaust_Filter](https://github.com/VoronDesign/Voron-2/tree/Voron2.4/STLs/VORON2.4/Exhaust_Filter)

```
[  ]         [a]_filter_access_cover.stl
[  ]  [  ]   [a]_exhaust_filter_mount_x2.stl
[  ]         exhaust_filter_grill.stl
[  ]         exhaust_filter_housing.stl
```

--------------------------------------------------------------------------------

### Electronics Mounting (page 112)

#### [Electronics_Compartment/DIN_Brackets](https://github.com/VoronDesign/Voron-2/tree/Voron2.4/STLs/VORON2.4/Electronics_Compartment/DIN_Brackets)

_There are a number of different brackets here depending on your electronics selection._

```
[  ]  [  ]         duet_duex_bracket_x2.stl
[  ]               lrs_psu_bracket_clip.stl
[  ]  [  ]  [  ]   pcb_din_clip_x3.stl
[  ]  [  ]         ramps_bracket_x2.stl
[  ]               raspberrypi_bracket.stl
[  ]               rs25_psu_bracket_clip.stl
[  ]  [  ]         skr_1.3_bracket_x2.stl
[  ]  [  ]         skr_mini_e2_bracket_x2.stl
[  ]  [  ]         skr_mini_e3_bracket_x2.stl
```