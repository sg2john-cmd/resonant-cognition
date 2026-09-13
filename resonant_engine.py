import numpy as np
import time
import threading
import sys
import asyncio
import json

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

# Global WebSockets Broker to handle live communication streams natively
CONNECTED_DASHBOARDS = set()

async def network_broker_handler(websocket, path=None):
    """Registers streams and listens for remote vector injections directly from the Web UI"""
    CONNECTED_DASHBOARDS.add(websocket)
    try:
        async for message in websocket:
            # Catch raw string sequences transmitted directly from the browser sidebar
            txt_command = message.strip().lower()
            if txt_command == 'sleep':
                # Force sleep loops asynchronously
                threading.Thread(target=engine.execute_sleep_consolidation, args=("REMOTE_GUI",), daemon=True).start()
            elif txt_command == 'standby':
                engine.standby_mode_active = not engine.standby_mode_active
            else:
                # Parse vector numbers straight into processing steps
                try:
                    raw_sequences = txt_command.split('|')
                    for idx, raw_vector in enumerate(raw_sequences, start=1):
                        coords = [float(val) for val in raw_vector.strip().split(',')]
                        if len(coords) == 3:
                            engine.process_intent(coords, seq_index=idx, mode="EXTERNAL")
                except Exception:
                    pass
    except asyncio.exceptions.ConnectionClosedOK:
        pass
    finally:
        CONNECTED_DASHBOARDS.remove(websocket)


# FIXED: Explicit async wrapper to prevent the "A coroutine object is required" TypeError
async def send_to_all(message):
    if CONNECTED_DASHBOARDS:
        await asyncio.gather(*[ws.send(message) for ws in CONNECTED_DASHBOARDS])

def broadcast_telemetry(payload):
    """Fires telemetry dictionaries straight across the local hardware port loop"""
    if not CONNECTED_DASHBOARDS:
        return
    message = json.dumps(payload)
    # Safely schedule the true coroutine wrapper inside the running network thread loop
    asyncio.run_coroutine_threadsafe(send_to_all(message), GLOBAL_NET_LOOP)



