from load_image import ft_load
import matplotlib.pyplot as plt
import numpy as np


def main():
    try:
        pxArr = ft_load("../animal.jpeg")
        if not len(pxArr):
            return

        pxArr
        pxArr = pxArr[100:500, 450:850]
        pxArr = ((0.21256 * pxArr[:, :, 0:1] + 0.7174 * pxArr[:, :, 1:2] +
                  0.0721 * pxArr[:, :, 2:3])).astype(int)

        print("Shape of the image is: ", pxArr.shape, "or",
              (pxArr.shape[0], pxArr.shape[1]))
        np.set_printoptions(threshold=100, edgeitems=3)
        print(pxArr[0:1])

        pxArr = np.array([np.array([row[y] for row in pxArr])
                          for y in range(pxArr.shape[1])])

        print("New shape after Transpose: ",
              (pxArr.shape[0], pxArr.shape[1]))
        print(pxArr[0:1])

        plt.imshow(pxArr, cmap='gray')
        plt.show()

    except KeyboardInterrupt:
        print(f"{KeyboardInterrupt.__name__}")


if __name__ == "__main__":
    main()
