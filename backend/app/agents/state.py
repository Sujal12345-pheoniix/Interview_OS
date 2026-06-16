from __future__ import annotations

from typing import Any, Annotated, Optional
from dataclasses import dataclass, field
from typing import TypedDict


class AgentMessage(TypedDict):
    """Message passed between agents"""
    agent: str
    status: str  # "started" | "completed" | "failed"
    output: Optional[Any]
    error: Optional[str]
    duration_seconds: Optional[float]


@dataclass
class ResumeAnalysis:
    """Output from Resume Analyzer Agent"""
    skills: list[str] = field(default_factory=list)
    technical_skills: list[str] = field(default_factory=list)
    soft_skills: list[str] = field(default_factory=list)
    projects: list[dict] = field(default_factory=list)
    experience: list[dict] = field(default_factory=list)
    education: list[dict] = field(default_factory=list)
    certifications: list[str] = field(default_factory=list)
    gaps: list[str] = field(default_factory=list)
    strengths: list[str] = field(default_factory=list)
    years_experience: int = 0
    seniority_level: str = "mid"
    embedding_id: Optional[str] = None


@dataclass
class JDAnalysis:
    """Output from JD Analyzer Agent"""
    required_skills: list[str] = field(default_factory=list)
    preferred_skills: list[str] = field(default_factory=list)
    responsibilities: list[str] = field(default_factory=list)
    requirements: list[str] = field(default_factory=list)
    culture_signals: list[str] = field(default_factory=list)
    seniority_level: str = "mid"
    tech_stack: list[str] = field(default_factory=list)
    match_score: float = 0.0
    missing_skills: list[str] = field(default_factory=list)
    embedding_id: Optional[str] = None


@dataclass
class GeneratedQuestion:
    """A single generated interview question"""
    question_text: str
    question_type: str
    difficulty: str
    expected_answer: str
    evaluation_rubric: dict
    tags: list[str] = field(default_factory=list)
    follow_up_hints: list[str] = field(default_factory=list)


@dataclass
class QuestionResponse:
    """Candidate's response to a question"""
    question_id: str
    question_text: str
    response_text: str
    duration_seconds: float = 0.0
    word_count: int = 0
    filler_word_count: int = 0


@dataclass
class QuestionScore:
    """Evaluation score for a single response"""
    question_id: str
    overall_score: float
    communication_score: float
    technical_score: float
    behavioral_score: float
    reasoning: str
    better_answer: str
    rubric_breakdown: dict = field(default_factory=dict)


@dataclass
class EvaluationScores:
    """Complete evaluation scores for an interview"""
    overall_score: float = 0.0
    communication_score: float = 0.0
    technical_score: float = 0.0
    problem_solving_score: float = 0.0
    confidence_score: float = 0.0
    leadership_score: float = 0.0
    hiring_recommendation: str = "no_hire"  # strong_hire, hire, no_hire
    strengths: list[str] = field(default_factory=list)
    weaknesses: list[str] = field(default_factory=list)
    missed_opportunities: list[str] = field(default_factory=list)
    better_answers: list[dict] = field(default_factory=list)


@dataclass
class LearningPlanData:
    """90-day learning plan from Learning Coach"""
    target_role: str = ""
    current_level: str = ""
    target_level: str = ""
    priority_skills: list[str] = field(default_factory=list)
    weeks: list[dict] = field(default_factory=list)  # 12 weeks
    resources: list[dict] = field(default_factory=list)
    milestones: list[dict] = field(default_factory=list)
    daily_practice_minutes: int = 60
    estimated_readiness_date: str = ""


class InterviewState(TypedDict, total=False):
    """
    Central state object passed through the LangGraph workflow.
    All agents read from and write to this state.
    """
    # Input data
    interview_id: str
    user_id: str
    interview_type: str
    interview_subtype: str
    difficulty: str
    duration_minutes: int
    target_role: Optional[str]
    target_company: Optional[str]

    # Resume & JD data
    resume_text: Optional[str]
    resume_id: Optional[str]
    jd_text: Optional[str]
    jd_id: Optional[str]
    resume_analysis: Optional[ResumeAnalysis]
    jd_analysis: Optional[JDAnalysis]

    # Questions
    questions: list[GeneratedQuestion]
    current_question_index: int

    # Responses
    responses: list[QuestionResponse]
    question_scores: list[QuestionScore]

    # Final evaluation
    evaluation_scores: Optional[EvaluationScores]
    learning_plan: Optional[LearningPlanData]

    # Execution metadata
    agent_messages: list[AgentMessage]
    errors: list[str]
    started_at: str
    completed_at: Optional[str]
