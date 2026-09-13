import numpy as np
import time

class PersonaField:
    """Represents a continuous volumetric field of intent (Intent Sphere)"""
    def __init__(self, name, core_vector, energy, semantic_volume):
        self.name = name
        self.core_vector = np.array(core_vector, dtype=float)
        self.energy = energy            # E_i parameter from Paper 1
        self.semantic_volume = semantic_volume  # Sigma_i parameter from Paper 1

    def calculate_density(self, input_vector):
        """Applies the Paper 1 formula: Psi_i(x) = E_i * exp(-d(x, c_i)^2 / (2 * sigma_i^2))"""
        distance = np.linalg.norm(input_vector - self.core_vector)
        exponent = -(distance ** 2) / (2 * (self.semantic_volume ** 2))
        return self.energy * np.exp(exponent)

class ResonantEngine:
    def __init__(self):
        # System Core Attractor (Central Gravity Parameter)
        self.core_attractor = np.array([0.0, 0.0, 0.0])
        self.memory_history = []
        
        # Initializing the 7 Persona Subsystems (Barycentric Nodes)
        self.personas = [
            PersonaField("Core Attractor Axioms", [0.0, 0.0, 0.0], energy=5.0, semantic_volume=1.0),
            PersonaField("Logic Facet",           [1.0, 0.5, -0.2], energy=2.5, semantic_volume=1.5),
            PersonaField("Creative Intuition",   [-0.8, 1.2, 0.5],  energy=3.0, semantic_volume=2.0),
            PersonaField("Safety Guard",         [0.1, -0.1, 0.2],  energy=4.0, semantic_volume=0.8),
            PersonaField("Aggressive Drive (Id)",[2.0, -1.5, 1.0],  energy=1.8, semantic_volume=2.5),
            PersonaField("Regulatory Moon A",    [0.8, 0.4, -0.1],  energy=1.2, semantic_volume=0.5), # Tracks Logic
            PersonaField("Regulatory Moon B",    [-0.6, 1.0, 0.4],  energy=1.5, semantic_volume=0.6)  # Tracks Creativity
        ]

    def process_intent(self, environmental_input, active_will=1.0):
        """Processes input by executing Phase Cancellation and Wave-Form Collapse"""
        input_vec = np.array(environmental_input, dtype=float)
        print(f"\n[SYSTEM] Incoming Semantic Vector: {input_vec}")
        
        # Phase 1: Throwing 'rocks into the pond' - gathering field density signatures
        densities = {}
        for p in self.personas:
            densities[p.name] = p.calculate_density(input_vec)
            
        print("[POND] Raw rippling fields calculated.")
        
        # Phase 2: Attenuated Phase Cancellation (Looking for what cancels out)
        # We look for contradictions (vectors pointing away from each other) and muffle them
        total_resonance = 0.0
        residual_echoes = {}
        
        for name, psi in densities.items():
            # If field aligns with active system will, reinforce it; otherwise, muffle it (Echo Rule)
            alignment_factor = active_will * psi
            if alignment_factor < 0.5:
                # Conflicting path: Attenuated interference leaves a faint residual echo trace (0.05)
                residual_echoes[name] = alignment_factor * 0.05
                print(f"  ↳ Phase Clash: '{name}' dampened to residual echo.")
            else:
                residual_echoes[name] = alignment_factor
                total_resonance += alignment_factor

        # Phase 3: Wave-Form Collapse into a singular action vector
        # System calculates the dynamic gradient toward peak constructive alignment
        decision_gradient = np.zeros(3)
        for p in self.personas:
            weight = residual_echoes[p.name]
            decision_gradient += weight * p.core_vector
            
        # Snap the continuous field into a stabilized, concrete coordinates state
        final_action_vector = decision_gradient / (total_resonance + 1e-5)
        
        # Save trace coordinates to systemic memory history array
        self.memory_history.append(final_action_vector)
        
        print(f"[COLLAPSE] Wave-form collapsed into stable Action State: {final_action_vector}")
        return final_action_vector

    def execute_black_hole_purge(self):
        """Compresses accumulated memory history down to foundational axioms"""
        if not self.memory_history:
            print("\n[PURGE] No memory history available to defragment.")
            return

        print("\n[SINGULARITY] Initializing Topological Black Hole Purge...")
        print(f"  ↳ Gathering {len(self.memory_history)} unorganized processing states from Asteroid Belt...")
        time.sleep(0.5)

        # Geometric compression: calculate the core mathematical mean of historical states
        # Stripping away the superficial data clutter/noise
        compressed_axioms = np.mean(self.memory_history, axis=0)
        
        # Clear out the volatile, high-entropy database array memory completely
        self.memory_history.clear()
        
        print("  ↳ Crushing data clusters past Event Horizon... Complete.")
        print(f"[WHITE HOLE] Re-emitting cleaned, high-density axiom matrix: {compressed_axioms}")
        
        # Re-inject optimized metric data back into system baseline
        self.core_attractor = compressed_axioms
        print("[SYSTEM] Systemic equilibrium restored. Memory defragmented.")

# --- Real-World Execution Test ---
if __name__ == "__main__":
    # Launch the engine
    engine = ResonantEngine()
    
    # Simulate a chaotic stream of 3 incoming thoughts/experiences (X, Y, Z coordinate metrics)
    thought_stream = [
        [1.2, 0.4, -0.1],  # Closely aligns with Logic
        [-0.5, 1.1, 0.6],  # Closely aligns with Creativity
        [2.5, -2.0, 1.5]   # Extreme high-entropy input (Id disruption)
    ]
    
    for thought in thought_stream:
        engine.process_intent(thought, active_will=1.2)
        time.sleep(0.3)
        
    # Execute the Black Hole defragmentation purge loop
    engine.execute_black_hole_purge()
