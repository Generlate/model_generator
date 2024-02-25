import random


VERTICES = [
    [-1, -1, -1],  # Vertex 0
    [1, -1, -1],   # Vertex 1
    [1, 1, -1],    # Vertex 2
    [-1, 1, -1],   # Vertex 3
    [-1, -1, 1],   # Vertex 4
    [1, -1, 1],    # Vertex 5
    [1, 1, 1],     # Vertex 6
    [-1, 1, 1]     # Vertex 7
]

FACES = [
    [0, 1, 2, 3],  # Face 0
    [1, 5, 6, 2],  # Face 1
    [5, 4, 7, 6],  # Face 2
    [4, 0, 3, 7],  # Face 3
    [3, 2, 6, 7],  # Face 4
    [4, 5, 1, 0]   # Face 5
]


def generate_box(width, height, depth, filename):
    with open(filename, 'w') as f:
        f.write('OFF\n')
        f.write(f'{len(VERTICES)} {len(FACES)} 0\n')

        for vertex in VERTICES:
            f.write(f'{vertex[0]:.2f} {vertex[1]:.2f} {vertex[2]:.2f}\n')

        for face in FACES:
            f.write(f'{len(face)} {" ".join(map(str, face))}\n')


def generate_multiple_boxes(num_boxes):
    for i in range(num_boxes):
        width, height, depth = [random.randint(1, 10) for _ in range(3)]
        filename = f'box{i}.off'
        generate_box(width, height, depth, filename)
        print(f'Box {i} with dimensions '
              f'{width:.2f}x{height:.2f}x{depth:.2f} '
              f'exported to {filename}.')


generate_multiple_boxes(100)
