def start_game():
    print("Setting & Theme: Sci-Fi, Exploration, Survival")
    print("Character Role: A Deep Space Explorer")
    print("\n--- BEGIN ---")
    print(
        "You awake with a jolt, your head throbbing. The emergency lights of your exploratory vessel, the 'Aetherius', cast long, flickering shadows across the control panel. Alarms blare, and the ship shudders violently. You remember nothing of the past few hours. A distress beacon flashes on the console: 'Unidentified gravitational anomaly detected. Hull breach imminent.' You have two options:")
    print("1. Attempt to stabilize the Aetherius and repair the hull breach.")
    print("2. Abandon ship and deploy the emergency escape pod.")
    choice = input("Enter your choice (1 or 2): ")
    return choice


def stabilize_ship():
    print(
        "You rush to the main control panel, your fingers flying across the damaged interface. The ship continues to shake, and warning lights blink ominously. You manage to reroute power to the damaged sections, but the hull breach is severe. You can:")
    print("1. Focus all remaining power on repairing the hull, risking system overload.")
    print(
        "2. Attempt to plot a course to the nearest star system, hoping to reach safety before the ship breaks apart.")
    choice = input("Enter your choice (1 or 2): ")
    if choice == "1":
        repair_hull()
    elif choice == "2":
        plot_course()
    else:
        print("Invalid choice. The ship's systems are failing. You have no time to waste.")
        stabilize_ship()


def repair_hull():
    print(
        "You divert all available power to the repair drones, forcing them to work at maximum capacity. The ship groans under the strain, and sparks fly from the overloaded circuits. The drones manage to seal the major breaches, but the Aetherius is critically damaged. You can:")
    print("1. Attempt to send a distress signal to any nearby ships.")
    print("2. Investigate the source of the gravitational anomaly.")
    choice = input("Enter your choice (1 or 2): ")
    if choice == "1":
        distress_signal()
    elif choice == "2":
        investigate_anomaly()
    else:
        print("Invalid choice. The ship's systems are failing. You have no time to waste.")
        repair_hull()


def plot_course():
    print(
        "You desperately try to plot a course to the nearest star system, but the ship's navigation systems are severely damaged. The gravitational anomaly is pulling you towards an unknown point in space. You can:")
    print("1. Attempt to override the navigation system and manually steer the ship.")
    print("2. Prepare for impact and brace for the unknown.")
    choice = input("Enter your choice (1 or 2): ")
    if choice == "1":
        manual_steering()
    elif choice == "2":
        brace_impact()
    else:
        print("Invalid choice. The ship's systems are failing. You have no time to waste.")
        plot_course()


def distress_signal():
    print(
        "You manage to send out a weak distress signal, but you are unsure if anyone will receive it. The ship continues to lose power, and the gravitational anomaly is still pulling you closer. You notice strange readings on the sensor array. You can:")
    print("1. Try to decode the sensor readings.")
    print("2. Focus on conserving remaining power and await rescue.")
    choice = input("Enter your choice (1 or 2): ")
    if choice == "1":
        decode_sensors()
    elif choice == "2":
        await_rescue()
    else:
        print("Invalid choice. The ship's systems are failing. You have no time to waste.")
        distress_signal()


def investigate_anomaly():
    print(
        "You venture into the damaged engineering section, following the sensor readings. The air is thick with smoke, and sparks fly from exposed wires. You find a strange, pulsating energy source emanating from a breach in the hull. You can:")
    print("1. Attempt to disable the energy source.")
    print("2. Collect a sample of the energy source for analysis.")
    choice = input("Enter your choice (1 or 2): ")
    if choice == "1":
        disable_source()
    elif choice == "2":
        collect_sample()
    else:
        print("Invalid choice. The ship's systems are failing. You have no time to waste.")
        investigate_anomaly()


def manual_steering():
    print(
        "You fight against the ship's automated systems, attempting to manually steer the Aetherius away from the gravitational anomaly. The ship responds sluggishly, and the controls are erratic. You manage to alter the ship's course slightly, but the anomaly's pull is still strong. You spot an asteroid field ahead. You can:")
    print("1. Attempt to navigate through the asteroid field.")
    print("2. Accept your fate and prepare for the inevitable.")
    choice = input("Enter your choice (1 or 2): ")
    if choice == "1":
        navigate_asteroids()
    elif choice == "2":
        accept_fate()
    else:
        print("Invalid choice. The ship's systems are failing. You have no time to waste.")
        manual_steering()


def brace_impact():
    print(
        "You strap yourself into the pilot's chair and brace for impact. The ship is violently pulled towards the anomaly, and the hull groans under immense pressure. The lights flicker and die, plunging you into darkness. Then, silence.")
    print("--- BAD ENDING: Consumed by the Anomaly ---")
    return


def decode_sensors():
    print(
        "You attempt to decode the sensor readings, and discover that the strange readings are not natural. The gravitational anomaly is emitting a signal. It reads: '...INITIATING CONTACT...'.")
    print("1. Attempt to respond to the signal.")
    print("2. Attempt to block the signal.")
    choice = input("Enter your choice (1 or 2): ")
    if choice == "1":
        respond_signal()
    elif choice == "2":
        block_signal()
    else:
        print("Invalid choice. The ship's systems are failing. You have no time to waste.")
        decode_sensors()


def await_rescue():
    print(
        "You conserve power and wait. Hours pass, and the ship drifts further into the unknown. The gravitational anomaly intensifies. Suddenly, a faint signal appears on the long-range scanners. It reads: '...RESCUE VESSEL APPROACHING...'.")
    print("--- NEUTRAL ENDING: Rescued, but the mystery remains ---")
    return


