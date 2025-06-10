from jax.extend.backend import get_backend

print("XLA backend: ", get_backend().platform)


import jax.numpy as jnp
from jax import grad, jit, vmap


nx, xy = 3, 5


def calc_sfuff(x, y, do_it=True):
    return jnp.where(do_it, x + y, 0.0)


vcalc_sfuff = vmap(calc_sfuff)
vcalc_sfuff2 = jit(vmap(vcalc_sfuff))

x = jnp.linspace(0, 1, nx)
y = jnp.linspace(0, 1, xy)
X, Y = jnp.meshgrid(x, y)
Do_it = jnp.where((X > 0.5) & (Y > 0.5), True, False)


Z = vcalc_sfuff2(X, Y, do_it=Do_it)
