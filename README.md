# Open Design and Technology  
## Final Project README

> **Project Weight:** 70%  
> **Team Size:** 2 students  
> **Project Duration:** 4 weeks  
> **Class Time Available:** 6 hours per class  
> **Total Time Available:** 48 effort-hours per team  
> **Project Type:** Playful, interactive, technology-based experience

---

# Before you begin

## Fork and rename this repository
After forking this repository, rename it using the format:

`ODT-2026-TeamName`

### Example
`ODT-2026-PixelWizards`

Do not keep the default repository name.

---

# How to use this README

This file is your team’s **working project document**.

You must keep updating it throughout the 4-week build period.  
By the final review, this README should clearly show:
- your idea,
- your planning,
- your design decisions,
- your technical process,
- your build progress,
- your testing,
- your failures and changes,
- your final outcome.

## Rules
- Fill every section.
- Do not delete headings.
- If something does not apply, write `Not applicable` and explain why.
- Add images, screenshots, sketches, links, and videos wherever useful.
- Update task status and weekly logs regularly.
- Use this file as evidence of process, not only as a final report.

---

# 1. Team Identity

## 1.1 Studio / Group Name
`[Pirate escape maze]`

## 1.2 Team Members

| Name | Primary Role | Secondary Role | Strengths Brought to the Project |
|---|---|---|---|
| `[Munna Madhurima]` | `[Electronics / Coding]` | `[Fabrication / Mechanics]` | `[Developed MicroPython code, integrated ESP32 with sensors and actuators, built and tested obstacle mechanisms, debugged hardware and power issues]` |
| `[Lara Ruth Pinto]` | `[ Fabrication / Mechanics]` | `[Electronics / Coding ]` | `[Designed visual theme and pirate aesthetics, created props and physical elements, tested obstacle mechanisms, developed layout and user experience, ensured engaging presentation of the maze]` |

## 1.3 Project Title
`[Pirate escape maze ]`

## 1.4 One-Line Pitch
`[An interactive pirate-themed escape maze where players solve clues and trigger sensor-based obstacles to unlock a hidden treasure.]`

## 1.5 Expanded Project Idea
In 1–2 paragraphs, explain:
- what your project is,
- what kind of playful experience it creates,
- what makes it fun, curious, engaging, strange, satisfying, competitive, or delightful,
- what technologies are involved.

**Response:**  
`[This project is a life-sized pirate treasure hunt played across four Z-boards arranged like a maze. Players move from one obstacle to the next, finding coordinates on maps, targeting the right ship, and finally unlocking a treasure chest using collected cards. The experience mixes simple logic puzzles with physical actions: searching through maps, entering codes, aiming at an enemy ship with laser, and choosing the correct pattern card to place on the chest. Servo-driven reveals, an RFID card reader, and sound feedback (including the Pirates of the Caribbean theme) make each correct action feel like a small win that leads to the final treasure. Technologies used include an ESP32 microcontroller, push buttons, servo motors, LDR sensor, laser module, RFID reader, buzzer, and audio output.]`

---

# 2. Philosophy Fit

## 2.1 Experience, Not Social Problem
This module does **not** require your project to solve a large social problem.

You are allowed to build:
- toys,
- games,
- interactive objects,
- playful machines,
- kinetic artifacts,
- humorous devices,
- strange but delightful experiences,
- things that are entertaining to use or watch.

## 2.2 What kind of experience are you creating?
Answer the following:
- What is the experience?
- What do you want the player or participant to feel?
- Why would someone want to try it again?

**Response:**  
`[1. This is a short, physical treasure hunt where players walk through a set of pirate‑themed boards and solve linked clues to reach a chest.
2. Curious at the start, slightly tense while solving each step, and satisfied when the chest finally unlocks and the music plays.
3. They may want to see how fast they can clear all three obstacles, or watch friends struggle on the steps that they solved.]`

## 2.3 Design Persona
Complete the sentence below:

> We are designing this project as if we are a small creative studio making a **[toy / game / playable object / interactive experience]** for **[children / teens / adults / classmates / exhibition visitors / mixed audience]**.

**Response:**  
`[We are designing this project as if we are a small creative studio making an interactive game experience for classmates and exhibition visitors.]`

---

# 3. Inspiration

## 3.1 References
List what inspired the project.

| Source Type | Title / Link | What Inspired You |
|---|---|---|
| `YouTube` | `Pirate Escape Room Videos` | `[Inspired the idea of clue based progression and themed storytelling through multiple stages]` |
| `[Escape/Mystery room/laser tag]` | `Laser Target Shooting Games` | `Inspired the use of laser aiming and sensor based interaction for triggering events` |
| `[Movie ]` | `[Pirates of the Caribbean]` | `[Inspired the pirate theme, treasure hunt concept, and use of sound and atmosphere to create immersion]` |

## 3.2 Original Twist
What makes your project original?

**Response:**  
`[Instead of one big lock at the end, the “key” for the chest is built up across the whole journey. Players collect physical cards from earlier obstacles, and only one of them will actually unlock the chest.
The other twist is scale: this is not a board game on a table. Players walk through a mini maze of Z‑boards, aim at enemy ships, and reach into openings for cards, so their whole body is involved, not just their hands.]`

---

# 4. Project Intent

## 4.1 Core Interaction Loop
Describe the main loop of interaction.

Examples:
- press → launch → score → reset
- connect → control → observe → repeat
- turn → trigger → react → repeat
- move object → sensor detects → sound/light response → player reacts

**Response:**  
`[At each obstacle:
see a hint, 
try something in the space, 
watch what moves or makes sound, 
collect a card, 
move on to the next obstacle
Repeated 2 times, building up to the final chest where all the earlier choices matter.]`

## 4.2 Intended Player / Audience    

