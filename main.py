import XlrsReader as xl
from A_star import A_star


if __name__ == '__main__':

    vertices,edges,departure,arrival = xl.GetData()

    print(vertices)
    print(edges)

    A_star(edges,vertices,departure,arrival)