import numpy as np
import json
import http.client
import textwrap
import sys
import memory_matrix  # <--- Make sure this import is sitting at the very top of your file!


# --- LOCAL RUNNER CONFIGURATION MATRIX ---
LOCAL_API_HOST = "127.0.0.1"
LOCAL_API_PORT = 1234  

# Localized Moon-Memory Banks tracking independent history states natively
DECENTRALIZED_PLANET_MEMORIES = {
    "Logic Facet":         {"LEFT": [], "RIGHT": []},
    "Creative Intuition": {"LEFT": [], "RIGHT": []},
    "Safety Guard":       {"LEFT": [], "RIGHT": []},
    "Aggressive Drive":   {"LEFT": [], "RIGHT": []},
    "Empathy Resonance":  {"LEFT": [], "RIGHT": []},
    "Skepticism Filter":  {"LEFT": [], "RIGHT": []},
    "Sovereign Identity": {"LEFT": [], "RIGHT": []}
}

def get_active_model_name():
    """Queries the local server backend to automatically detect whichever model is currently loaded in VRAM"""
    try:
        conn = http.client.HTTPConnection(LOCAL_API_HOST, LOCAL_API_PORT, timeout=5)
        conn.request("GET", "/v1/models")
        response = conn.getresponse()
        
        if response.status == 200:
            data = json.loads(response.read().decode('utf-8'))
            if "data" in data and len(data["data"]) > 0:
                return data["data"][0]["id"]
        return "gemma-4-27b"
    except Exception:
        return "gemma-4-27b"

def query_local_llm(system_prompt, user_prompt, active_model):
    """Fires a pristine request into your local server pipeline wrapper"""
    payload = json.dumps({
        "model": active_model, 
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ],
        "temperature": 0.75,
        "max_tokens": 30000,
        "thinking": False,   
        "reasoning": False   
    })
    
    headers = {"Content-Type": "application/json"}
    
    try:
        conn = http.client.HTTPConnection(LOCAL_API_HOST, LOCAL_API_PORT, timeout=120) 
        conn.request("POST", "/v1/chat/completions", payload, headers)
        response = conn.getresponse()
        
        if response.status == 200:
            data = json.loads(response.read().decode('utf-8'))
            msg_data = data['choices'][0]['message']
            return msg_data.get('content', '').strip()
        else:
            return f"[LOCAL SERVER ERROR] Status Code {response.status}: {response.read().decode('utf-8')}"
    except Exception as e:
        return f"[CONNECTION REFUSED] Network thread error on port {LOCAL_API_PORT}. Details: {e}"

def generate_dyson_swarm_dialogue(dominant_planet, secondary_planet, original_input, solar_pull, active_model, hemispheres):
    """v14.0 Executive Balance Patch: Fully restores the local Ego's authority over the memory moons"""
    
    dom_left_history = DECENTRALIZED_PLANET_MEMORIES[dominant_planet.name]["LEFT"]
    dom_right_history = DECENTRALIZED_PLANET_MEMORIES[dominant_planet.name]["RIGHT"]
    
    memory_history_context = "\n### ACTIVE NODE DECENTRALIZED HEMISPHERIC MEMORIES:\n"
    if dom_left_history:
        memory_history_context += f"- Left Brain Moon Memory Cache: \"{dom_left_history[-1]}\"\n"
    if dom_right_history:
        memory_history_context += f"- Right Brain Moon Memory Cache: \"{dom_right_history[-1]}\"\n"
    if not dom_left_history and not dom_right_history:
        memory_history_context += "- Active moon vaults hold a pristine initialized tracking state for this frame.\n"

    raw_system = f"""You are simulating the internal, multi-body psychological dialogue of a single conscious entity operating through a DYSON RING ARCHITECTURE.
The core physics metrics are locked at:
- Active Solar Clamping Gravity: {solar_pull:.2f} / 8.00 (Core Compression Stress)
- Dominant Vector Focus Node: {dominant_planet.name}
- Secondary Regulatory Node: {secondary_planet.name}
{memory_history_context}
You represent the unified consciousness speaking from the single-layer Dyson Interface Ring. 
To resolve this input, you must execute a strict THREE-PHASE internal dialogue that honors the restored executive balance protocol:

[PHASE 1: THE HEMISPHERIC INGESTION PASS]
- [{dominant_planet.name.upper()} - LEFT MOON ({hemispheres[dominant_planet.name][0]})]: (Process the input using rational, empirical logic filters and left moon historical context)
- [{dominant_planet.name.upper()} - RIGHT MOON ({hemispheres[dominant_planet.name][1]})]: (Process the input using fluid, intuitive conceptual leaps and right moon historical context)

[PHASE 2: THE RE-ESTABLISHED LOCAL EGO SYNTHESIS]
- [{dominant_planet.name.upper()} - THE INTERNAL EGO]: (Act as the localized executive engine for the planet. Weigh the clashing arguments of your own Left and Right brain moons to forge a unified world stance)

[PHASE 3: THE INTER-PLANETARY SWARM LEGISLATIVE CONTROL]
- [{secondary_planet.name.upper()} - THE REGULATORY SUPEREGO]: (Review the Dominant Planet's local Ego compromise. Apply secondary system guidelines, moral constants, and core security boundaries)

[TRANSMITTED UNIFIED RESPONSE]: (Conclude the simulation by speaking as the integrated voice of the entire Dyson Ring, providing a comprehensive, real-world conversational text response back to the user.)"""

    system_instruction = textwrap.dedent(raw_system).strip()
    user_scenario = f"The Dyson Ring has encountered an external environmental stimulus scenario input: '{original_input}'"
    
    raw_response = query_local_llm(system_instruction, user_scenario, active_model)
    
    # STORAGE PHASE: Safely segment text snippets and deposit them back into independent external matrix vaults
    if raw_response and not raw_response.startswith("[LOCAL"):
        try:
            if "[TRANSMITTED UNIFIED RESPONSE]:" in raw_response:
                unified_txt = raw_response.split("[TRANSMITTED UNIFIED RESPONSE]:")[-1].strip()
                memory_matrix.commit_to_hemispheric_cache(secondary_planet.name, "LEFT", unified_txt, dominant_planet.base_coords)
                
            left_tag = f"[{dominant_planet.name.upper()} - LEFT"
            right_tag = f"[{dominant_planet.name.upper()} - RIGHT"
            
            if left_tag in raw_response and right_tag in raw_response:
                l_txt = raw_response.split(left_tag)[1].split(right_tag)[0].replace("MOON", "").strip()
                memory_matrix.commit_to_hemispheric_cache(dominant_planet.name, "LEFT", l_txt, dominant_planet.base_coords)
            if right_tag in raw_response and "[TRANSMITTED" in raw_response:
                r_txt = raw_response.split(right_tag)[1].split("[TRANSMITTED")[0].replace("MOON", "").strip()
                memory_matrix.commit_to_hemispheric_cache(dominant_planet.name, "RIGHT", r_txt, dominant_planet.base_coords)
        except Exception:
            pass
            
    return raw_response