class ResonantEngine:
    def __init__(self):
        # John's Solar Compass: Heavy moral baseline boundary field
        self.central_star_barycenter = np.array([0.1, -0.8, -0.3])
        self.base_solar_mass = 1.5
        self.max_solar_mass = 8.0
        
        self.memory_history = []
        self.last_input_time = time.time()
        self.previous_action_vector = np.array([0.0, 0.0, 0.0])
        self.standby_mode_active = False 
        self.is_sleeping = False
        
        # True 7-Planet Grid Node Array
        self.planets = [
            CosmologicalPlanet("Logic Facet",         [1.2, -0.4, 0.2],  energy=3.0, semantic_volume=1.2),
            CosmologicalPlanet("Creative Intuition", [-1.0, 1.4, -0.3],  energy=3.5, semantic_volume=1.8),
            CosmologicalPlanet("Safety Guard",       [0.2, -1.2, -0.4],  energy=4.5, semantic_volume=0.8),
            CosmologicalPlanet("Aggressive Drive",   [1.8, 1.0, 1.5],    energy=2.0, semantic_volume=2.0),
            CosmologicalPlanet("Empathy Resonance",  [-0.5, -0.8, 0.8],  energy=2.8, semantic_volume=1.4),
            CosmologicalPlanet("Skepticism Filter",  [0.8, 0.2, -0.9],   energy=3.2, semantic_volume=1.1),
            CosmologicalPlanet("Sovereign Identity", [0.0, 0.0, 1.2],    energy=4.0, semantic_volume=1.0)
        ]
        
        # Deploying 2 unique corrective moons inside EVERY single planet (14 total)
        for p in self.planets:
            p.add_satellite(f"{p.name} Alpha Moon", offset_multiplier=0.04, weight=1.0)
            p.add_satellite(f"{p.name} Beta Moon",  offset_multiplier=0.06, weight=0.8)

    def process_intent(self, environmental_input, active_will=1.2, seq_index=1, mode="EXTERNAL"):
        input_vec = np.array(environmental_input, dtype=float)
        self.last_input_time = time.time()
        
        momentum_ratio = 0.15
        fused_input = (input_vec * (1.0 - momentum_ratio)) + (self.previous_action_vector * momentum_ratio)
        
        if mode == "EXTERNAL":
            print(f"\n[EXTERNAL COMET STREAM {seq_index}] Input Vector: {input_vec}")
        elif mode == "DREAM_REPLAY":
            print(f"  🎬 [REM CYCLE] Replaying State Trace {seq_index}: {input_vec}")
        else:
            print(f"\n[{mode} INPUT] Vector: {input_vec}")

        # Update 14 Nested Satellite Moons
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

        # Maya's Interconnected Gravity Balancing
        normalized_stress = aggregate_system_stress / len(self.planets)
        dynamic_solar_mass = self.base_solar_mass + (normalized_stress ** 1.8)
        dynamic_solar_mass = min(dynamic_solar_mass, self.max_solar_mass)
        
        if mode == "EXTERNAL":
            print(f"[ORBIT] 7-Planet Field Dissonance: {normalized_stress:.2f} | Adaptive Solar Pull: {dynamic_solar_mass:.2f}")

        # Evaluate Planetary Fractal Densities
        densities = {}
        for p in self.planets:
            densities[p.name] = p.calculate_fractal_density(fused_input) * active_will

        # Phase Cancellation & Synergy Spikes
        residual_weights = {}
        active_spikes = []
        for name, density in densities.items():
            if density < 0.6:
                residual_weights[name] = density * 0.05
            else:
                synergy_spike = density ** 2.2 
                residual_weights[name] = synergy_spike
                active_spikes.append({"name": name, "weight": synergy_spike})
                if mode == "EXTERNAL":
                    print(f"  🔥 Constructive Resonance: '{name}' spiked (Weight: {synergy_spike:.2f})")

        # Wave-Form Collapse across the 22-Body Field
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

        # Broadcast live data straight to Web UI Panel
        broadcast_telemetry({
            "type": "STIMULUS_EVENT" if mode != "DREAM_REPLAY" else "SLEEP_REPLAY_EVENT",
            "mode": "REM_SLEEP" if self.is_sleeping else ("STANDBY" if mode == "STANDBY_DAWN" else "WAKING_STATE"),
            "dissonance": normalized_stress,
            "solar_mass": dynamic_solar_mass,
            "input_coords": list(environmental_input),
            "spikes": active_spikes
        })
        
        if mode == "EXTERNAL":
            print(f"[COLLAPSE] Unified 22-Body Action State: {final_action_vector}")
        return final_action_vector
    def execute_sleep_consolidation(self, triggered_by="MANUAL"):
        """Triggers the time-bounded two-pass sleep filtration network loop"""
        if not self.memory_history:
            print(f"\n[SLEEP] Entry rejected. Memory buffers empty. No data to consolidate.")
            return

        self.is_sleeping = True
        broadcast_telemetry({"type": "SYSTEM_LOG", "message": f"💤 INITIALIZING SYSTEMIC SLEEP CYCLE ({triggered_by})", "msg_style": "highlight", "dissonance": 0, "solar_mass": 8.0, "mode": "REM_SLEEP"})
        
        print(f"\n=================================================================")
        print(f"       💤 INITIALIZING SYSTEMIC SLEEP CYCLE ({triggered_by} OVERRIDE)")
        print(f"=================================================================")
        print(f"[SLEEP] External comet arrays locked out. Core consciousness deactivated.")
        print(f"[SLEEP] Total waking memory trace units queued: {len(self.memory_history)}")
        time.sleep(1.0)

        # PASS 1: Synaptic Dream Replay
        print("\n🌙 PHASE I: Synaptic Replay Loop (Deep REM Processing)")
        print("-----------------------------------------------------------------")
        replayed_states = list(self.memory_history)
        for idx, trace in enumerate(replayed_states, start=1):
            self.process_intent(list(trace), active_will=0.7, seq_index=idx, mode="DREAM_REPLAY")
            time.sleep(0.4)

        # PASS 2: Synaptic Pruning & Singularity Compression
        print("\n✨ PHASE II: Synaptic Pruning & Thermodynamic Consolidation")
        print("-----------------------------------------------------------------")
        broadcast_telemetry({"type": "SYSTEM_LOG", "message": "✨ PHASE II: Executing Thermodynamic Compression...", "msg_style": "", "dissonance": 0, "solar_mass": 4.0, "mode": "REM_SLEEP"})
        time.sleep(0.5)
        
        distilled_axioms = np.mean(self.memory_history, axis=0)
        self.memory_history.clear()
        self.previous_action_vector = np.array([0.0, 0.0, 0.0])
        
        # PASS 3: The White Hole Awakening parameter shift
        self.central_star_barycenter = (self.central_star_barycenter * 0.6) + (distilled_axioms * 0.4)
        
        print(f"\n[WHITE HOLE] Realignment Complete. New Solar Moral Base Matrix: {self.central_star_barycenter}")
        print("=================================================================")
        print("       🌅 COGNITIVE WAKING TRANSITION EXECUTED SUCCESSFUL")
        print("=================================================================")
        
        broadcast_telemetry({
            "type": "SYSTEM_LOG", "message": "🌅 WHITE HOLE AWAKENING SUCCESSFUL. Core Recalibrated.", "msg_style": "highlight",
            "dissonance": 0, "solar_mass": 1.5, "mode": "WAKING_STATE"
        })
        
        self.is_sleeping = False
        self.last_input_time = time.time()

