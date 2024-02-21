from jax.lib import xla_bridge

print("XLA backend: ", xla_bridge.get_backend().platform)
