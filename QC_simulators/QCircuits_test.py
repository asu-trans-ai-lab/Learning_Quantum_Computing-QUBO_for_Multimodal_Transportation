'''
the source at github.com/grey-area/qcircuits
http://www.awebb.info/qcircuits/index.html

install step:
python -m pip install --upgrade pip
pip install qcircuits

'''
import qcircuits as qc


# Quantum Teleportation: transmitting two classical bits to transport a qubit state
# Alice has a qubit in a given quantum state.
# Alice and Bob have previously prepared a Bell state, and have since
# physically separated the qubits.
# Alice manipulates her hidden qubit and her half of the Bell state, and then
# measures both qubits.
# She sends the result (two classical bits) to Bob, who is able to reconstruct
# Alice's state by applying operators based on the measurement outcomes.


def quantum_teleportation(alice_state):
    # Get operators we will need
    CNOT = qc.CNOT()
    H = qc.Hadamard()
    X = qc.PauliX()
    Z = qc.PauliZ()

    # The prepared, shared Bell state
    bell = qc.bell_state(0, 0)
    # The whole state vector
    state = alice_state * bell

    # Apply CNOT and Hadamard gate
    state = CNOT(state, qubit_indices=[0, 1])
    state = H(state, qubit_indices=[0])

    # Measure the first two bits
    # The only uncollapsed part of the state vector is Bob's
    M1, M2 = state.measure(qubit_indices=[0, 1], remove=True)

    # Apply X and/or Z gates to third qubit depending on measurements
    if M2:
        state = X(state)
    if M1:
        state = Z(state)

    return state


if __name__ == '__main__':
    # Alice's original state to be teleported to Bob
    alice = qc.qubit(theta=1.5, phi=0.5, global_phase=0.2)

    # Bob's state after quantum teleportation
    bob = quantum_teleportation(alice)

    print('Original state:', alice)
    print('\nTeleported state:', bob)
# Original state: 1-qubit state. Tensor:
# [0.71710381+0.14536414j 0.52134608+0.43912375j]
# Teleported state: 1-qubit state. Tensor:
# [0.71710381+0.14536414j 0.52134608+0.43912375j]