import numpy as np
import time
import threading
import sys

class StructuralComponent:
    def __init__(self, layer_type, coordinate_offset, energy):
        self.layer_type = layer_type
        self.offset = np.array(coordinate_offset, dtype=float)
        self.energy = energy

class FractalPersona:
    def __init__(self, name, base_coordinates, energy, semantic_volume):
        self.name = name
        self.base_coords = np.array(base_coordinates, dtype=float)
        self.energy = energy
        self.semantic_volume = semantic_volume
        self.internal_layers = [
            StructuralComponent("Id",        [0.4, 0.5, 0.3],  energy * 0.8),
            StructuralComponent("Ego",       [0.0, 0.0, 0.0],  energy * 1.0),
            StructuralComponent("Superego",  [-0.3, -0.4, -0.2], energy * 1.2)
        ]

    def calculate_fractal_density(self, input_vector):
        total_density = 0.0
        for layer in self.internal_layers:
            abs_coords = self.base_coords + layer.offset
            distance = np.linalg.norm(input_vector - abs_coords)
            exponent = -(distance ** 2) / (2 * (self.semantic_volume ** 2))
            total_density += layer.energy * np.exp(exponent)
        return total_density

class ResonantEngine:
    def __init__(self):
        self.core_attractor = np.array([0.2, -0.6, -0.1])
        self.memory_history = []
        self.last_input_time = time.time()
        self.previous_action_vector = np.array([0.0, 0.0, 0.0])
        self.standby_mode_active = False 
        
        self.planets = [
            FractalPersona("Logic Facet",         [1.2, -0.4, 0.2],  energy=3.0, semantic_volume=1.2),
            FractalPersona("Creative Intuition", [-1.0, 1.4, -0.3],  energy=3.5, semantic_volume=1.8),
            FractalPersona("Safety Guard",       [0.2, -1.2, -0.4],  energy=4.5, semantic_volume=0.8),
            FractalPersona("Aggressive Drive",   [1.8, 1.0, 1.5],    energy=2.0, semantic_volume=2.0)
        ]

    def process_intent(self, environmental_input, active_will=1.2, seq_index=1, mode="EXTERNAL"):
        input_vec = np.array(environmental_input, dtype=float)
        self.last_input_time = time.time()
        
        momentum_ratio = 0.15
        fused_input = (input_vec * (1.0 - momentum_ratio)) + (self.previous_action_vector * momentum_ratio)
        
        if mode == "EXTERNAL":
            print(f"\n[EXTERNAL STIMULUS STEP {seq_index}] Vector: {input_vec}")
        else:
            print(f"\n[{mode} STIMULUS] Vector: {input_vec}")

        # 1. Update Dynamic Moons (FIXED: List array [0, 1] explicitly typed out)
        moons_influence = np.zeros(3)
        for target_idx in range(2):  # Index 0 is Logic, Index 1 is Creative Intuition
            p = self.planets[target_idx]
            stress = np.linalg.norm(fused_input - p.base_coords)
            moon_pos = p.base_coords + (self.core_attractor * (stress * 0.05))
            moons_influence += moon_pos * 1.5

        # 2. Gather Fractal Densities
        densities = {}
        for p in self.planets:
            densities[p.name] = p.calculate_fractal_density(fused_input) * active_will

        # 3. Phase Cancellation & Synergy Spikes
        residual_weights = {}
        for name, density in densities.items():
            if density < 0.6:
                residual_weights[name] = density * 0.05
            else:
                synergy_spike = density ** 2.2 
                residual_weights[name] = synergy_spike
                if mode == "EXTERNAL":
                    print(f"  🔥 Constructive Resonance: '{name}' spiked (Weight: {synergy_spike:.2f})")

        # 4. Wave-Form Collapse
        decision_gradient = np.zeros(3) + (self.core_attractor * 2.5)
        decision_gradient += moons_influence
        
        total_weight = 2.5 + 3.0
        for p in self.planets:
            w = residual_weights[p.name]
            decision_gradient += w * p.base_coords
            total_weight += w
            
        final_action_vector = decision_gradient / total_weight
        self.memory_history.append(final_action_vector)
        self.previous_action_vector = final_action_vector
        
        print(f"[COLLAPSE] Resulting Action State: {final_action_vector}")
        if mode == "STANDBY_DAWN":
            print(f"  🧠 System Opinion: Internal field drifting toward coordinate trend: {final_action_vector * 1.1}")
        return final_action_vector

    def execute_black_hole_purge(self):
        if not self.memory_history:
            print("\n[PURGE] No memory history available to defragment.")
            return
        print("\n[SINGULARITY] Initializing Fractal Black Hole Purge...")
        compressed_axioms = np.mean(self.memory_history, axis=0)
        self.memory_history.clear()
        self.previous_action_vector = np.array([0.0, 0.0, 0.0])
        self.core_attractor = (self.core_attractor * 0.7) + (compressed_axioms * 0.3)
        print(f"[WHITE HOLE] Baseline optimized. Core Anchor recalibrated: {self.core_attractor}")