| Question | Response |
|---|---|
| Who is this for? | `[Classmates, exhibition visitors, and general audience]` |
| Age range | `[15 to 18 years, but suitable for older users as well]` |
| Solo or multiplayer | `[Both, can be played individually or in small groups]` |
| Expected duration of one round | `[3 to 10 minutes]` |
| What should the player feel? | `[Curiosity, excitement, challenge, and satisfaction]` |
| Is explanation required before use? | `[Minimal explanation required, basic instructions are enough]` |

## 4.3 Player Journey
Describe exactly how a player will use the project.

1. **Approach:** `[The player notices a pirate themed setup with a map and treasure elements that attract attention.]`
2. **Start:** `[At the first board, they notice several maps on a table and a short hint about coordinates and “a single number not being enough.” ]`
3. **First Action:** `[The player identifies the coordinates clue and presses the correct buttons to input the code, giving them a card to take ahead into the maze.]`
4. **Main Interaction:** `[The player continues solving puzzles, aiming the laser at the correct target, and collecting clue cards while interacting with different obstacles.]`
5. **System Response:** `[The system responds through servo movements such as card release and box opening, along with sound feedback like buzzer alerts or theme music.]`
6. **Win / Lose / End Condition:** `[They “win” when they place the correct final card, hear the Pirates of the Caribbean tune, and the chest lid lifts. They “lose” if they never reach that state before time, patience, or a soft time‑limit runs out.]`
7. **Reset:** `[We reset by putting cards back into their slots, closing the chest, returning the maps, and setting all servos to their starting positions.]`

## 4.4 Rules of Play
If your project is a game, list the rules clearly.

- `[- Players must go through the obstacles in order and cannot skip ahead to the chest.  ]`
- `[- They should interact only with the provided elements such as buttons, laser, and cards ]`
- `[- At the ship board, they can only shoot once they unlock the math equation. ]`
- `[- The chest only unlocks when the correct final card is placed on the RFID sensor; decoy cards will trigger the error buzzer and keep it locked. ]`

---

# 5. Definition of Success

## 5.1 Definition of “Playable”
Your project will be considered complete only if these conditions are met.

- [ ] `All three obstacles can be completed in one continuous run without manual fixing in between. ]`
- [ ] `[Servos consistently provide cards at every obstacle and open the final chest without stalling. ]`
- [ ] `[Laser detection using LDR correctly triggers the second mechanism  ]`
- [ ] `[RFID system correctly identifies cards, plays the theme song and opens the treasure box]`
- [ ] `[The buzzer clearly plays the theme for success and a distinct long tone for errors.]`
- [ ] `[A first‑time player can finish a round after only a short explanation at the start.]`


## 5.2 Minimum Viable Version
What is the smallest version of this project that still delivers the core experience?

**Response:**  
`[The minimum version of this project includes one working puzzle followed by a final treasure box interaction. For example, a single input based challenge such as button or laser interaction that releases a card, followed by an RFID based system that opens the treasure box. This still delivers the core experience of solving a clue and unlocking the treasure.]`

## 5.3 Stretch Features
What features are nice to have but not essential?

- `[Additional obstacles or puzzle stages to increase difficulty ]`
- `[LED lighting effects to enhance visual feedback and theme ]`
- `[Timer or scoring system to make the experience more competitive  ]`

---

# 6. System Overview

## 6.1 Project Type
Check all that apply.

- [x] Electronics-based  
- [x] Mechanical  
- [x] Sensor-based  
- [ ] App-connected  
- [x] Motorized  
- [x] Sound-based  
- [x] Light-based  
- [ ] Screen/UI-based  
- [x] Fabricated structure  
- [x] Game logic based  
- [x] Installation / tabletop experience  
- [ ] Other:  

## 6.2 High-Level System Description
Explain how the system works in simple terms.

Include:
- input,
- processing,
- output,
- physical structure,
- app interaction if any.

**Response:**  
`[ The system is built using an ESP32 microcontroller and is divided into two setups. Inputs include push buttons for entering a passcode, an LDR sensor for detecting laser light, and an RFID reader for identifying cards. These inputs are used at different stages of the maze to interact with the system.The processing is handled by the ESP32 using MicroPython, where the program checks conditions such as correct button combinations, laser detection, and valid RFID card input. Based on these conditions, the system decides the next action.The outputs include servo motors that perform physical actions such as sliding out cards and opening the treasure box. Sound output is provided using a buzzer and audio module for feedback such as success music or error alerts.The physical structure consists of a pirate themed maze with props, maps, clue cards, and a treasure box that guides the player through each obstacle. The first obstacle uses a breadboard and direct power supply, while the second and third obstacles use a separate setup powered through a buck converter for stable operation.There is no app interaction in this project, as it is a fully standalone physical interactive system.]`

## 6.3 Input / Output Map

| System Part | Type | What It Does |
|---|---|---|
| `[ Push buttons, LDR sensor, RFID reader]` | Input  | `[Takes user actions such as button press, laser detection, and card scanning ]` |
| `[ESP32 microcontroller]` | Processing | `[Processes inputs using MicroPython logic and decides the correct output action]` |
| `[Servo motors, buzzer]` | Output | `[Controls physical movement like card release and box opening, and provides sound feed]` |
| `[Maze structure, props, treasure box]` | Physical Action | `[Provides the physical setup where players interact, solve puzzles, and progress through the game]` |

---

# 7. Sketches and Visual Planning

## 7.1 Concept Sketch
Add an early sketch of the full idea.

**Insert image below:**  
`[Upload image and link here]`

Example:
```md

```

## 7.2 Labeled Build Sketch
Add a sketch with labels showing:
- structure,
- electronics placement,
- user touch points,
- moving parts,
- output elements.

