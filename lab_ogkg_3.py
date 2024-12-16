import numpy as np
import matplotlib.pyplot as plt

def read_file():
    with open("DS6_2.txt") as f:
        coordinates = f.readlines()
    return coordinates

def int_coordinates(coordinates):
    parsed_coords = []
    for coord in coordinates:
        x, y = map(int, coord.split())
        parsed_coords.append((x, y))
    return parsed_coords

def get_coordinates():
    return int_coordinates(read_file())

def rotation_matrix(angle, rotation_point):
    cos_theta = np.cos(angle)
    sin_theta = np.sin(angle)
    
    px, py = rotation_point
    
    matrix = np.array([
        [cos_theta, -sin_theta, px - px * cos_theta + py * sin_theta],
        [sin_theta, cos_theta, py - px * sin_theta - py * cos_theta],
        [0, 0, 1]
    ])
    
    return matrix

def rotate_point(point, pivot, angle):
    x_due_to_point = point[0] - pivot[0]
    y_due_to_point = point[1] - pivot[1]
    
    cos_theta = np.cos(angle)
    sin_theta = np.sin(angle)
    
    new_x = x_due_to_point * cos_theta - y_due_to_point * sin_theta
    new_y = x_due_to_point * sin_theta + y_due_to_point * cos_theta
    
    return (
        new_x + pivot[0], 
        new_y + pivot[1]
    )

def main():
    original_coords = get_coordinates()
    
    rotation_point = (480, 480)
    
    rotation_angle = 1.22173
    
    transform_matrix = rotation_matrix(rotation_angle, rotation_point)
    
    final_matrix = np.round(transform_matrix, 5)
    
    print("Матриця афінного пертворення:")
    print(np.array2string(final_matrix, formatter={"float_kind":lambda x: f"{x:.5f}"}))
    
    rotated_coords = [rotate_point(point, rotation_point, rotation_angle) 
                      for point in original_coords]
    
    plt.figure(figsize=(10, 10), dpi=96)
        
    new_x = [point[0] for point in rotated_coords]
    new_y = [point[1] for point in rotated_coords]

    plt.scatter(new_x, new_y, color="blue", label="Точки обернуті навколо")    
    plt.scatter(rotation_point[0], rotation_point[1], color="black", s=50, label="Точка обертання")
    
    plt.title("Афінне обертання навколо точки на 70 градусів")
    plt.xlabel("Вісь абсцис(X)")
    plt.ylabel("Вісь ординат(Y)")
    plt.legend()
    plt.grid(True)
    plt.axis("equal")
    plt.xlim(0, 960)
    plt.ylim(0, 960)
    plt.savefig("affine_transformation.jpg", dpi=100)
    plt.show()

if __name__ == "__main__":
    main()
