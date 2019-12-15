import numpy as np
import skimage


# filtro Gaussiano
def matlab_style_gauss2d(shape=(3, 3), sigma=0.5):
    """
    2D gaussian mask - should give the same result as MATLAB's
    fspecial('gaussian',[shape],[sigma])
    """
    m,n = [(ss-1.)/2. for ss in shape]
    y,x = np.ogrid[-m:m+1,-n:n+1]
    h = np.exp( -(x*x + y*y) / (2.*sigma*sigma) )
    h[ h < np.finfo(h.dtype).eps*h.max() ] = 0
    sumh = h.sum()
    if sumh != 0:
        h /= sumh
    return h


a = np.array([[0,  0,  0,  0,  0],
              [0,  0,  0,  0,  0],
              [0,  0,  1,  0,  0],
              [0,  0,  0,  0,  0],
              [0,  0,  0,  0,  0]])

with_noise = skimage.util.random_noise(a, mode='gaussian', seed=None, clip=True) # mode=['gaussian', 'LocalVar', 'Poisson', 's', 'p', ''s&p]

print(with_noise)
