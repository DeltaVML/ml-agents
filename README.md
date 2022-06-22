# Unity ML-Agents Toolkit with Hugging Face 🤗

This is a Fork of the Unity ML-Agents toolkit. This version allows you to **publish your trained agents in one line of code to the Hugging Face Hub**, **download powerful agents** from the community, and **watch a replay of your agent without using the Unity Editor**.

⚠️ This is an experimental version, that might be subject to change. If you **encounter some issues, please open an issue**. Don't forget to check [what environments are currently available](https://github.com/huggingface/ml-agents#the-environments).

## Getting started

➡️ We wrote a complete tutorial to learn to **train your first agent using ML-Agents and publish it to the Hub**: 

### Step 1: Install the package
```
# Clone the repository
git clone https://github.com/huggingface/ml-agents/

# Go inside the repository and install the package
cd ml-agents
pip3 install -e ./ml-agents-envs
pip3 install -e ./ml-agents
```

### Step 2:




## The Environments

| ML-Agent Environment |                                                                                                                | Windows Executable                                       | Mac Executable | Linux Executable | Visualize your agent online with Hugging Face Spaces |
|----------------------|----------------------------------------------------------------------------------------------------------------|----------------------------------------------------------|----------------|------------------|------------------------------------------------------|
| [Pyramids](https://github.com/Unity-Technologies/ml-agents/blob/main/docs/Learning-Environment-Examples.md#pyramids)             | <img src="https://github.com/Unity-Technologies/ml-agents/raw/main/docs/images/pyramids.png" alt="Pyramids" /> | ✔️                                                        | 🏗️              | 🏗️                | ✔️ https://huggingface.co/spaces/unity/ML-Agents-Pyramids                                                       |
| [Walker](https://github.com/Unity-Technologies/ml-agents/blob/main/docs/Learning-Environment-Examples.md#walker)               | <img src="https://github.com/Unity-Technologies/ml-agents/raw/main/docs/images/walker.png" alt="Walker"/>      | ✔️                                                        | 🏗️              | 🏗️                | ✔️ https://huggingface.co/spaces/unity/ML-Agents-Walker                                                   |
| [Worm](https://github.com/Unity-Technologies/ml-agents/blob/main/docs/Learning-Environment-Examples.md#worm)                 | <img src="https://github.com/Unity-Technologies/ml-agents/raw/main/docs/images/worm.png" alt="Worm" />         | ✔️                                                        | 🏗️              | 🏗️                | ✔️ https://huggingface.co/spaces/unity/ML-Agents-Worm                                                    |
| [Push Block](https://github.com/Unity-Technologies/ml-agents/blob/main/docs/Learning-Environment-Examples.md#push-block)              | <img src="https://github.com/Unity-Technologies/ml-agents/raw/main/docs/images/push.png" alt="Push Block" />   |✔️                                                       | 🏗️              | 🏗️                | ✔️ https://huggingface.co/spaces/unity/ML-Agents-Push-Block                                                         |
| [Basic](https://github.com/Unity-Technologies/ml-agents/blob/main/docs/Learning-Environment-Examples.md#basic)              | <img src="https://github.com/Unity-Technologies/ml-agents/raw/main/docs/images/basic.png" alt="Basic" />   | 🏗️                                                        | 🏗️              | 🏗️                | 🏗️                                                    |
| [Crawler](https://github.com/Unity-Technologies/ml-agents/blob/main/docs/Learning-Environment-Examples.md#crawler)              | <img src="https://github.com/Unity-Technologies/ml-agents/raw/main/docs/images/crawler.png" alt="Crawler" />   | 🏗️                                                        | 🏗️              | 🏗️                | 🏗️                                                    |
| [Wall Jump](https://github.com/Unity-Technologies/ml-agents/blob/main/docs/Learning-Environment-Examples.md#wall-jump)             | <img src="https://github.com/Unity-Technologies/ml-agents/raw/main/docs/images/wall.png" alt="WallJump" />     | 🏗️                                                        | 🏗️              | 🏗️                | 🏗️                                                    |
| [PushBlock](https://github.com/Unity-Technologies/ml-agents/blob/main/docs/Learning-Environment-Examples.md#push-block)            | <img src="https://github.com/Unity-Technologies/ml-agents/raw/main/docs/images/push.png" alt="PushBlock" />    | 🏗️                                                        | 🏗️              | 🏗️                |      🏗️                                                |
|                      | 
| [3DBall: 3D Balance Ball](https://github.com/Unity-Technologies/ml-agents/blob/main/docs/Learning-Environment-Examples.md#3dball-3d-balance-ball)             | <img src="https://github.com/Unity-Technologies/ml-agents/raw/main/docs/images/balance.png" alt="Balance" />     | 🏗️                                                        | 🏗️              | 🏗️                | 🏗️                                                    |
| [GridWorld](https://github.com/Unity-Technologies/ml-agents/blob/main/docs/Learning-Environment-Examples.md#gridworld)             | <img src="https://github.com/Unity-Technologies/ml-agents/raw/main/docs/images/gridworld.png" alt="Grid World" />     | 🏗️                                                        | 🏗️              | 🏗️                | 🏗️                                                    |
| [Wall Jump](https://github.com/Unity-Technologies/ml-agents/blob/main/docs/Learning-Environment-Examples.md#wall-jump)             | <img src="https://github.com/Unity-Technologies/ml-agents/raw/main/docs/images/wall.png" alt="Wall Jump" />     | 🏗️                                                        | 🏗️              | 🏗️                | 🏗️                                                    |
| [Food Collector](https://github.com/Unity-Technologies/ml-agents/blob/main/docs/Learning-Environment-Examples.md#food-collector)             | <img src="https://github.com/Unity-Technologies/ml-agents/raw/main/docs/images/foodCollector.png" alt="Food Collector" />     | 🏗️                                                        | 🏗️              | 🏗️                | 🏗️                                                    |
| [Hallway](https://github.com/Unity-Technologies/ml-agents/blob/main/docs/Learning-Environment-Examples.md#hallway)             | <img src="https://github.com/Unity-Technologies/ml-agents/raw/main/docs/images/hallway.png" alt="Hallway" />     | 🏗️                                                        | 🏗️              | 🏗️                | 🏗️                                                    |
| [Soccer Twos](https://github.com/Unity-Technologies/ml-agents/blob/main/docs/Learning-Environment-Examples.md#soccer-twos)             | <img src="https://github.com/Unity-Technologies/ml-agents/raw/main/docs/images/soccer.png" alt="Soccer" />     | 🏗️                                                        | 🏗️              | 🏗️                | 🏗️                                                    |
| [Strikers Vs. Goalie](https://github.com/Unity-Technologies/ml-agents/blob/main/docs/Learning-Environment-Examples.md#strikers-vs-goalie)             | <img src="https://github.com/Unity-Technologies/ml-agents/raw/main/docs/images/strikersvsgoalie.png" alt="Strikers Vs. Goalie" />     | 🏗️                                                        | 🏗️              | 🏗️                | 🏗️                                                    |
| [Match 3](https://github.com/Unity-Technologies/ml-agents/blob/main/docs/Learning-Environment-Examples.md#match-3)             | <img src="https://github.com/Unity-Technologies/ml-agents/raw/main/docs/images/match3.png" alt="Match 3" />     | 🏗️                                                        | 🏗️              | 🏗️                | 🏗️                                                    |
| [Sorter](https://github.com/Unity-Technologies/ml-agents/blob/main/docs/Learning-Environment-Examples.md#sorter)             | <img src="https://github.com/Unity-Technologies/ml-agents/blob/main/docs/Learning-Environment-Examples.md#sorter" alt="Sorter" />     | 🏗️                                                        | 🏗️              | 🏗️                | 🏗️                                                    |
| [Cooperative Push Block](https://github.com/Unity-Technologies/ml-agents/blob/main/docs/Learning-Environment-Examples.md#cooperative-push-block)             | <img src="https://github.com/Unity-Technologies/ml-agents/raw/main/docs/images/cooperative_pushblock.png" alt="Cooperative Push Block" />     | 🏗️                                                        | 🏗️              | 🏗️                | 🏗️                                                    |
| [Dungeon Escape](https://github.com/Unity-Technologies/ml-agents/blob/main/docs/Learning-Environment-Examples.md#dungeon-escape)             | <img src="https://github.com/Unity-Technologies/ml-agents/raw/main/docs/images/dungeon_escape.png" alt="Dungeon Escape" />     | 🏗️                                                        | 🏗️              | 🏗️                | 🏗️                                                    |
