import numpy as np
import SimpleITK as sitk
import matplotlib.pyplot as plt
from scipy.io import loadmat

def load_mida_data(file_path):
    if file_path.endswith('.mat'):
        data = loadmat(file_path)
        print("Keys in the .mat file:", data.keys())
        if 'tissuedistrib' in data:
            voxels = data['tissuedistrib']
            print(f"Loaded voxel data shape: {voxels.shape}")
            return voxels
        else:
            raise ValueError("'tissuedistrib' key not found in the .mat file")
    elif file_path.endswith('.nii'):
        image = sitk.ReadImage(file_path)
        voxels = sitk.GetArrayFromImage(image)
        return voxels
    else:
        raise ValueError("Unsupported file format")

# Step 2: Assign tissue properties
def assign_tissue_properties(voxels):
    # This is a simplified example. You'll need to define a mapping of tissue IDs to properties
    tissue_properties = {
        0: {'conductivity': 0.1, 'permittivity': 1.0},  # Example values
        1: {'conductivity': 0.2, 'permittivity': 2.0},
        # Add more tissue types and their properties
    }
    
    conductivity_map = np.zeros_like(voxels, dtype=float)
    permittivity_map = np.zeros_like(voxels, dtype=float)
    
    for tissue_id, props in tissue_properties.items():
        mask = (voxels == tissue_id)
        conductivity_map[mask] = props['conductivity']
        permittivity_map[mask] = props['permittivity']
    
    return conductivity_map, permittivity_map

# Step 3: Implement a simple FDTD simulation (placeholder)
def simple_fdtd_simulation(conductivity_map, permittivity_map):
    # This is a placeholder for the actual FDTD simulation
    # You would implement the full FDTD algorithm here
    print("Running FDTD simulation...")
    # For now, we'll just return a dummy electric field
    return np.random.rand(*conductivity_map.shape)

# Step 4: Visualize results
def visualize_results(electric_field):
    plt.figure(figsize=(10, 10))
    plt.imshow(electric_field[:, :, electric_field.shape[2]//2], cmap='hot')
    plt.colorbar(label='Electric Field Strength')
    plt.title('Electric Field Distribution (Mid Slice)')
    plt.show()

if __name__ == "__main__":
    file_path = "data/MIDA_v1.mat"  # Make sure this path is correct
    
    # Load data
    voxels = load_mida_data(file_path)
    
    # Assign tissue properties
    conductivity_map, permittivity_map = assign_tissue_properties(voxels)
    
    # Run simulation
    electric_field = simple_fdtd_simulation(conductivity_map, permittivity_map)
    
    # Visualize
    visualize_results(electric_field)
    # After loading voxels
unique_tissues = np.unique(voxels)
print(f"Number of unique tissue types: {len(unique_tissues)}")
print(f"Unique tissue IDs: {unique_tissues}")

# To see the distribution of tissues
for tissue_id in unique_tissues:
    count = np.sum(voxels == tissue_id)
    percentage = (count / voxels.size) * 100
    print(f"Tissue ID {tissue_id}: {count} voxels ({percentage:.2f}%)")