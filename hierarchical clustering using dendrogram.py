
# coding: utf-8

# In[1]:


# needed imports
from matplotlib import pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage
import numpy as np


# In[2]:


# some setting for this notebook to actually show the graphs inline
get_ipython().run_line_magic('matplotlib', 'inline')
np.set_printoptions(precision=5, suppress=True)  # suppress scientific float notation


# In[3]:


# generate two clusters: a with 100 points, b with 50:
np.random.seed(4711)  # for repeatability of this tutorial
a = np.random.multivariate_normal([10, 0], [[3, 1], [1, 4]], size=[100,])
b = np.random.multivariate_normal([0, 20], [[3, 1], [1, 4]], size=[50,])
X = np.concatenate((a, b),)


# In[4]:


# generate the linkage matrix
Z = linkage(X, 'ward')


# In[5]:


# calculate full dendrogram
plt.figure(figsize=(25, 10))
plt.title('Hierarchical Clustering Dendrogram')
plt.xlabel('sample index')
plt.ylabel('distance')
dendrogram(
    Z,
    leaf_rotation=90.,  # rotates the x axis labels
    leaf_font_size=8.,  # font size for the x axis labels
)
plt.show()

