from point import Point, Line

class Cell:
    def __init__(self, win=None):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = None
        self._x2 = None
        self._y1 = None
        self._y2 = None
        self._win = win
        self.visited = False
        
    def draw(self, x1, y1, x2, y2):
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2
        if self._win:
            left_line = Line(Point(x1, y1), Point(x1, y2))
            if self.has_left_wall:
                self._win.draw_line(left_line, "black")
            else:
                self._win.draw_line(left_line, "white")
                
            right_line = Line(Point(x2, y1), Point(x2, y2))
            if self.has_right_wall:
                self._win.draw_line(right_line, "black")
            else:
                self._win.draw_line(right_line, "white")
                
            top_line = Line(Point(x1, y1), Point(x2, y1))
            if self.has_top_wall:
                self._win.draw_line(top_line, "black")
            else:
                self._win.draw_line(top_line, "white")
                
            bottom_line = Line(Point(x1, y2), Point(x2, y2))
            if self.has_bottom_wall:
                self._win.draw_line(bottom_line, "black")
            else:
                self._win.draw_line(bottom_line, "white")
            
    def draw_move(self, to_cell, undo=False):
        origin_x = self._x1 + (self._x2 - self._x1) / 2
        origin_y = self._y1 + (self._y2 - self._y1) / 2
        
        target_x = to_cell._x1 + (to_cell._x2 - to_cell._x1) / 2
        target_y = to_cell._y1 + (to_cell._y2 - to_cell._y1) / 2    
        
        line = Line(Point(origin_x, origin_y), Point(target_x, target_y))
        if not undo:        
            self._win.draw_line(line, "red")
        else:
            self._win.draw_line(line, "gray")
    
    