# Project: OpenSpiel LLM Arena

## 0. Project Goal
The goal of this project is to evaluate the decision-making capabilities of Large Language Models (LLMs) by engaging them in simple games implemented using Google's OpenSpiel framework. The LLMs can play against:
1. A random bot.
2. Another LLM.
3. Themselves (self-play).

This project explores how LLMs interpret game states, make strategic decisions, and adapt their behavior through natural language prompts.

---

## 1. How to Run

### Prerequisites
1. **Python Environment**:
   - Python 3.7 or higher.
   - Install the required dependencies:
     ```bash
     pip install -r requirements.txt
     ```

2. **Install OpenSpiel Framework**:
   - Clone and set up OpenSpiel from its official repository:
     ```bash
     git clone https://github.com/deepmind/open_spiel.git
     cd open_spiel
     ./install.sh
     ```

3. **Project Setup**:
   - Clone this repository:
     ```bash
     git clone <repository-url>
     cd <repository-folder>
     ```

---

### Running the Simulator
1. Use the main binary:
   ```bash
   python scripts/run_simulation.py --game tic_tac_toe
   ```

2. Command-line options:
   - `--game`: Specify the game to simulate. Available options:
     - `tic_tac_toe`
     - `prisoners_dilemma`
     - `rps`
   - Example usage:
     ```bash
     python scripts/run_simulation.py --game tic_tac_toe
     ```

---

## 2. Directory Structure

### Packages
- **`open_spiel_simulation/`**: Root package containing all simulation logic.
  - **`games/`**: Game-specific logic (e.g., rules for Tic-Tac-Toe).
  - **`simulators/`**: Simulator logic for each game.
  - **`utils/`**: Shared utility functions (e.g., prompt generation, LLM integration).

### Binary
- **`scripts/run_simulation.py`**: The main script to run simulations. This is the entry point for the project.

### Tests
- **`tests/`**: Unit tests for utilities and simulators.

---

## 3. Games Available

### List of Supported Games
1. **Tic-Tac-Toe**:
   - A classic 3x3 grid game where players aim to align three symbols horizontally, vertically, or diagonally.

2. **Python Iterated Prisoner’s Dilemma**:
   - A repeated strategy game where players choose between cooperation and defection to maximize rewards over multiple rounds.

3. **Rock-Paper-Scissors**:
   - A simultaneous-move game where rock beats scissors, scissors beats paper, and paper beats rock.

4. **Matching Pennies** (Planned):
   - A simple two-player game where Player 1 wins if both players’ choices match, and Player 2 wins if they differ.

---

## 4. Features
- **LLM Integration**:
  - Uses Hugging Face Transformers to incorporate open-source LLMs (e.g., GPT-2, FLAN-T5).
  - Converts game states into natural language prompts for LLM decision-making.

- **Flexible Opponent Options**:
  - LLMs can play against random bots, other LLMs, or themselves.

- **Extensible Framework**:
  - Supports adding new OpenSpiel games by defining custom simulators and integrating them into the pipeline.

---

## 5. Contribution Guidelines

### Steps to Contribute:
1. Fork this repository.
2. Create a feature branch.
3. Follow the directory structure and coding style outlined in this README.
4. Add appropriate unit tests for your contribution.
5. Submit a pull request with a detailed explanation of your changes.

---

## 6. Example Output

### Game: Tic-Tac-Toe
```
Current state of Tic-Tac-Toe:
x.o
...
...
LLM chooses action: 4
...
Final state of Tic-Tac-Toe:
x.o
..x
.o.
Scores: {'LLM_1': 1.0, 'Random_Bot': -1.0}
```

