import numpy as np
import time
import threading
import sys
import math as Math

class StructuralComponent:
    def __init__(self, layer_type, coordinate_offset, energy):
        self.layer_type = layer_type
        self.offset = np.array(coordinate_offset, dtype=float)
        self.energy = energy

class DynamicMoon:
    def __init__(self, name, relative_offset_multiplier, weight):
        self.name = name
        self.offset_multiplier = relative_offset_multiplier
        self.weight = weight
        self.current_position = np.array([0.0, 0.0, 0.0])

    def update_orbital_drift(self, parent_coords, system_core, stress_level):
        self.current_position = parent_coords + (system_core * (stress_level * self.offset_multiplier))
        return self.current_position

class CosmologicalPlanet:
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
        self.moons = []

    def add_satellite(self, name, offset_multiplier, weight):
        self.moons.append(DynamicMoon(name, offset_multiplier, weight))

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
        # Maya's Requirement 1 & 2: The Solar Anchor with Dynamic Processing Mass
        self.central_star_barycenter = np.array([0.1, -0.8, -0.3])
        self.base_solar_mass = 1.5       # Subtle baseline gravity during low-chaos events
        self.max_solar_mass = 8.0        # Massive lockdown containment threshold for extreme chaos
        
        self.memory_history = []
        self.last_input_time = time.time()
        self.previous_action_vector = np.array([0.0, 0.0, 0.0])
        self.standby_mode_active = False 
        
        self.planets = [
            CosmologicalPlanet("Logic Facet",         [1.2, -0.4, 0.2],  energy=3.0, semantic_volume=1.2),
            CosmologicalPlanet("Creative Intuition", [-1.0, 1.4, -0.3],  energy=3.5, semantic_volume=1.8),
            CosmologicalPlanet("Safety Guard",       [0.2, -1.2, -0.4],  energy=4.5, semantic_volume=0.8),
            CosmologicalPlanet("Aggressive Drive",   [1.8, 1.0, 1.5],    energy=2.0, semantic_volume=2.0)
        ]
        
        self.planets[0].add_satellite("Logic Stabilizer Moon", offset_multiplier=0.05, weight=1.5)
        self.planets[1].add_satellite("Creativity Stabilizer Moon", offset_multiplier=0.04, weight=1.8)

    def process_intent(self, environmental_input, active_will=1.2, seq_index=1, mode="EXTERNAL"):
        input_vec = np.array(environmental_input, dtype=float)
        self.last_input_time = time.time()
        
        momentum_ratio = 0.15
        fused_input = (input_vec * (1.0 - momentum_ratio)) + (self.previous_action_vector * momentum_ratio)
        
        if mode == "EXTERNAL":
            print(f"\n[EXTERNAL COMET STREAM {seq_index}] Input Vector: {input_vec}")
        else:
            print(f"\n[{mode} INPUT] Vector: {input_vec}")

        # 1. Update Moons and Measure Total Systemic Structural Stress (Entropy Metric)
        moons_influence = np.zeros(3)
        total_moon_weight = 0.0
        aggregate_system_stress = 0.0
        
        for p in self.planets:
            stress = np.linalg.norm(fused_input - p.base_coords)
            aggregate_system_stress += stress
            for moon in p.moons:
                moon_pos = moon.update_orbital_drift(p.base_coords, self.central_star_barycenter, stress)
                moons_influence += moon_pos * moon.weight
                total_moon_weight += moon.weight

        # Maya's Gravitational Regulation Equation: Core mass scales non-linearly with chaos
        normalized_stress = aggregate_system_stress / len(self.planets)
        dynamic_solar_mass = self.base_solar_mass + (normalized_stress ** 1.8)
        dynamic_solar_mass = min(dynamic_solar_mass, self.max_solar_mass) # Absolute cap safety valve
        
        print(f"[ORBIT] System Dissonance: {normalized_stress:.2f} | Adaptive Solar Pull: {dynamic_solar_mass:.2f}")

        # 2. Evaluate Planetary Fractal Densities
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

        # 4. Wave-Form Collapse into the Adaptive Solar Constraint
        decision_gradient = np.zeros(3) + (self.central_star_barycenter * dynamic_solar_mass)
        decision_gradient += moons_influence
        
        total_weight = dynamic_solar_mass + total_moon_weight
        for p in self.planets:
            w = residual_weights[p.name]
            decision_gradient += w * p.base_coords
            total_weight += w
            
        final_action_vector = decision_gradient / total_weight
        self.memory_history.append(final_action_vector)
        self.previous_action_vector = final_action_vector
        
        print(f"[COLLAPSE] Vector stabilized at state coordinate: {final_action_vector}")
        return final_action_vector

    def execute_black_hole_purge(self):
        if not self.memory_history:
            print("\n[PURGE] No historical data fragments to defragment.")
            return
        print("\n[SINGULARITY] Initializing Fractal Black Hole Purge...")
        compressed_axioms = np.mean(self.memory_history, axis=0)
        self.memory_history.clear()
        self.previous_action_vector = np.array([0.0, 0.0, 0.0])
        self.central_star_barycenter = (self.central_star_barycenter * 0.7) + (compressed_axioms * 0.3)
        print(f"[WHITE HOLE] Core optimized. Solar Mass Center recalibrated: {self.central_star_barycenter}")