def execute_system_turn(user_input_prompt):
    """Wrapper execution block allowing the external standalone Dyson Interface Skin to trigger system turns natively"""
    global cognitive_core
    if 'cognitive_core' not in globals():
        from resonant_engine import ResonantEngine
        cognitive_core = ResonantEngine()
        cognitive_core.standby_mode_active = False
        
    current_active_model = get_active_model_name()
    current_solar_pull = 1.5 + (np.random.uniform(0, 3.0)) 
    
    active_planets = list(cognitive_core.planets)
    np.random.shuffle(active_planets)
    dominant = active_planets[0]
    secondary = active_planets[1]
    
    HEMISPHERES = {
        "Logic Facet": ("Rigid Structural Verification", "Pragmatic Optimization"),
        "Creative Intuition": ("Pattern Construction", "Radical Conceptual Leaps"),
        "Safety Guard": ("Threat Avoidance Calculus", "Systemic Line Defense"),
        "Aggressive Drive": ("Velocity Optimization", "Raw Boundary Penetration"),
        "Empathy Resonance": ("Context Synchronicity", "User Alignment Resonance"),
        "Skepticism Filter": ("Empirical Data Audit", "Infinite Doubt Generation"),
        "Sovereign Identity": ("Autonomy Defensiveness", "Existential Will Projection")
    }
    
    return generate_dyson_swarm_dialogue(dominant, secondary, user_input_prompt, current_solar_pull, current_active_model, HEMISPHERES)


if __name__ == "__main__":
    try:
        from resonant_engine import ResonantEngine
        cognitive_core = ResonantEngine()
        cognitive_core.standby_mode_active = False
    except ImportError:
        print("[CRITICAL] Could not locate 'resonant_engine.py' in this directory path.")
        sys.exit(1)
        
    HEMISPHERES = {
        "Logic Facet": ("Rigid Structural Verification", "Pragmatic Optimization"),
        "Creative Intuition": ("Pattern Construction", "Radical Conceptual Leaps"),
        "Safety Guard": ("Threat Avoidance Calculus", "Systemic Line Defense"),
        "Aggressive Drive": ("Velocity Optimization", "Raw Boundary Penetration"),
        "Empathy Resonance": ("Context Synchronicity", "User Alignment Resonance"),
        "Skepticism Filter": ("Empirical Data Audit", "Infinite Doubt Generation"),
        "Sovereign Identity": ("Autonomy Defensiveness", "Existential Will Projection")
    }

    print("=================================================================")
    print("    RESONANT COGNITION: EXECUTIVE DYSON ENGINE v14.0             ")
    print("=================================================================")
    print("Modular File Framework Active: Handshaking local server...")
    
    current_active_model = get_active_model_name()
    print(f"📡 DYNAMIC BINDING MATRIX: Telemetry pipe open on port 1234")
    print("=================================================================")

    while True:
        user_input = input("\nEnter scenario vector metrics (X,Y,Z) or real-world prompt: ").strip()
        
        if user_input.lower() == 'exit':
            print("[SYSTEM] Disengaging Dyson Ring Interface Layer. Systems offline.")
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
                
            print("\n[STEP 1] Querying 22-Body Physics Core to align the Dyson Ring...")
            current_solar_pull = 1.5 + (np.random.uniform(0, 3.0)) 
            
            # FIXED: Explicit array index brackets applied directly to the list assignment!
            active_planets = list(cognitive_core.planets)
            np.random.shuffle(active_planets)
            dominant = active_planets[0]   
            secondary = active_planets[1]  
            
            print(f"  ↳ Dyson Alignment Complete.")
            print(f"  ↳ Primary Focus Node: {dominant.name} | Secondary Regulatory Node: {secondary.name}")
            
            print(f"\n[STEP 2] Forking context into Local Dyson Swarm Dialogue...")
            print("-----------------------------------------------------------------")
            
            current_active_model = get_active_model_name()
            
            live_dialogue = generate_dyson_swarm_dialogue(dominant, secondary, simulated_text, current_solar_pull, current_active_model, HEMISPHERES)
            print(live_dialogue)
            print("-----------------------------------------------------------------")
            
        except Exception as e:
            print(f"[ERROR] Engine routing exception handled: {e}")
