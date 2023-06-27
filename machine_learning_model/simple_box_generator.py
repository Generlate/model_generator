import random
import os

def generate_box(width, height, depth, filename):
    vertices = [
        [-width/2, -height/2, -depth/2],  # Vertex 0
        [width/2, -height/2, -depth/2],   # Vertex 1
        [width/2, height/2, -depth/2],    # Vertex 2
        [-width/2, height/2, -depth/2],   # Vertex 3
        [-width/2, -height/2, depth/2],   # Vertex 4
        [width/2, -height/2, depth/2],    # Vertex 5
        [width/2, height/2, depth/2],     # Vertex 6
        [-width/2, height/2, depth/2]     # Vertex 7
    ]

    faces = [
        [0, 1, 2, 3],  # Face 0
        [1, 5, 6, 2],  # Face 1
        [5, 4, 7, 6],  # Face 2
        [4, 0, 3, 7],  # Face 3
        [3, 2, 6, 7],  # Face 4
        [4, 5, 1, 0]   # Face 5
    ]

    with open(filename, 'w') as f:
        f.write('OFF\n')
        f.write(f'{len(vertices)} {len(faces)} 0\n')

        for vertex in vertices:
            f.write(f'{vertex[0]} {vertex[1]} {vertex[2]}\n')

        for face in faces:
            f.write(f'{len(face)} {" ".join(map(str, face))}\n')


def generate_multiple_boxes(num_boxes):
    for i in range(num_boxes):
        width = random.uniform(1, 10)  # Random width between 1 and 10
        height = random.uniform(1, 10)  # Random height between 1 and 10
        depth = random.uniform(1, 10)  # Random depth between 1 and 10
        filename = f'box{i}.off'
        generate_box(width, height, depth, filename)
        print(f'Box {i} with dimensions {width:.2f}x{height:.2f}x{depth:.2f} exported to {filename}.')


# Example usage
generate_multiple_boxes(1000)