**Insert image below:**  
`[Upload image and link here]`

## 7.3 Approximate Dimensions

| Dimension | Value |
|---|---|
| Length | `[Approximately 6 to 7 meters]` |
| Width | `[Approximately 4 to 5 meters]` |
| Height | `[Write here Approximately 1.8 to 2 meters (Z board height)]` |
| Estimated weight | `[Approximately 25 to 35 kg including boards, A0 posters, electronics, and props]` |

---

# 8. Mechanical Planning

## 8.1 Mechanical Features
Check all that apply.

- [ ] Gears  
- [ ] Pulleys  
- [ ] Belt drives  
- [ ] Linkages  
- [x] Hinges  
- [ ] Shafts  
- [ ] Springs  
- [ ] Bearings  
- [ ] Wheels  
- [x] Sliders  
- [ ] Levers  
- [ ] Not applicable  

## 8.2 Mechanical Description
Describe the mechanism and what it is meant to do.

**Response:**  
`[The mechanical system of the project is based on servo motor movements that create physical interactions. In the first and second obstacles, servo motors are used to slide out cards when the correct input is detected. This is achieved using simple sliding mechanisms where the servo rotation (360 and 180) pushes or releases the card.In the final obstacle, a servo motor is placed inside the treasure box to control the opening and closing of the lid using a hinge mechanism. Additional support elements were used to stabilize the servo and maintain balance inside the box, ensuring smooth and reliable movement.The overall mechanism is simple but effective, focusing on controlled motion and physical feedback. These movements help create a clear cause and effect interaction, making the experience more engaging for the player.]`

## 8.3 Motion Planning
If something moves, explain:
- what moves,
- what causes the movement,
- how far it moves,
- how fast it moves,
- what could go wrong.

**Response:**  
`[The main movements in the system are the sliding of cards and the opening of the treasure box. These movements are caused by servo motors that rotate when the correct input is detected by the system.The cards move a short distance forward when released, enough for the player to collect them. The treasure box lid rotates using a hinge mechanism to open and close. The speed of movement is moderate, controlled through the servo to ensure smooth and visible motion for the player.Possible issues include the servo not having enough power to move the mechanism, misalignment of the sliding parts, or unstable mounting inside the treasure box. These were managed by adjusting positioning and adding support elements to stabilize the components.]`

## 8.4 Simulation / CAD / Animation Before Making
If your project includes mechanical motion, document the digital planning before fabrication.

| Tool Used | File / Link | What Was Tested |
|---|---|---|
| `[Procreate, Illustrator, Photoshop]` | `[Design files]` | `[Visual layout, poster design, and overall theme planning]` |



| `[Manual prototyping for obstacles]` |[ <img width="1280" height="960" alt="image" src="https://github.com/user-attachments/assets/ccf278fe-937a-46ad-8260-b500184a8ed2" /> <img width="1280" height="960" alt="image" src="https://github.com/user-attachments/assets/f5d4259c-eefd-4b5d-bf8b-3c3d732b4973" />  <img width="1280" height="960" alt="image" src="https://github.com/user-attachments/assets/9f6e3452-f732-4f3b-95e3-9a7ddcfe730f" /> ] | `[Tested circuit connections, sensor responses, and servo behavior before final setup]` |

## 8.5 Changes After Digital Testing
What changed after the CAD, animation, or simulation stage?

**Response:**  
`[After initial testing and prototyping, several changes were made to improve stability and functionality. The positioning of servo motors was adjusted to ensure proper movement, and additional support elements were added inside the treasure box to maintain balance. The circuit setup was divided into two systems with a buck converter used for the later stages to provide stable power as 2 servo motors and an RFID card reader were operating on the same breadboard. The placement of sensors and components was also refined to improve accuracy and user interaction.]`

---

# 9. Electronics Planning

## 9.1 Electronics Used

| Component | Quantity | Purpose |
|-----------|----------|---------|
| `[ESP32]` | `[2]` | `[Main controller for handling inputs and outputs across obstacles]` |
| `[Servo Motor (SG90)]` | `[3]` | `[Used to slide cards and open the treasure box]` |
| `[Push Buttons]` | `[2]` | `[Used for passcode input in the first obstacle]` |
| `[LDR Sensor]` | `[1]` | `[Detects laser light in the aiming challenge]` |
| `[Laser Module]` | `[1]` | `[Used as the aiming tool for the second obstacle]` |
| `[RFID Reader (MFRC522)]` | `[1]` | `[Detects correct card for final treasure unlock]` |
| `[Buzzer]` | `[1]` | `[Provides error sound feedback]` |
| `[Audio Module / Speaker]` | `[1]` | `[Plays pirate theme music on success]` |
| `[Breadboard]` | `[2]` | `[Used for circuit connections]` |
| `[Buck Converter]` | `[1]` | `[Provides stable voltage for later obstacles]` |
| `[Power Supply]` | `[2]` | `[Supplies power to both setups]` |
| `[Jumper Wires]` | `[Multiple]` | `[Connects all components together]` |

## 9.2 Wiring Plan
Describe the main electrical connections.

**Response:**  
`[The system is divided into two main circuits. In the first circuit, push buttons are connected to the ESP32 input pins, and a servo motor is connected to a PWM pin to control card movement. This setup is powered using a direct power supply through a breadboard.In the second circuit, the LDR sensor and RFID reader are connected to the ESP32 as input devices, while servo motors, buzzer, and audio module are connected as outputs. A buck converter is used to regulate voltage and provide stable power to the components. All components share a common ground to ensure proper signal flow.]`

## 9.3 Circuit Diagram
Insert a hand-drawn or software-made circuit diagram.

