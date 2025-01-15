# HIT137-Group-13-Assignment-2
The repository includes all programming files, outputs, and the required text files for submission, along with the GitHub link in "github_link.txt". All group contributions and progress are recorded here until submission."
# question 3 done by s371430

import turtle

# Set up the turtle
t = turtle.Turtle()
t.speed(0)
t.left(90)  # Point the turtle upwards (towards the top of the screen)

# Recursive function to draw tree branches
def branch(length, t):
    if length <= 5:  # Base case: stop when the branch is too small
        return
    else:
        t.forward(length)  # Draw the current branch
        t.right(20)  # Turn right to draw the right branch
        branch(length - 15, t)  # Recursively draw the right subtree
        t.left(40)  # Turn left to draw the left branch
        branch(length - 15, t)  # Recursively draw the left subtree
        t.right(20)  # Turn back to the original angle
        t.backward(length)  # Move the turtle back to the original position

# Start drawing the tree
branch(100, t)  # Start with an initial branch length of 100

# Keep the window open
turtle.mainloop()
