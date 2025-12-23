
import os
import time
import zipfile
import cadquery as cq
from config import relief_lengths
from umbilical import makeRelief, makeClip, makeTerminator

printers        = ["voron", "micron"]
umb_types       = ["spring", "wire"]
cable_diameters = [3.7, 4, 4.5, 5, 5.5, 6, 6.35]


def makePath(p, readme=None):
    if not os.path.exists(p):
        print("Creating directory", p)
        os.makedirs(p)

    if readme:
        with open(os.path.join(p, "README.md"), "w") as f:
            f.write(readme)


def main():
    x_offset = 0
    y_offset = 0

    parent_path    = os.path.abspath(os.path.join(os.getcwd(), os.pardir))
    stl_path       = os.path.join(parent_path, "STL")
    umbilical_path = os.path.join(stl_path, "TPU Umbilical")

    makePath(stl_path)
    makePath(umbilical_path)
    
    plug = makeRelief("plug", "voron")
    cq.exporters.export(plug, os.path.join(umbilical_path, "Relief_Plug.stl"), angularTolerance=0.3)

    main_assm = cq.Assembly("UMB")
    main_assm.add(plug, name="Relief_Plug")

    for printer in printers:
        y_offset -= 20
        x_offset = 0

        printer_path = os.path.join(umbilical_path, printer.title())
        makePath(printer_path)

        for umb in umb_types:
            umb_path = os.path.join(printer_path, umb.title())
            makePath(umb_path)

            for cable in cable_diameters:
                cable_path = os.path.join(umb_path, f"{cable}mm Cable")
                makePath(cable_path)

                relief     = makeRelief(umb, printer, cable_dia=cable)
                clip       = makeClip(umb, printer, cable_dia=cable)
                terminator = makeTerminator(umb, printer, cable_dia=cable)

                r_name = f"{printer.title()}_Relief_{umb}_{cable}mm"
                c_name = f"{printer.title()}_Clip_{umb}_{cable}mm"
                t_name = f"{printer.title()}_Terminator_{umb}_{cable}mm"

                print("Generating", f"{r_name}.stl")
                cq.exporters.export(relief, os.path.join(cable_path, f"{r_name}.stl"), angularTolerance=0.3)

                print("Generating", f"{c_name}.stl")
                cq.exporters.export(clip, os.path.join(cable_path, f"{c_name}.stl"), angularTolerance=0.3)

                print("Generating", f"{t_name}.stl")
                cq.exporters.export(terminator, os.path.join(cable_path, f"{t_name}.stl"), angularTolerance=0.3)

                name = f"{printer.title()}_{umb}_{cable}mm"

                assm = cq.Assembly(name=name)

                assm.add(relief.translate((x_offset, y_offset, 0)), name=r_name)
                assm.add(clip.translate((x_offset, y_offset, relief_lengths[printer]+23.5)), name=c_name)
                assm.add(terminator.translate((x_offset, y_offset, relief_lengths[printer]+23.5+15)), name=t_name)

                main_assm.add(assm, name=name)

                x_offset += 20

    # Export the CAD file
    print("Exporting CAD file")
    cad_path = os.path.join(parent_path, "CAD")
    cad_file = os.path.join(cad_path, "All TPU Parts.step")
    cad_zip  = os.path.join(cad_path, "CAD - TPU Parts.zip")

    makePath(cad_path)
    main_assm.save(cad_file)

    # Zip the CAD file to save space
    print("Compressing CAD file")
    zip = zipfile.ZipFile(cad_zip, "w", zipfile.ZIP_DEFLATED)
    zip.write(cad_file, "All TPU Parts.step")
    zip.close()

    print("Removing Uncompressed CAD file")
    os.remove(cad_file)


if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()

    exit(end-start)