def idle_sleep_timer_worker(engine):
    while True:
        time.sleep(1.0)
        if engine.standby_mode_active and not engine.is_sleeping:
            if time.time() - engine.last_input_time >= 15.0 and len(engine.memory_history) > 0:
                engine.execute_sleep_consolidation(triggered_by="AUTO_IDLE_TIMER")
                print("\n[ACTIVE] Workstation back online.")
                print(f"\n[Standby: ACTIVE] Enter input or command: ", end="", flush=True)

# Modernized Asynchronous network server management thread loop (FIXED for websockets 14.0+)
def network_server_thread_worker(loop):
    asyncio.set_event_loop(loop)
    import websockets
    
    async def start_server():
        async with websockets.serve(network_broker_handler, 'localhost', 8765):
            await asyncio.Future()  # Keeps the server running indefinitely
            
    loop.run_until_complete(start_server())

if __name__ == "__main__":
    engine = ResonantEngine()
    
    # Ignition of the Local Asynchronous Handshake Network Server
    GLOBAL_NET_LOOP = asyncio.new_event_loop()
    net_thread = threading.Thread(target=network_server_thread_worker, args=(GLOBAL_NET_LOOP,), daemon=True)
    net_thread.start()
    
    idle_worker = threading.Thread(target=idle_sleep_timer_worker, args=(engine,), daemon=True)
    idle_worker.start()

    print("=================================================================")
    print("    RESONANT COGNITION LIVE BROADCASTER CORE ENGINE v9.5        ")
    print("=================================================================")
    print("MAPPED ASSETS: 22-Body Gravitational Spectrum Live Broadcasting Active.")
    print("Local WebSockets server tracking communication channel: Port 8765")
    print("=================================================================")

    while True:
        try:
            current_status = "ACTIVE" if engine.standby_mode_active else "DORMANT"
            user_input = input(f"\n[Standby: {current_status}] Enter input or command: ").strip().lower()
        except (KeyboardInterrupt, EOFError):
            break
            
        if user_input == 'exit':
            break
        elif user_input == 'sleep':
            engine.execute_sleep_consolidation(triggered_by="MANUAL_COMMAND")
            continue
        elif user_input == 'standby':
            engine.standby_mode_active = not engine.standby_mode_active
            continue
            
        try:
            if engine.is_sleeping:
                continue
            raw_sequences = user_input.split('|')
            for idx, raw_vector in enumerate(raw_sequences, start=1):
                coords = [float(val) for val in raw_vector.strip().split(',')]
                if len(coords) != 3:
                    break
                engine.process_intent(coords, seq_index=idx, mode="EXTERNAL")
                time.sleep(0.1)
        except ValueError:
            print("[ERROR] Invalid numeric configuration entry.")
