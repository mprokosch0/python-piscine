from load_image import ft_load
import numpy as np
import matplotlib.pyplot as plt


def main():
    try:
        pxArr = ft_load("../animal.jpeg")
        if not len(pxArr):
            return
        print(pxArr[0:4:4])

        # slicing numpy array to apply 'zoom'
        pxArr = pxArr[100:500, 450:850]
        pxArr = ((0.21256 * pxArr[:, :, 0:1] + 0.7174 * pxArr[:, :, 1:2]
                  + 0.0721 * pxArr[:, :, 2:3])).astype(int)
        print("New shape after slicing: ", pxArr.shape, "or",
              (pxArr.shape[0], pxArr.shape[1]))
        np.set_printoptions(threshold=100, edgeitems=3)
        print(pxArr[0:1])

        plt.imshow(pxArr, cmap='gray')
        plt.show()

    except KeyboardInterrupt:
        print(f"{KeyboardInterrupt.__name__}")


if __name__ == "__main__":
    main()
