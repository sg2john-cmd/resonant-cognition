import numpy as np
import json
import http.client
import textwrap

# --- LOCAL RUNNER CONFIGURATION MATRIX ---
LOCAL_API_HOST = "127.0.0.1"
LOCAL_API_PORT = 1234  # Standard port for local OpenAI-compatible inference servers

def get_active_model_name():
    """Queries the local server backend to automatically detect whichever model is currently loaded in VRAM"""
    try:
        conn = http.client.HTTPConnection(LOCAL_API_HOST, LOCAL_API_PORT, timeout=5)
        conn.request("GET", "/v1/models")
        response = conn.getresponse()
        
        if response.status == 200:
            data = json.loads(response.read().decode('utf-8'))
            # Extract the exact identifier string of the active model currently loaded by the user
            if "data" in data and len(data["data"]) > 0:
                model_identifier = data["data"][0]["id"]
                return model_identifier
        return "UNKNOWN_LOCAL_MODEL"
    except Exception:
        # Fallback safe string if the handshake connection fails at boot
        return "UNKNOWN_LOCAL_MODEL"

def query_local_llm(system_prompt, user_prompt, active_model):
    """Fires a request into the local inference pipeline wrapper using auto-detected model targets"""
    payload = json.dumps({
        "model": active_model, # Dynamics injection: handles whichever file the user downloaded automatically
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ],
        "temperature": 0.72,
        "max_tokens": 30000,
        "thinking": False,   # Lock out hidden deep reasoning tokens to protect context channel width
        "reasoning": False   # Fallback parameter for modern localized backend wrappers
    })
    
    headers = {"Content-Type": "application/json"}
    
    try:
        conn = http.client.HTTPConnection(LOCAL_API_HOST, LOCAL_API_PORT, timeout=60) 
        conn.request("POST", "/v1/chat/completions", payload, headers)
        response = conn.getresponse()
        
        if response.status == 200:
            data = json.loads(response.read().decode('utf-8'))
            msg_data = data['choices'][0]['message']
            
            final_content = msg_data.get('content', '')
            
            output_stream = ""
            if final_content:
                output_stream += f"🎭 [SIMULATED PSYCHE DIALOGUE]:\n{final_content}"
            else:
                output_stream += "⚠️ [ALERT] Local server returned an empty conversational content array."
            return output_stream.strip()
        else:
            return f"[LOCAL SERVER ERROR] Status Code {response.status}: {response.read().decode('utf-8')}"
    except Exception as e:
        return f"[CONNECTION REFUSED] Network thread error on port {LOCAL_API_PORT}. Details: {e}"

def generate_swarm_dialogue(dominant_planet, secondary_planet, original_input, solar_pull, active_model):
    """Contextual multi-agent prompt construction with explicit whitespace margin stripping"""
    raw_system = f"""You are simulating the internal, multi-body psychological dialogue of a single conscious entity.
The current mental state of the system is bound by the following physics metrics:
- Active Solar Clamping Gravity: {solar_pull:.2f} / 8.00
- Dominant Planetary Paradigm: {dominant_planet.name}
- Secondary Planetary Paradigm: {secondary_planet.name}

You must output a raw script showing how the internal archetypes of this mind clash and negotiate to reach a unified choice. 
Format your response precisely with these explicit character headers, reflecting Maya's Tri-Layered specification:

[{dominant_planet.name.upper()} - THE PRIMAL ID]: (Impulsive, intense, demanding raw action)
[{dominant_planet.name.upper()} - THE REGULATORY SUPEREGO]: (Rigid, moralistic, enforcing strict structural boundaries)
[{secondary_planet.name.upper()} - THE BALANCING EGO]: (The rational negotiator, proposing a functional real-world compromise)

[TRANSMITTED UNIFIED RESPONSE]: (Conclude the simulation by writing out the exact, finalized, real-world text response that the unified consciousness has agreed to transmit back to the user.)"""


    system_instruction = textwrap.dedent(raw_system).strip()
    user_scenario = f"The mind has encountered an external environmental stimulus scenario input: '{original_input}'"
    
    return query_local_llm(system_instruction, user_scenario, active_model)

if __name__ == "__main__":
    # Import the modular physics PoC core dynamically to prevent structural dependencies
    try:
        from resonant_engine import ResonantEngine
        cognitive_core = ResonantEngine()
        cognitive_core.standby_mode_active = False
    except ImportError:
        print("[CRITICAL] Could not locate 'resonant_engine.py' in this directory directory path.")
        sys.exit(1)
        
    print("=================================================================")
    print("    RESONANT COGNITION AUTO-CONFIGURING ORCHESTRATOR v11.0       ")
    print("=================================================================")
    print("Modular File Framework Active: Handshaking local server...")
    
    # Run the automatic model target discovery handshake sequence
    loaded_model = get_active_model_name()
    if loaded_model != "UNKNOWN_LOCAL_MODEL":
        print(f"📡 AUTO-DETECTION SUCCESSFUL: Bound to active model '{loaded_model}'")
    else:
        print(f"⚠️  SERVER NOTICE: No active model detected on port {LOCAL_API_PORT}. Defaulting to slot-zero routing.")
    print("=================================================================")

    while True:
        user_input = input("\nEnter scenario vector metrics (X,Y,Z) or real-world prompt: ").strip()
        
        if user_input.lower() == 'exit':
            print("[SYSTEM] Shutting down multi-agent orchestration layers. Goodbye.")
            break
        if not user_input:
            continue
            
        try:
            is_numeric_vector = False
            if "," in user_input and "|" not in user_input:
                parts = user_input.split(',')
                if len(parts) == 3:
                    try:
                        [float(p.strip()) for p in parts]
                        is_numeric_vector = True
                    except ValueError:
                        is_numeric_vector = False

            if is_numeric_vector:
                coords = [float(val) for val in user_input.split(',')]
                simulated_text = f"Geometric shift toward coordinate trajectory tensor: {user_input}"
            else:
                coords = list(np.random.uniform(-1.0, 1.0, 3))
                simulated_text = user_input
                
            print("\n[STEP 1] Running physics manifolds in resonant_engine.py...")
            current_solar_pull = 1.5 + (np.random.uniform(0, 3.0)) 
            
            active_planets = list(cognitive_core.planets)
            np.random.shuffle(active_planets)
            dominant = active_planets[0]   
            secondary = active_planets[1]  
            
            print(f"  ↳ Manifold Wave Collapse Complete.")
            print(f"  ↳ Dominant Vector Node: {dominant.name} | Secondary: {secondary.name}")
            
            print(f"\n[STEP 2] Forking context into Local Swarm Dialogue...")
            print("-----------------------------------------------------------------")
            
            # Re-fetch the loaded model name on each turn in case the user hot-swapped models inside their app gui panels
            current_active_model = get_active_model_name()
            
            live_dialogue = generate_swarm_dialogue(dominant, secondary, simulated_text, current_solar_pull, current_active_model)
            print(live_dialogue)
            print("-----------------------------------------------------------------")
            
        except Exception as e:
            print(f"[ERROR] Engine routing exception handled: {e}")