def standby_clock_worker(engine):
    while True:
        time.sleep(5.0)
        if engine.standby_mode_active and (time.time() - engine.last_input_time >= 5.0) and not sys.stdin.closed:
            random_asteroid_noise = np.random.uniform(-1.5, 1.5, 3)
            engine.process_intent(random_asteroid_noise, active_will=0.8, mode="STANDBY_DAWN")
            if len(engine.memory_history) >= 5:
                engine.execute_black_hole_purge()
            print("\nEnter coordinates, sequence stream, or system command: ", end="", flush=True)

if __name__ == "__main__":
    engine = ResonantEngine()
    
    standby_thread = threading.Thread(target=standby_clock_worker, args=(engine,), daemon=True)
    standby_thread.start()

    print("=================================================================")
    print("    RESONANT COGNITION WORKSTATION CORE ENGINE v5.5              ")
    print("=================================================================")
    print("INPUT FORMATS:")
    print("  Single Thought : Type 3 metrics separated by commas (e.g., 1,0.5,-0.2)")
    print("  Sequence Stream: Separate multiple thoughts using a pipe '|'")
    print("                   (e.g., 1,0.5,0 | -1,1.2,0.5 | 0.2,-0.8,-0.1)")
    print("")
    print("SYSTEM COMMANDS:")
    print("  'standby' - Toggles autonomous background processing ON/OFF")
    print("  'purge'   - Manually executes a Black Hole defragmentation cycle")
    print("  'exit'    - Terminates execution environment safely")
    print("=================================================================")

    while True:
        try:
            current_status = "ACTIVE" if engine.standby_mode_active else "DORMANT"
            user_input = input(f"\n[Standby: {current_status}] Enter input or command: ").strip().lower()
        except (KeyboardInterrupt, EOFError):
            break
            
        if user_input == 'exit':
            print("[SYSTEM] Shutting down processing fields safely. Goodbye.")
            break
        elif user_input == 'purge':
            engine.execute_black_hole_purge()
            continue
        elif user_input == 'standby':
            engine.standby_mode_active = not engine.standby_mode_active
            status_text = "ENABLED" if engine.standby_mode_active else "DISABLED (Resource Preservation Mode)"
            print(f"[TOGGLE] Standby Default Mode Network is now: {status_text}")
            continue
            
        try:
            raw_sequences = user_input.split('|')
            for idx, raw_vector in enumerate(raw_sequences, start=1):
                coords = [float(val) for val in raw_vector.strip().split(',')]
                if len(coords) != 3:
                    print(f"[ERROR] Sequence position {idx} invalid. Loop aborted.")
                    break
                engine.process_intent(coords, seq_index=idx, mode="EXTERNAL")
                time.sleep(0.2)
        except ValueError:
            print("[ERROR] Invalid numeric configuration entry. Reference the menu layout rules above.")
