import time
from __init__ import Vector4,Momentum4

def test3():

    start_time = time.time()

    # Define the initial Lorentz vector (px, py, pz, E)
    vector = Momentum4(1.0, 2.0, 3.0, 4.0)
    temp = Momentum4(1.0, 2.0, 3.0, 4.0)

    betaX = Momentum4(1,0.3,0.0,0.0)  # Velocity in x-direction
    betaY = Momentum4(1,0.0,0.2,0.0)  # Velocity in y-direction
    betaZ = Momentum4(1,0.0,0.0,0.1)  # Velocity in z-direction


    # Define the number of boost iterations
    num_boosts = 100000

    # Perform the Lorentz boost in a loop
    i=0
    for _ in range(num_boosts):
        # Perform the Lorentz boost along the x-axis
        vector1 = vector.boost(1,0,0,gamma = 1.1547)

        # Perform the Lorentz boost along the y-axis
        vector2 = vector.boost(0,1,0,gamma = 1.09109)

        # Perform the Lorentz boost along the z-axis
        vector3 = vector.boost(0,0,1,gamma = 1.04828)

        vector = temp

    end_time = time.time()

    # Print out the original and boosted vectors
    print("Original vector: Px={}, Py={}, Pz={}, E={}".format(*vector.components))

    # Print out the duration
    print("Boost time for {} iterations: {:.6f} seconds".format(num_boosts, end_time - start_time))

    # Print out the boosted vectors along x, y, and z axes
    print("Vector1: Px={}, Py={}, Pz={}, E={}".format(*vector1.components))
    print("Vector2: Px={}, Py={}, Pz={}, E={}".format(*vector2.components))
    print("Vector3: Px={}, Py={}, Pz={}, E={}".format(*vector3.components))


if __name__ == "__main__":
    test3()