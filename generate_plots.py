import control as ct
import matplotlib.pyplot as plt
import numpy as np
import os

# Define systems
# G1: Stable (Suspension)
num1 = [10]
den1 = [1, 6, 11, 6]
G1 = ct.TransferFunction(num1, den1)

# G2: Integrator (Satellite)
num2 = [5]
den2 = [1, 3, 2, 0]
G2 = ct.TransferFunction(num2, den2)

# G3: Unstable (Inverted Pendulum)
num3 = [10, -10]
den3 = [1, 5, 6]
G3 = ct.TransferFunction(num3, den3)

# Style configuration for dark theme
plt.style.use('dark_background')
plt.rcParams.update({
    'figure.facecolor': '#0f172a',  # Slate-900
    'axes.facecolor': '#0f172a',
    'axes.edgecolor': '#475569',    # Slate-600
    'axes.labelcolor': '#94a3b8',   # Slate-400
    'xtick.color': '#94a3b8',
    'ytick.color': '#94a3b8',
    'text.color': '#e2e8f0',        # Slate-200
    'grid.color': '#334155',        # Slate-700
    'grid.alpha': 0.5,
    'lines.linewidth': 2.5
})

def save_bode(sys, filename, title, color='#818cf8'):
    plt.figure(figsize=(10, 6))
    ct.bode_plot(sys, dB=True, color=color)
    # Customize the plot created by control library
    # Note: control library creates subplots, so we need to adjust current figure
    fig = plt.gcf()
    fig.suptitle(title, color='#e2e8f0', fontsize=16, fontweight='bold')
    
    # Adjust axes of the subplots
    for ax in fig.axes:
        ax.grid(True, which='both', color='#334155', alpha=0.5)
        
    plt.tight_layout()
    plt.savefig(filename, dpi=150, bbox_inches='tight', facecolor=fig.get_facecolor())
    plt.close()

def save_nyquist(sys, filename, title, color='#f43f5e', xlim=None, ylim=None):
    plt.figure(figsize=(8, 8))
    # Nyquist plot
    ct.nyquist_plot(sys, color=color)
    
    fig = plt.gcf()
    ax = plt.gca()
    ax.set_title(title, color='#e2e8f0', fontsize=16, fontweight='bold', pad=20)
    ax.grid(True, which='both', color='#334155', alpha=0.5)
    
    # Add unit circle for reference
    circle = plt.Circle((0, 0), 1, color='#475569', fill=False, linestyle='--', alpha=0.7)
    ax.add_artist(circle)
    
    # Mark critical point
    ax.plot(-1, 0, 'rx', markersize=10, markeredgewidth=3)
    
    if xlim:
        ax.set_xlim(xlim)
    if ylim:
        ax.set_ylim(ylim)
        
    plt.tight_layout()
    plt.savefig(filename, dpi=150, bbox_inches='tight', facecolor=fig.get_facecolor())
    plt.close()

# Generate Plots
print("Generating Gabriel's Bode Plot...")
save_bode(G1, 'gabriel_bode.png', 'Bode - G1: Estável (Suspensão)', color='#818cf8')

print("Generating Cintia's Nyquist Plot...")
save_nyquist(G1, 'cintia_nyquist.png', 'Nyquist - G1: Estável', color='#6366f1')

print("Generating Nick's Nyquist Plot...")
# Using default limits usually works well for G2 with control library, 
# but we can enforce a range if needed. The library handles asymptotes well.
save_nyquist(G2, 'nick_nyquist.png', 'Nyquist - G2: Integrador (Satélite)', color='#d97706', xlim=[-5, 5], ylim=[-15, 15])

print("Generating Dierson's Bode Plot...")
save_bode(G3, 'dierson_bode.png', 'Bode - G3: Instável (Pêndulo)', color='#f43f5e')

print("Generating Dierson's Nyquist Plot...")
save_nyquist(G3, 'dierson_nyquist.png', 'Nyquist - G3: Instável', color='#fb7185', xlim=[-4, 4], ylim=[-4, 4])

print("All plots generated successfully.")
