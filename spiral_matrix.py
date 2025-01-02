def spiral_matrix(n):
    # Boş bir n x n matris oluşturma
    matrix = [[0] * n for _ in range(n)]

    num = 1  # Matrise yazılacak sayıdır
    top, bottom, left, right = 0, n - 1, 0, n - 1  # Üst,alt,sol,sağ sınırlar

    while num <= n * n:
        # Sol-sağ
        for i in range(left, right + 1):
            matrix[top][i] = num
            num += 1
        top += 1  # Üst sınırı bir azaltma

        # Yukarı-aşağı
        for i in range(top, bottom + 1):
            matrix[i][right] = num
            num += 1
        right -= 1  # Sağ sınırı bir azaltma

        # Sağ-sol
        for i in range(right, left - 1, -1):
            matrix[bottom][i] = num
            num += 1
        bottom -= 1  # Alt sınırı bir azaltma

        # Aşağı-yukarı
        for i in range(bottom, top - 1, -1):
            matrix[i][left] = num
            num += 1
        left += 1  # Sol sınırı bir artırma

    return matrix