**Insert image below:**  
[ <img width="2480" height="3508" alt="obstacle 1 circuit" src="https://github.com/user-attachments/assets/bb7cd715-f570-4909-a7b7-9b3cea788bd9" /> <img width="2480" height="3508" alt="obstacle 2 and 3 circuit" src="https://github.com/user-attachments/assets/60e973e6-b04c-4b31-9698-5f7f5a78a919" /> ]


## 9.4 Power Plan

| Question | Response |
|---|---|
| Power source | `[Adapter and external power supply]` |
| Voltage required | `[[5V for servo motors and components, 3.3V for ESP32 logic]` |
| Current concerns | `[Servo motors may draw higher current, requiring stable supply and buck converter]` |
| Safety concerns | `[Proper wiring, avoiding short circuits, and ensuring correct voltage levels to prevent damage]` |

---

# 10. Software Planning

## 10.1 Software Tools

| Tool / Platform | Purpose |
|---|---|
| `[MicroPython ]` | `[Used to program ESP32 for handling inputs, logic, and outputs]` |
| `[Thonny IDE]` | `[Used to write, upload, and debug MicroPython code]` |

## 10.2 Software Logic
Describe what the code must do.

Include:
- startup behavior,
- input handling,
- sensor reading,
- decision logic,
- output behavior,
- communication logic,
- reset behavior.

**Response:**  
`[The system starts by initializing all components such as input pins for buttons, LDR sensor, and RFID reader, along with output devices like servo motors, buzzer, and audio module. At startup, the system remains in a waiting state until the player begins interaction.Input handling is done by continuously checking button presses, laser detection through the LDR sensor, and RFID card input. Sensor readings are used to detect whether the correct action has been performed by the player.The decision logic checks if the inputs match the expected conditions for each obstacle. For example, correct button combinations trigger the first servo, correct laser detection triggers the second mechanism, and valid RFID input unlocks the treasure box.Output behavior includes activating servo motors to move or open mechanisms, and playing sound feedback through the buzzer or audio module. The system responds immediately after detecting correct or incorrect inputs.There is no communication logic as the system is standalone. Reset behavior is handled by returning all components to their initial state, such as closing the treasure box and resetting the obstacle conditions for the next player.]`

## 10.3 Code Flowchart
Insert a flowchart showing your code logic.

Suggested sequence:
- start,
- initialize,
- wait for input,
- read input,
- decision,
- trigger output,
- repeat or reset,
- error handling.

**Insert image below:**  

[<img width="1600" height="1200" alt="image" src="https://github.com/user-attachments/assets/f5c4330b-ade4-4c7d-a24e-2441fbabfd6f" />
<img width="865" height="453" alt="image" src="https://github.com/user-attachments/assets/73d580fd-1c2a-48f0-8e8f-64db6f722910" />]



`[Initialize all components including ESP32, servo motors, LDR sensor, RFID reader, and buzzer
Wait for input
System continuously waits for user interaction through laser input or RFID card
Read input
Read LDR sensor values to detect laser
Check for RFID card presence and read UID
Decision
Check if laser is detected based on LDR threshold
Check if RFID UID matches the stored correct UID
Trigger output
If laser is detected, rotate servo to release card
If correct RFID card is detected, open treasure box and play pirate sound
If wrong RFID card is detected, trigger error buzzer
Error handling
If incorrect input is given, no action or error sound is triggered
Repeat or reset
System resets servo positions and continues looping for the next player]`



## 10.4 Pseudocode

```text
[Start system
Initialize pins, sensors, and outputs

While system is running:
    Wait for button input
    If correct button combination:
        Activate servo to release card

    Wait for laser detection using LDR
    If laser detected:
        Activate servo to release next card

    Wait for RFID card input
    If correct card detected:
        Open treasure box using servo
        Play success sound
    Else:
        Play error sound

Reset system for next player
Repeat]
```

---

# 11. MIT App Inventor Plan

## 11.1 Is an app part of this project?
- [ ] Yes  
- [x] No  

If yes, complete this section.

## 11.2 Why is the app needed?
Explain what the app adds to the experience.

Examples:
- remote control,
- score tracking,
- mode selection,
- personalization,
- triggering effects,
- displaying data.

**Response:**  
`[Write here]`

## 11.3 App Features

| Feature | Purpose |
|---|---|
| `[Bluetooth connect button]` | `[Purpose]` |
| `[Score display]` | `[Purpose]` |
| `[Control button / slider / label]` | `[Purpose]` |

## 11.4 UI Mockup
Insert a sketch or screenshot of the app interface.

**Insert image below:**  
`[Upload image and link here]`

## 11.5 App Screen Flow

1. `[Step 1]`
2. `[Step 2]`
3. `[Step 3]`
4. `[Step 4]`

---

# 12. Bill of Materials

## 12.1 Full BOM

| Item | Quantity | In Kit? | Need to Buy? | Estimated Cost | Material / Spec | Why This Choice? |
|---|---:|---|---|---:|---|---|
| Item | Quantity | In Kit? | Need to Buy? | Estimated Cost | Material / Spec | Why This Choice? |
|---|---:|---|---|---:|---|---|
| `[ESP32]` | `2` | `1` | `1` | `375` | `[30-pin microcontroller]` | `[Main controller for handling inputs and outputs]` |
| `[Servo Motor (SG90)]` | `4` | `No` | `Yes` | `400` | `[90° micro servo]` | `[Used for movement like card release and box opening]` |
| `[LDR Sensor Module]` | `4` | `No` | `Yes` | `110` | `[Light sensor module]` | `[Used for laser detection]` |
| `[RFID Reader (RC522)]` | `1` | `No` | `Yes` | `150` | `[MFRC522 module]` | `[Used for final card detection]` |
| `[Breadboard Power Supply]` | `3` | `1` | `2` | `130` | `[5V/3.3V module]` | `[Used to provide stable power]` |
| `[Breadboard]` | `2` | `Yes` | `No` | `0` | `[Standard breadboard]` | `[Used for circuit connections]` |
| `[Jumper Wires Set]` | `1` | `Yes` | `No` | `0` | `[Male-Male/Female wires]` | `[Used for wiring connections]` |
| `[Push Buttons]` | `10` | `Yes` | `No` | `0` | `[Tactile switches]` | `[Used for input interactions]` |
| `[Buzzer]` | `1` | `Yes` | `No` | `0` | `[Piezo buzzer]` | `[Used for sound feedback]` |
| `[Buck Converter]` | `1` | `No` | `No (Borrowed)` | `0` | `[DC-DC converter]` | `[Used for stable voltage supply]` |