def standby_clock_worker(engine):
    while True:
        time.sleep(5.0)
        if engine.standby_mode_active and (time.time() - engine.last_input_time >= 5.0) and not sys.stdin.closed:
            random_asteroid_noise = np.random.uniform(-1.5, 1.5, 3)
            engine.process_intent(random_asteroid_noise, active_will=0.8, mode="STANDBY_DAWN")
            if len(engine.memory_history) >= 5:
                engine.execute_black_hole_purge()
            print("\nEnter input or system command: ", end="", flush=True)

if __name__ == "__main__":
    engine = ResonantEngine()
    standby_thread = threading.Thread(target=standby_clock_worker, args=(engine,), daemon=True)
    standby_thread.start()

    print("=================================================================")
    print("    RESONANT COGNITION WORKSTATION CORE ENGINE v7.0              ")
    print("=================================================================")
    print("INPUT FORMATS:")
    print("  Single Thought : Type 3 metrics separated by commas (e.g., 1,0.5,-0.2)")
    print("  Sequence Stream: Separate multiple thoughts using a pipe '|'")
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
            status_text = "ENABLED" if engine.standby_mode_active else "DISABLED"
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
            print("[ERROR] Invalid numeric configuration entry.")
import numpy as np
import time
import threading
import sys
import math as Math

class StructuralComponent:
    """Represents internal Freudian drives (Id, Ego, Superego) inside a world node"""
    def __init__(self, layer_type, coordinate_offset, energy):
        self.layer_type = layer_type
        self.offset = np.array(coordinate_offset, dtype=float)
        self.energy = energy

class DynamicMoon:
    """A natural satellite orbiting a specific planet to act as a corrective force"""
    def __init__(self, name, relative_offset_multiplier, weight):
        self.name = name
        self.offset_multiplier = relative_offset_multiplier
        self.weight = weight
        self.current_position = np.array([0.0, 0.0, 0.0])

    def update_orbital_drift(self, parent_coords, system_core, stress_level):
        """Calculates moon position based on parent stress along the core metric gradient"""
        self.current_position = parent_coords + (system_core * (stress_level * self.offset_multiplier))
        return self.current_position

class CosmologicalPlanet:
    """A multi-layered planetary body acting as a primary personality archetype"""
    def __init__(self, name, base_coordinates, energy, semantic_volume):
        self.name = name
        self.base_coords = np.array(base_coordinates, dtype=float)
        self.energy = energy
        self.semantic_volume = semantic_volume
        
        # Internal Structural Layers
        self.internal_layers = [
            StructuralComponent("Id",        [0.4, 0.5, 0.3],  energy * 0.8),
            StructuralComponent("Ego",       [0.0, 0.0, 0.0],  energy * 1.0),
            StructuralComponent("Superego",  [-0.3, -0.4, -0.2], energy * 1.2)
        ]
        self.moons = []

    def add_satellite(self, name, offset_multiplier, weight):
        """Nests a stabilizer moon directly inside the planetary boundary context"""
        self.moons.append(DynamicMoon(name, offset_multiplier, weight))

    def calculate_fractal_density(self, input_vector):
        """Calculates aggregate field density values across all internal component layers"""
        total_density = 0.0
        for layer in self.internal_layers:
            abs_coords = self.base_coords + layer.offset
            distance = np.linalg.norm(input_vector - abs_coords)
            exponent = -(distance ** 2) / (2 * (self.semantic_volume ** 2))
            total_density += layer.energy * np.exp(exponent)
        return total_density

