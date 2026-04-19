"""Public disclosure markers for inter-LLM comparison reports."""
from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable


@dataclass(frozen=True)
class ModelDisclosure:
    model_id: str
    public_name: str
    marker: str
    attempted_stories: int
    completed_stories: int
    refused_stories: int
    comparison_pair_story_rows: int
    comparison_unique_story_indices: int
    note: str

    @property
    def refusal_rate(self) -> float:
        assert self.attempted_stories > 0
        return float(self.refused_stories / self.attempted_stories)

    def markdown_note(self) -> str:
        return (
            f"{self.marker} `{self.model_id}`: {self.note} "
            f"Generation sidecars show {self.refused_stories}/{self.attempted_stories} "
            f"story prompts refused ({self.refusal_rate:.1%}); "
            f"{self.completed_stories} story outputs were available. "
            "Comparison prompts and ratings use completed stories only "
            f"({self.comparison_pair_story_rows} pair-story rows, "
            f"{self.comparison_unique_story_indices} distinct story indices in the current comparison scope). "
            "No score was imputed for the refused prompts, so this is a coverage caveat rather than a direct rating penalty."
        )

    def chart_note(self) -> str:
        return (
            f"{self.marker} {self.public_name}: refused "
            f"{self.refused_stories}/{self.attempted_stories} story prompts; "
            f"rating uses {self.completed_stories} completed stories."
        )


OPUS_47_REFUSAL_DISCLOSURE = ModelDisclosure(
    model_id="claude-opus-4-7-adaptive",
    public_name="Claude Opus 4.7",
    marker="†",
    attempted_stories=400,
    completed_stories=347,
    refused_stories=53,
    comparison_pair_story_rows=480,
    comparison_unique_story_indices=265,
    note="Claude Opus 4.7 refused a subset of creative-writing generation prompts in this run.",
)

MODEL_DISCLOSURES: dict[str, ModelDisclosure] = {
    OPUS_47_REFUSAL_DISCLOSURE.model_id: OPUS_47_REFUSAL_DISCLOSURE,
}


def disclosure_for_model(model_id: str) -> ModelDisclosure | None:
    return MODEL_DISCLOSURES.get(str(model_id))


def label_with_disclosure_marker(model_id: str, label: str) -> str:
    disclosure = disclosure_for_model(model_id)
    if disclosure is None:
        return str(label)
    return f"{label}{disclosure.marker}"


def markdown_model_label(model_id: str) -> str:
    return label_with_disclosure_marker(model_id, str(model_id))


def disclosure_markdown_notes(model_ids: Iterable[str]) -> list[str]:
    present = {
        str(model_id)
        for model_id in model_ids
        if disclosure_for_model(str(model_id)) is not None
    }
    return [
        disclosure.markdown_note()
        for model_id, disclosure in MODEL_DISCLOSURES.items()
        if model_id in present
    ]


def disclosure_chart_note(model_ids: Iterable[str]) -> str:
    present = {
        str(model_id)
        for model_id in model_ids
        if disclosure_for_model(str(model_id)) is not None
    }
    notes = [
        disclosure.chart_note()
        for model_id, disclosure in MODEL_DISCLOSURES.items()
        if model_id in present
    ]
    return "\n".join(notes)