## 12.2 Material Justification
Explain why you selected your main materials and components.

Examples:
- Why acrylic instead of cardboard?
- Why MDF instead of 3D print?
- Why servo instead of DC motor?
- Why bearing instead of a plain shaft hole?

**Response:**  
`[The project uses foam board as the primary material for the structure due to its lightweight nature, ease of cutting, and flexibility in creating quick prototypes. It allows for fast iteration and easy modification, which was important during testing and changes in the design.Servo motors were chosen over DC motors because they provide precise control over angle and position, which is necessary for actions like sliding cards and opening the treasure box accurately.For the laser mechanism, a simple cylindrical structure made from readily available materials was used to guide and stabilize the laser module. This approach was cost-effective and easy to fabricate while still achieving the required functionality.Electronic components such as the ESP32, LDR sensors, and RFID module were selected because they are reliable, easy to integrate, and suitable for handling interactive input and output within the system.Overall, the materials were chosen based on availability, ease of fabrication, cost efficiency, and suitability for creating an interactive and functional prototype.]`

## 12.3 Items to Purchase Separately

| Item | Why Needed | Purchase Link | Latest Safe Date to Procure | Status |
|---|---|---|---|---|
| `[Item]` | `[Reason]` | `[Link]` | `[Date]` | `[Pending / Ordered / Received]` |
| `[Item]` | `[Reason]` | `[Link]` | `[Date]` | `[Pending / Ordered / Received]` |

## 12.4 Budget Summary

| Budget Item | Estimated Cost |
|---|---:|
| Item | Why Needed | Purchase Link | Latest Safe Date to Procure | Status |
|------|------------|---------------|-----------------------------|--------|
| `[ESP32]` | `[Replacement unit required after damage during testing]` | `[Local electronics store]` | `[Week 2]` | `[Received]` |
| `[Servo Motor (SG90)]` | `[Required for multiple movement mechanisms]` | `[Local electronics store]` | `[Week 2]` | `[Received]` |
| `[LDR Sensor Module]` | `[Initially planned for laser maze; one used for detection, others used as visual/dummy elements]` | `[Local electronics store]` | `[Week 3]` | `[Received]` |
| `[RFID Reader (RC522)]` | `[Required for final obstacle interaction]` | `[Local electronics store]` | `[Week 3]` | `[Received]` |
| `[Breadboard Power Supply]` | `[Purchased for power stability; later optimized using buck converter, resulting in excess units]` | `[Local electronics store]` | `[Week 2]` | `[Received]` |

## 12.5 Budget Reflection
If your cost is too high, what can be simplified, removed, substituted, or shared?

**Response:**  
`[The cost of the project can be reduced by minimizing the number of extra components purchased during experimentation. For example, fewer LDR sensors and power supply modules could have been used if the final design was decided earlier. Some components like the buck converter were shared instead of purchased, which helped reduce cost.The project can also be simplified by reusing components from the initial kit and avoiding duplicate purchases unless necessary. Additionally, using basic materials like foam board for structure instead of expensive materials helped keep the cost low. Overall, better planning and early decision making could help optimize the budget further.]`

---

# 13. Planning the Work

## 13.1 Team Working Agreement
Write how your team will work together.

Include:
- how tasks are divided,
- how decisions are made,
- how progress will be checked,
- what happens if a task is delayed,
- how documentation will be maintained.

**Response:**  
`[The team worked by dividing tasks based on strengths, with one member focusing on electronics and coding, and the other focusing on design, visuals, and fabrication. Decisions were made through discussion and testing different ideas before finalizing the approach.Progress was checked regularly by testing each obstacle and ensuring it worked before moving to the next stage. If a task was delayed, responsibilities were adjusted, and both members worked together to solve the issue.Documentation was maintained throughout the project by updating the README, recording changes, and organizing all components and steps clearly. This helped in keeping track of progress and ensuring smooth collaboration.]`

## 13.2 Task Breakdown

| Task ID | Task | Owner | Estimated Hours | Deadline | Dependency | Status |
|---|---|---|---:|---|---|---|
| T1 | `[Finalize concept and ideation (laser maze to escape maze)]` | `[Munna Madhurima]` | `3` | `[Week 1]` | `None` | `Done` |
| T2 | `[Complete BOM and component planning]` | `[Munna Madhurima]` | `1` | `[Week 1]` | `T1` | `Done` |
| T3 | `[Test electronics and components]` | `[Munna Madhurima]` | `3` | `[Week 2]` | `T1` | `Done` |
| T4 | `[Build structure and obstacles]` | `[Munna Madhurima]` | `5` | `[Week 2]` | `T1` | `Done` |
| T5 | `[Write control code for obstacles]` | `[Munna Madhurima]` | `5` | `[Week 3]` | `T3` | `Done` |
| T6 | `[Assist coding (first obstacle) and design visuals]` | `[Lara Ruth Pinto]` | `3` | `[Week 3]` | `T4, T5` | `Done` |
| T7 | `[Playtesting and debugging]` | `[Both]` | `2` | `[Week 3]` | `T6` | `Done` |
| T8 | `[Refine system and complete documentation]` | `[Both]` | `3` | `[Week 4]` | `T7` | `Done` |