def disable_source():
    print(
        "You attempt to disable the energy source, but it reacts violently. A surge of energy erupts, knocking you back. The breach in the hull widens, and the ship's systems fail completely. You are pulled into the anomaly.")
    print("--- BAD ENDING: Consumed by the Anomaly ---")
    return


def collect_sample():
    print(
        "You manage to collect a small sample of the energy source and seal it in a containment unit. As you return to the bridge, you notice the ship's systems are stabilizing. The energy source seems to be counteracting the gravitational anomaly. You can:")
    print("1. Attempt to analyze the sample and understand its properties.")
    print("2. Use the energy source to boost the ship's engines and escape the anomaly's pull.")
    choice = input("Enter your choice (1 or 2): ")
    if choice == "1":
        analyze_sample()
    elif choice == "2":
        boost_engines()
    else:
        print("Invalid choice. The ship's systems are failing. You have no time to waste.")
        collect_sample()


def navigate_asteroids():
    print(
        "You attempt to navigate through the asteroid field, but the ship is too damaged to maneuver effectively. The Aetherius collides with a large asteroid, and the ship explodes.")
    print("--- BAD ENDING: Destroyed in the Asteroid Field ---")
    return


def accept_fate():
    print(
        "You accept your fate and watch as the ship is pulled into the anomaly. The ship is torn apart, and you are lost in the vastness of space.")
    print("--- BAD ENDING: Lost in Space ---")
    return


def respond_signal():
    print(
        "You attempt to respond to the signal, and a strange, alien message appears on the console. It reads: '...WE ARE THE KEEPERS. WE HAVE OBSERVED YOU. WE REQUIRE YOUR ASSISTANCE...'.")
    print("1. Agree to assist the alien entity.")
    print("2. Refuse to assist and attempt to escape.")
    choice = input("Enter your choice (1 or 2): ")
    if choice == "1":
        assist_keepers()
    elif choice == "2":
        refuse_keepers()
    else:
        print("Invalid choice. The ship's systems are failing. You have no time to waste.")
        respond_signal()


def block_signal():
    print(
        "You attempt to block the signal, but it is too powerful. The ship's systems overload, and the Aetherius is pulled into the anomaly. You are consumed by the unknown.")
    print("--- BAD ENDING: Consumed by the Keepers ---")
    return


def analyze_sample():
    print(
        "You analyze the sample and discover that it is a form of exotic energy that can manipulate gravity. You realize that this energy could revolutionize space travel. You manage to stabilize the ship and escape the anomaly. You can:")
    print("1. Return to Earth with your discovery.")
    print("2. Explore further, searching for the source of the energy.")
    choice = input("Enter your choice (1 or 2): ")
    if choice == "1":
        return_earth()
    elif choice == "2":
        explore_source()
    else:
        print("Invalid choice. The ship's systems are failing. You have no time to waste.")
        analyze_sample()


def boost_engines():
    print(
        "You use the energy source to boost the ship's engines, and the Aetherius surges forward. You manage to escape the anomaly's pull, but the ship is severely damaged. You can:")
    print("1. Attempt to repair the ship and return to Earth.")
    print("2. Continue exploring, hoping to find a safe haven.")
    choice = input("Enter your choice (1 or 2): ")
    if choice == "1":
        repair_return()
    elif choice == "2":
        continue_explore()
    else:
        print("Invalid choice. The ship's systems are failing. You have no time to waste.")
        boost_engines()


def assist_keepers():
    print(
        "You agree to assist the alien entity, and the ship is enveloped in a bright light. You find yourself in a strange, otherworldly dimension. The Keepers explain that they are guardians of the galaxy, and they need your help to stop a cosmic threat. You embark on a perilous journey, becoming an intergalactic hero.")
    print("--- GOOD ENDING: Intergalactic Hero ---")
    return


def refuse_keepers():
    print(
        "You refuse to assist the alien entity, and the ship is violently ejected from the anomaly. The Aetherius is heavily damaged, and you are lost in uncharted space. You drift for years, becoming a legend among deep space explorers.")
    print("--- NEUTRAL ENDING: Lost Legend ---")
    return


def return_earth():
    print(
        "You return to Earth with your discovery, and the energy source revolutionizes space travel. You become a celebrated scientist, but the mystery of the Keepers remains unsolved.")
    print("--- GOOD ENDING: Scientific Breakthrough ---")
    return


def explore_source():
    print(
        "You decide to explore further, searching for the source of the energy. You discover a hidden dimension, home to the Keepers. You learn their secrets and become a guardian of the galaxy.")
    print("--- SECRET ENDING: Guardian of the Galaxy ---")
    return


def repair_return():
    print(
        "You manage to repair the ship and return to Earth. You share your discovery, but the mystery of the Keepers remains unsolved. You live a quiet life, haunted by the encounter.")
    print("--- NEUTRAL ENDING: Quiet Return ---")
    return


def continue_explore():
    print(
        "You continue exploring, hoping to find a safe haven. You discover a hidden colony of survivors, and you become their leader. You build a new life in the vastness of space.")
    print("--- NEUTRAL ENDING: New Colony ---")
    return


# Game Flow
choice = start_game()
if choice == "1":
    stabilize_ship()
elif choice == "2":
    brace_impact()
else:
    print("Invalid choice. The ship's systems are failing. You have no time to waste.")
    start_game()
