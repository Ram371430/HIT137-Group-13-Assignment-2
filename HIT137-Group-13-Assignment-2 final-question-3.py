# HIT137-Group-13-Assignment-2
# The repository includes all programming files, outputs, and the required text files for submission, along with the GitHub link in "github_link.txt". All group contributions and progress are recorded here until submission."
# question 3 done by s371430 - Ram Mani Phuyal 



import turtle

def draw_tree(branch_length, angle_left, angle_right, depth, reduction_factor):
    if depth == 0:
        return
    else:
        turtle.forward(branch_length)
        turtle.left(angle_left)
        draw_tree(branch_length * reduction_factor, angle_left, angle_right, depth - 1, reduction_factor)
        turtle.right(angle_left + angle_right)
        draw_tree(branch_length * reduction_factor, angle_left, angle_right, depth - 1, reduction_factor)
        turtle.left(angle_right)
        turtle.backward(branch_length)

def main():
    turtle.speed(0)
    turtle.left(90)
    turtle.penup()
    turtle.backward(100)
    turtle.pendown()
    
    # Set fixed values for the tree parameters
    angle_left = 30
    angle_right = 30
    branch_length = 100
    depth = 5
    reduction_factor = 0.7
    
    draw_tree(branch_length, angle_left, angle_right, depth, reduction_factor)
    turtle.hideturtle()
    turtle.done()

if __name__ == "__main__":
    main()