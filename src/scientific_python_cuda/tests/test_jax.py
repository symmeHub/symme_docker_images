from jax.lib import xla_bridge

print("XLA backend: ", xla_bridge.get_backend().platform)


import jax.numpy as jnp
from jax import grad, jit, vmap
from jax import random


def selu(x, alpha=1.67, lmbda=1.05):
    return lmbda * jnp.where(x > 0, x, alpha * jnp.exp(x) - alpha)


key = random.key(0)
x = random.normal(key, (1000000,))
y = selu(x).block_until_ready()
