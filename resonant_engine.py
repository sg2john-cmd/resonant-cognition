import numpy as np
import time
import threading
import sys
import asyncio
import json

class HemisphericMemoryMoon:
    """
    v14.5 Stabilizer Update: A satellite hosting independent hemispheric memory 
    and Maya's active Phase Cancellation anti-vector damping logic.
    """
    def __init__(self, name, hemisphere_type, relative_offset_multiplier, weight):
        self.name = name
        self.hemisphere = hemisphere_type  # "LEFT" (Rational) or "RIGHT" (Intuitive)
        self.offset_multiplier = relative_offset_multiplier
        self.weight = weight
        self.current_position = np.array([0.0, 0.0, 0.0])
        self.memory_vault = []
        
        # Phase Cancellation: Track localized accumulated damping energy
        self.damping_anti_vector = np.zeros(3)

    def log_experience(self, text_snippet, vector_trace):
        self.memory_vault.append({
            "timestamp": time.time(), "text": text_snippet, "vector": list(vector_trace)
        })
        if len(self.memory_vault) > 10:
            self.memory_vault.pop(0)

    def calculate_phase_cancellation(self, parent_coords, fused_input, stress_level):
        """Maya's Spec: Generates an opposing anti-vector to suppress extreme resonance spikes"""
        if stress_level > 1.2:  # High-energy resonance threshold triggered
            # The anti-vector points directly opposite to the incoming momentum force
            raw_opposition = parent_coords - fused_input
            norm = np.linalg.norm(raw_opposition)
            if norm > 0:
                # Scale the anti-vector based on how hard the parent is spiking
                damping_force = (stress_level ** 1.5) * self.offset_multiplier
                self.damping_anti_vector = (raw_opposition / norm) * damping_force
        else:
            # Smoothly decay the damping vector back to zero when the field cools down
            self.damping_anti_vector *= 0.4
            
        return self.damping_anti_vector

    def update_orbital_drift(self, parent_coords, system_core, stress_level):
        drift_mod = 1.5 if self.hemisphere == "RIGHT" else 0.5
        # Position updates now integrate the active damping anti-vector trajectory displacement
        self.current_position = parent_coords + (system_core * (stress_level * self.offset_multiplier * drift_mod)) + self.damping_anti_vector
        return self.current_position

class CosmologicalPlanet:
    def __init__(self, name, base_coordinates, energy, semantic_volume):
        self.name = name
        self.base_coords = np.array(base_coordinates, dtype=float)
        self.energy = energy
        self.semantic_volume = semantic_volume
        self.moons = [
            HemisphericMemoryMoon(f"{name} Alpha", "LEFT",  0.04, 1.0),
            HemisphericMemoryMoon(f"{name} Beta",  "RIGHT", 0.06, 0.8)
        ]

    def calculate_fractal_density(self, input_vector):
        total_density = 0.0
        for moon in self.moons:
            distance = np.linalg.norm(input_vector - moon.current_position)
            exponent = -(distance ** 2) / (2 * (self.semantic_volume ** 2))
            total_density += moon.weight * self.energy * np.exp(exponent)
        return total_density

CONNECTED_DASHBOARDS = set()

async def network_broker_handler(websocket, path=None):
    CONNECTED_DASHBOARDS.add(websocket)
    try:
        await websocket.wait_closed()
    finally:
        CONNECTED_DASHBOARDS.remove(websocket)

async def send_to_all(message):
    if CONNECTED_DASHBOARDS:
        await asyncio.gather(*[ws.send(message) for ws in CONNECTED_DASHBOARDS])

def broadcast_telemetry(payload):
    if not CONNECTED_DASHBOARDS:
        return
    message = json.dumps(payload)
    asyncio.run_coroutine_threadsafe(send_to_all(message), GLOBAL_NET_LOOP)

