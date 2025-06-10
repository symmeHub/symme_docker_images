import jax
import jax.numpy as jnp
import matplotlib.pyplot as plt
from diffrax import diffeqsolve, ODETerm, SaveAt, Tsit5
import test


def force(t, args):
    m, c = args
    return m * t + c


def vector_field(t, y, args):
    return -y + force(t, args)


@jax.jit
def solve(y0, args):
    term = ODETerm(vector_field)
    solver = Tsit5()
    t0 = 0
    t1 = 10
    dt0 = 0.1
    saveat = SaveAt(ts=jnp.linspace(t0, t1, 1000))
    sol = diffeqsolve(term, solver, t0, t1, dt0, y0, args=args, saveat=saveat)
    return sol


y0 = 1.0
args = (0.1, 0.02)
sol = solve(y0, args)


def test_diffrax():
    assert True


if __name__ == "__main__":
    pass
