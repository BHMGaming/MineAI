# MineAI
An API To Read And Interact With The Game Minecraft.
Go to Github Page
 
1. Open "MineAI" (And Minecraft).
2. Copy and paste these two commmands there:
python -i start.py &
main()
3. Scroll down for more info.

MineAI

This is an API to read, write and react to the game Minecraft.

Bar's Site
A (now obsolete) API for RL agents in Minecraft
BHMGaming on Youtube

README.md
Minecraft AI
Using reinforcement learning to design an intelligent AI for Minecraft. The model uses image analysis to "see" it's world and optimizes play in a closed system

Installation
You must be running Windows to run this AI (We require keybindings,screen capturing, and mouse control through the win32api)

Create a conda environment using

conda create --name ENV_NAME python=3.4
Install from the list of requirements.

pip install -r requirements.txt
How to Run
To run the AI, do the following. We assume that you have already started your conda environment using

source activate ENV_NAME
First, we must configure Minecraft to the correct settings. As of the moment, you must set the following options:
Resolution: 1366x768
Block Distance: less than 10
No Light Shading
Windowed Mode
Start Minecraft

Run the following command

python -i start.py

main()

A prompt will appear to switch to your minecraft window: do so, and watch the AI run

TODO
Allow computer to control game inputs
Get display
Machine learning algorithm for detecting block

(C) BHMGaming Current Year
Bar is awesome!
