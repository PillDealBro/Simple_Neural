from typing import Callable

Vektor = [float]
AktFunk = Callable[[float],float]

def neuron(ulaz: Vektor, tegovi: Vektor, akt_funk: AktFunk) -> float:
    return akt_funk(
        sum(
            z[0] * z[1] for z in zip([1.0]+ulaz,tegovi)
        )
    )
def step(x: float) -> float:
    return 1 if x>0 else 0


NI = [1.5,-1,-1]
ILI =[-0.5,1,1]
I =[-1,1,1]

def XILI_mreza (ulaz:Vektor) -> float:
    return neuron(
        ulaz=[
            neuron(ulaz,NI,step),
            neuron(ulaz, ILI,step)
        ],
        tegovi = I,
        akt_funk=step
    )
ulazi = [
        [0,0],
        [1,0],
        [0,1],
        [1,1],
]
for i in ulazi:
    print(i,XILI_mreza(i))

