# Maxwell-Boltzmann Distribution

Write a function to the plot the Maxwell-Boltzmann Distribution of molecular speed for a gas of particles of a given mass at a given temperature, indicating the modal speed ($v_{*}$), mean ($\langle v \rangle$), and root mean square (rms, $\langle v^{2} \rangle^{1/2}$) speeds with vertical lines.

Call this function for the atomic gasses Helium (m = 4u), and Argon (m = 40u) at 300 K.

__Hints__: The modal speed is the maximum of the probability distribution and can be found $df/dv$. The mean and rms speeds can be obtained, respectively, from the integrals.

$\langle v\rangle = \int_{0}^{\infty} vf(v)$ and $\langle v^{2} \rangle = \int_{0}^{\infty} v^{2}f(v) dv$.

The following expression for the different types of average speed can be derived:

- $v_{*} = \sqrt{\frac{2k_{B}T}{m}}$ (mode)
- $\langle v \rangle = \sqrt{\frac{8k_{B}T}{\pi m}}$ (mean)
- $\langle v^{2} \rangle^{1/2} = \sqrt{\frac{3k_{B}T}{m}}$ (rms speed).
