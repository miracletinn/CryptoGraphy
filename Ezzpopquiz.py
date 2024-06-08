def modular_sqrt(a, p):
    """ Tonelli-Shanks algorithm for finding square roots modulo a prime """
    # Check if solution exists
    if pow(a, (p - 1) // 2, p) != 1:
        return None  # No solution exists

    # Simple cases
    if a == 0:
        return 0
    if p == 2:
        return a % p
    if p % 4 == 3:
        return pow(a, (p + 1) // 4, p)

    # Find Q and S such that p-1 = Q * 2^S with Q odd
    S = 0
    Q = p - 1
    while Q % 2 == 0:
        S += 1
        Q //= 2

    # Find a non-residue z
    z = 2
    while pow(z, (p - 1) // 2, p) == 1:
        z += 1

    M = S
    c = pow(z, Q, p)
    t = pow(a, Q, p)
    R = pow(a, (Q + 1) // 2, p)

    while t != 0 and t != 1:
        t2i = t
        for i in range(1, M):
            t2i = pow(t2i, 2, p)
            if t2i == 1:
                break

        b = pow(c, 1 << (M - i - 1), p)
        M = i
        c = pow(b, 2, p)
        t = (t * c) % p
        R = (R * b) % p

    return R

# Given parameters
p = 12060761007342792389727454255724405807409304271375733358258283397590233420679076390553468835661300143930898274850936437602846568280070388550368168750979099
y_squared = 7231461461802238983774396255031931017441460242339685541807891051051604457092785729103727369205368822775690895955232522851256252340162494609975485713653013

# Calculate y using modular square root function
y = modular_sqrt(y_squared, p)
if y is not None:
    print(f"Nilai y yang mungkin adalah: {y} dan {p - y}")
else:
    print("Tidak ada solusi untuk y di modulo ini")