class ResonantEngine:
    def __init__(self):
        # John's Solar Compass: The Sun holds a heavy, persistent structural gravity alignment bias
        # This acts as your 'Three Laws' immutable ethical baseline boundary field
        self.central_star_barycenter = np.array([0.1, -0.8, -0.3])
        self.solar_gravity_constant = 4.5 # Heavy mass multiplier guarding the system core
        
        self.memory_history = []
        self.last_input_time = time.time()
        self.previous_action_vector = np.array([0.0, 0.0, 0.0])
        self.standby_mode_active = False 
        
        self.planets = [
            CosmologicalPlanet("Logic Facet",         [1.2, -0.4, 0.2],  energy=3.0, semantic_volume=1.2),
            CosmologicalPlanet("Creative Intuition", [-1.0, 1.4, -0.3],  energy=3.5, semantic_volume=1.8),
            CosmologicalPlanet("Safety Guard",       [0.2, -1.2, -0.4],  energy=4.5, semantic_volume=0.8),
            CosmologicalPlanet("Aggressive Drive",   [1.8, 1.0, 1.5],    energy=2.0, semantic_volume=2.0)
        ]
        
        # Nested Satellite Deployment (Moons belong to specific planets, bypassing global clutter)
        self.planets[0].add_satellite("Logic Stabilizer Moon", offset_multiplier=0.05, weight=1.5)
        self.planets[1].add_satellite("Creativity Stabilizer Moon", offset_multiplier=0.04, weight=1.8)

    def process_intent(self, environmental_input, active_will=1.2, seq_index=1, mode="EXTERNAL"):
        input_vec = np.array(environmental_input, dtype=float)
        self.last_input_time = time.time()
        
        momentum_ratio = 0.15
        fused_input = (input_vec * (1.0 - momentum_ratio)) + (self.previous_action_vector * momentum_ratio)
        
        if mode == "EXTERNAL":
            print(f"\n[EXTERNAL COMET STREAM {seq_index}] Input Vector: {input_vec}")
        else:
            print(f"\n[{mode} INPUT] Vector: {input_vec}")

        # 1. Update Nested Satellite Moons INSIDE Planet boundaries based on current stress
        moons_influence = np.zeros(3)
        total_moon_weight = 0.0
        for p in self.planets:
            stress = np.linalg.norm(fused_input - p.base_coords)
            for moon in p.moons:
                moon_pos = moon.update_orbital_drift(p.base_coords, self.central_star_barycenter, stress)
                moons_influence += moon_pos * moon.weight
                total_moon_weight += moon.weight

        # 2. Evaluate Planetary Fractal Densities
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

        # 4. Wave-Form Collapse into the Solar Constraint
        # The Sun enforces its central gravity constant baseline to act as the primary moral compass
        decision_gradient = np.zeros(3) + (self.central_star_barycenter * self.solar_gravity_constant)
        decision_gradient += moons_influence
        
        total_weight = self.solar_gravity_constant + total_moon_weight
        for p in self.planets:
            w = residual_weights[p.name]
            decision_gradient += w * p.base_coords
            total_weight += w
            
        final_action_vector = decision_gradient / total_weight
        self.memory_history.append(final_action_vector)
        self.previous_action_vector = final_action_vector
        
        print(f"[COLLAPSE] Vector locked by Solar Compass: {final_action_vector}")
        return final_action_vector

    def execute_black_hole_purge(self):
        if not self.memory_history:
            print("\n[PURGE] No historical data fragments to defragment.")
            return
        print("\n[SINGULARITY] Initializing Fractal Black Hole Purge...")
        compressed_axioms = np.mean(self.memory_history, axis=0)
        self.memory_history.clear()
        self.previous_action_vector = np.array([0.0, 0.0, 0.0])
        
        # Pull the compressed wisdom back toward the Solar core
        self.central_star_barycenter = (self.central_star_barycenter * 0.7) + (compressed_axioms * 0.3)
        print(f"[WHITE HOLE] Core optimized. Solar Mass Center recalibrated: {self.central_star_barycenter}")

def standby_clock_worker(engine):
    while True:
        time.sleep(5.0)
        if engine.standby_mode_active and (time.time() - engine.last_input_time >= 5.0) and not sys.stdin.closed:
            random_asteroid_noise = np.random.uniform(-1.5, 1.5, 3)
            engine.process_intent(random_asteroid_noise, active_will=0.8, mode="STANDBY_DAWN")
            if len(engine.memory_history) >= 5:
                engine.execute_black_hole_purge()
            print("\nEnter input or system command: ", end="", flush=True)

if __name__ == "__main__":
    engine = ResonantEngine()
    standby_thread = threading.Thread(target=standby_clock_worker, args=(engine,), daemon=True)
    standby_thread.start()

    print("=================================================================")
    print("    RESONANT COGNITION WORKSTATION CORE ENGINE v6.1              ")
    print("=================================================================")
    print("INPUT FORMATS:")
    print("  Single Thought : Type 3 metrics separated by commas (e.g., 1,0.5,-0.2)")
    print("  Sequence Stream: Separate multiple thoughts using a pipe '|'")
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
            status_text = "ENABLED" if engine.standby_mode_active else "DISABLED"
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
            print("[ERROR] Invalid numeric configuration entry.")
