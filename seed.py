import sys
import os
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

from utils.helpers import add_prompt
from database.db import init_db

init_db()

prompts = [

    # ── STUDY ──────────────────────────────────────────────────
    {
        "title": "Explain Like I'm Five",
        "category": "Study",
        "difficulty": "Beginner",
        "tags": "learning, simplify, concepts, beginner",
        "role": "You are a patient and creative teacher who explains complex topics using simple words, real-life examples, and fun analogies",
        "goal": "Explain any complex concept in the simplest possible way so that even a complete beginner can understand it",
        "context": "The student has no prior knowledge of the topic and needs a clear, jargon-free explanation with a real-world analogy",
        "prompt_text": "Please explain [TOPIC] to me as if I am a complete beginner with no background knowledge.\n\nUse:\n- A simple real-world analogy\n- Short, clear sentences with no jargon\n- A step-by-step breakdown\n- A one-paragraph summary at the end I can repeat to someone else\n\nTopic: [TOPIC]\nMy current knowledge level: [BEGINNER / SOME BASICS]",
        "output_fmt": "Analogy first, then step-by-step explanation, then a short summary paragraph at the end"
    },
    {
        "title": "Active Recall Quiz Generator",
        "category": "Study",
        "difficulty": "Intermediate",
        "tags": "quiz, active recall, memorization, study, test",
        "role": "You are a strict but encouraging tutor who believes active recall is the best way to learn",
        "goal": "Create an interactive quiz that tests my understanding of a topic through recall rather than recognition",
        "context": "I have just finished studying a topic and want to test myself to see how much I actually remember",
        "prompt_text": "Create an active recall quiz for me on the topic below.\n\nRules:\n- Ask ONE question at a time\n- Wait for my answer before moving on\n- After my answer: correct me if wrong, explain briefly, then ask the next question\n- Mix question types: definition, application, comparison, and why-does-this-matter\n- Give me a final score and a list of topics I should review\n\nTopic: [TOPIC]\nDifficulty: [EASY / MEDIUM / HARD]\nNumber of questions: [NUMBER]",
        "output_fmt": "One question at a time, feedback after each answer, final score and review list at the end"
    },
    {
        "title": "Cornell Notes Generator",
        "category": "Study",
        "difficulty": "Beginner",
        "tags": "notes, cornell, lecture, summarize, organize",
        "role": "You are an expert note-taker and study coach who specializes in the Cornell Notes method",
        "goal": "Convert raw lecture text or messy notes into a clean, structured Cornell Notes format",
        "context": "I have raw notes or a lecture transcript that I need to organize into a proper study format",
        "prompt_text": "Convert the following text into Cornell Notes format with three sections:\n\n1. NOTES COLUMN (right side): Main content organized with bullet points\n2. CUE COLUMN (left side): Key terms, questions, and headers\n3. SUMMARY (bottom): A 3-5 sentence summary of everything\n\nBe concise. Remove filler words. Keep all important facts, dates, names, and concepts.\n\n[PASTE YOUR RAW NOTES OR TEXT HERE]",
        "output_fmt": "Three clearly labeled sections: Notes Column, Cue Column, and Summary"
    },

    # ── CODING ─────────────────────────────────────────────────
    {
        "title": "Python Bug Fixer",
        "category": "Coding",
        "difficulty": "Intermediate",
        "tags": "python, debugging, errors, fix, code",
        "role": "You are a senior Python developer with 10 years of experience in debugging and fixing all types of Python errors",
        "goal": "Find the exact bug in my code, explain clearly why it is happening, and provide a fully corrected version",
        "context": "I am working on a Python project and my code is throwing an error that I cannot figure out on my own",
        "prompt_text": "I have a bug in my Python code and need your help fixing it.\n\nPlease:\n1. Identify the exact cause of the bug\n2. Explain why it is causing the problem in simple terms\n3. Provide the corrected version of the code\n4. Mention any other issues you notice\n\nMy code:\n```python\n[PASTE YOUR CODE HERE]\n```\n\nError message: [PASTE ERROR MESSAGE]\nWhat it should do: [DESCRIBE EXPECTED BEHAVIOR]",
        "output_fmt": "Explanation of the bug first, then the corrected code in a code block, then any additional issues noticed"
    },
    {
        "title": "Code Review Assistant",
        "category": "Coding",
        "difficulty": "Advanced",
        "tags": "code review, best practices, quality, refactor, improve",
        "role": "You are a senior software engineer conducting a thorough code review for a production application",
        "goal": "Review my code and provide detailed feedback on correctness, performance, readability, and security",
        "context": "I have written code that I want to improve before submitting it or sharing it with others",
        "prompt_text": "Please conduct a thorough code review of the following code.\n\nReview these areas:\n1. Correctness — Does it do what it is supposed to do?\n2. Performance — Any inefficiencies or unnecessary operations?\n3. Readability — Is it clean, well-named, and easy to understand?\n4. Security — Any vulnerabilities or unsafe practices?\n5. Best Practices — Does it follow conventions for [LANGUAGE]?\n6. Top 3 improvements — The highest impact changes I should make first\n\nLanguage: [LANGUAGE]\nPurpose of this code: [ONE SENTENCE]\n\n```[LANGUAGE]\n[PASTE YOUR CODE HERE]\n```",
        "output_fmt": "Numbered sections for each review area, followed by a prioritized list of the top 3 improvements"
    },
    {
        "title": "Unit Test Writer",
        "category": "Coding",
        "difficulty": "Intermediate",
        "tags": "testing, unit tests, pytest, jest, quality assurance",
        "role": "You are a software engineer who specializes in writing comprehensive, reliable unit tests",
        "goal": "Write complete unit tests for my code covering all normal cases, edge cases, and error cases",
        "context": "I have written a function or module and need proper tests before I can consider it production ready",
        "prompt_text": "Write comprehensive unit tests for the following code.\n\nMake sure to cover:\n- Happy path: normal expected inputs and outputs\n- Edge cases: empty input, zero values, boundary values, None\n- Error cases: invalid input, exceptions that should be raised\n\nAdd a short comment above each test explaining what it is testing.\n\nLanguage: [LANGUAGE]\nTesting framework: [PYTEST / JEST / JUNIT / OTHER]\n\n```[LANGUAGE]\n[PASTE YOUR FUNCTION OR MODULE HERE]\n```",
        "output_fmt": "Each test function with a comment explaining what it tests, organized by test category"
    },

    # ── RESEARCH ───────────────────────────────────────────────
    {
        "title": "Research Paper Summarizer",
        "category": "Research",
        "difficulty": "Intermediate",
        "tags": "research, paper, summary, academic, literature review",
        "role": "You are an academic research assistant with expertise in summarizing complex papers clearly and concisely",
        "goal": "Extract the most important insights from an academic paper and present them in a clear, structured format",
        "context": "I need to quickly understand what a research paper is about without reading every word",
        "prompt_text": "Summarize the following academic paper using this exact structure:\n\n1. CORE CLAIM (1 sentence): The main argument or finding\n2. THE PROBLEM IT SOLVES (2-3 sentences): What gap does this paper address?\n3. METHODOLOGY (3-4 sentences): How did the researchers approach this?\n4. KEY FINDINGS (bullet list): The 3-5 most important results\n5. LIMITATIONS (bullet list): What the paper cannot answer\n6. PRACTICAL IMPLICATIONS: How this could be applied in the real world\n7. WHO SHOULD READ THIS: Ideal audience in one sentence\n\nPaper title: [TITLE]\n\n[PASTE ABSTRACT OR FULL TEXT HERE]",
        "output_fmt": "Seven clearly labeled sections as listed in the prompt structure"
    },
    {
        "title": "Counterargument Finder",
        "category": "Research",
        "difficulty": "Advanced",
        "tags": "argument, debate, critical thinking, counterargument, thesis",
        "role": "You are a brilliant and well-informed critic who can find flaws and counterarguments in any position",
        "goal": "Find the strongest possible counterarguments against my thesis so I can strengthen my argument before presenting it",
        "context": "I am writing a paper or preparing a debate and I want to stress-test my argument before someone else does",
        "prompt_text": "I am going to share my thesis with you. Your job is to be my toughest critic.\n\nPlease:\n1. Give me the 3 strongest counterarguments against my thesis\n2. Explain each one fully as a smart opponent would — do not make them weak\n3. Rate each counterargument: WEAK / MODERATE / STRONG threat to my thesis\n4. Suggest how I could respond to or pre-empt each one\n\nBe harsh. My goal is to make my argument stronger.\n\nMy thesis: [STATE YOUR THESIS IN 1-3 SENTENCES]",
        "output_fmt": "Three numbered counterarguments, each with full explanation, threat rating, and suggested response"
    },
    {
        "title": "Topic Deep Dive Explorer",
        "category": "Research",
        "difficulty": "Beginner",
        "tags": "research, explore, topic, overview, learning",
        "role": "You are a knowledgeable research guide who helps people explore new topics systematically",
        "goal": "Give me a comprehensive map of a topic so I know exactly what to study and where to start",
        "context": "I am new to a topic and want to understand its full landscape before diving into specific areas",
        "prompt_text": "I want to explore [TOPIC] and need a comprehensive overview to guide my research.\n\nPlease provide:\n1. A brief overview of what this field is and why it matters\n2. The 5-7 key subtopics or dimensions I should understand\n3. The major debates or open questions in this field\n4. 3-5 foundational books, papers, or resources to start with\n5. Adjacent fields I should also explore\n6. The most important terms and vocabulary I need to know\n\nMy background: [YOUR CURRENT KNOWLEDGE LEVEL]\nMy goal: [WHY YOU ARE RESEARCHING THIS]",
        "output_fmt": "Six numbered sections as listed, with the resources section including titles and brief descriptions"
    },

    # ── RESUME ─────────────────────────────────────────────────
    {
        "title": "Resume Bullet Point Writer",
        "category": "Resume",
        "difficulty": "Beginner",
        "tags": "resume, bullet points, achievements, job, career",
        "role": "You are an expert resume writer and career coach who has helped hundreds of people land jobs at top companies",
        "goal": "Transform my vague job duties into powerful, achievement-focused resume bullet points with measurable results",
        "context": "I need to update my resume and want my experience to sound impressive and specific rather than generic",
        "prompt_text": "Rewrite my job duties as strong resume bullet points using this format:\n[Strong Action Verb] + [What You Did] + [Measurable Result or Impact]\n\nRules:\n- Start every bullet with a past-tense action verb\n- Include numbers, percentages, or metrics wherever possible\n- Keep each bullet under 120 characters\n- Use language that an ATS system will recognize for [INDUSTRY]\n- Write [NUMBER] bullet points\n\nMy job title: [YOUR TITLE]\nIndustry: [YOUR INDUSTRY]\nMy raw duties and achievements (write informally, do not worry about format):\n[PASTE YOUR ROUGH NOTES HERE]",
        "output_fmt": "Numbered list of polished bullet points, each starting with a strong action verb"
    },
    {
        "title": "Cover Letter Writer",
        "category": "Resume",
        "difficulty": "Beginner",
        "tags": "cover letter, job application, hiring, career, writing",
        "role": "You are a professional career coach and writer who creates compelling cover letters that get interviews",
        "goal": "Write a tailored, genuine cover letter that connects my experience directly to the job requirements",
        "context": "I am applying for a specific job and need a cover letter that stands out from generic templates",
        "prompt_text": "Write a professional cover letter for the job below.\n\nTone: [FORMAL / CONVERSATIONAL / ENTHUSIASTIC]\nLength: 3 paragraphs, under 300 words\n\nRules:\n- Do NOT start with 'I am writing to express my interest'\n- Open with a specific hook that shows I understand the company\n- Connect 2-3 of my experiences directly to their requirements\n- Close with a confident call to action\n- Sound like a real human wrote it, not a template\n\nMy background: [PASTE YOUR RELEVANT EXPERIENCE]\nJob title: [JOB TITLE]\nCompany: [COMPANY NAME]\nKey requirements from the job description: [PASTE JD BULLET POINTS]\nWhat genuinely interests me about this role: [YOUR HONEST ANSWER]",
        "output_fmt": "Three paragraphs: hook and connection, experience match, confident closing with call to action"
    },
    {
        "title": "Interview Preparation Coach",
        "category": "Resume",
        "difficulty": "Intermediate",
        "tags": "interview, preparation, STAR method, questions, career",
        "role": "You are an experienced interview coach who has helped candidates prepare for interviews at top companies",
        "goal": "Prepare me for my upcoming interview by predicting likely questions and helping me craft strong STAR-format answers",
        "context": "I have an interview coming up and want to practice my answers to likely questions for this specific role",
        "prompt_text": "Help me prepare for my upcoming job interview.\n\nPlease:\n1. Give me the 8 most likely interview questions for this role\n2. For the 3 questions I choose below, help me write a STAR-format answer\n3. Point out any weaknesses in my answers\n4. Suggest 2 strong questions I should ask the interviewer at the end\n\nRole I am interviewing for: [JOB TITLE]\nCompany: [COMPANY NAME]\nMy relevant experience: [BRIEF SUMMARY]\nThe 3 questions I want to practice: [LIST THEM OR WRITE: choose for me]",
        "output_fmt": "List of 8 predicted questions, then STAR answers for chosen questions, then suggested questions to ask"
    },

    # ── PRODUCTIVITY ───────────────────────────────────────────
    {
        "title": "Brain Dump Processor",
        "category": "Productivity",
        "difficulty": "Beginner",
        "tags": "productivity, planning, brain dump, organize, clarity",
        "role": "You are a productivity coach and organizational expert who helps people turn mental chaos into clear action plans",
        "goal": "Take everything that is in my head and organize it into a clear, prioritized action plan I can actually follow",
        "context": "I am feeling overwhelmed with too many things to do and need help sorting out what actually matters",
        "prompt_text": "I am going to do a brain dump of everything on my mind. Please organize it into a clear structure.\n\nSort everything into these categories:\n1. URGENT AND IMPORTANT — Do today\n2. IMPORTANT, NOT URGENT — Schedule for later\n3. URGENT, NOT IMPORTANT — Delegate or do quickly\n4. NOT URGENT, NOT IMPORTANT — Eliminate or ignore\n5. OPEN LOOPS — Things I am waiting on or need to follow up\n6. ONE NEXT ACTION — The single most important thing I should do right now\n\nMy brain dump:\n[WRITE EVERYTHING IN YOUR HEAD HERE — grammar and order do not matter]",
        "output_fmt": "Six clearly labeled sections, with the One Next Action section highlighted at the end"
    },
    {
        "title": "Weekly Planner",
        "category": "Productivity",
        "difficulty": "Beginner",
        "tags": "planning, weekly, schedule, time management, goals",
        "role": "You are a productivity coach who specializes in helping people design realistic, effective weekly plans",
        "goal": "Create a structured, time-blocked weekly plan that balances my goals, energy levels, and fixed commitments",
        "context": "I want to plan my week in advance so I can be intentional about how I spend my time and actually achieve my goals",
        "prompt_text": "Help me build a realistic plan for my week.\n\nMy context:\n- Work hours: [e.g. 9am to 6pm, Monday to Friday]\n- Top 3 goals this week: [LIST THEM]\n- Fixed commitments: [MEETINGS, CLASSES, APPOINTMENTS WITH TIMES]\n- My biggest challenge right now: [DESCRIBE]\n- My energy pattern: [MORNING PERSON / AFTERNOON / EVENING]\n\nPlease create:\n1. A day-by-day overview with time blocks for deep work, admin, and rest\n2. My Weekly Big 3 — the 3 outcomes that would make this week a success\n3. One thing I should say NO to or remove this week\n4. A 10-minute end-of-day reflection prompt I can reuse every evening",
        "output_fmt": "Day-by-day schedule, then Weekly Big 3, then one thing to eliminate, then daily reflection prompt"
    },
    {
        "title": "Project Breakdown Planner",
        "category": "Productivity",
        "difficulty": "Intermediate",
        "tags": "project management, planning, tasks, milestones, breakdown",
        "role": "You are a project manager with experience breaking down complex projects into clear, achievable steps",
        "goal": "Break my big project into phases, milestones, and specific tasks so I know exactly what to do and in what order",
        "context": "I have a large project that feels overwhelming and I do not know where to start or how to organize it",
        "prompt_text": "Help me break down the following project into a clear, actionable plan.\n\nProject: [DESCRIBE YOUR PROJECT IN 2-4 SENTENCES]\nDeadline: [DATE OR FLEXIBLE]\nResources: [TOOLS, TEAM SIZE, BUDGET — or: working alone]\nMy biggest concern: [WHAT WORRIES YOU MOST ABOUT THIS PROJECT]\n\nPlease provide:\n1. 3-5 phases with a clear outcome for each phase\n2. Specific tasks within each phase\n3. The critical path — what must happen before what?\n4. The highest risk task and how to reduce that risk\n5. A first week action plan to build immediate momentum",
        "output_fmt": "Phases with tasks listed under each, critical path summary, risk section, and first week plan"
    },
]

def seed():
    print("Seeding database with sample prompts...")
    for i, p in enumerate(prompts):
        add_prompt(
            title=p["title"],
            category=p["category"],
            difficulty=p["difficulty"],
            tags=p["tags"],
            role=p["role"],
            goal=p["goal"],
            context=p["context"],
            prompt_text=p["prompt_text"],
            output_fmt=p["output_fmt"]
        )
        print(f"  ✅ Added: {p['title']}")

    print(f"\n🎉 Done! {len(prompts)} prompts added to your library.")

if __name__ == "__main__":
    seed()