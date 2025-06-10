import cudf
import cuml
import numpy as np

print(cudf.Series([1, 2, 3]))


ary = np.array([[1.0, 4.0, 4.0], [2.0, 2.0, 2.0], [5.0, 1.0, 1.0]])

kmeans = cuml.KMeans(n_clusters=2)
kmeans.fit(ary)
print(type(kmeans.labels_))
