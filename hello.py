# 🌸 Pretty Sakura Tree 🌸

import time
import os

tree = r"""
                🌸
              🌸🌸🌸
            🌸🌸🌸🌸🌸
          🌸🌸🌸🌸🌸🌸🌸
        🌸🌸🌸🌸🌸🌸🌸🌸🌸
      🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸

               ||||
             \\||||//
              \\||//
               \\//
                \/
             ___||___
           /          \
          /____________\

        ✨ Sakura Tree ✨
"""

os.system('cls' if os.name == 'nt' else 'clear')

print("\n")
for line in tree.splitlines():
    print(line)
    time.sleep(0.08)

print("\n🌸 Hello World 🌸")
