#include <iostream>
#include <vector>

using namespace std;

void count_stars(vector<string>& grid, vector<vector<bool>>& visited, int start_x, int start_y);

int main() {
    int height, width;

    int case_no = 1;
    while (cin >> height >> width) {
        vector<string> grid;

        for (int i = 0; i < height; i++) {
            string x;
            cin >> x;
            grid.push_back(x);
        }

        vector<vector<bool>> visited(height, vector<bool>(width, false));
        int stars = 0;
        
        for (int i = 0; i < height; i++) {
            for (int j = 0; j < width; j++) {
                if (grid[i][j] == '-' && !visited[i][j]) {
                    count_stars(grid, visited, j, i);
                    stars++;
                }
            }
        }

        cout << "Case " << case_no << ": " << stars << endl;
        case_no++;
    }

    return 0;
}

void count_stars(vector<string>& grid, vector<vector<bool>>& visited, int start_x, int start_y) {
    if (start_x < 0 || start_y < 0 || start_y >= grid.size() ||
        start_x >= grid[0].length() || visited[start_y][start_x] ||
        grid[start_y][start_x] == '#') {
        return;
    }

    visited[start_y][start_x] = true;

    count_stars(grid, visited, start_x + 1, start_y);
    count_stars(grid, visited, start_x - 1, start_y);
    count_stars(grid, visited, start_x, start_y + 1);
    count_stars(grid, visited, start_x, start_y - 1);
}