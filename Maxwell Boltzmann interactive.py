{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "3c3ed2d8-2b64-4092-9d8a-acec94b53d15",
   "metadata": {},
   "source": [
    "# Maxwell-Boltzmann Distribution\n",
    "\n",
    "Write a function to the plot the Maxwell-Boltzmann Distribution of molecular speed for a gas of particles of a given mass at a given temperature, indicating the modal speed ($v_{*}$), mean ($\\langle v \\rangle$), and root mean square (rms, $\\langle v^{2} \\rangle^{1/2}$) speeds with vertical lines.\n",
    "\n",
    "Call this function for the atomic gasses Helium (m = 4u), and Argon (m = 40u) at 300 K.\n",
    "\n",
    "__Hints__: The modal speed is the maximum of the probability distribution and can be found $df/dv$. The mean and rms speeds can be obtained, respectively, from the integrals.\n",
    "\n",
    "$\\langle v\\rangle = \\int_{0}^{\\infty} vf(v)$ and $\\langle v^{2} \\rangle = \\int_{0}^{\\infty} v^{2}f(v) dv$.\n",
    "\n",
    "The following expression for the different types of average speed can be derived:\n",
    "\n",
    "- $v_{*} = \\sqrt{\\frac{2k_{B}T}{m}}$ (mode)\n",
    "- $\\langle v \\rangle = \\sqrt{\\frac{8k_{B}T}{\\pi m}}$ (mean)\n",
    "- $\\langle v^{2} \\rangle^{1/2} = \\sqrt{\\frac{3k_{B}T}{m}}$ (rms speed)."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "c48badf8-e0a6-4d31-a3be-8391267f0c51",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "1a48486baf27480b9b98cbf8a9ddba6a",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "interactive(children=(IntSlider(value=300, description='T', max=1000, min=100, step=50), Output()), _dom_class…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/plain": [
       "<function __main__.plot_MB(T=300)>"
      ]
     },
     "execution_count": 1,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import numpy as np\n",
    "import matplotlib.pyplot as plt\n",
    "from ipywidgets import interact\n",
    "\n",
    "# Boltzman constant, J.K-1, atomis mass unit (kg)\n",
    "kB, u = 1.381e-23, 1.661e-27\n",
    "\n",
    "# Gas particle masses, in kg\n",
    "m_He, m_Ar = 4 * u, 40 * u\n",
    "\n",
    "# Temperature in K\n",
    "T = 300\n",
    "\n",
    "# The value of the Maxwell-Boltzmann distribution\n",
    "def fMB(v, T, m): # mass in kg, at temperature in K, at the speed v (in m.s-1)\n",
    "    fac = m /2 /kB/T\n",
    "    return (fac / np.pi)**1/5 * 4 * np.pi * v**2 * np.exp(-fac * v **2)\n",
    "\n",
    "def plot_MB(T=300):\n",
    "    v= np.linspace(0, 3000, 3000)\n",
    "    fv_He = fMB(v, T, m_He)\n",
    "    fv_Ar = fMB(v, T, m_Ar)\n",
    "\n",
    "# Plot He and Ar distribution\n",
    "    plt.plot(figsize=(8,6))\n",
    "    plt.plot(v, fv_He, color='orange', label=f'He, T{T}K')\n",
    "    plt.plot(v, fv_Ar, color='blue', ls='--', label=f'Ar, T{T}K')\n",
    "    \n",
    "    plt.xlabel('Speed v /m.s-1', fontsize=14)\n",
    "    plt.ylabel('Density f(v) /s.m-1', fontsize=14)\n",
    "    plt.legend()\n",
    "    plt.legend(framealpha=0.7, fontsize=14, loc='upper right', bbox_to_anchor=(0.98, 1))\n",
    "    plt.grid(True, color='gray', zorder=0, linestyle='--')\n",
    "    plt.show()\n",
    "\n",
    "interact(plot_MB, T=(100, 1000, 50))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "893b6a24-775b-48ec-ac44-66d188be717f",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "myenv",
   "language": "python",
   "name": "myenv"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.13.9"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
