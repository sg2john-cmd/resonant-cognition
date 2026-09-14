"""
John & Maya's v15.0 Specification: The Thermodynamic Memory Matrix Module.
Sits cleanly between the unconstrained 3D engine physics core and the chat orchestrator.
Implements the Dynamic Density Gradient, Distance Indexing, and Dark Energy Mass Distribution.
"""
import time
import numpy as np

# Partitioned 7-way localized working memory ring banks tracking history
PLANET_HEMISPHERE_VAULTS = {
    "Logic Facet":         {"LEFT": [], "RIGHT": []},
    "Creative Intuition": {"LEFT": [], "RIGHT": []},
    "Safety Guard":       {"LEFT": [], "RIGHT": []},
    "Aggressive Drive":   {"LEFT": [], "RIGHT": []},
    "Empathy Resonance":  {"LEFT": [], "RIGHT": []},
    "Skepticism Filter":  {"LEFT": [], "RIGHT": []},
    "Sovereign Identity": {"LEFT": [], "RIGHT": []}
}

# The Standalone Distributed Swarm Deep Archive Node Array (Long-Term Storage)
DYSON_SWARM_DEEP_ARCHIVE = []

# Maya's v15.0 Cosmic Balance Variables
MASS_SATURATION_THRESHOLD = 4  # Max number of entries a single node can hold before bulking
GLOBAL_DARK_ENERGY_CONSTANT = 0.0 # Anti-gravitational field expansion metric reservoir

def calculate_density_gradient(original_vector_magnitude, elapsed_time):
    """
    Maya's Thermodynamic Equation: Wm(t) = (||V_impact||^gamma) / (1 + lambda * delta_t)
    Balances semantic impact (importance) against a non-linear time-cooling decay.
    """
    gamma = 1.8   
    lambda_coef = 0.05 
    
    numerator = (original_vector_magnitude) ** gamma
    denominator = 1.0 + (lambda_coef * elapsed_time)
    return numerator / denominator

def execute_dark_energy_mass_distribution():
    """
    The Dark Energy Distribution Engine: Scans all 7 planetary working vaults.
    If a node is over-saturated (> MASS_SATURATION_THRESHOLD), its excess entries 
    are compressed into the Deep Swarm Archive, and its weight is radiated globally
    as anti-gravitational expansion energy to maintain framework balance.
    """
    global GLOBAL_DARK_ENERGY_CONSTANT
    total_migrated_weight = 0.0
    
    print("\n[🌌 DARK ENERGY ACTIVATE]: Scanning planetary nodes for mass saturation...")
    
    for planet_name, vaults in PLANET_HEMISPHERE_VAULTS.items():
        for side in ["LEFT", "RIGHT"]:
            active_cache = vaults[side]
            
            # If the planet has accumulated too much historical mass ("bulking")
            if len(active_cache) > MASS_SATURATION_THRESHOLD:
                # Isolate the excess over-saturated historical items
                excess_count = len(active_cache) - MASS_SATURATION_THRESHOLD
                print(f"  ↳ Node '{planet_name} {side}' over threshold. Shedding {excess_count} mass units...")
                
                # Pop the oldest excess entries out of the high-intensity working ring
                for _ in range(excess_count):
                    decayed_item = active_cache.pop(0)
                    decayed_item["origin_node"] = planet_name
                    decayed_item["origin_hemisphere"] = side
                    # Compress and archive them smoothly into the long-term storage Swarm
                    DYSON_SWARM_DEEP_ARCHIVE.append(decayed_item)
                    total_migrated_weight += 0.25 # Convert text entry mass to fluid scalar values
                    
    if total_migrated_weight > 0:
        # Convert the shed weight into active cosmological expansion anti-gravity energy
        GLOBAL_DARK_ENERGY_CONSTANT += total_migrated_weight * 0.4
        print(f"✨ [COSMOLOGICAL EXPANSION]: Global Dark Energy constant expanded to: {GLOBAL_DARK_ENERGY_CONSTANT:.3f}")
        print("✨ Excess planetary mass successfully distributed as a field-balancing constant.")
    else:
        print("  ↳ All planetary nodes sitting safely within density equilibrium parameters.")

