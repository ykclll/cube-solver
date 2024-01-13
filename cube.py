from queue import Queue
import time
from PySide6.QtCore import QObject, Signal


class Cube(QObject):
    # 发送给主线程的信号
    bfsFinishedSignal = Signal(str)
    dfsFinishedSignal = Signal(str)
    error_signal      = Signal(int)
    bfsStartedSignal  = Signal(str)
    dfsStartedSignal  = Signal(str)

    def __init__(self):
        super().__init__()
        self.restored_state = 0b11000101001000001100010000010000000
        self.layer_digits = {
            "U": [0, 1, 2, 3],
            "R": [2, 5, 4, 3],
            "F": [1, 6, 5, 2],
        }
        self.layer_angles = [1, 2, 3]
        self.pattern_indexes = [
            [0, 16, 13],
            [2, 4, 17],
            [3, 8, 5],
            [1, 12, 9],
            [23, 11, 14],
            [21, 7, 10],
            [20, 19, 6],
            [22, 15, 18],
        ]
        self.corner_id = {
            "WOB": 0,
            "WGO": 1,
            "WRG": 2,
            "WBR": 3,
            "YRB": 4,
            "YGR": 5,
            "YOG": 6,
            "YBO": 7,
        }

        self.pattern = ""

    # 从某个状态中获取指定层的角块信息
    def extract_corners(self, state, layer):
        corners = [0] * 4
        for i, digit in enumerate(self.layer_digits[layer]):
            corners[i] = (state & (0b11111 << (digit * 5))) >> (digit * 5)
        return corners

    # 给定四个角块和它们所在的层,返回顺时针转动九十度后的四个角块
    def turn_corners(self, corners, layer):
        corners = corners[1:] + [corners[0]]
        if layer == "R" or layer == "F":
            corners[1], corners[3] = self.turn_corner(
                corners[1], "f"), self.turn_corner(corners[3], "f")
            corners[0], corners[2] = self.turn_corner(
                corners[0], "r"), self.turn_corner(corners[2], "r")
        return corners

    # 更改角块的角度信息
    def turn_corner(self, corner, method):
        angle = corner & 0b11
        if method == "f":
            angle = (angle + 1) % 3
        elif method == "r":
            angle = (angle - 1) if angle > 0 else 2
        corner &= 0b11100
        return corner | angle

    # 将转动后的角块填回魔方并返回魔方状态
    def fill_corners(self, state, corners, layer):
        for i, digit in enumerate(self.layer_digits[layer]):
            state &= ~(0b11111 << (digit * 5))
            state |= (corners[i] << (digit * 5))
        return state

    # 转换为二进制
    def pattern_to_corners(self, pattern):
        if len(pattern) != 24:
            raise ValueError("Invalid cube pattern")
        corners = [0] * 8
        for i in range(8):
            corner_pattern = [""] * 3
            id, angle = 0, 0
            for j, index in enumerate(self.pattern_indexes[i]):
                corner_pattern[j] = pattern[index]
                if corner_pattern[j] == "W" or corner_pattern[j] == "Y":
                    angle = j
            corner_pattern = corner_pattern[angle:] + corner_pattern[:angle]
            corner_str = "".join(corner_pattern)
            if corner_str in self.corner_id:
                id = self.corner_id[corner_str]
            else:
                raise ValueError("Invalid corner: {}".format(corner_pattern))
            corners[i] = (id << 2) | angle
        return corners

    def is_cube_valid(self, corners):
        exist_corners = [False] * 8
        angle_sum = 0
        for corner in corners:
            id, angle = corner >> 2, corner & 0b11
            exist_corners[id] = True
            angle_sum += angle
        return all(exist_corners) and angle_sum % 3 == 0

    def x_move(self, corners, times):
        new_corners = [0] * 8
        for m, n in enumerate([7, 0, 3, 4, 5, 2, 1, 6]):
            new_corners[m] = corners[n]
        corners = new_corners
        for i, corner in enumerate(corners):
            if i % 2 == 0:
                corners[i] = self.turn_corner(corner, "r")
            else:
                corners[i] = self.turn_corner(corner, "f")
        if times == 1:
            return corners
        return self.x_move(corners, times - 1)

    def y_move(self, corners, times):
        corners = corners[1:4] + [corners[0], corners[7], corners[4], corners[5], corners[6]]
        if times == 1:
            return corners
        return self.y_move(corners, times - 1)

    def z_move(self, corners, times):
        new_corners = [0] * 8
        for m, n in enumerate([7, 6, 1, 0, 3, 2, 5, 4]):
            new_corners[m] = corners[n]
        corners = new_corners
        for i, corner in enumerate(corners):
            if i % 2 == 0:
                corners[i] = self.turn_corner(corner, "f")
            else:
                corners[i] = self.turn_corner(corner, "r")
        if times == 1:
            return corners
        return self.z_move(corners, times - 1)

    # 还原七号角块
    def get_prefix(self, corners):
        i = 0
        prefix = []
        for j, c in enumerate(corners):
            if c >> 2 == 0b111:
                i = j
                break
        corner = corners[i]
        angle = corner & 0b11
        if angle == 0:
            if i > 3:
                for j in range(7 - i):
                    corners = self.y_move(corners, 1)
                    prefix.append("Y")
                new_corners = corners[:7]
                return new_corners, prefix

            for j in range((i + 1) % 4):
                corners = self.y_move(corners, 1)
                prefix.append("Y")
            new_corners = self.z_move(corners, 2)[:7]
            prefix.extend(["Z", "Z"])
            return new_corners, prefix

        elif angle == 1:
            if i > 3:
                for j in range((8 - i) % 4):
                    corners = self.y_move(corners, 1)
                    prefix.append("Y")
                new_corners = self.z_move(corners, 1)[:7]
                prefix.append("Z")
                return new_corners, prefix
            for j in range(i):
                corners = self.y_move(corners, 1)
                prefix.append("Y")
            new_corners = self.z_move(corners, 3)[:7]
            prefix.extend(['Z', 'Z', 'Z'])
            return new_corners, prefix

        elif angle == 2:
            if i > 3:
                y_moves = [2, 1, 0, 3]
                for j in range(y_moves[i - 4]):
                    corners = self.y_move(corners, 1)
                    prefix.append("Y")
                new_corners = self.x_move(corners, 1)[:7]
                prefix.append("X")
                return new_corners, prefix
            for j in range(i):
                corners = self.y_move(corners, 1)
                prefix.append("Y")
            new_corners = self.x_move(corners, 3)[:7]
            prefix.extend(['X', 'X', 'X'])
            return new_corners, prefix

        else:
            raise ValueError("It's impossible, haha")

    def dfs_solve(self, last_layer, index):
        if index >= 11:
            return False
        elif self.state in self.seen:
            moveLength = self.seen[self.state]
            if moveLength <= index:
                return False
        elif self.state == self.restored_state:
            self.move_length = index
            return True

        self.seen[self.state] = index
        state = self.state

        for layer in ["U", "R", "F"]:
            if layer == last_layer:
                continue

            corners = self.extract_corners(self.state, layer)
            for angle in self.layer_angles:
                corners = self.turn_corners(corners, layer)
                self.state = self.fill_corners(state, corners, layer)
                self.moves[index] = "{}{}".format(layer, angle)
                if self.dfs_solve(layer, index + 1):
                    return True
            self.state = state

        self.moves[index] = ""
        return False

    def bfs_sovle(self):
        has_seen = set()
        state = self.state
        moves = []
        q = Queue()
        q.put([state, moves.copy()])

        while not q.empty():
            state, moves = q.get()
            if len(moves) > 11:
                return False
            if state == self.restored_state:
                self.moves = moves
                return True
            for layer in ["U", "R", "F"]:
                # 如果与上一次转动层相同则跳过
                if len(moves) and layer == moves[-1][0]:
                    continue
                corners = self.extract_corners(state, layer)
                for angle in self.layer_angles:
                    corners = self.turn_corners(corners, layer)
                    new_state = self.fill_corners(state, corners, layer)
                    new_move = moves + ["{}{}".format(layer, angle)]
                    if new_state not in has_seen:
                        q.put([new_state, new_move.copy()])
                        has_seen.add(new_state)
        return False

    def solve_cube_bfs(self):
        try:
            self.state, self.prefix = self.parse_pattern(self.pattern)
            self.bfsStartedSignal.emit("BFS求解中,请耐心等待...")
            start = time.time()
            if self.bfs_sovle() == True:
                end = time.time()
                self.bfsFinishedSignal.emit(self.merge_result(self.prefix, self.moves, "BFS", end-start))
                # return self.merge_result(self.prefix, self.moves, "BFS", end - start)
            else:
                return "bfs求解失败"
        except ValueError:
            self.error_signal.emit(1)

    def solve_cube_dfs(self):
        try:
            self.state, self.prefix = self.parse_pattern(self.pattern)
            self.dfsStartedSignal.emit("DFS求解中,请耐心等待...")
            start = time.time()
            self.seen = {}
            self.moves = [""] * 11
            self.move_length = 0
            if self.dfs_solve("", 0) == True:
                end = time.time()
                self.dfsFinishedSignal.emit(self.merge_result(self.prefix, self.moves[:self.move_length], "DFS", end - start))
                # return self.merge_result(self.prefix, self.moves[:self.move_length], "DFS", end - start)
            else:
                return "dfs求解失败"
        except ValueError:
            self.error_signal.emit(1)

    def merge_result(self, prefix, moves, method, time):
        time = '{:.2f}'.format(time)
        dic = {
            "X": {
                "U": "B",
                "R": "R",
                "F": "U",
                "L": "L",
                "B": "D",
                "D": "F"
            },
            "Y": {
                "U": "U",
                "R": "B",
                "F": "R",
                "L": "F",
                "B": "L",
                "D": "D"
            },
            "Z": {
                "U": "L",
                "R": "U",
                "F": "F",
                "L": "D",
                "B": "B",
                "D": "R"
            },
        }

        for i in range(len(prefix) - 1, -1, -1):
            for j in range(len(moves)):
                moves[j] = dic[prefix[i]][moves[j][0]] + moves[j][1:]

        result = " ".join(moves).replace("3", "'").replace("1", "")
        return method + "求解结果为:" + "\n" + result + "\n" + "耗时" + str(time) + 's'

    def parse_pattern(self, pattern):
        corners = self.pattern_to_corners(pattern)
        if not self.is_cube_valid(corners):
            raise ValueError("Invalid cube pattern")
        corners, prefix = self.get_prefix(corners)

        state = 0
        for i, corner in enumerate(corners):
            state |= corner << (i * 5)
        return state, prefix

if __name__ == "__main__":
    print("")
