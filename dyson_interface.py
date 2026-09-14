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
