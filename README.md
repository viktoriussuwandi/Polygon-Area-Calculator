# Polygon Area Calculator
#### Solution running on : https://replit.com/@ViktoriusSuwand/Polygon-Area-Calculator

This is tthe complete Polygon Area Calculator project. Instructions for building your project can be found at
https://www.freecodecamp.org/learn/scientific-computing-with-python/scientific-computing-with-python-projects/polygon-area-calculator

### Some of additional features :
    * under development

### Description :
In this project you will use object oriented programming to create a Rectangle class and a Square class. The Square class should be a subclass of Rectangle and inherit methods and attributes.
#### Rectangle class
When a Rectangle object is created, it should be initialized with `width` and `height` attributes. The class should also contain the following methods:
- `set_width`
- `set_height`
- `get_area` : Returns area (`width * height`)
- `get_perimeter` : Returns perimeter (`2 * width + 2 * height`)
- `get_diagonal` : Returns diagonal (`(width ** 2 + height ** 2) ** .5`)
- `get_picture` : Returns a string that represents the shape using lines of "*". The number of lines should be equal to the height and the number of "*" in each line should be equal to the width. There should be a new line (`\n`) at the end of each line. If the width or height is larger than 50, this should return the string: "Too big for picture.".
- `get_amount_inside` : Takes another shape (square or rectangle) as an argument. Returns the number of times the passed in shape could fit inside the shape (with no rotations). For instance, a rectangle with a width of 4 and a height of 8 could fit in two squares with sides of 4.
Additionally, if an instance of a Rectangle is represented as a string, it should look like: `Rectangle(width=5, height=10)`

### Development
Write your code in shape_`calculator.py`. For development, you can use `main.py` to test your `shape_calculator()` function. Click the "run" button and `main.py` will run.

### Testing
We imported the tests from` test_module.py` to `main.py` for your convenience. The tests will run automatically whenever you hit the "run" button.

#### Test Result
![complete](complete.jpg)
