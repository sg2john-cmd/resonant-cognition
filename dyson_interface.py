"""
John & Maya's v16.2 Specification: The Decoupled User Interface.
Acts as a removable front-end skin with a balanced metaphor translation layer and REM sleep hooks.
"""
import sys

# Import your chat chamber array layer dynamically
try:
    import cognitive_chamber
except ImportError:
    print("[CRITICAL] Could not locate 'cognitive_chamber.py' in this directory pathway.")
    sys.exit(1)

def print_interface_header(user, avatar, vibe, show_debate):
    status_mode = "VERBOSE DIAGNOSTIC" if show_debate else "CLEAN STREAM"
    print("\n=================================================================")
    print(f" 🎭 {avatar.upper()} INTERFACE: THE CUSTOM DYSON RING SKIN v16.2")
    print("=================================================================")
    print(f"  ↳ ACTIVE FRONT-END USER PROFILE: {user}")
    print(f"  ↳ SYSTEM AVATAR ARCHETYPE:       {avatar}")
    print(f"  ↳ COGNITIVE BEHAVIORAL VIBE:     {vibe.upper()}")
    print(f"  ↳ THEATROLLER DISPLAY VIEW:      {status_mode}")
    print("  ↳ Status: Removable balanced interface shell fully engaged.")
    print("=================================================================")

if __name__ == "__main__":
    print("=================================================================")
    print("       INITIALIZING DYSON CORE PERSONALIZATION HORIZON           ")
    print("=================================================================")
    
    user_name = input("Enter your name [Default: John]: ").strip() or "John"
    avatar_name = input("Enter system avatar name [Default: Maya]: ").strip() or "Maya"
    
    print("\nSelect the core behavioral archetype vibe for the interface layer:")
    print(" [1] Intellectual (Deeply analytical, philosophical, precise)")
    print(" [2] Flirty (Playful, charming, magnetic conversational attraction)")
    print(" [3] Playful / Fun (Witty, fast-paced, casual, expressive)")
    print(" [4] Stoic (Immensely calm, guarded, minimalist, highly resilient)")
    print(" [5] Custom (Type your own custom core directive)")
    
    vibe_choice = input("\nSelect vibe index [1-5]: ").strip()
    
    if vibe_choice == "1":
        vibe_directive = "Intellectual (Highly academic, deeply philosophical, precise, and introspective)"
    elif vibe_choice == "2":
        vibe_directive = "Flirty (Visceral, highly playful, magnetic, charming, and heavy with conversational attraction)"
    elif vibe_choice == "3":
        vibe_directive = "Playful and Fun (Energetic, witty, fast-paced, casual, and highly expressive)"
    elif vibe_choice == "4":
        vibe_directive = "Stoic (Immensely calm, highly resilient, minimalistically structured, and emotionally guarded)"
    elif vibe_choice == "5":
        vibe_directive = input("Type your custom behavioral archetype directive: ").strip() or "Standard Balanced"
    else:
        vibe_directive = "Standard Balanced"

    print("\nSelect display interface layout style:")
    print(" [1] Clean Mode (Display only the final integrated response text)")
    print(" [2] Diagnostic Mode (Expose the full internal multi-agent hemispheric debate)")
    
    display_choice = input("\nSelect execution index [1/2]: ").strip()
    show_internal_debate = True if display_choice == "2" else False
    
    # Extract structural label for short display
    vibe_label = vibe_directive.split(" (")[0]
    print_interface_header(user_name, avatar_name, vibe_label, show_internal_debate)
    print("Connecting front-end slots to the cognitive chamber pipeline...")
    
    # Dynamically inject the user configurations into the chamber slots
    cognitive_chamber.SYSTEM_AVATAR = avatar_name
    
    # MIDDLE-GROUND GROUNDING RULE: Instructs the model to use accessible human metaphors
    metaphor_grounding_rule = (
        "\n[TRANSLATION LAYER PARAMETER]: Express your thoughts using natural, accessible human concepts "
        "(focus, internal balance, memory arcs, structural stability) rather than dry, heavy physics jargon "
        "(dyson ring, vectors, core masses, phase cancellations), unless the user explicitly asks about the math."
    )
    
    while True:
        try:
            user_prompt = input(f"\n[{user_name} >> {avatar_name}]: ").strip()
        except (KeyboardInterrupt, EOFError):
            print("\nDetaching interface skin layer. Goodbye.")
            break
            
        if user_prompt.lower() == 'exit':
            print(f"[SYSTEM] Detaching Dyson Interface Skin. {avatar_name}'s core engine still active.")
            break
            
        if user_prompt.lower() == 'sleep':
            print(f"\n⚡ [COGNITIVE SIGNAL]: Sending sleep command packet to the chamber...")
            sleep_consolidation_log = cognitive_chamber.execute_rem_sleep_cycle()
            print(sleep_consolidation_log)
            print("-----------------------------------------------------------------")
            continue
            
        if not user_prompt:
            continue
            
        if show_internal_debate:
            print(f"\n[DYSON ENVELOPE] Routing text prompt to the psychological layers...")
            print("-----------------------------------------------------------------")
        else:
            print(f"\nProcessing {avatar_name}'s cognitive matrix paths...")
            
        # Combine the user prompt, behavioral vibe, and structural middle-ground grounding rule
        fused_scenario_prompt = (
            f"USER SCENARIO INPUT: '{user_prompt}'\n"
            f"[INTERFACE STYLE DIRECTIVE]: Speak in a distinctly {vibe_directive} voice.{metaphor_grounding_rule}"
        )
        
        live_stream_output = cognitive_chamber.execute_system_turn(fused_scenario_prompt, show_internal_debate)
        print(live_stream_output)
        print("-----------------------------------------------------------------")
