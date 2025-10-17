# 🎮 Pacman Game - Cấu trúc dự án đã được tái tổ chức

## 📁 Cấu trúc thư mục mới

```
pacman_game/
├── main.py                    # CLI entry point cho AI algorithm
├── run_game.py               # Entry point cho game
├── config.py                 # Configuration tổng
├── requirements.txt          # Dependencies
│
├── game/                     # 🎮 Game Logic (Core)
│   ├── __init__.py
│   ├── game.py              # Main game class
│   ├── player.py            # Pacman player
│   ├── ghost.py             # Ghost AI
│   ├── board.py             # Maze board
│   ├── ui.py                # Game UI
│   └── constants.py         # Game constants
│
├── ai/                       # 🤖 AI Algorithm
│   ├── __init__.py
│   ├── environment.py       # AI environment
│   ├── heuristics.py        # AI heuristics
│   └── auto.py              # Auto mode
│
├── integration/              # 🔗 Integration Layer
│   ├── __init__.py
│   ├── coordinate_mapper.py # Coordinate mapping
│   └── layout_converter.py  # Layout conversion
│
├── ui/                      # 🎨 Extended UI (Future)
│   └── __init__.py
│
├── layouts/                 # 📁 Layout Files
│   ├── small_basic.txt
│   ├── medium_twists.txt
│   ├── large_multi_pie.txt
│   └── maze.txt
│
└── assets/                  # 🖼️ Assets
    ├── player_images/
    └── ghost_images/
```

## 🚀 Cách chạy

### Chạy Game:
```bash
python run_game.py
```

### Chạy AI Algorithm:
```bash
python main.py --layout layouts/small_basic.txt --heuristic exact-mst
```

## 🔧 Cải thiện đã thực hiện

### ✅ **Tách biệt rõ ràng:**
- **game/**: Logic game thuần túy (không thay đổi)
- **ai/**: Thuật toán AI (không thay đổi)
- **integration/**: Kết nối giữa game và AI
- **ui/**: UI mở rộng (sẵn sàng cho tương lai)

### ✅ **Import paths được cập nhật:**
- Tất cả relative imports (`.module`)
- Không còn conflict giữa các module
- Dễ dàng maintain và extend

### ✅ **Cấu trúc scalable:**
- Dễ thêm tính năng mới
- Tách biệt concerns
- Code organization tốt hơn

## 📋 Các file đã được di chuyển

### Game Logic:
- `game.py` → `game/game.py`
- `player.py` → `game/player.py`
- `ghost.py` → `game/ghost.py`
- `board.py` → `game/board.py`
- `ui.py` → `game/ui.py`
- `constants.py` → `game/constants.py`

### AI Algorithm:
- `environment.py` → `ai/environment.py`
- `heuristics.py` → `ai/heuristics.py`
- `auto.py` → `ai/auto.py`

### Integration:
- Tạo mới: `integration/coordinate_mapper.py`
- Tạo mới: `integration/layout_converter.py`

## 🎯 Lợi ích của cấu trúc mới

1. **Separation of Concerns**: Mỗi module có trách nhiệm rõ ràng
2. **Maintainability**: Dễ maintain và debug
3. **Scalability**: Dễ thêm tính năng mới
4. **Reusability**: Các component có thể tái sử dụng
5. **Testing**: Dễ viết unit tests cho từng module
6. **Documentation**: Cấu trúc rõ ràng, dễ hiểu

## 🔄 Migration Notes

- Tất cả import statements đã được cập nhật
- Game logic hoàn toàn không thay đổi
- AI algorithm hoàn toàn không thay đổi
- Chỉ thêm integration layer
- Backward compatible
