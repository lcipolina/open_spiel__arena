# scripts/run_simulation.py
"""Main entry point for running game simulations.

This script serves as the main binary for executing simulations of various games
using OpenSpiel and Large Language Models (LLMs). It supports command-line
arguments to specify the game and simulation configurations.
"""

import argparse
from transformers import pipeline
from simulators.tic_tac_toe_simulator import TicTacToeSimulator
from simulators.prisoners_dilemma_simulator import PrisonersDilemmaSimulator
from simulators.rock_paper_scissors_simulator import RockPaperScissorsSimulator
from utils.llm_utils import generate_prompt, llm_decide_move
from games.tic_tac_toe import get_tic_tac_toe_game
from games.prisoners_dilemma import get_prisoners_dilemma_game
from games.rock_paper_scissors import get_rps_game

import os
os.environ["TRANSFORMERS_BACKEND"] = "pt"  # Force PyTorch as the backend


def main() -> None:
    """Main function for running game simulations."""
    parser = argparse.ArgumentParser(description="Run OpenSpiel simulations.")
    parser.add_argument(
        "--game",
        type=str,
        choices=["tic_tac_toe", "prisoners_dilemma", "rps"],
        required=True,
        help="The name of the game to simulate."
    )
    args = parser.parse_args()

    # Load LLMs
    llms = {
        "google/flan-t5-small": pipeline("text-generation", model="google/flan-t5-small"),
        "gpt2": pipeline("text-generation", model="gpt2"),
    }

    # Select the game and simulator
    if args.game == "tic_tac_toe":
        game = get_tic_tac_toe_game()
        simulator = TicTacToeSimulator(game, "Tic-Tac-Toe", llms, random_bot=True)
    elif args.game == "prisoners_dilemma":
        game = get_prisoners_dilemma_game()
        simulator = PrisonersDilemmaSimulator(
            game, "Iterated Prisoner's Dilemma", llms, play_against_itself=True, max_iterations=10
        )
    elif args.game == "rps":
        game = get_rps_game()
        simulator = RockPaperScissorsSimulator(game, "Rock-Paper-Scissors", llms)
    else:
        raise ValueError(f"Unsupported game: {args.game}")

    # Run the simulation
    print(f"Starting simulation for {args.game}...")
    results = simulator.simulate()
    print("Simulation completed.")
    print("Results:")
    for llm, score in results.items():
        print(f"{llm}: {score}")

if __name__ == "__main__":
    main()
