import numpy as np
import laspy
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D 

def main():
    print('Loading in .laz file . . .')
    las = laspy.read('./data/points.laz')

    print('Filtering to specified zoom . . .')
    mask = (
        (las.x <= 2037080.5) & (las.x >= 2036943) &
        (las.y <= 5721227.069) & (las.y >= 5721174)
    )

    new = laspy.create(point_format=las.header.point_format, file_version=las.header.version)
    new.points = las.points[mask]

    rgb_colours = np.array([[new.red[i] / 65535, new.green[i] / 65535, new.blue[i] / 65535] for i in range(len(new.red))])

    print(f'Variable lengths: x->{len(new.x)}, y->{len(new.y)}, z->{len(new.z)}, rgb->{rgb_colours.shape}')

    print('Plotting . . .')
    # creating figure 
    fig = plt.figure() 
    ax = fig.add_subplot(projection='3d')
    ax.scatter(new.x,new.y,new.z,s=9,c=rgb_colours)
    fig.savefig('3D plot.png')
    plt.show()

if __name__ == '__main__':
    main()