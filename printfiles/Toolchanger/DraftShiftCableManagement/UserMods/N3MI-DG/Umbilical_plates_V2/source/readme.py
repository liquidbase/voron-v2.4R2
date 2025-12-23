
import os
from config import frames, docks


def main():
    printers = [
        {"name": "voron", "sizes": [250, 300, 350], "dock_widths": [60, 76], "port_types": ["TPU", "THREAD"]},
        {"name": "micron", "sizes": [180], "dock_widths": [60], "port_types": ["TPU"]}
    ]

    port_positions  = ["left", "right", "center", "split"]
    umb_types       = ["spring", "wire"]
    cable_diameters = [3.7, 4, 4.5, 5, 5.5, 6, 6.35]
    parent_path     = os.path.abspath(os.path.join(os.getcwd(), os.pardir))


    readme = "# Umbilical System for StealthChanger\n"
    readme += "![](images/plate_tpu.jpg)\n"
    readme += "## Introduction\n"
    readme += "This umbilical system is ultimately made up of 2 components. The \"Umbilical Plate\" which mounts to the rear panel of your Voron V2 or Micron printer and the \"Umbilical Restraints\" that help tame the umbilical on its way to the tool head.\n"
    readme += "There are various combinations on how these components can be configured, choose wisely.\n"

    readme += "## Umbilical Plate\n"

    readme += "To choose the appropriate umbilical plate for your setup there are 6 things to consider.\n"
    readme += "- The type of printer you have.\n"
    readme += "- The size of the printer.\n"
    readme += "- The amount of tools you want to support.\n"
    readme += "- The type of umbilical you are using, TPU or Threaded.\n"
    readme += "- The width of the docks for the tools you are using.\n"
    readme += "- How the docks are positioned on the printer, Left, Right, Centered or Split.\n"
    readme += "\n"


    readme += "The docks play a big role in this system and based on which tools you are using there can be 2 different nominal dock widths.\n"
    readme += "\n"

    for dock in docks:
        readme += f"###### {dock['width']}mm Nominal Width Docks\n"

        for tn in dock['tools']:
            readme += f"- {tn}\n"

        readme += "\n"

    readme += "From the below tables, select the appropriate umbilical plate configuration for your setup.\n"

    for printer in printers:
        for size in printer['sizes']:
            for port_type in printer['port_types']:
                for dock_width in printer['dock_widths']:
                    
                    readme += "<details name=\"printers\">\n"
                    readme += f"<summary style=\"cursor: pointer;\">{printer['name'].title()} {size}mm {port_type if port_type == 'TPU' else 'Threaded'} {dock_width}mm Wide Dock</summary>\n\n"
                    
                    readme += f"### {printer['name'].title()} {size}mm {port_type if port_type == 'TPU' else 'Threaded'} {dock_width}mm Wide Dock\n"
                    readme += "| Tool Count |"

                    for port_pos in port_positions:
                        readme += f" {port_pos.title()} |"
                    
                    readme += "\n"
                    readme += "|-|-|-|-|-|\n"

                    for tool_count in range(2, frames[size][2 if dock_width == 60 else 3]+1):
                        readme += f"| {tool_count} |"

                        for port_pos in port_positions:
                            fn = f"{printer['name'].title()}_{size}_{dock_width}mm_{tool_count}tools_{port_pos}_{port_type}.svg"
                            if os.path.exists(os.path.join(parent_path, "SVG", fn)):
                                    img_file = f"SVG/{fn}"
                                    readme += f"[<img src=\"{img_file}\">](STL/Plates/{printer['name'].title()}/{size}/{tool_count}%20Tools/{dock_width}mm%20Wide%20Dock/{port_type.title()+'ed' if port_type == 'THREAD' else port_type}/{port_pos.title()}/) |"
                            else:
                                readme += " - |"

                        readme += "\n"

                    readme += "\n</details>\n\n"

            readme += "\n"


    readme += "### Umbilical Plate Installation\n"
    # readme += "![](images/plate_tpu.jpg) ![](images/plate_thread.jpg)\n"
    readme += "If you have one, install the logo insert. The insert is indexed with a couple tabs which need to be inserted first. The bottom will press fit in to place.\n"
    readme += "![](images/insert.jpg)\n"
    readme += "The Voron face plate requires 4 heatset inserts to be installed.\n"
    readme += "![](images/heaset_insert.jpg)\n"
    readme += "Optionally you can add some foam to the mating surface of the face place.\n"
    readme += "![](images/foam.jpg)\n"
    readme += "If you have a SC Barf LED, press fit it in to the outer plate.\n"
    readme += "![](images/sc_barf.jpg)\n"
    readme += "Mate the face plate and outer plate together by putting the face plate over one side of the ports and flexing it over the other. It may feel like the pieces don't fit at first, but with a bit of flex and force the face plate will go over all of the ports.\n"
    readme += "![](images/flex.jpg)\n"
    readme += "Install the plates on to the back panel of the printer. You need to have the panel removed from the frame or at least undo the top clips so that it can be installed from the outside of the printer.\n"
    readme += "![](images/panel.jpg)\n"
    readme += "For the Voron version, secure the back plate to the frame with 2 M5x10 BHCS screws and the outer plate to the face plate with 4 M3x8 SHCS screws.\n"
    readme += "![](images/installed_voron.jpg)\n"
    readme += "The Micron version gets secured to the frame with 2 M3x10 SHCS and the outer plate to the face plate with 2 M2x10 self tapping screws.\n"
    readme += "![](images/installed_micron.jpg)\n"
    readme += "If you are using the threaded back plates the spring steel/piano wire can be secured to the back plate with a M3 heat insert, M3x6 BHCS and M3 washer.\n"
    readme += "![](images/installed_micron.jpg)\n"

    readme += "___\n"

    readme +=  "## Umbilical Restraints\n"
    readme += "There are 2 different ports for the umbilical plates.\n"
    readme += "- TPU - Uses a TPU printed cable relief.\n"
    readme += "- THREADED - Uses either M12x1.5 or PG7 cable glands.\n"
    readme += "\n"
    readme += "There are 2 supported methods of taming the umbilical.\n"
    readme += "- Flat Spring Steel - 0.3x3mm (preferred) [Link](https://www.aliexpress.com/item/1005006731615186.html \"Aliexpress\")\n"
    readme += "- Piano Wire - 1mm\n"
    readme += "\n"
    readme += "### TPU STL Files\n"
    readme += "To download the TPU restraint STL files select one of the links below.\n"

    for umb in umb_types:
        readme += f"###### {'Spring Steel' if umb == 'spring' else 'Piano Wire'}\n"

        for printer in printers:
            for cable in cable_diameters:
                readme += f"- [{printer['name'].title()} {cable}mm cable](STL/TPU%20Umbilical/{printer['name'].title()}/{umb.title()}/{cable}mm%20Cable)\n"

    readme += "\n"
    readme += " Optionally, there is also a TPU plug to block the ports if you do not have all of your tools built. [Link](STL/TPU%20Umbilical/Relief_Plug.stl, \"TPU Plug\")\n"

    readme += "### Installation\n"
    readme += "You need to print 1 Relief, 1 Terminator and enough Clips to keep your umbilical tidy (typically 4-6) per tool.\n"
    readme += "The spring steel/piano wire length should be the diagonal length of your bed + enough material for bending (~25mm). This is a good starting point for Voron printers.\n"

    readme += "#### Spring Steel\n"
    readme += "Spring steel can snap rather easily when bending. Before bending heat the area with a blow torch or lighter to a cherry red and let it cool. This makes the steel more ductile and will bend without snapping.\n"
    readme += "If there is too much friction while feeding the spring steel you can add a dab of dish washing liquid as a lubricant.\n"

    readme += "<br/>Insert the spring steel through the strain relief and out the back. Bend it 180 degrees 12mm from the end.\n![](images/bend1.jpg) ![](images/bend1_1.jpg)\n"
    readme += "<br/>Do a second bend at ~60 degrees 6mm from the end that was bent in the previous step.\n![](images/bend2.jpg) ![](images/bend2_1.jpg)\n"
    readme += "<br/>"
    readme += "![](images/relief.jpg)\n"
    readme += "<br/>Feed the spring steel through all of the clips matching the hole orientation to the strain relief."
    readme += "<br/>"
    readme += "![](images/clips.jpg)\n"
    readme += "<br/>Feed the spring steel through the terminator and do 2 bends at ~30 degrees. Feed the spring steel back until the bend is inside the slot for the spring steel."
    readme += "<br/>"
    readme += "![](images/bend3.jpg) ![](images/terminator.jpg)\n"

    readme += "<br/>"
    readme += "Mount the bowden tube and cable in the strain relief and inset the strain relief into the plate. "
    readme += "This is the time to determine the length you need. With the strain relief inserted in the back plate, run your cable to the tool while it is at the largest travel position for that specific tool. "
    readme += "For instance, T0 would be at MAX_X and MIN_Y, The last tool would be at MIN_X and MIN_Y. "
    readme += "Make sure that at that position there is minimal slack, but there should be some. "
    readme += "You do not want the umbilical to be putting strain on the toolhead. "
    readme += "Then work your way back from the toolhead and insert the bowden tube and cable into the termination print, and then the clips (which can be spaced evenly). "
    readme += "If at any point there is too little or too much slack, pull out the strain relief and adjust it.\n"
    readme += "![](images/umbilical.jpg)\n"
    readme += "<br/>"

    readme += "Optionally you can add some heat shrink (with glue) to keep the clips from moving."
    readme += "<br/>"
    readme += "![](images/shrink.jpg)\n"

    readme += "#### Piano Wire\n"
    readme += "The procedure for piano wire is much the same as spring steel except the wire gets 2 90 degree bends at the Relief and Terminator.\n"
    readme += "![](images/wire_1.jpg)\n"
    readme += "![](images/wire_3.jpg)\n"
    readme += "![](images/wire_2.jpg)\n"

    readme += "___\n"

    readme += "# Credits\n"
    readme += "Developed by [N3MI-DG](https://github.com/N3MI-DG)\n"
    readme += "- [viesturz](https://github.com/viesturz) for the Tapchanger TPU umbilicals, which were the inspiration for this system.\n"
    readme +="- [hartk1213](https://github.com/hartk1213) as the umbilical plate aesthetics were recreated based on his Micron R1 exhaust plate."


    with open("../README.md", "w") as f:
        f.write(readme)


if __name__ == "__main__":
    main()
