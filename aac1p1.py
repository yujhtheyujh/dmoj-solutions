a, b = map(int, input().split())
print(["SQUARE", "CIRCLE"][a ** 2 < b ** 2 * 3.14])