## 13.3 Responsibility Split

| Area | Main Owner | Support Owner |
|---|---|---|
| Concept and gameplay | `[Munna Madhurima]` | `[Lara Ruth Pinto]` 
| Electronics  | `[Lara Ruth Pinto]` | `[Munna Madhurima]`|
| Coding | `[Munna Madhurima]` | `[Lara Ruth Pinto]` |
| App | `[None]` | `[None]` |
| Mechanical build | `[Munna Madhurima]` | `[Lara Ruth Pinto]` |
| Testing | `[Munna Madhurima]` | `[Lara Ruth Pinto]` |
| Documentation | `[Both]` | `[Both]` |

---

# 14. Weekly Milestones

## 14.1 Four-Week Plan

### Week 1 – Plan and De-risk  
Expected outcomes:  
- [x] Idea finalized  
- [x] Core interaction decided  
- [x] Sketches made  
- [x] BOM completed  
- [x] Purchase needs identified  
- [x] Key uncertainty identified  
- [x] Basic feasibility tested  

### Week 2 – Build Subsystems  
Expected outcomes:  
- [x] Electronics tests completed  
- [x] CAD / structure planning completed  
- [ ] App UI started if needed  
- [x] Mechanical concept tested  
- [x] Main subsystems partially working  

### Week 3 – Integrate  
Expected outcomes:  
- [x] Physical body built  
- [x] Electronics integrated  
- [x] Code connected to hardware  
- [ ] App connected if required  
- [x] First playable version exists  

### Week 4 – Refine and Finish  
Expected outcomes:  
- [x] Technical bugs reduced  
- [x] Playtesting completed  
- [x] Improvements made  
- [x] Documentation completed  
- [x] Final build ready  
## 14.2 Weekly Update Log

| Week | Planned Goal | What Actually Happened | What Changed | Next Steps |
|---|---|---|---|---|

| Week 1 | `[Finalize idea and test laser maze]` | `[Ideated laser maze and tested with smoke (humidifier, incense)]` | `[Laser visibility and reliability issues]` | `[Shift to new concept]` |
| Week 2 | `[Develop working prototype]` | `[Changed to pirate escape maze, built first and final obstacles]` | `[Concept shifted from laser maze to escape game]` | `[Develop second obstacle]` |
| Week 3 | `[Complete all obstacles and integrate]` | `[Tested multiple ideas for second obstacle (load sensor, wheel, shock sensor), finalized laser + LDR]` | `[Simplified design for stability and reliability]` | `[Integrate and test full system]` |
| Week 4 | `[Refine and finalize project]` | `[Fixed issues, improved visuals, completed documentation]` | `[Minor refinements and debugging]` | `[Prepare for exhibition]` |

---

# 15. Risks and Unknowns

## 15.1 Risk Register

| Risk | Type | Likelihood | Impact | Mitigation Plan | Owner |
|------|------|------------|--------|------------------|--------|
| `[Servo malfunction or inconsistency]` | `[Technical]` | `[Medium]` | `[High]` | `[Test repeatedly and adjust angles]` | `[Munna Madhurima]` |
| `[Power supply instability]` | `[Technical]` | `[Medium]` | `[High]` | `[Use buck converter and stable connections]` | `[Munna Madhurima]` |
| `[Sensor detection errors (LDR/RFID)]` | `[Technical]` | `[Medium]` | `[Medium]` | `[Calibrate values and test conditions]` | `[Munna Madhurima]` |
| `[Mechanical parts not aligning properly]` | `[Mechanical]` | `[Medium]` | `[Medium]` | `[Adjust structure and reinforce components]` | `[Munna Madhurima]` |
| `[User confusion in gameplay]` | `[Gameplay]` | `[Low]` | `[Medium]` | `[Improve instructions and visual clarity]` | `[Both]` |

## 15.2 Biggest Unknown Right Now
What is the single biggest uncertainty in your project at this stage?

**Response:**  
`[The biggest uncertainty during the project was ensuring that all sensors and mechanical components worked reliably together in a real-time interactive setup. Issues like inconsistent laser detection, power instability, and mechanical alignment required multiple iterations. However, through testing and simplification of the system, these uncertainties were gradually resolved.]`

---

# 16. Testing and Playtesting

## 16.1 Technical Testing Plan

| What Needs Testing | How You Will Test It | Success Condition |
|-------------------|---------------------|-------------------|
| `[Servo movement]` | `[Trigger each obstacle multiple times]` | `[Smooth and correct movement every time]` |
| `[Sensor behavior (LDR)]` | `[Test laser detection at different distances and lighting]` | `[Consistent detection only when laser is aimed correctly]` |
| `[RFID system]` | `[Scan correct and incorrect cards]` | `[Correct card opens box, wrong card triggers error]` |
| `[Power stability]` | `[Run system continuously for multiple trials]` | `[No resets or power drops during use]` |

## 16.2 Playtesting Plan

| Question | How You Will Check |
|----------|-------------------|
| Do players understand what to do? | `[Observe if players can complete tasks without help]` |
| Is the interaction satisfying? | `[Ask players for feedback after playing]` |
| Do players want another turn? | `[Check if players show interest in replaying]` |
| Is the challenge balanced? | `[Observe time taken and difficulty faced]` |
| Is the response clear and immediate? | `[Check if outputs match actions instantly]` |

## 16.3 Testing and Debugging Log

