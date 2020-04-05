def matryoshka(n):
    if n == 1:
        print("Matryoshe4ka")
    else:
        print(f"Top Matryoshe4ka n={n}")
        matryoshka(n-1)
        print(f"Bottom matryosh34ka n={n}")


matryoshka(5)
