import os

days_config = [
    {
        "day": 1,
        "topic": "Python Basics & Data Structures",
        "story": "Opening VS Code for the first time, feeling overwhelmed, and writing the first line of code.",
        "hook": "I have exactly 90 days to learn Data Science from scratch, or I’ll be stuck in my current career forever.",
        "learning": "Starting small is the only way to beat overwhelm.",
        "emotion": "Determined and slightly anxious.",
        "on_camera_dialogue": "Today is Day 1. [Slight smile] The mission? Python basics. Opening VS Code for the first time was super intimidating. [Look down slightly, then back to camera]. But I started small. Variables, basic math, and finally getting my first line of code to actually work. [Small triumphant smile]. It’s a tiny win, but I'll take it. Tomorrow, we tackle loops. Wish me luck.",
        "b_rolls": ["Cross off Day 1 on calendar", "Staring intently at laptop", "Typing print('Hello World')"]
    },
    {
        "day": 2,
        "topic": "Data Types & Type Conversion",
        "story": "Spent 45 minutes stuck on a TypeError trying to add a string and integer.",
        "hook": "I thought Python was supposed to be easy. I was wrong.",
        "learning": "Strings and integers don't mix without conversion.",
        "emotion": "Frustration turning into relief.",
        "on_camera_dialogue": "Day 2, and I’m learning about data types. [Sigh, slight head shake]. I literally spent 45 minutes trying to figure out why the computer was yelling at me for adding a number to a word. [Pause for effect]. Pro tip: you can't do that. After a ton of Googling and feeling really dumb, I finally learned about type conversion. [Relieved exhale]. Brain is completely fried, but the code works!",
        "b_rolls": ["Big red TypeError on screen", "Aggressively rubbing face", "Typing int() and hitting run"]
    },
    {
        "day": 3,
        "topic": "Conditional Statements",
        "story": "Nesting if/else statements and breaking the logic. Used rubber duck debugging.",
        "hook": "If you want to be a programmer, get ready to talk to yourself a lot.",
        "learning": "Rubber duck debugging is a real, effective strategy.",
        "emotion": "Humorous realization.",
        "on_camera_dialogue": "Day 3, and today was all about conditional statements. [Chuckle]. It sounds easy, right? But when you nest them together, your logic can break instantly. [Look slightly off camera, recalling]. I literally had to explain my code out loud to an empty room to find my mistake. It's called rubber duck debugging... and guys, it actually works.",
        "b_rolls": ["Talking to the laptop", "Messy if-elif-else block", "Rubber duck on desk"]
    },
    {
        "day": 4,
        "topic": "Loops",
        "story": "Accidentally creating an infinite while loop and crashing the terminal.",
        "hook": "I just accidentally crashed my computer with 3 lines of code.",
        "learning": "Always write the loop break condition first.",
        "emotion": "Panic turning into a lesson learned.",
        "on_camera_dialogue": "Welcome to Day 4. Today I learned about 'while' loops. [Wide eyes]. I forgot to write the false condition. My laptop fan literally sounded like an airplane taking off. [Mime taking off]. Complete panic. Lesson learned: always write your loop control first. My laptop survived.",
        "b_rolls": ["Terminal scrolling infinitely", "Panicked hitting Ctrl+C", "Slumping in chair relieved"]
    },
    {
        "day": 5,
        "topic": "Lists & Tuples",
        "story": "Trying to memorize methods and realizing professional devs just read docs.",
        "hook": "Here’s a secret about coding: you don’t actually memorize anything.",
        "learning": "Stop memorizing, start understanding and reading docs.",
        "emotion": "Enlightenment.",
        "on_camera_dialogue": "Day 5, Lists and Tuples. [Leaning in]. At first, I was trying to memorize every single method like a textbook. [Shake head]. It was exhausting. Then I realized... nobody does that. Real developers use Google and read the docs. Once I stopped memorizing, my coding speed doubled.",
        "b_rolls": ["Messy notebook with crossed lines", "Python docs next to VS Code", "Typing smoothly with coffee"]
    },
    {
        "day": 6,
        "topic": "Dictionaries & Sets",
        "story": "Structuring real information with key-value pairs, feeling like real data science.",
        "hook": "Today, my code finally started to look like actual data science.",
        "learning": "Key-value pairs make data retrieval instant and logical.",
        "emotion": "Satisfaction and progress.",
        "on_camera_dialogue": "Day 6. Dictionaries and Sets. For the first time, I wasn't just printing random strings. [Confident look]. I was structuring real data using key-value pairs. I wrote a script that can look up info instantly. It honestly felt like solving a puzzle where all the pieces finally snapped together.",
        "b_rolls": ["Clean Python Dictionary on screen", "Working at desk during golden hour", "Crossing Day 6 on calendar"]
    },
    {
        "day": 7,
        "topic": "Functions",
        "story": "Packaging messy code into reusable blocks. Completing week 1.",
        "hook": "I just survived my first full week of coding every single day.",
        "learning": "Functions make code clean, reusable, and professional.",
        "emotion": "Triumphant and proud.",
        "on_camera_dialogue": "Day 7. [Big smile]. Today was the boss fight: Functions. Instead of copy-pasting the same twenty lines, I learned how to package it into one reusable block. [Pause]. It was confusing at first. But when it clicked? My code went from a messy draft to a clean machine. Week one is officially in the books.",
        "b_rolls": ["GitHub 7-day streak", "Replacing code with calculate_data()", "Stretching arms up at desk"]
    },
    {
        "day": 8,
        "topic": "File Handling",
        "story": "Making the code remember data by reading and writing to text files.",
        "hook": "Today I gave my code the ability to remember things.",
        "learning": "File handling connects code to the hard drive.",
        "emotion": "Excited about new capabilities.",
        "on_camera_dialogue": "Day 8, beginning of week two. Up until today, every time I closed my program, all the data vanished. [Serious face]. But today, I learned File Handling. Seeing my code manipulate actual files on my hard drive felt like unlocking a massive new superpower. We are finally moving beyond the terminal.",
        "b_rolls": ["Running script then opening .txt file", "Typing 'with open'", "Nodding in approval at screen"]
    },
    {
        "day": 9,
        "topic": "Object-Oriented Programming (OOP)",
        "story": "Hitting a wall with classes and polymorphism, drawing it out on paper.",
        "hook": "I stared at my screen for an hour today and understood absolutely nothing.",
        "learning": "Stepping away and drawing concepts out makes complex logic simple.",
        "emotion": "Vulnerable, then determined.",
        "on_camera_dialogue": "Day 9. I finally hit my first real wall: Object-Oriented Programming. [Defeated sigh]. Classes, objects, polymorphism... I just couldn't grasp it. So, I stepped away. I made a coffee and literally drew it out on paper. [Slight smile]. And you know what? It slowly started making sense. It was brutal, but I didn't quit.",
        "b_rolls": ["Head on desk in defeat", "Drawing Car class on paper", "Stirring coffee staring out window"]
    },
    {
        "day": 10,
        "topic": "Constructors & Mini Project",
        "story": "Building a working system to prove understanding of OOP.",
        "hook": "10 days ago, I couldn't write a single line of code. Today, I built a system.",
        "learning": "Understanding 'self' and constructors solidifies OOP.",
        "emotion": "Victorious and ready for the future.",
        "on_camera_dialogue": "Day 10. After completely struggling with OOP yesterday, I had to prove to myself that I understood it. [Confident stance]. I used constructors to build a mini project. Actually typing 'self.name' and knowing exactly what it means? [Smile]. Unbelievably rewarding. Ten days down, eighty to go. Tomorrow... the real data science begins.",
        "b_rolls": ["Crossing Day 10 with thick marker", "Scrolling clean OOP code with __init__", "Confident smile at camera"]
    }
]