| Date | Problem Found | Type | What You Tried | Result | Next Action |
|------|--------------|------|----------------|--------|-------------|
| `[Week 1]` | `[Laser maze visibility not working]` | `[Technical]` | `[Used humidifier and incense]` | `[Failed]` | `[Changed concept]` |
| `[Week 2]` | `[Servo inconsistency]` | `[Technical]` | `[Adjusted angles and power supply]` | `[Partly]` | `[Stabilized with better power]` |
| `[Week 3]` | `[Second obstacle unreliable]` | `[Technical]` | `[Tried load sensor, wheel, shock sensor]` | `[Failed]` | `[Switched to LDR + laser]` |
| `[Week 3]` | `[RFID detection delay]` | `[Technical]` | `[Adjusted code timing]` | `[Worked]` | `[Finalized system]` |

## 16.4 Playtesting Notes

| Tester | What They Did | What Confused Them | What They Enjoyed | What You Will Change |
|--------|--------------|--------------------|--------------------|----------------------|
| `[Classmate]` | `[Completed all obstacles]` | `[Second obstacle instructions unclear]` | `[Final treasure box opening]` | `[Improve instructions]` |
| `[Friend]` | `[Tried solving puzzles]` | `[Laser aiming accuracy]` | `[Interactive elements and theme]` | `[Adjust sensor sensitivity]` |

---

# 17. Build Documentation

## 17.1 Fabrication Process
Describe how the project was physically made.

Include:
- cutting,
- 3D printing,
- assembly,
- fastening,
- wiring,
- finishing,
- revisions.

**Response:**  
`[The project was built using foam board as the main structural material. Cutting was done manually using blades to create panels for each obstacle and the overall maze setup. The foam board allowed quick adjustments and easy shaping during the build process.There was no 3D printing involved, as all components were fabricated using simple materials. Assembly was done by joining foam board pieces using adhesive and tape to create stable structures for each obstacle.Servo motors were mounted inside the structures and connected to moving parts such as sliding card mechanisms and the treasure box lid. Additional lightweight materials were used to balance and support the servo movement where required.Wiring was done using jumper wires on breadboards, connecting components like ESP32, LDR sensors, RFID module, buzzer, and servos. Power was managed using breadboard power supplies and a buck converter for stable voltage.Finishing included attaching printed visuals and posters to the foam board to match the pirate theme, improving the overall look and user experience.Revisions were made throughout the process, especially when the initial laser maze idea failed. The design was adapted into an escape maze, and multiple iterations were done for the second obstacle before finalizing the laser and LDR-based solution.]`

## 17.2 Build Photos
Add photos throughout the project.

