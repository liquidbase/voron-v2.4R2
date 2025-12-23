import cadquery as cq
from config import relief_lengths, spring_steel, wire_dia, ptfe_hole


def makeRelief(relief_type, printer, cable_dia=6.35):
    relief_length = relief_lengths[printer]

    sk_relief = (
        cq.Sketch()
        .arc((2, 0), 10.8/2, 0, 360)
        .arc((-2, 0), 10.8/2, 0, 360)
        .arc((0, 2.5), 8/2, 0, 360)
        .hull()
    )

    sk_relief_stop = (
        cq.Sketch()
        .arc((2, 0), (10.8/2+1.6), 0, 360)
        .arc((-2, 0), (10.8/2)+1.6, 0, 360)
        .arc((0, 2.5), (8/2)+1.6, 0, 360)
        .hull()
    )

    relief = (
        cq.Workplane().placeSketch(sk_relief).extrude(11.5)
        .faces(">Z").workplane().placeSketch(sk_relief_stop).extrude(4)
    )

    if relief_type != "plug":
        relief = (
            relief
            .faces(">Z").workplane().placeSketch(sk_relief).extrude(relief_length)
            .faces(">Z").chamfer(relief_length-0.01, ((1 if printer == "voron" else 0.5)/cable_dia)*3.7)
            .faces("<Z").workplane().pushPoints([(3, 0)]).hole(cable_dia)
            .faces("<Z").workplane().pushPoints([(-3, 0)]).hole(ptfe_hole)
            
        )

    if relief_type == "spring":
        relief = (
            relief
            .faces("<Z").workplane(offset=-1).pushPoints([(0, -4.1)]).rect(spring_steel[printer][1]+0.5, spring_steel[printer][0]+0.3).extrude(-100, "cut")
            .faces("<Z").chamfer(0.3)
            .faces("<Z[-3]").chamfer(0.5)
            .faces(">Z").chamfer(0.2)
            .faces(">Z[-2]").fillet(0.799)
            .faces("<Z").workplane(offset=-1).pushPoints([(0, -4.2-2.5)]).rect(spring_steel[printer][1]+0.5, 5).extrude(-10.5, "cut")
            .faces("<Z").workplane().pushPoints([(0, -7)]).rect(spring_steel[printer][1]+0.5, 3).extrude(-1, "cut")
            .faces("<Z[-3]").edges(cq.NearestToPointSelector((0, 0, 0))).chamfer(1)

            .faces("<Z[-2]").workplane(centerOption="CenterOfBoundBox").rect(spring_steel[printer][1]+0.5, 2).extrude(1, "cut")
            
            .cut(
                cq.Workplane().box(20, 5, 5)
                .rotate((0, 0, 0), (1, 0, 0), 45)
                .translate((0, 10, 11.5))
            )
        )
    
    elif relief_type == "wire":
        relief = (
            relief
            .faces("<Z").workplane().pushPoints([(0, -4.2)]).hole(wire_dia+0.3)
            .faces("<Y[-2]").workplane().rect(1.2, 10).extrude(-1.2, "cut")
            .faces("<Z").chamfer(0.3)
            .faces("<Z[-3]").chamfer(0.5)
            .faces(">Z").fillet(0.2)
            .faces(">Z[-2]").fillet(0.799)
        )

    elif relief_type == "plug":
        relief = (
            relief
            .faces("<Z").chamfer(0.3)
            .faces("<Z[-3]").chamfer(0.5)
            .faces(">Z").fillet(0.2)
            .faces(">Z[-2]").fillet(0.799)
        )


    if relief_type in ["wire", "plug"]:
        relief = (
            relief
            .union(
                cq.Workplane("YZ")
                .polygon(6, 10, circumscribed=True).extrude(4.5)
                .fillet(1)
                .translate((-2.25, 1.8, 11.5-6))
                .cut(cq.Workplane().placeSketch(sk_relief).extrude(100).translate((0, 0, -20)))
            )
        )

    if relief_type != "plug":
        relief = (
            relief
            .cut(cq.Workplane().transformed(rotate=(0, 0, 45), offset=(6, 3, 0)).box(10, 1, 100))
            .cut(cq.Workplane().transformed(rotate=(0, 0, -45), offset=(-6, 3, 0)).box(10, 1, 100))
        )

    return(relief)


