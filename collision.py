e = input("Enter the coefficient of restitution:")

speed1 = input("Enter the speed of the first ball:")
mass1 = input("Enter the mass of the first ball")

speed2 = input("Enter the speed of the second ball:")
mass2 = input("Enter the mass of the second ball")


def collision(u1, u2, m1, m2):
    momentum = float(u1*m1) + float(u2*m2)
    v2 = float(float(e) * (float(u2) - float(u1))) + float(momentum)
    v1 = float(momentum) - float(v2)
    print("The speed of the first ball after collision is: ", v1)
    print("The speed of the second ball after collision is: ", v2)

collision(float(speed1), float(speed2), float(mass1), float(mass2))