Suggested images:
- early sketch,
- prototype,
- electronics testing,
- mechanism test,
- app screenshot,
- final build.
[<img width="960" height="1280" alt="image" src="https://github.com/user-attachments/assets/74c34ff9-f437-4c31-9294-e9f04846cd34" />
<img width="1280" height="960" alt="image" src="https://github.com/user-attachments/assets/15224191-fa09-49f2-97b2-85b154395cf6" />
<img width="1600" height="1200" alt="image" src="https://github.com/user-attachments/assets/83851db9-8bf5-4c5f-9c6d-12baeedd36b9" />
<img width="1280" height="960" alt="image" src="https://github.com/user-attachments/assets/57d43414-6f2d-4b3a-a861-86807b521686" />
<img width="1280" height="960" alt="image" src="https://github.com/user-attachments/assets/96878f28-6f26-432b-960f-a59d09c14855" />
<img width="1280" height="720" alt="image" src="https://github.com/user-attachments/assets/4d7b53d9-e2aa-4816-b529-95ec752b558d" />
<img width="1280" height="960" alt="image" src="https://github.com/user-attachments/assets/28f46078-568b-4087-8bf9-d8a7c1374a09" />
<img width="1280" height="960" alt="image" src="https://github.com/user-attachments/assets/15ba53cd-86cd-4c83-8436-418cdad453fd" />
<img width="960" height="1280" alt="image" src="https://github.com/user-attachments/assets/ae7cf06b-5863-4aaa-bfd1-cd887d22ef0b" />
<img width="960" height="1280" alt="image" src="https://github.com/user-attachments/assets/e9e15681-d8ba-4b19-ae13-5eebb042ce70" />
<img width="1200" height="1600" alt="image" src="https://github.com/user-attachments/assets/e1ee25bb-abe1-4414-a779-79de6f2256f8" />
<img width="1599" height="899" alt="image" src="https://github.com/user-attachments/assets/c4fa7b39-2916-470c-a13e-73f137415b70" />




Example:
```md



```

## 17.3 Version History

| Version | Date | What Changed | Why |
|---|---|---|---|
| `v1` | `[Week 1]` | `[Initial ideation of a laser maze using smoke effects like humidifier and incense to visualize laser paths]` | `[The concept aimed to create an immersive experience, but visibility and reliability issues made it difficult to use]` |
| `v2` | `[Week 2]` | `[Shifted to a pirate-themed escape maze; developed first obstacle with buttons and servo, and final treasure box with RFID]` | `[The laser maze was unstable, so the idea was changed to a more controlled and interactive system]` |
| `v3` | `[Week 3]` | `[Multiple iterations for second obstacle including load sensor, rotating wheel, and shock sensor; finalized using laser and LDR]` | `[Earlier ideas had connection issues and were unreliable; laser and LDR provided a simpler and more stable solution]` |

---

# 18. Final Outcome

## 18.1 Final Description
Describe the final version of your project.

**Response:**  
`[The final project is an interactive pirate-themed escape maze where players solve a sequence of challenges to unlock a treasure. The experience begins with a map-based clue where players decode coordinates to find a passcode and input it using push buttons, triggering a servo motor to release the first card.The second obstacle involves solving a logic-based puzzle and using a laser to aim at the correct target. An LDR sensor detects the laser, and upon correct input, another servo mechanism releases the next card. Players collect clue cards as they progress through the maze.    In the final stage, players use RFID cards to interact with a treasure box. The correct card triggers the servo motor to open the box and plays a pirate-themed audio track, while incorrect cards produce an error sound. The project combines electronics, mechanical movement, and physical interaction to create an engaging and immersive gameplay experience.]`

## 18.2 What Works Well
- `[The overall flow of the maze is clear and keeps the player engaged through each stage]`
- `[Different interaction types such as buttons, laser, and RFID make the experience varied and interesting]`
- `[The sensor responses and servo actions provide clear feedback to the player]`
- `[The final treasure box interaction creates a satisfying and rewarding ending]`
- `[The pirate theme and visuals make the experience immersiveg]`
  
## 18.3 What Still Needs Improvement
- `[Card sliding mechanisms can be made smoother and more reliable]`
- `[Wiring and power setup need better organization and stability]`
- `[Sensor accuracy, especially laser detection, can be improved]`
- `[Instructions and clues can be made clearer for better user understanding]`
- `[Overall finishing and durability of the setup can be improved]`

## 18.4 What Changed From the Original Plan
How did the project change from the initial idea?

**Response:**  
`[Initially, the project was planned as a laser-based maze system. However, during development, we faced multiple challenges such as unreliable sensor detection, alignment issues, and hardware limitations that made the system difficult to maintain consistently. Due to these constraints, the concept was adapted into a multi-stage interactive escape maze that still included a laser-based element but combined it with other interaction methods like button input and RFID.This change allowed us to create a more stable and engaging experience while still keeping the core idea of interaction and problem-solving. The shift also helped in better managing the available components and improving the overall reliability of the system.]`

---

# 19. Reflection

## 19.1 Team Reflection
What did your team do well?      
What slowed you down?  
How well did you manage time, tasks, and responsibilities?

**Response:**  
`[As a team, we worked well by dividing responsibilities based on our strengths, with one member focusing more on electronics and coding, and the other on visuals and physical design. This helped us progress efficiently and maintain balance between functionality and aesthetics.One challenge we faced was managing hardware issues and time constraints, especially when components did not behave as expected. Debugging and fixing these problems sometimes slowed down progress.Overall, we managed time and tasks reasonably well by adapting to problems and making necessary changes to the plan. Collaboration and continuous adjustments helped us complete the project successfully.]`

## 19.2 Technical Reflection
What did you learn about:
- electronics,
- coding,
- mechanisms,
- fabrication,
- integration?

**Response:**  
`[Through this project, we learned how to integrate multiple electronic components such as sensors, servo motors, and RFID modules into a single system. We improved our understanding of MicroPython coding, especially in handling inputs, conditions, and controlling outputs. We also explored how mechanical movement works along with electronics, such as using servo motors for controlled actions like sliding and opening mechanisms. In terms of fabrication, we gained experience in building structures using foam board and assembling components practically. A key learning was system integration, where multiple obstacles and circuits had to function together smoothly. Debugging issues, especially related to power supply and servo performance, helped us understand real-world challenges in building interactive systems.]`

## 19.3 Design Reflection
What did you learn about:
- designing for play,
- delight,
- clarity,
- physical interaction,
- player understanding,
- iteration?

**Response:**  
`[We learned how to design for play by focusing on creating an engaging and interactive experience rather than just a functional system. The pirate theme helped make the experience immersive and enjoyable. We understood the importance of clarity in instructions so that players can easily understand what to do at each stage without confusion. Physical interaction, such as pressing buttons, aiming a laser, and using cards, made the experience more engaging. We also learned to think from the player’s perspective and design the flow accordingly. Iteration played an important role, as we continuously improved placement, interactions, and overall experience based on testing.]`

## 19.4 If You Had One More Week
What would you improve next?

**Response:**  
`[If we had one more week, we would improve the stability and finish of the system, especially the mechanical parts and wiring. We would refine the obstacle interactions to make them more reliable and smoother. We would also enhance the visual experience by adding more props, better detailing, and stronger thematic elements to make the environment more immersive. Lighting effects and clearer instructions would further improve usability. Additionally, we would test the system with more users and make improvements based on their feedback to make the experience more intuitive and engaging.]`

---

# 20. Final Submission Checklist

Before submission, confirm that:
- [x] Team details are complete  
- [x] Project description is complete  
- [x] Inspiration sources are included  
- [x] Player journey is written  
- [x] Sketches are added  
- [x] BOM is complete  
- [x] Purchase list is complete  
- [x] Budget summary is complete  
- [x] Mechanical planning is documented if applicable  
- [x] App planning is documented if applicable  
- [x] Code flowchart is added  
- [x] Task breakdown is complete  
- [x] Weekly logs are updated  
- [x] Risk register is complete  
- [x] Testing log is updated  
- [x] Playtesting notes are included  
- [x] Build photos are included  
- [x] Final reflection is written  

---

# 21. Suggested Repository Structure

```text
project-repo/
├── README.md
├── images/
│   ├── concept-sketch.jpg
│   ├── labeled-sketch.jpg
│   ├── circuit-diagram.jpg
│   ├── ui-mockup.jpg
│   ├── prototype-1.jpg
│   └── final-build.jpg
├── code/
│   ├── main.py
│   ├── test_code.py
│   └── notes.md
├── cad/
│   ├── models/
│   └── screenshots/
└── docs/
    ├── references.md
    └── extra-notes.md
```

---

# 22. Instructor Review

## 22.1 Proposal Approval
- [ ] Approved to proceed
- [ ] Approved with changes
- [ ] Rework required before proceeding

**Instructor comments:**  
`[Instructor fills this section]`

## 22.2 Midpoint Review
`[Instructor fills this section]`

## 22.3 Final Review Notes
`[Instructor fills this section]`
