import unittest
from maze import Maze
from cell import Cell

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(len(m1._cells), num_cols)
        self.assertEqual(len(m1._cells[0]), num_rows)
        
    def test_grid_consistency(self):
        num_cols = 20
        num_rows = 20
        m1 = Maze(0, 0, num_rows, num_cols, 15, 15)
        for column in m1._cells:
            for cell in column:
                self.assertTrue(isinstance(cell, Cell))  
                
    def test_grid_dimensions(self):
        num_cols = 20
        num_rows = 15
        m1 = Maze(0, 0, num_rows, num_cols, 12, 12)
        grid_width = 0
        grid_height = 0
        for _ in m1._cells:
            grid_width += m1.cell_size_x
        for _ in m1._cells[0]:
            grid_height += m1.cell_size_y
        self.assertEqual(grid_width, num_cols * m1.cell_size_x)
        self.assertEqual(grid_height, num_rows * m1.cell_size_y)
        
    def test_entrance_and_exit_removed(self):
        num_cols = 20
        num_rows = 15
        m1 = Maze(0, 0, num_rows, num_cols, 12, 12)        
        self.assertFalse(m1._cells[0][0].has_top_wall)
        self.assertFalse(m1._cells[num_cols-1][num_rows-1].has_bottom_wall)
        
    def test_reset_cells_visited(self):
        num_cols = 20
        num_rows = 15
        m1 = Maze(0, 0, num_rows, num_cols, 12, 12) 
        for column in m1._cells:
            for cell in column:
                self.assertFalse(cell.visited)
        
    
        
if __name__ == "__main__":
    unittest.main()