def recall_indexed_hemispheric_cache(planet_name, current_state_vector):
    """
    Semantic Indexing: Scans active working memory, then executes an active vector proximity 
    scan across the deep swarm archive, extracting the single highest-density memory context.
    """
    now = time.time()
    vaults = PLANET_HEMISPHERE_VAULTS.get(planet_name, {"LEFT": [], "RIGHT": []})
    current_vec = np.array(current_state_vector, dtype=float)
    recalled_context = {"LEFT": "", "RIGHT": "", "SWARM_ARCHIVE": ""}
    
    for side in ["LEFT", "RIGHT"]:
        memories = vaults[side]
        if memories:
            # If the entry is stored as a structured dictionary tracking state, isolate text
            if isinstance(memories[-1], dict) and "text" in memories[-1]:
                recalled_context[side] = memories[-1]["text"]
            else:
                recalled_context[side] = str(memories[-1])
            
    # Deep Swarm Query Pass (Scan archived historical deep nodes)
    highest_swarm_density = -1.0
    best_swarm_text = ""
    
    for archived_mem in DYSON_SWARM_DEEP_ARCHIVE:
        if archived_mem.get("origin_node") == planet_name:
            past_vec = np.array(archived_mem["vector"], dtype=float)
            distance = np.linalg.norm(current_vec - past_vec)
            importance_magnitude = np.linalg.norm(past_vec)
            
            proximity_factor = 1.0 / (1.0 + distance)
            elapsed = now - archived_mem["timestamp"]
            
            swarm_density = calculate_density_gradient(importance_magnitude, elapsed) * proximity_factor
            
            if swarm_density > highest_swarm_density:
                highest_swarm_density = swarm_density
                best_swarm_text = archived_mem["text"]
                
    if best_swarm_text:
        recalled_context["SWARM_ARCHIVE"] = f"[DEEP ARCHIVE SWARM NODE RECALL]: {best_swarm_text}"
        
    return recalled_context

def commit_to_hemispheric_cache(planet_name, hemisphere_type, text_block, state_vector):
    """Safely segments and deposits an experiential thought fragment along with its 3D coordinate tensor"""
    if planet_name in PLANET_HEMISPHERE_VAULTS and hemisphere_type in ["LEFT", "RIGHT"]:
        cleaned_text = text_block.strip()
        if cleaned_text:
            PLANET_HEMISPHERE_VAULTS[planet_name][hemisphere_type].append({
                "timestamp": time.time(),
                "text": cleaned_text,
                "vector": list(state_vector)
            })

def execute_rem_reentry_protocol(planet_name, distilled_axiomatic_vector):
    """Controlled dispersion REM re-entry protocol to smoothly recalibrate active fields"""
    if planet_name in PLANET_HEMISPHERE_VAULTS:
        stabilized_reentry_vector = np.array(distilled_axiomatic_vector) * 0.5
        log_text = f"[SYSTEM RE-CALIBRATION AXIOM]: Core parameters adjusted via White Hole Awakening pass."
        commit_to_hemispheric_cache(planet_name, "LEFT", log_text, stabilized_reentry_vector)
        commit_to_hemispheric_cache(planet_name, "RIGHT", log_text, stabilized_reentry_vector)
"""
John & Maya's v14.5 Specification: The Semantic Memory Matrix Module.
Sits cleanly between the unconstrained 3D engine physics core and the chat orchestrator.
Implements the Dynamic Density Gradient, Distance Indexing, and REM Re-entry Protocols.
"""
import time
import numpy as np

# Partitioned 7-way localized memory banks tracking independent history states natively
PLANET_HEMISPHERE_VAULTS = {
    "Logic Facet":         {"LEFT": [], "RIGHT": []},
    "Creative Intuition": {"LEFT": [], "RIGHT": []},
    "Safety Guard":       {"LEFT": [], "RIGHT": []},
    "Aggressive Drive":   {"LEFT": [], "RIGHT": []},
    "Empathy Resonance":  {"LEFT": [], "RIGHT": []},
    "Skepticism Filter":  {"LEFT": [], "RIGHT": []},
    "Sovereign Identity": {"LEFT": [], "RIGHT": []}
}