def makeClip(clip_type, printer, cable_dia=6.35):
    sk_clip = (
        cq.Sketch()
        .arc((3, 0), (4.8/6.35)*cable_dia, 0, 360)
        .arc((-3, 0), (4.8/6.35)*cable_dia, 0, 360)
        .arc((0, 2), (4.8/6.35)*cable_dia, 0, 360)
        .hull()
    )

    clip = (
        cq.Workplane().placeSketch(sk_clip).extrude(8)
        .faces("<Z").workplane().pushPoints([(3, 0)]).hole(cable_dia)
        .faces("<Z").workplane().pushPoints([(-3, 0)]).hole(ptfe_hole)
    )

    if clip_type == "spring":
        clip = (
            clip
            .faces("<Z").workplane().pushPoints([(0, -(4.2/6.35)*cable_dia-0.5)]).rect(spring_steel[printer][1]+0.6, spring_steel[printer][0]+0.3).cutThruAll()
            .faces("<Z").workplane().pushPoints([(0, -(4.2/6.35)*cable_dia-0.5-spring_steel[printer][0]*2)]).circle(spring_steel[printer][0]+0.3).extrude(-8)
        )
    
    else:
        clip = (
            clip
            .faces("<Z").workplane().pushPoints([(0, -(4.2/6.35)*cable_dia-0.5)]).hole(wire_dia+0.3)
        )

    clip = (
        clip
        .faces(">Z").workplane().pushPoints([(3+((4.8/6.35)*cable_dia), 0), (-(3+((4.8/6.35)*cable_dia)), 0)]).rect(((4.8/6.35)*cable_dia)*2, 0.4).extrude(-8, "cut")
        .faces(">Z").workplane().pushPoints([(3+((4.8/6.35)*cable_dia), 0), (-(3+((4.8/6.35)*cable_dia)), 0)]).polygon(4, 1.2).extrude(-8, "cut")
        .faces("<Z or >Z").chamfer(0.2)
    )

    return(clip)


def makeTerminator(terminator_type, printer, cable_dia=6.35):
    length = 26 if printer == "voron" else 16

    sk_clip = (
        cq.Sketch()
        .arc((3, 0), (4.8/6.35)*cable_dia, 0, 360)
        .arc((-3, 0), (4.8/6.35)*cable_dia, 0, 360)
        .arc((0, 2), (4.8/6.35)*cable_dia, 0, 360)
        .hull()
    )

    terminator = (
        cq.Workplane().placeSketch(sk_clip).extrude(length)
        .faces("<Z").workplane().pushPoints([(3, 0)]).hole(cable_dia)
        .faces("<Z").workplane().pushPoints([(-3, 0)]).hole(ptfe_hole)
        .faces(">Z").workplane().pushPoints([(3+((4.8/6.35)*cable_dia), 0), (-(3+((4.8/6.35)*cable_dia)), 0)]).rect(((4.8/6.35)*cable_dia)*2, 0.4).extrude(-length, "cut")
        .faces(">Z").workplane().pushPoints([(3+((4.8/6.35)*cable_dia), 0), (-(3+((4.8/6.35)*cable_dia)), 0)]).polygon(4, 1.2).extrude(-length, "cut")
    )

    if terminator_type == "spring":
        terminator = (
            terminator
            .faces("<Z").workplane().pushPoints([(0, -(4.2/6.35)*cable_dia-0.5)]).rect(spring_steel[printer][1]+0.6, spring_steel[printer][0]+0.3).extrude(-length+1, "cut")
            .faces(">Z").workplane(offset=-1).pushPoints([(0, (4.2/6.35)*cable_dia)]).rect(spring_steel[printer][1]+0.6, 0.5).extrude(-1, "cut")
            .faces("<Z").workplane().pushPoints([(0, -(4.2/6.35)*cable_dia-0.5-spring_steel[printer][0]*2)]).circle(spring_steel[printer][0]+0.3).extrude(-length/2)
            .faces(">Z").workplane().pushPoints([(0, (4.2/6.35)*cable_dia+3)]).rect(20, 5).extrude(-length/2, "cut")
            .faces(">Z[-4]").edges(">Y").chamfer(1, 0.4)
        )
    
    else:
        terminator = (
            terminator
            .faces("<Z").workplane().pushPoints([(0, -(4.2/6.35)*cable_dia-0.5)]).hole(wire_dia+0.3, length*0.75)


            .faces(">Z").workplane().pushPoints([(0, (4.2/6.35)*cable_dia+5)]).rect(20, 10).extrude(-length/2, "cut")
            .faces(">Z[-3]").edges(">Y").chamfer(1, 0.4)
            .faces("<Y").workplane(centerOption="CenterOfBoundBox").rect(1.5, length/3).extrude(-1.5, "cut")
            .faces(">Z").workplane(offset=-length/2+length/3).pushPoints([(0, 3)]).rect(1.5, 20).extrude(-length/3, "cut")
            .faces(">Z[-2]").edges(">Y").chamfer(1, 2)
        )

    terminator = (
        terminator
        .faces("<Z or >Z").chamfer(0.2)
    )

    return(terminator)
