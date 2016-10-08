__author__ = 'jonathanmares'

# rotates an image 90 degrees
# requires an image represented as a list of lists, where each list is a row in the
# matrix
def rotate_image(img):
    nrows = len(img)
    ncols = len(img[0])
    new_img = []
    for col in range(0,ncols):
        new_row = []
        for row in range(nrows-1,-1,-1):
            new_row.append(img[row][col])
        new_img.append(new_row)
    return new_img

def main():
    img = [[1,2,3],[4,5,6],[7,8,9]]
    img2 = [[5]]
    print(rotate_image(img2))

main()