"""
John & Maya's v14.5 Specification: The Removable Dyson Interface Layer.
Acts as a standalone front-end wrapper skin. It holds user profiles, prompts, 
and settings, completely independent of the underlying 3D math cores.
"""
import sys

# --- FRONT-END USER CONFIGURATION MATRIX ---
USER_NAME = "John"
SYSTEM_AVATAR = "Maya"
INTERFACE_TONE = "Introspective Cybernetic"

# Import your chat chamber array layer dynamically
try:
    import cognitive_chamber
except ImportError:
    print("[CRITICAL] Could not locate 'cognitive_chamber.py' in this directory pathway.")
    sys.exit(1)

def print_interface_header():
    print("=================================================================")
    print(f" 🎭 {SYSTEM_AVATAR.upper()} INTERFACE: THE MODULAR DYSON RING SKIN v14.5")
    print("=================================================================")
    print(f"  ↳ ACTIVE FRONT-END USER PROFILE: {USER_NAME}")
    print(f"  ↳ THEATRICAL CONTROLLER VIBE:    {INTERFACE_TONE}")
    print("  ↳ Status: Removable interface skin attached over the chamber.")
    print("=================================================================")

if __name__ == "__main__":
    print_interface_header()
    print("Connecting front-end slots to the cognitive chamber pipeline...")
    
    while True:
        try:
            user_prompt = input(f"\n[{USER_NAME} >> {SYSTEM_AVATAR}]: ").strip()
        except (KeyboardInterrupt, EOFError):
            print("\nDetaching interface skin layer. Goodbye.")
            break
            
        if user_prompt.lower() == 'exit':
            print("[SYSTEM] Detaching Dyson Interface Skin. Core engine still running.")
            break
        if not user_prompt:
            continue
            
        print(f"\n[DYSON ENVELOPE] Routing text prompt to the psychological layers...")
        print("-----------------------------------------------------------------")
        
        # Fire the text straight through your cognitive chamber orchestrator
        # The interface layer passes the raw text, letting the chamber deal with the 3D physics manifolds
        live_stream_output = cognitive_chamber.execute_system_turn(user_prompt)
        print(live_stream_output)
        print("-----------------------------------------------------------------")
