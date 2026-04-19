#!/usr/bin/env python3
"""
Question weighting system for Creative Writing Benchmark.

This module applies category-based weights to balance major story aspects (Q1–Q8)
vs element integration (Q9A–Q9J) using a 60/40 category ratio. With 8 questions
in the first block and 10 in the second, per‑question weights are set so that the
total weight across Q1–Q8 : Q9A–J is 60 : 40. One convenient choice is:
  • Q1–Q8 per‑question = 1.875 (8×1.875 = 15)
  • 9A–9J per‑question = 1.0   (10×1.0 = 10)
giving a 15:10 = 60:40 category total. After normalizing over 18 questions, the
per‑question weights become ≈1.35 (Q1–Q8) and ≈0.72 (9A–9J).
"""

import math

# Category weights - these determine the relative importance
CATEGORY_WEIGHTS = {
    # 60/40 category ratio across Q1–Q8 (8 items) vs Q9A–J (10 items).
    # Per-question weights: 1.875 for major aspects, 1.0 for element integration
    # (ratio 1.875×). This yields a 60:40 category total before normalization and
    # preserves that share after normalization (~1.35 vs ~0.72 per question).
    "major_aspects": 1.875,     # Q1–Q8 per‑question weight (category total 15 ⇒ 60%)
    "element_integration": 1.0   # 9A–J per‑question weight (category total 10 ⇒ 40%)
}

# Question to category mapping
QUESTION_CATEGORIES = {
    # Major story aspects (Q1-8)
    "1": "major_aspects",   # Character Development & Motivation
    "2": "major_aspects",   # Plot Structure & Coherence
    "3": "major_aspects",   # World-Building & Atmosphere
    "4": "major_aspects",   # Story Impact & Overall Craft
    "5": "major_aspects",   # Authenticity & Originality
    "6": "major_aspects",   # Execution & Thematic Cohesion
    "7": "major_aspects",   # Voice & Point of View
    "8": "major_aspects",   # Prose Quality & Line-Level Craft

    # Element integration (Q9A-9J)
    "9A": "element_integration",  # Character Element
    "9B": "element_integration",  # Object Element
    "9C": "element_integration",  # Concept Element
    "9D": "element_integration",  # Attribute Element
    "9E": "element_integration",  # Action Element
    "9F": "element_integration",  # Method Element
    "9G": "element_integration",  # Setting Element
    "9H": "element_integration",  # Timeframe Element
    "9I": "element_integration",  # Motivation Element
    "9J": "element_integration",  # Tone Element
}


def _normalize_question_id(question: str) -> str:
    question_id = str(question).upper().strip()
    if question_id == "":
        raise ValueError("Question ID must not be empty")
    return question_id

def get_question_weight(question: str) -> float:
    """
    Get the weight for a specific question based on its category.

    Args:
        question: Question ID (e.g., "1", "9A")

    Returns:
        Weight value for the question
    """
    question = _normalize_question_id(question)
    if question not in QUESTION_CATEGORIES:
        raise KeyError(f"Unknown question ID: {question}")
    category = QUESTION_CATEGORIES[question]
    return CATEGORY_WEIGHTS[category]

def get_all_question_weights() -> dict:
    """
    Get weights for all questions.

    Returns:
        Dictionary mapping question IDs to weights
    """
    return {q: get_question_weight(q) for q in QUESTION_CATEGORIES.keys()}

def get_normalized_weights() -> dict:
    """
    Get weights normalized so the average weight is 1.0.
    This preserves the relative importance while keeping scores in the 0-10 range.

    Returns:
        Dictionary of normalized weights
    """
    weights = get_all_question_weights()
    total_weight = sum(weights.values())
    n_questions = len(weights)
    normalization_factor = n_questions / total_weight

    return {q: w * normalization_factor for q, w in weights.items()}

def calculate_weighted_score(scores_dict: dict, normalize: bool = True) -> float:
    """
    Calculate weighted average score from a dictionary of question scores.

    Args:
        scores_dict: Dictionary mapping question IDs to scores
        normalize: Whether to use normalized weights

    Returns:
        Weighted average score
    """
    if not scores_dict:
        raise ValueError("scores_dict must not be empty")
    if normalize:
        weights = get_normalized_weights()
    else:
        weights = get_all_question_weights()

    weighted_sum = 0.0
    weight_sum = 0.0

    for question, score in scores_dict.items():
        question_id = _normalize_question_id(question)
        if question_id not in weights:
            raise KeyError(f"Unknown question ID: {question_id}")
        numeric_score = float(score)
        if not math.isfinite(numeric_score):
            raise ValueError(f"Score for question {question_id} must be finite")
        weight = weights[question_id]
        weighted_sum += numeric_score * weight
        weight_sum += weight

    if weight_sum <= 0.0:
        raise ValueError("Total question weight must be positive")
    return weighted_sum / weight_sum

def get_category_statistics() -> dict:
    """
    Get statistics about the weighting system.

    Returns:
        Dictionary with category statistics
    """
    normalized = get_normalized_weights()

    # Count questions per category
    major_count = sum(1 for q, c in QUESTION_CATEGORIES.items() if c == "major_aspects")
    element_count = sum(1 for q, c in QUESTION_CATEGORIES.items() if c == "element_integration")

    # Calculate effective percentages
    major_weight_sum = CATEGORY_WEIGHTS["major_aspects"] * major_count
    element_weight_sum = CATEGORY_WEIGHTS["element_integration"] * element_count
    total_weight = major_weight_sum + element_weight_sum

    return {
        "major_aspects": {
            "count": major_count,
            "weight_per_question": CATEGORY_WEIGHTS["major_aspects"],
            "normalized_weight": normalized["1"],
            "percentage_of_total": (major_weight_sum / total_weight) * 100
        },
        "element_integration": {
            "count": element_count,
            "weight_per_question": CATEGORY_WEIGHTS["element_integration"],
            "normalized_weight": normalized["9A"],
            "percentage_of_total": (element_weight_sum / total_weight) * 100
        }
    }

if __name__ == "__main__":
    # Print weight information
    print("Question Weighting System")
    print("=" * 50)

    print("\nCategory Weights:")
    for category, weight in CATEGORY_WEIGHTS.items():
        print(f"  {category}: {weight}")

    print("\nIndividual Question Weights (Normalized):")
    normalized = get_normalized_weights()
    for question in ["1", "2", "3", "4", "5", "6", "7", "8"]:
        print(f"  Q{question}: {normalized[question]:.3f}")
    print()
    for question in ["9A", "9B", "9C", "9D", "9E", "9F", "9G", "9H", "9I", "9J"]:
        print(f"  Q{question}: {normalized[question]:.3f}")

    print("\nCategory Statistics:")
    stats = get_category_statistics()
    for category, info in stats.items():
        print(f"\n  {category}:")
        print(f"    Questions: {info['count']}")
        print(f"    Weight per question: {info['weight_per_question']}")
        print(f"    Normalized weight: {info['normalized_weight']:.3f}")
        print(f"    Percentage of total: {info['percentage_of_total']:.1f}%")
