from cell import Cell
import time
import random

class Maze:
    def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        win=None,
        seed=None
    ):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        if seed:
            random.seed(seed)
            
        self._cells = self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(self._cells[0][0], 0, 0)
        self._reset_cells_visited()
        
    def _create_cells(self):
        cells_list = []
        for i in range(self.num_cols):
            cells_column = []
            for j in range(self.num_rows):
                cell = Cell(self.win)
                self._draw_cell(cell, i, j)
                cells_column.append(cell)
            cells_list.append(cells_column)
        
        return cells_list
    
    def _draw_cell(self, cell, i, j):
        x1 = self.x1 + self.cell_size_x * i
        y1 = self.y1 + self.cell_size_y * j
        x2 = x1 + self.cell_size_x
        y2 = y1 + self.cell_size_y
        cell.draw(x1, y1, x2, y2)
        self._animate()
        
    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._draw_cell(self._cells[0][0], 0, 0)
        
        self._cells[self.num_cols-1][self.num_rows-1].has_bottom_wall = False
        self._draw_cell(self._cells[self.num_cols-1][self.num_rows-1], self.num_cols-1, self.num_rows-1)
        
    def _break_walls_r(self, cell, i, j):
        cell.visited = True
        while True:
            to_visit_list = []
            if i < self.num_cols - 1 and not self._cells[i+1][j].visited:
                to_visit_list.append([i+1,j])
            if j < self.num_rows - 1 and not self._cells[i][j+1].visited:
                to_visit_list.append([i,j+1])
            if i > 0 and not self._cells[i-1][j].visited:
                to_visit_list.append([i-1,j])
            if j > 0 and not self._cells[i][j-1].visited:
                to_visit_list.append([i,j-1])
                
            if len(to_visit_list) == 0:
                self._draw_cell(self._cells[i][j], i, j)
                return
            else:
                direction = random.choice(to_visit_list)
                if direction[0] == i + 1:
                    self._cells[i][j].has_right_wall = False
                    self._cells[i+1][j].has_left_wall = False
                elif direction[1] == j + 1:
                    self._cells[i][j].has_bottom_wall = False
                    self._cells[i][j+1].has_top_wall = False
                elif direction[0] == i - 1:
                    self._cells[i][j].has_left_wall = False
                    self._cells[i-1][j].has_right_wall = False
                elif direction[1] == j - 1:
                    self._cells[i][j].has_top_wall = False
                    self._cells[i][j-1].has_bottom_wall = False
                self._break_walls_r(self._cells[direction[0]][direction[1]], direction[0], direction[1])
                
    def _reset_cells_visited(self):
        for column in self._cells:
            for cell in column:
                cell.visited = False
                
    def _solve_r(self, i, j):
        self._animate()
        self._cells[i][j].visited = True
        if i == self.num_cols - 1 and j == self.num_rows - 1:
            return True
        
        #[i+1][j] -> right
        if (
            i < self.num_cols - 1 
            and self._cells[i][j].has_right_wall == False
            and self._cells[i+1][j].has_left_wall == False
            and not self._cells[i+1][j].visited):
            self._cells[i][j].draw_move(self._cells[i+1][j])   
            result = self._solve_r(i + 1, j)
            if result:
                return True
            else:
                 self._cells[i+1][j].draw_move(self._cells[i][j], undo=True)         
        #[i][j+1] -> down       
        if (
            j < self.num_rows - 1 
            and self._cells[i][j].has_bottom_wall == False
            and self._cells[i][j+1].has_top_wall == False
            and not self._cells[i][j+1].visited):
            self._cells[i][j].draw_move(self._cells[i][j+1])
            result = self._solve_r(i, j + 1)
            if result:
                return True
            else:
                 self._cells[i][j+1].draw_move(self._cells[i][j], undo=True)                   
        #[i-1][j] -> left   
        if (
            i > 0 
            and self._cells[i][j].has_left_wall == False
            and self._cells[i-1][j].has_right_wall == False
            and not self._cells[i-1][j].visited):
            self._cells[i][j].draw_move(self._cells[i-1][j])
            result = self._solve_r(i - 1, j) 
            if result:
                return True
            else:
                 self._cells[i-1][j].draw_move(self._cells[i][j], undo=True)              
        #[i][j-1] -> up 
        if (
            j > 0 
            and self._cells[i][j].has_top_wall == False
            and self._cells[i][j-1].has_bottom_wall == False
            and not self._cells[i][j-1].visited):
            self._cells[i][j].draw_move(self._cells[i][j-1])  
            result = self._solve_r(i, j - 1) 
            if result:
                return True
            else:
                 self._cells[i][j-1].draw_move(self._cells[i][j], undo=True)                   
        
        return False
    
    def solve(self):
        return self._solve_r(0, 0)
        
    def _animate(self):
        if not self.win:
            return
        self.win.redraw()
        time.sleep(0.02)