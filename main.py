import selenium


import cv2

def sum(a,b):
    """[summary]

    Args:
        a ([int]): [a]
        b ([int]): [b]

    Returns:
        [int]: [sum of a and b]
    """
    return a+b
def main():
    print("Hello world")
    # added comment
    cap = cv2.imread("img.jpg")

    cap = cv2.resize(cap, (1200, 720))
    cv2.circle(cap, (20, 20), 20, (255, 0, 255), 3)

    cv2.imshow("Image", cap)
    cv2.waitKey()

    print("Hello WOrld")

if __name__ == "__main__":
    main()
