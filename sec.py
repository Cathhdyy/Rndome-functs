def sec(a):
    min=a//60
    secc=a-(60*min)
    hr=min//60
    min=min-(60*hr)
    day=hr//24
    hr=hr-(24*day)
    r=f"{day} D : {hr} H : {min} m : {secc} s"
    return r
