'''
https://toqito.readthedocs.io/en/latest/getting_started.html

install step:
pip install toqito
'''
from toqito.states import basis
from toqito.states import bell
import numpy as np
# |0>
basis(2, 0)
# [[1]
# [0]]
# |1>
basis(2, 1)
# [[0]
# [1]]
e_0, e_1 = basis(2, 0), basis(2, 1)
u_0 = 1/np.sqrt(2) * (np.kron(e_0, e_0) + np.kron(e_1, e_1))
rho_0 = u_0 * u_0.conj().T
bell(0)