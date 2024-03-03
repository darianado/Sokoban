def parse_plan(plan_str):
    lines = plan_str.strip().split('\n')
    actions = [line for line in lines if line.startswith("move") or line.startswith("push")]
    return actions

def apply_action(state, action):
    parts = action.split()
    action_name = parts[0]
    locations = parts[1:]

    if action_name.startswith("move-agent"):
        state["agent-at"] = locations[1]

    elif action_name.startswith("push-box"):
        box_location = locations[0]
        new_box_location = locations[2]
        state["box-at"].discard(box_location)
        state["box-at"].add(new_box_location)
        state["agent-at"] = box_location

    return state

def calculate_novelty(state, seen_states):
    hashable_state = (state["agent-at"], frozenset(state["box-at"]))
    if hashable_state not in seen_states:
        seen_states.add(hashable_state)
        return len(hashable_state) 
    return 0

# Initial state for the Sokoban problem
initial_state = {
    "agent-at": "l25",  # Adjust this as per your problem's initial state
    "box-at": set(["l23", "l33", "l34","l46"])  # Adjust this as per your problem's initial box locations
}

# Replace this string with your actual plan
plan_str = """move-agent-s l25 l35 (1)
move-agent-s l35 l45 (1)
move-agent-v l45 l44 (1)
move-agent-v l44 l43 (1)
move-agent-v l43 l42 (1)
move-agent-n l42 l32 (1)
move-agent-n l32 l22 (1)
push-box-e l23 l22 l24 (1)
push-box-s l33 l23 l43 (1)
move-agent-n l33 l23 (1)
push-box-e l24 l23 l25 (1)
push-box-e l25 l24 l26 (1)
move-agent-s l25 l35 (1)
move-agent-e l35 l36 (1)
move-agent-e l36 l37 (1)
move-agent-s l37 l47 (1)
push-box-v l46 l47 l45 (1)
push-box-v l45 l46 l44 (1)
move-agent-n l45 l35 (1)
move-agent-n l35 l25 (1)
move-agent-v l25 l24 (1)
move-agent-v l24 l23 (1)
move-agent-s l23 l33 (1)
push-box-e l34 l33 l35 (1)
move-agent-v l34 l33 (1)
move-agent-v l33 l32 (1)
move-agent-s l32 l42 (1)
move-agent-s l42 l52 (1)
move-agent-e l52 l53 (1)
push-box-n l43 l53 l33 (1)
move-agent-v l43 l42 (1)
move-agent-n l42 l32 (1)
move-agent-n l32 l22 (1)
move-agent-e l22 l23 (1)
move-agent-e l23 l24 (1)
move-agent-s l24 l34 (1)
push-box-e l35 l34 l36 (1)
move-agent-s l35 l45 (1)
move-agent-e l45 l46 (1)
move-agent-e l46 l47 (1)
move-agent-n l47 l37 (1)
push-box-v l36 l37 l35 (1)
move-agent-s l36 l46 (1)
move-agent-v l46 l45 (1)
push-box-v l44 l45 l43 (1)
move-agent-n l44 l34 (1)
move-agent-n l34 l24 (1)
move-agent-v l24 l23 (1)
move-agent-v l23 l22 (1)
move-agent-s l22 l32 (1)
push-box-e l33 l32 l34 (1)
move-agent-v l33 l32 (1)
move-agent-s l32 l42 (1)
move-agent-s l42 l52 (1)
move-agent-e l52 l53 (1)
push-box-n l43 l53 l33 (1)"""

actions = parse_plan(plan_str)
current_state = initial_state
seen_states = set()
novelty_scores = []

for action in actions:
    current_state = apply_action(current_state, action)
    novelty = calculate_novelty(current_state, seen_states)
    novelty_scores.append(novelty)

# Print the novelty of each state
for i, novelty in enumerate(novelty_scores):
    print(f"Step {i+1}, Action: {actions[i]}, Novelty: {novelty}")










