from window import Window
from maze import Maze

def main():
    win = Window(800, 600)   
    
    m1 = Maze(10, 10, 20, 20, 25, 25, win)
    
    m1.solve()
    
    win.wait_for_close()
    
        
if __name__ == "__main__":
    main()
    