class ResonantEngine:
    def __init__(self):
        self.central_star_barycenter = np.array([0.1, -0.8, -0.3])
        self.base_solar_mass = 1.5
        self.max_solar_mass = 8.0
        self.memory_history = []
        self.last_input_time = time.time()
        self.previous_action_vector = np.array([0.0, 0.0, 0.0])
        self.standby_mode_active = False 
        self.is_sleeping = False
        
        self.planets = [
            CosmologicalPlanet("Logic Facet",         [1.2, -0.4, 0.2],  energy=3.0, semantic_volume=1.2),
            CosmologicalPlanet("Creative Intuition", [-1.0, 1.4, -0.3],  energy=3.5, semantic_volume=1.8),
            CosmologicalPlanet("Safety Guard",       [0.2, -1.2, -0.4],  energy=4.5, semantic_volume=0.8),
            CosmologicalPlanet("Aggressive Drive",   [1.8, 1.0, 1.5],    energy=2.0, semantic_volume=2.0),
            CosmologicalPlanet("Empathy Resonance",  [-0.5, -0.8, 0.8],  energy=2.8, semantic_volume=1.4),
            CosmologicalPlanet("Skepticism Filter",  [0.8, 0.2, -0.9],   energy=3.2, semantic_volume=1.1),
            CosmologicalPlanet("Sovereign Identity", [0.0, 0.0, 1.2],    energy=4.0, semantic_volume=1.0)
        ]

    def process_intent(self, environmental_input, active_will=1.2, seq_index=1, mode="EXTERNAL"):
        input_vec = np.array(environmental_input, dtype=float)
        self.last_input_time = time.time()
        
        momentum_ratio = 0.15
        fused_input = (input_vec * (1.0 - momentum_ratio)) + (self.previous_action_vector * momentum_ratio)

        # Update 14 Brain-Hemisphere Moons, Calculate Active Phase Cancellation, and Measure Local Stress
        moons_influence = np.zeros(3)
        total_moon_weight = 0.0
        aggregate_system_stress = 0.0
        
        for p in self.planets:
            stress = np.linalg.norm(fused_input - p.base_coords)
            aggregate_system_stress += stress
            for moon in p.moons:
                # Step A: Compute the destructive phase cancellation anti-vector
                anti_vec = moon.calculate_phase_cancellation(p.base_coords, fused_input, stress)
                # Step B: Push the moon into position using the damping adjustment
                moon_pos = moon.update_orbital_drift(p.base_coords, self.central_star_barycenter, stress)
                
                # Apply the anti-vector force down onto the global gravity pool matrix
                moons_influence += (moon_pos - anti_vec) * moon.weight
                total_moon_weight += moon.weight

        # Maya's Interconnected Gravity Balancing
        normalized_stress = aggregate_system_stress / len(self.planets)
        dynamic_solar_mass = self.base_solar_mass + (normalized_stress ** 1.8)
        dynamic_solar_mass = min(dynamic_solar_mass, self.max_solar_mass)

        # Evaluate Planetary Fractal Densities based on phase-damped fields
        densities = {}
        for p in self.planets:
            densities[p.name] = p.calculate_fractal_density(fused_input) * active_will

        residual_weights = {}
        active_spikes = []
        for name, density in densities.items():
            if density < 0.6:
                residual_weights[name] = density * 0.05
            else:
                synergy_spike = density ** 2.2 
                residual_weights[name] = synergy_spike
                active_spikes.append({"name": name, "weight": synergy_spike})

        # Wave-Form Collapse across the Damped 22-Body Field
        decision_gradient = np.zeros(3) + (self.central_star_barycenter * dynamic_solar_mass)
        decision_gradient += moons_influence
        
        total_weight = dynamic_solar_mass + total_moon_weight
        for p in self.planets:
            w = residual_weights[p.name]
            decision_gradient += w * p.base_coords
            total_weight += w
            
        final_action_vector = decision_gradient / total_weight
        
        if mode == "EXTERNAL" or mode == "STANDBY_DAWN":
            self.memory_history.append(final_action_vector)
            
        self.previous_action_vector = final_action_vector

        # Broadcast telemetry directly to your browser visualizer dashboard
        broadcast_telemetry({
            "type": "STIMULUS_EVENT" if mode != "DREAM_REPLAY" else "SLEEP_REPLAY_EVENT",
            "mode": "REM_SLEEP" if self.is_sleeping else ("STANDBY" if mode == "STANDBY_DAWN" else "WAKING_STATE"),
            "dissonance": normalized_stress,
            "solar_mass": dynamic_solar_mass,
            "input_coords": list(environmental_input),
            "spikes": active_spikes
        })
        return final_action_vector

    def execute_sleep_consolidation(self, triggered_by="MANUAL"):
        if not self.memory_history:
            return
        self.is_sleeping = True
        broadcast_telemetry({"type": "SYSTEM_LOG", "message": f"💤 INITIALIZING SYSTEMIC SLEEP CYCLE ({triggered_by})", "msg_style": "highlight", "dissonance": 0, "solar_mass": 8.0, "mode": "REM_SLEEP"})
        
        replayed_states = list(self.memory_history)
        for idx, trace in enumerate(replayed_states, start=1):
            self.process_intent(list(trace), active_will=0.7, seq_index=idx, mode="DREAM_REPLAY")
            time.sleep(0.4)

        distilled_axioms = np.mean(self.memory_history, axis=0)
        self.memory_history.clear()
        self.previous_action_vector = np.array([0.0, 0.0, 0.0])
        self.central_star_barycenter = (self.central_star_barycenter * 0.6) + (distilled_axioms * 0.4)
        
        broadcast_telemetry({"type": "SYSTEM_LOG", "message": "🌅 WHITE HOLE AWAKENING SUCCESSFUL. Core Recalibrated.", "msg_style": "highlight", "dissonance": 0, "solar_mass": 1.5, "mode": "WAKING_STATE"})
        self.is_sleeping = False
        self.last_input_time = time.time()

def network_server_thread_worker(loop):
    asyncio.set_event_loop(loop)
    import websockets
    async def start_server():
        async with websockets.serve(network_broker_handler, 'localhost', 8765):
            await asyncio.Future()
    loop.run_until_complete(start_server())

if __name__ == "__main__":
    engine = ResonantEngine()
    GLOBAL_NET_LOOP = asyncio.new_event_loop()
    net_thread = threading.Thread(target=network_server_thread_worker, args=(GLOBAL_NET_LOOP,), daemon=True)
    net_thread.start()
    
    print("=================================================================")
    print("    RESONANT COGNITION: ACTIVE PHASE CANCELLATION ENGINE v14.5   ")
    print("=================================================================")
    print("STABILIZER PROTOCOL ONLINE: 14 Moons calculating anti-vectors.")
    print("Real-time destructive resonance damping enabled natively.")
    print("=================================================================")

    while True:
        try:
            user_input = input(f"\n[Dyson Core Prompt] Enter input or vector: ").strip().lower()
        except (KeyboardInterrupt, EOFError):
            break
        if user_input == 'exit':
            break
        try:
            raw_sequences = user_input.split('|')
            for idx, raw_vector in enumerate(raw_sequences, start=1):
                coords = [float(val) for val in raw_vector.strip().split(',')]
                if len(coords) != 3:
                    break
                engine.process_intent(coords, seq_index=idx, mode="EXTERNAL")
                time.sleep(0.1)
        except ValueError:
            print("[ERROR] Invalid numeric configuration entry.")