import os

base_dir = "Content_System"
os.makedirs(base_dir, exist_ok=True)

for day_info in days_config:
    day_num_str = f"{day_info['day']:02d}"
    day_path = os.path.join(base_dir, f"Day_{day_num_str}")
    os.makedirs(day_path, exist_ok=True)

    # 1. Script.md
    with open(os.path.join(day_path, "Script.md"), "w") as f:
        f.write(f"""# Video Overview: Day {day_info['day']}

## Meta
- **Title**: Day {day_info['day']} of Becoming a Data Scientist
- **Topic**: {day_info['topic']}
- **Duration**: ~45-55 seconds
- **Goal**: Show authentic progress and struggles of the day.
- **Emotion**: {day_info['emotion']}

## Core Narrative
- **Hook (0-5s)**: "{day_info['hook']}"
- **Main Story**: {day_info['story']}
- **Key Learning**: {day_info['learning']}
""")

    # 2. Shot_List.md
    with open(os.path.join(day_path, "Shot_List.md"), "w") as f:
        f.write(f"""# Shot List: Day {day_info['day']}

## Main Shots (A-Roll)
1. **The Hook Shot (0-5s)**: Frontal Mid-Shot on tripod. Looking directly into lens. 
2. **The Storyteller (10-35s)**: Same angle, used as base narrative track. Portable Ulanzi light on.
3. **The Payoff (50-60s)**: Slight punch-in on face for emotional ending.

## B-Roll List (20-40 Cinematic Ideas)
*Remember: No filler. Every shot must show emotion or progress.*
1. **{day_info['b_rolls'][0]}**: POV angle. Purpose: Establish time/progress.
2. **{day_info['b_rolls'][1]}**: Over the shoulder. Purpose: Show the struggle/action.
3. **{day_info['b_rolls'][2]}**: Screen recording. Purpose: Show the code working (or failing).
4. **Typing on Keyboard**: Extreme close up. Shallow depth of field.
5. **Mouse Click**: Macro shot.
6. **Coffee Cup Placement**: Side angle, low to desk.
7. **Opening Laptop**: POV shot.
8. **GitHub Commits**: Screen recording with smooth zoom in post.
9. **Stretching at desk**: Wide shot, tripod.
10. **Walking to desk**: Tracking shot (Gimbal).
*(Film 10-15 more variations of studying, note-taking, and screen elements to intercut)*
""")

    # 3. Camera_Guide.md
    with open(os.path.join(day_path, "Camera_Guide.md"), "w") as f:
        f.write("""# Camera Guide

## Vlogging Fundamentals (Applied Daily)
- **Framing**: Use Rule of Thirds grid. Eyes on the top-third line.
- **Look Space**: If not looking at the lens, leave empty space in the direction you are looking.
- **Stabilization**: A-Roll must be on a TRIPOD. Dynamic B-roll must be on a GIMBAL or very stable handheld.
- **Lighting**: Use Ulanzi VL49 (or similar) portable light mounted on the phone for all face shots to eliminate shadows. Ensure face is brighter than background.
- **Exposure**: Lock focus and exposure (AE/AF lock) on phone before recording to prevent flickering.

## Shot Types to Capture
- **POV**: Chest height, immersive.
- **Over-the-shoulder**: Show you and the screen together.
- **Macro/Close-up**: Fingers typing, eyes scanning.
""")

    # 4. Voiceover.md
    with open(os.path.join(day_path, "Voiceover.md"), "w") as f:
        f.write(f"""# Voiceover Script

*Record this in a quiet environment if the room tone is too loud during A-Roll recording. Keep it conversational.*

"{day_info['hook']} {day_info['on_camera_dialogue']}"

**Direction**: Don't read like a robot. Imagine you are leaving a voice note for a close friend explaining your day. Pause where natural.
""")

    # 5. On_Camera.md
    with open(os.path.join(day_path, "On_Camera.md"), "w") as f:
        f.write(f"""# On-Camera Dialogue Guide

**Dialogue**: 
"{day_info['hook']}"
*(Cut to B-Roll)*
"{day_info['on_camera_dialogue']}"

**Performance Notes**:
- Emotion: {day_info['emotion']}
- Eye Contact: Maintain strong eye contact during the hook and the ending.
- Pauses: Let the realizations breathe. Don't rush the words.
""")

    # 6. Editing_Guide.md
    with open(os.path.join(day_path, "Editing_Guide.md"), "w") as f:
        f.write("""# Editing Guide

## Philosophy
- **NO FILLER**: If a scene doesn't push the story forward, cut it.
- **Pacing**: Cut all dead air and breathing pauses between sentences.
- **Transitions**: Hard cuts only. No flashy slide/zoom transitions unless specifically motivated by the story (e.g., passing time).
- **A-Roll to B-Roll**: Start hearing the B-Roll audio slightly before seeing it (J-Cut).

## Export Settings
- Minimum 1080p, 60fps (or match source frame rate).
- High Bitrate.
""")

    # 7. Thumbnail.md
    with open(os.path.join(day_path, "Thumbnail.md"), "w") as f:
        f.write(f"""# Thumbnail & Freeze Frame

## Composition
- **Freeze Frame Selection**: Choose a highly emotional frame (Frustrated, victorious, or deeply focused).
- **Facial Expression**: {day_info['emotion']}
- **Overlay Text**: Very short (1-3 words). E.g., "DAY {day_info['day']}: {day_info['topic'].split()[0].upper()}!"
- **Contrast**: Ensure your face is bright and the background is slightly darkened.
""")

    # 8. Upload_Checklist.md
    with open(os.path.join(day_path, "Upload_Checklist.md"), "w") as f:
        f.write(f"""# Upload Package

## Metadata
- **YouTube Title**: Day {day_info['day']} of Becoming a Data Scientist | {day_info['topic']}
- **Description**: Documenting my 90-Day Data Science Journey. Today was Day {day_info['day']} covering {day_info['topic']}. {day_info['learning']}
- **Hashtags**: #DataScience #Coding #Python #ProgrammingJourney #100DaysOfCode
- **Pinned Comment**: What was your biggest struggle when learning {day_info['topic']}? Let me know 👇

## Checklist
- [ ] Thumbnail selected
- [ ] Title optimized
- [ ] Tags added
- [ ] End screen added
- [ ] Pinned comment posted
""")

    # 9. Assets.md
    with open(os.path.join(day_path, "Assets.md"), "w") as f:
        f.write(f"""# Post-Production Assets

## Sound Design (SFX)
- **Keyboard Typing**: Underneath all coding B-rolls.
- **Mouse Click**: To emphasize an action (running code).
- **Whoosh/Swoosh**: Subtle, only for fast B-roll movements or text appearing.
- **Room Ambience**: Soft background noise if A-Roll is completely silent.

## Music Guide
- **Mood**: {day_info['emotion']} to Hopeful.
- **Style**: Lo-fi beats or cinematic documentary (e.g., Artlist/Epidemic Sound).
- **Volume**: Ducked to -18dB to -24dB under the voice track.

## Text Overlays
- **Hook Text**: Pop in exactly when spoken.
- **Day Tracker**: "Day {day_info['day']}/90" in a clean, minimal font (e.g., Montserrat or Roboto) in the corner.
- **Animation**: Simple pop or slight scale up. No aggressive shaking.

## Color Grading
- **Vibe**: Keep it consistent for the 90 days. Slightly warm, good contrast.
- **Faces**: Keep skin tones natural.
- **Shadows**: Slightly lifted for a modern cinematic look.
""")

print(f"Successfully generated Content_System with 10 days and 90 files.")
