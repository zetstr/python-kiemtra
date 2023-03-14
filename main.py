import random
from hinh import Circle
from hinh import Rectangle
from hinh import Triangle

def generate_input_file(filename, num_rectangles, max_width):
    # Mở file để ghi dữ liệu vào
    with open(filename, 'w') as f:
        # Sinh ngẫu nhiên thông tin cho từng hình chữ nhật
        for i in range(num_rectangles):
            # Sinh ngẫu nhiên chiều rộng và chiều cao của hình chữ nhật
            widthRect = random.randint(1, max_width)
            heightRect = random.randint(1, max_width)
            xRect = random.randint(0, 99 - max_width)
            yRect = random.randint(0, 99 - max_width)
            
             # Sinh ngẫu nhiên chiều rộng và chiều cao của hình tròn
            rCircle = random.randint(1, max_width)
            xCircle = random.randint(0, 99 - max_width)
            yCircle = random.randint(0, 99 - max_width)
            
            # Sinh ngẫu nhiên chiều rộng và chiều cao của hình tam giác
            aTria = random.randint(1, 50 - max_width)
            bTria = random.randint(1, 50 - max_width)
            cTria = random.randint(abs(aTria-bTria)+1, aTria+bTria-1)
            xTria = random.randint(0, 99 - max_width)
            yTria = random.randint(0, 99 - max_width)
            # Ghi thông tin hình chữ nhật vào file
            f.write("#Rect\n")
            f.write(f"{widthRect} {heightRect}\n")
            f.write(f"{xRect} {yRect}\n")
            f.write("#Circle\n")
            f.write(f"{rCircle}\n")
            f.write(f"{xCircle} {yCircle}\n")
            f.write("#Triangle\n")
            f.write(f"{aTria} {bTria} {cTria}\n")
            f.write(f"{xTria} {yTria}\n")
            
def read_input_file(filename):
    maxArea = 0
    maxperimeter = 0
    stringMaxArea = ""
    stringMaxperimeter = ""

    # Mở file để đọc dữ liệu
    with open(filename, 'r') as f:
        for line in f:
            print(line)
            line = line.strip()
            if line == '#Rect':
                # đọc thông tin hình chữ nhật
                width, height = map(int, f.readline().split())
                x, y = map(int, f.readline().split())
                # tính chu vi và diện tích
                rectangle = Rectangle(x, y, width, height);
                area = rectangle.area();
                perimeter = rectangle.perimeter();
                if maxArea < area:
                    maxArea = area
                    stringMaxArea = f"Rectangle at ({x},{y}): area = {maxArea}"
                if maxperimeter < perimeter:
                    maxperimeter = perimeter
                    stringMaxperimeter = f"Rectangle at ({x},{y}): perimeter = {maxperimeter}"
                
            elif line == '#Circle':
                # đọc thông tin hình tròn
                radius = int(f.readline())
                x, y = map(int, f.readline().split())
                # tính chu vi và diện tích
                circle = Circle(x, y, radius);
                area = circle.area();
                perimeter = circle.perimeter();
                if maxArea < area:
                        maxArea = area
                        stringMaxArea = f"Circle at radius = ({radius}): area = {maxArea}"
                perimeter = rectangle.perimeter();
                if maxperimeter < perimeter:
                    maxperimeter = perimeter
                    stringMaxperimeter = f"Circle at radius =({radius}): perimeter = {maxperimeter}"
                
            elif line == '#Triangle':
                # đọc thông tin hình tam giác
                a, b, c = map(int, f.readline().split())
                x, y = map(int, f.readline().split())
                # tính chu vi và diện tích
                triangle = Triangle(a, b, c, x, y);
                area = triangle.area();
                perimeter = triangle.perimeter();   
                if maxArea < area:
                        maxArea = area
                        stringMaxArea = f"Triangle at ({a},{b},{c}): area = {maxArea}"
                perimeter = rectangle.perimeter();
                if maxperimeter < perimeter:
                    maxperimeter = perimeter
                    stringMaxperimeter = f"Triangle at ({a},{b},{c}): perimeter = {maxperimeter}"
    
    print(f"Hình có diện tích lớn nhất là {stringMaxArea}\n")   
    print(f"Hình có chu vi lớn nhất là {stringMaxperimeter}")                    

generate_input_file("input.txt", 20, 20); 
read_input_file("input.txt");           