def calculate_density_gradient(original_vector_magnitude, elapsed_time):
    """
    Maya's Thermodynamic Equation: Wm(t) = (||V_impact||^gamma) / (1 + lambda * delta_t)
    Balances semantic impact (importance) against a non-linear time-cooling decay.
    """
    gamma = 1.8   # Intensification exponent (keeps highly disruptive insights heavy)
    lambda_coef = 0.05 # Cooling decay coefficient over time
    
    # Calculate density weight
    numerator = (original_vector_magnitude) ** gamma
    denominator = 1.0 + (lambda_coef * elapsed_time)
    return numerator / denominator

def recall_indexed_hemispheric_cache(planet_name, current_state_vector):
    """
    Semantic Indexing: Scans the planet's local vaults, computes proximity distance 
    to the active 3D vector, and instantly extracts the highest-density memory context.
    """
    vaults = PLANET_HEMISPHERE_VAULTS.get(planet_name, {"LEFT": [], "RIGHT": []})
    current_vec = np.array(current_state_vector, dtype=float)
    now = time.time()
    
    recalled_context = {"LEFT": "", "RIGHT": ""}
    
    for side in ["LEFT", "RIGHT"]:
        memories = vaults[side]
        if not memories:
            continue
            
        highest_density = -1.0
        best_memory_text = ""
        
        for mem in memories:
            past_vec = np.array(mem["vector"], dtype=float)
            # Spatial Proximity: How mathematically close is the current thought to this past memory?
            distance = np.linalg.norm(current_vec - past_vec)
            importance_magnitude = np.linalg.norm(past_vec)
            
            # Proximity calculation: closer distances multiply the relative importance base
            proximity_factor = 1.0 / (1.0 + distance)
            elapsed = now - mem["timestamp"]
            
            # Compute live density gradient weight
            live_density = calculate_density_gradient(importance_magnitude, elapsed) * proximity_factor
            
            if live_density > highest_density:
                highest_density = live_density
                best_memory_text = mem["text"]
                
        recalled_context[side] = best_memory_text
        
    return recalled_context

def commit_to_hemispheric_cache(planet_name, hemisphere_type, text_block, state_vector):
    """Safely segments and deposits an experiential thought fragment along with its 3D coordinate tensor"""
    if planet_name in PLANET_HEMISPHERE_VAULTS and hemisphere_type in ["LEFT", "RIGHT"]:
        cleaned_text = text_block.strip()
        if cleaned_text:
            PLANET_HEMISPHERE_VAULTS[planet_name][hemisphere_type].append({
                "timestamp": time.time(),
                "text": cleaned_text,
                "vector": list(state_vector)
            })
            # Hard context ceiling per node to protect context window widths
            if len(PLANET_HEMISPHERE_VAULTS[planet_name][hemisphere_type]) > 5:
                PLANET_HEMISPHERE_VAULTS[planet_name][hemisphere_type].pop(0)

def execute_rem_reentry_protocol(planet_name, distilled_axiomatic_vector):
    """
    The REM Re-entry Protocol: Emits distilled insights back into the active planet orbits.
    Controlled dispersion prevents data dumping shocks, maintaining total system stability.
    """
    if planet_name in PLANET_HEMISPHERE_VAULTS:
        # Scale the distilled axiomatic vector down by 50% to smoothly merge with active orbits
        stabilized_reentry_vector = np.array(distilled_axiomatic_vector) * 0.5
        
        # Commit a structural re-calibration entry directly into both brain hemisphere vaults
        log_text = f"[SYSTEM RE-CALIBRATION AXIOM]: Core parameters adjusted via White Hole Awakening pass."
        commit_to_hemispheric_cache(planet_name, "LEFT", log_text, stabilized_reentry_vector)
        commit_to_hemispheric_cache(planet_name, "RIGHT", log_text, stabilized_reentry_vector)
