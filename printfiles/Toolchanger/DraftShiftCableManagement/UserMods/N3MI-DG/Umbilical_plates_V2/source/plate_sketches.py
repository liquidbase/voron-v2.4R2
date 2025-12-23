import cadquery as cq

tpu_sk = (
    cq.Sketch()
    .arc((2, 0), 8, 0, 360)
    .arc((-2, 0), 8, 0, 360)
    .arc((0, 2.5), 6.7, 0, 360)
    .hull()
)

tpu_sk_inner = (
    cq.Sketch()
    .arc((2, 0), 10.8/2, 0, 360)
    .arc((-2, 0), 10.8/2, 0, 360)
    .arc((0, 2.5), 8/2, 0, 360)
    .hull()
)

tpu_sk_clear = (
    cq.Sketch()
    .arc((2, 0), 8.7, 0, 360)
    .arc((-2, 0), 8.7, 0, 360)
    .arc((0, 2.5), 7.4, 0, 360)
    .hull()
)

tpu_sk_clear2 = (
    cq.Sketch()
    .arc((5, 0), 8.2, 0, 360)
    .arc((-2, 0), 8.2, 0, 360)
    .arc((0, 2.5), 7.2, 0, 360)
    .hull()
)

tpu_sk_clear3 = (
    cq.Sketch()
    .arc((2, 0), 8.2, 0, 360)
    .arc((-5, 0), 8.2, 0, 360)
    .arc((0, 2.5), 7.2, 0, 360)
    .hull()
)

thread_sk = (
    cq.Sketch()
    .arc((0, 0), 9, 0, 360)
    .arc((0, 11.2), 3.5, 0, 360)
    .hull()
)

thread_sk_inner = (
    cq.Sketch()
    .circle(5.3)
)

thread_sk_clear = (
    cq.Sketch()
    .arc((0, 0), 9+0.7, 0, 360)
    .arc((0, 11.2), 3.5+0.7, 0, 360)
    .hull()
)

thread_sk_clear2 = (
    cq.Sketch()
    .arc((0, 0), 9+0.7, 0, 360)
    .arc((0, 11.2), 3.5+0.7, 0, 360)
    .arc((3, 0), 9.5, 0, 360)
    .arc((3, 11.2), 3.5, 0, 360)
    .hull()
)

thread_sk_clear3 = (
    cq.Sketch()
    .arc((0, 0), 9+0.7, 0, 360)
    .arc((0, 11.2), 3.5+0.7, 0, 360)
    .arc((-3, 0), 9.5, 0, 360)
    .arc((-3, 11.2), 3.5, 0, 360)
    .hull()
)
