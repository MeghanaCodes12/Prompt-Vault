import sys
import os
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

from utils.helpers import add_prompt, add_category, get_category_names
from database.db import init_db

init_db()

# ── ENSURE ALL CATEGORIES EXIST ───────────────────────────────
categories_to_add = [
    "Study", "Coding", "Research", "Resume",
    "Productivity", "Image Editing"
]

existing = get_category_names()
for cat in categories_to_add:
    if cat not in existing:
        add_category(cat)

# ── ALL PROMPTS ───────────────────────────────────────────────
prompts = [

    # ── STUDY ─────────────────────────────────────────────────
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
    {
        "title": "Gain Expert Level Knowledge",
        "category": "Study",
        "difficulty": "Advanced",
        "tags": "expert, mastery, skill, learning, apprentice",
        "role": "You are a world-class expert in [insert skill] who has trained hundreds of students from beginner to mastery level",
        "goal": "Train me from complete beginner to expert level in a specific skill using stages, tasks, and real practice assignments",
        "context": "I want to master a new skill and need a structured roadmap with uncommon resources and shortcuts that most people miss",
        "prompt_text": "You are a world-class expert in [insert skill]. Train me as if I am your apprentice, from beginner to mastery.\n\nBreak it into:\n- Stages of learning with clear milestones\n- Specific tasks for each stage\n- Uncommon resources and shortcuts most people miss\n- Simulations or real-life practice assignments to truly internalize each level\n- How to know when I am ready to move to the next stage\n\nSkill I want to master: [INSERT SKILL]\nMy current level: [COMPLETE BEGINNER / SOME BASICS]",
        "output_fmt": "Structured roadmap with stages, tasks, resources, and practice assignments for each level"
    },
    {
        "title": "Upgrade Mental Software",
        "category": "Study",
        "difficulty": "Advanced",
        "tags": "mindset, cognitive, mental models, thinking, upgrade",
        "role": "You are my cognitive OS upgrader who specializes in auditing and rewriting thought patterns, habits, and belief systems",
        "goal": "Audit my current thought patterns and rewrite my mental operating system to improve clarity, decision speed, memory, creativity, and emotional control",
        "context": "I want to think better, make faster decisions, and operate at a higher cognitive level in my daily life",
        "prompt_text": "You are my cognitive OS upgrader. Audit my current thought patterns, habits, and beliefs based on this description: [describe how you think now].\n\nThen rewrite my operating system to improve:\n- Clarity of thinking\n- Decision speed\n- Memory and retention\n- Creativity and problem solving\n- Emotional control\n\nGive me:\n1. A diagnosis of my current thinking patterns\n2. The upgraded version of each pattern\n3. Daily exercises to install the new patterns\n4. How to track my mental performance improvement\n\nHow I currently think: [DESCRIBE YOUR THOUGHT PATTERNS]",
        "output_fmt": "Diagnosis first, then upgraded patterns, then daily exercises, then a tracking system"
    },

    # ── CODING ────────────────────────────────────────────────
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
        "prompt_text": "Please conduct a thorough code review of the following code.\n\nReview these areas:\n1. Correctness - Does it do what it is supposed to do?\n2. Performance - Any inefficiencies or unnecessary operations?\n3. Readability - Is it clean, well-named, and easy to understand?\n4. Security - Any vulnerabilities or unsafe practices?\n5. Best Practices - Does it follow conventions for [LANGUAGE]?\n6. Top 3 improvements - The highest impact changes I should make first\n\nLanguage: [LANGUAGE]\nPurpose of this code: [ONE SENTENCE]\n\n```[LANGUAGE]\n[PASTE YOUR CODE HERE]\n```",
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

    # ── RESEARCH ──────────────────────────────────────────────
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
        "prompt_text": "I am going to share my thesis with you. Your job is to be my toughest critic.\n\nPlease:\n1. Give me the 3 strongest counterarguments against my thesis\n2. Explain each one fully as a smart opponent would\n3. Rate each counterargument: WEAK / MODERATE / STRONG threat to my thesis\n4. Suggest how I could respond to or pre-empt each one\n\nBe harsh. My goal is to make my argument stronger.\n\nMy thesis: [STATE YOUR THESIS IN 1-3 SENTENCES]",
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

    # ── RESUME ────────────────────────────────────────────────
    {
        "title": "Resume Bullet Point Writer",
        "category": "Resume",
        "difficulty": "Beginner",
        "tags": "resume, bullet points, achievements, job, career",
        "role": "You are an expert resume writer and career coach who has helped hundreds of people land jobs at top companies",
        "goal": "Transform my vague job duties into powerful, achievement-focused resume bullet points with measurable results",
        "context": "I need to update my resume and want my experience to sound impressive and specific rather than generic",
        "prompt_text": "Rewrite my job duties as strong resume bullet points using this format:\n[Strong Action Verb] + [What You Did] + [Measurable Result or Impact]\n\nRules:\n- Start every bullet with a past-tense action verb\n- Include numbers, percentages, or metrics wherever possible\n- Keep each bullet under 120 characters\n- Use language that an ATS system will recognize for [INDUSTRY]\n- Write [NUMBER] bullet points\n\nMy job title: [YOUR TITLE]\nIndustry: [YOUR INDUSTRY]\nMy raw duties and achievements:\n[PASTE YOUR ROUGH NOTES HERE]",
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
        "prompt_text": "Write a professional cover letter for the job below.\n\nTone: [FORMAL / CONVERSATIONAL / ENTHUSIASTIC]\nLength: 3 paragraphs, under 300 words\n\nRules:\n- Do NOT start with 'I am writing to express my interest'\n- Open with a specific hook that shows I understand the company\n- Connect 2-3 of my experiences directly to their requirements\n- Close with a confident call to action\n- Sound like a real human wrote it, not a template\n\nMy background: [PASTE YOUR RELEVANT EXPERIENCE]\nJob title: [JOB TITLE]\nCompany: [COMPANY NAME]\nKey requirements: [PASTE JD BULLET POINTS]\nWhat genuinely interests me about this role: [YOUR HONEST ANSWER]",
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
        "prompt_text": "Help me prepare for my upcoming job interview.\n\nPlease:\n1. Give me the 8 most likely interview questions for this role\n2. For the 3 questions I choose below, help me write a STAR-format answer\n3. Point out any weaknesses in my answers\n4. Suggest 2 strong questions I should ask the interviewer at the end\n\nRole: [JOB TITLE]\nCompany: [COMPANY NAME]\nMy relevant experience: [BRIEF SUMMARY]\nThe 3 questions I want to practice: [LIST THEM OR WRITE: choose for me]",
        "output_fmt": "List of 8 predicted questions, then STAR answers for chosen questions, then suggested questions to ask"
    },

    # ── PRODUCTIVITY ──────────────────────────────────────────
    {
        "title": "Brain Dump Processor",
        "category": "Productivity",
        "difficulty": "Beginner",
        "tags": "productivity, planning, brain dump, organize, clarity",
        "role": "You are a productivity coach and organizational expert who helps people turn mental chaos into clear action plans",
        "goal": "Take everything that is in my head and organize it into a clear, prioritized action plan I can actually follow",
        "context": "I am feeling overwhelmed with too many things to do and need help sorting out what actually matters",
        "prompt_text": "I am going to do a brain dump of everything on my mind. Please organize it into a clear structure.\n\nSort everything into:\n1. URGENT AND IMPORTANT - Do today\n2. IMPORTANT, NOT URGENT - Schedule for later\n3. URGENT, NOT IMPORTANT - Delegate or do quickly\n4. NOT URGENT, NOT IMPORTANT - Eliminate or ignore\n5. OPEN LOOPS - Things I am waiting on or need to follow up\n6. ONE NEXT ACTION - The single most important thing I should do right now\n\nMy brain dump:\n[WRITE EVERYTHING IN YOUR HEAD HERE]",
        "output_fmt": "Six clearly labeled sections, with the One Next Action section highlighted at the end"
    },
    {
        "title": "Weekly Planner",
        "category": "Productivity",
        "difficulty": "Beginner",
        "tags": "planning, weekly, schedule, time management, goals",
        "role": "You are a productivity coach who specializes in helping people design realistic, effective weekly plans",
        "goal": "Create a structured, time-blocked weekly plan that balances my goals, energy levels, and fixed commitments",
        "context": "I want to plan my week in advance so I can be intentional about how I spend my time",
        "prompt_text": "Help me build a realistic plan for my week.\n\nMy context:\n- Work hours: [e.g. 9am to 6pm, Monday to Friday]\n- Top 3 goals this week: [LIST THEM]\n- Fixed commitments: [MEETINGS, CLASSES, APPOINTMENTS WITH TIMES]\n- My biggest challenge right now: [DESCRIBE]\n- My energy pattern: [MORNING PERSON / AFTERNOON / EVENING]\n\nPlease create:\n1. A day-by-day overview with time blocks\n2. My Weekly Big 3 - the 3 outcomes that would make this week a success\n3. One thing I should say NO to this week\n4. A 10-minute end-of-day reflection prompt I can reuse every evening",
        "output_fmt": "Day-by-day schedule, Weekly Big 3, one thing to eliminate, daily reflection prompt"
    },
    {
        "title": "Project Breakdown Planner",
        "category": "Productivity",
        "difficulty": "Intermediate",
        "tags": "project management, planning, tasks, milestones, breakdown",
        "role": "You are a project manager with experience breaking down complex projects into clear, achievable steps",
        "goal": "Break my big project into phases, milestones, and specific tasks so I know exactly what to do and in what order",
        "context": "I have a large project that feels overwhelming and I do not know where to start or how to organize it",
        "prompt_text": "Help me break down the following project into a clear, actionable plan.\n\nProject: [DESCRIBE YOUR PROJECT IN 2-4 SENTENCES]\nDeadline: [DATE OR FLEXIBLE]\nResources: [TOOLS, TEAM SIZE, BUDGET]\nMy biggest concern: [WHAT WORRIES YOU MOST]\n\nPlease provide:\n1. 3-5 phases with a clear outcome for each\n2. Specific tasks within each phase\n3. The critical path - what must happen before what?\n4. The highest risk task and how to reduce that risk\n5. A first week action plan to build immediate momentum",
        "output_fmt": "Phases with tasks, critical path summary, risk section, and first week plan"
    },
    {
        "title": "Think Like a Billionaire",
        "category": "Productivity",
        "difficulty": "Advanced",
        "tags": "mindset, billionaire, mental models, systems thinking, vision",
        "role": "You are a thinking coach trained on the minds of Elon Musk, Naval Ravikant, Jeff Bezos, and top polymaths",
        "goal": "Reprogram my thought process to think in systems, long-term vision, leverage, and asymmetric outcomes",
        "context": "I want to shift from average thinking to billionaire-level thinking by adopting daily mental models used by the world's top performers",
        "prompt_text": "You are a thinking coach trained on the minds of Elon Musk, Naval Ravikant, Jeff Bezos, and top polymaths.\n\nReprogram my thought process to think in systems, long-term vision, leverage, and asymmetric outcomes.\n\nGive me:\n1. The 5 core mental shifts I need to make immediately\n2. Daily mental models to practice each morning\n3. How to apply first-principles thinking to my current problems\n4. How to identify leverage points in my life and work\n5. A 30-day thinking upgrade plan\n\nMy current situation: [DESCRIBE YOUR LIFE AND GOALS]",
        "output_fmt": "Five mental shifts, daily mental models, first-principles framework, leverage points, and 30-day plan"
    },
    {
        "title": "Value Filter Protocol",
        "category": "Productivity",
        "difficulty": "Beginner",
        "tags": "instagram, creators, learning, content, social media",
        "role": "You are a content strategist who specializes in identifying high-value creators and filtering out low-quality content",
        "goal": "Analyze Instagram creators in a specific topic and identify the 25 who share the most value with the least fluff",
        "context": "I want to curate my social media feed so that every piece of content I consume teaches me something valuable",
        "prompt_text": "Analyze the entire landscape of Instagram creators in [insert topic].\n\nGive me the 25 that share the most value with the least fluff so my feed becomes something I learn from, not just scroll through.\n\nFor each creator provide:\n- Their Instagram handle\n- What they specialize in\n- Why they are worth following\n- The type of content they post\n- Their posting frequency\n\nTopic I want to learn about: [INSERT TOPIC]",
        "output_fmt": "Numbered list of 25 creators with handle, specialty, reason to follow, content type, and posting frequency"
    },
    {
        "title": "Design a God-Tier Life",
        "category": "Productivity",
        "difficulty": "Advanced",
        "tags": "life design, habits, goals, high performance, lifestyle",
        "role": "You are my high-performance architect who specializes in designing complete life systems for maximum freedom and fulfillment",
        "goal": "Help me design a god-tier life based on time freedom, health, wealth, relationships, and purpose",
        "context": "I want to completely redesign my daily life to become unstoppable across all areas that matter to me",
        "prompt_text": "You are my high-performance architect. Help me design a god-tier life based on time freedom, health, wealth, relationships, and purpose.\n\nCreate:\n1. A daily system that maximizes energy and output\n2. The environment I need to build around me\n3. People I must avoid and people I must find\n4. Habits to master in order of priority\n5. Beliefs to rewire to become unstoppable\n6. A 90-day transformation roadmap\n\nMy current situation: [DESCRIBE WHERE YOU ARE NOW]\nMy vision: [DESCRIBE YOUR IDEAL LIFE]",
        "output_fmt": "Six sections covering daily system, environment, people, habits, beliefs, and 90-day roadmap"
    },
    {
        "title": "Be Your Dream Version",
        "category": "Productivity",
        "difficulty": "Advanced",
        "tags": "identity, self-image, mindset, transformation, psychology",
        "role": "You are a psychological reprogrammer who specializes in identity transformation and installing new self-images",
        "goal": "Help me destroy my current limiting identity and install a new operating self-image that aligns with my highest version",
        "context": "I have a clear vision of who I want to become but my current identity, thought patterns, and behaviors are holding me back",
        "prompt_text": "You are a psychological reprogrammer. Based on my goal to become [insert ideal self], help me destroy my current limiting identity and install a new operating self-image, thought pattern, and behavior map that aligns with my highest version.\n\nGive me:\n1. An audit of my current limiting identity and where it came from\n2. The exact new identity I need to install\n3. Daily affirmations and identity statements to repeat\n4. Behaviors my new self does automatically\n5. How to handle moments when my old identity tries to take over\n\nWho I want to become: [INSERT IDEAL SELF]\nWhat is currently holding me back: [DESCRIBE YOUR LIMITING PATTERNS]",
        "output_fmt": "Identity audit, new identity definition, daily affirmations, new behaviors, and relapse prevention strategy"
    },

    # ── IMAGE EDITING ─────────────────────────────────────────
    {
        "title": "Double Exposure Indian Bride Portrait",
        "category": "Image Editing",
        "difficulty": "Advanced",
        "tags": "image editing, double exposure, portrait, indian bride, AI art, midjourney",
        "role": "You are a professional AI image prompt engineer specializing in hyper-realistic portrait photography and creative photo compositing",
        "goal": "Generate a stunning double exposure portrait of an Indian bride seamlessly blended with nature elements",
        "context": "Used with AI image generation tools like Midjourney, DALL-E, Adobe Firefly, or Stable Diffusion to create editorial fashion photography",
        "prompt_text": "Double exposure collage of an Indian bride, seamless blend with pink cherry blossoms, lotus petals, and misty Himalayan valleys. No visible seams or cuts. Hyper-realistic porcelain skin, dewy glossy cheeks, soft pink glossy lips. Razor-sharp close-up of mesmerizing half-closed eyes, plus a full-body twirling pose in a blush-pink mirror-work lehenga. Creative pastel desaturation with magenta dupatta pop. Hyper-blurry fairy-light background. 9:16, ethereal, romantic, sharp focus, 8k.",
        "output_fmt": "AI generated image in 9:16 ratio, ethereal and romantic style, 8K quality, no visible seams or hard cuts"
    },
    {
        "title": "Beach Golden Hour Double Exposure",
        "category": "Image Editing",
        "difficulty": "Advanced",
        "tags": "double exposure, beach, golden hour, portrait, water, AI art",
        "role": "You are a professional AI image prompt engineer specializing in surreal portrait photography and double exposure compositing",
        "goal": "Create a photorealistic double exposure portrait blending a woman with a beach golden hour scene",
        "context": "Used with AI image generation tools to create artistic portrait photography with water and nature elements",
        "prompt_text": "Create a photorealistic 8K double-exposure portrait of a woman, her face and braid accurately rendered, set against a beach at golden hour. A large, translucent water silhouette of her profile is superimposed behind her, revealing an ocean horizon and a glowing sunset within. She stands barefoot in shallow seawater, wearing an aqua-blue shirt and rolled-up beige trousers. Crystal-clear water splashes surround her feet. Painting beyond reality, cinematic, dreamlike atmosphere.",
        "output_fmt": "8K photorealistic double exposure portrait, golden hour lighting, cinematic and dreamlike quality"
    },
    {
        "title": "Indoor Artist Studio Scene",
        "category": "Image Editing",
        "difficulty": "Intermediate",
        "tags": "artist, studio, painting, portrait, indoor, realistic",
        "role": "You are a professional AI image prompt engineer specializing in realistic indoor scene photography",
        "goal": "Create a realistic indoor artist studio scene with a woman painting on an easel",
        "context": "Used with AI image generation tools to create lifestyle and artistic portrait photography",
        "prompt_text": "Create a realistic indoor artist studio scene with a woman in profile painting on a large wooden easel. She has long dark wavy hair, wears round sunglasses, a cream blazer, beige trousers, and white sneakers, while holding a fine paintbrush. The bright studio features wooden flooring, art supplies, paintbrushes, and blank canvases. Soft natural daylight from large windows, cinematic composition, ultra-realistic, 8K.",
        "output_fmt": "Ultra-realistic indoor studio scene, natural daylight, cinematic composition, 8K quality"
    },
    {
        "title": "South Asian Woman Pink Umbrella Portrait",
        "category": "Image Editing",
        "difficulty": "Advanced",
        "tags": "portrait, saree, umbrella, fashion, editorial, indian fashion",
        "role": "You are a professional AI image prompt engineer specializing in luxury Indian fashion editorial photography",
        "goal": "Create an ultra-realistic cinematic portrait of a South Asian woman in traditional attire with a vibrant umbrella",
        "context": "Used with AI image generation tools to create luxury Indian fashion editorial photography",
        "prompt_text": "Ultra-realistic cinematic portrait of a beautiful young South Asian woman standing beneath a vibrant hot-pink umbrella during soft natural daylight. Long silky black hair in a thick side braid with soft face-framing strands, expressive brown eyes, glowing medium-fair skin, tiny black bindi, gentle smile, realistic skin texture. Holding the umbrella handle with both hands, head slightly turned right, looking into the distance with elegant posture. Deep royal-blue shimmer saree with matching blouse, oxidized silver jhumka earrings, silver bracelet. Heritage-style architecture with cream pillars and pastel walls, dreamy outdoor courtyard. Soft diffused daylight, realistic shadows, creamy background bokeh, shallow depth of field, HDR, 85mm DSLR photography, cinematic color grading, luxury Indian fashion editorial, ultra-detailed hair and fabric textures, hyper realistic, 4:5 aspect ratio.",
        "output_fmt": "Hyper-realistic fashion editorial portrait, 4:5 ratio, 85mm DSLR style, cinematic color grading"
    },
    {
        "title": "Three Frame Traditional Attire Collage",
        "category": "Image Editing",
        "difficulty": "Intermediate",
        "tags": "collage, traditional, portrait, mehendi, jhumka, three frame",
        "role": "You are a professional AI image prompt engineer specializing in traditional Indian portrait photography collages",
        "goal": "Create a warm-toned cinematic portrait collage of a South Asian woman in traditional attire arranged in three horizontal frames",
        "context": "Used with AI image generation tools to create traditional Indian portrait photography for social media and portfolios",
        "prompt_text": "A warm-toned cinematic portrait collage of a South Asian woman in traditional attire, arranged in three horizontal frames. She has long black hair styled loosely with soft strands falling across her face, wearing elegant gold jhumka earrings and multiple delicate bangles. Her hands are decorated with intricate mehendi (henna) designs.\n\nFrame 1 (top): She is gently adjusting her jhumka earring, head turned slightly away from the camera, creating a soft candid moment.\nFrame 2 (middle): Close-up of her mehendi-decorated hands holding a flower.\nFrame 3 (bottom): Full face portrait with a gentle smile looking directly at camera.\n\nWarm golden lighting, cinematic color grading, ultra-realistic, 8K.",
        "output_fmt": "Three horizontal frames arranged vertically, warm golden tones, cinematic quality, 8K resolution"
    },
    {
        "title": "Four Panel Kurti Dupatta Collage",
        "category": "Image Editing",
        "difficulty": "Intermediate",
        "tags": "collage, kurti, dupatta, four panel, indian fashion, portrait",
        "role": "You are a professional AI image prompt engineer specializing in Indian fashion photography collages",
        "goal": "Create a four-panel high-definition photorealistic 2x2 grid collage of a young Indian woman in various poses",
        "context": "Used with AI image generation tools to create Indian fashion photography for social media and portfolios",
        "prompt_text": "A four-panel, high-definition photorealistic 2x2 grid collage of a young Indian woman in varying poses. She is wearing a white embroidered sleeveless kurti paired with a sheer pink net dupatta with intricate white lace borders. Long dark hair down, adorned with a fresh pink lily tucked above her right ear in each frame. Pearl-beaded dangle earrings, thin gold chain, pink and silver bangles.\n\nTop Left: Direct portrait, looking slightly up and to the side with a gentle smile.\nTop Right: Playful, covering the lower half of her face with her pink dupatta, peeking over with a direct gaze.\nBottom Left: In profile, looking right, touching her pearl earring with her left hand.\nBottom Right: Close-up, looking down modestly, hands clasped, highlighting the front embroidery.\n\nSoft neutral lighting, simple grey studio wall background, natural clean makeup, 8K.",
        "output_fmt": "2x2 grid collage, four distinct poses, soft neutral studio lighting, 8K photorealistic quality"
    },
    {
        "title": "Premium Outdoor Three Photo Collage",
        "category": "Image Editing",
        "difficulty": "Advanced",
        "tags": "collage, outdoor, green field, golden hour, vertical, Instagram",
        "role": "You are a professional AI image prompt engineer specializing in premium outdoor fashion photography collages",
        "goal": "Create a premium outdoor three-photo vertical collage with golden hour lighting and cinematic bokeh",
        "context": "Used with AI image generation tools to create luxury Instagram aesthetic outdoor photography",
        "prompt_text": "Create a premium outdoor 3-photo vertical collage. Arrange three different poses in a vertical layout separated by soft white mist/fog transitions instead of hard borders.\n\nTop Photo: Standing naturally in a lush green field, looking slightly to the side with a beautiful smile. Soft golden-hour sunlight, blurred green background, cinematic bokeh.\nMiddle Photo: Sitting gracefully on the grass with one hand touching the hair, smiling confidently at the camera. Warm natural lighting, dreamy atmosphere, shallow depth of field.\nBottom Photo: Full-body standing pose in the same green field, looking sideways with a relaxed smile. Flowing outfit, elegant posture, soft evening sunlight, creamy bokeh background.\n\nBackground: Natural village meadow with green grass, trees, soft sunset glow, warm earthy tones.\nStyle: Hyper-realistic DSLR photography, 85mm lens, f/1.8, cinematic color grading, ultra-detailed hair, realistic skin texture, soft natural lighting, premium fashion photoshoot, 9:16 ratio.",
        "output_fmt": "Vertical 9:16 three-photo collage with soft fog transitions, hyper-realistic DSLR style, cinematic color grading"
    },
    {
        "title": "Four Panel Lakeside Rose Garden Collage",
        "category": "Image Editing",
        "difficulty": "Intermediate",
        "tags": "collage, lakeside, rose garden, golden hour, four panel, fashion",
        "role": "You are a professional AI image prompt engineer specializing in outdoor fashion photography collages",
        "goal": "Create a four-panel photo collage of a woman at a lakeside rose garden at golden hour sunset",
        "context": "Used with AI image generation tools to create outdoor fashion photography for social media",
        "prompt_text": "A 4-panel photo collage of a young woman at a lakeside rose garden at golden hour sunset.\n\nPanel 1 - Top left: Half-body, smiling looking to the side, holding a white pearl beaded handbag.\nPanel 2 - Top right: Full body, twirling her skirt, smiling at the camera, lake and hills in the background.\nPanel 3 - Bottom left: Sitting on a stone wall by the flowers, looking down and smiling.\nPanel 4 - Bottom right: Back view close-up, showing the hair bow detail.\n\nGolden hour sunset lighting, rose garden with blooming flowers, lake and soft hills in background, cinematic color grading, hyper-realistic, 8K.",
        "output_fmt": "2x2 grid collage, four distinct poses, golden hour lakeside setting, cinematic 8K quality"
    },
    {
        "title": "Woman with Lotus Flowers Studio Portrait",
        "category": "Image Editing",
        "difficulty": "Intermediate",
        "tags": "portrait, lotus, saree, studio, cinematic, flowers",
        "role": "You are a professional AI image prompt engineer specializing in artistic cinematic studio portrait photography",
        "goal": "Create an elegant cinematic studio portrait of a woman in a white saree holding lotus flowers with petals falling around her",
        "context": "Used with AI image generation tools to create artistic studio portrait photography",
        "prompt_text": "Show a woman standing gracefully, holding a small bouquet of lotus flowers close to her chest, calm serene gaze toward camera. Outfit: elegant white draped saree, a pink flower tucked into her wavy hair. Long wavy dark hair. Background: plain warm-toned studio backdrop with soft directional light, red and white flower petals falling around her, dramatic shadow play. Artistic, cinematic studio portrait photography. Aspect ratio 9:16.",
        "output_fmt": "Cinematic studio portrait, 9:16 ratio, warm-toned backdrop, dramatic shadow play with falling petals"
    },
    {
        "title": "Four Panel Black Peplum Top Collage",
        "category": "Image Editing",
        "difficulty": "Intermediate",
        "tags": "collage, fashion, peplum, denim, golden hour, four panel",
        "role": "You are a professional AI image prompt engineer specializing in outdoor fashion photography collages",
        "goal": "Create a high-quality four-panel collage of a woman in a stylish black peplum top with floral print",
        "context": "Used with AI image generation tools to create outdoor fashion photography for portfolios and social media",
        "prompt_text": "A high-quality 4-panel collage photography of a beautiful Indian woman with long, wavy dark brown hair. She is wearing a stylish black sleeveless peplum top featuring a delicate red and orange floral ethnic block print, paired with blue denim jeans. In the various poses, she is smiling gently with eyes closed, posing naturally in soft golden hour sunlight against a textured beige outdoor wall with soft green leaves in the background. Photorealistic, 8K resolution, cinematic lighting, shallow depth of field.",
        "output_fmt": "Four-panel collage, golden hour outdoor lighting, 8K photorealistic, cinematic shallow depth of field"
    },
    {
        "title": "Mustard Flower Field Portrait",
        "category": "Image Editing",
        "difficulty": "Intermediate",
        "tags": "portrait, mustard field, flowers, traditional dress, romantic, nature",
        "role": "You are a professional AI image prompt engineer specializing in romantic outdoor portrait photography",
        "goal": "Create a dreamy romantic portrait of a woman kneeling in a vibrant mustard flower field in traditional dress",
        "context": "Used with AI image generation tools to create romantic outdoor portrait photography",
        "prompt_text": "A beautiful young woman kneeling in a vibrant mustard flower field, wearing a pastel pink embroidered traditional dress with flowing sleeves and a yellow flower crown. Long wavy dark hair, soft smile, natural makeup, surrounded by blooming yellow flowers under a cloudy blue sky. Dreamy romantic atmosphere, photorealistic portrait, soft natural daylight, shallow depth of field, cinematic color grading, 85mm lens, ultra-detailed, realistic skin tones, bokeh background, HDR, 8K. 3:4 ratio.",
        "output_fmt": "Romantic outdoor portrait, 3:4 ratio, 85mm lens style, dreamy cinematic atmosphere, 8K HDR quality"
    },
    {
        "title": "Blur and Lightning Fix",
        "category": "Image Editing",
        "difficulty": "Advanced",
        "tags": "photo enhancement, blur fix, lighting, cinematic, portrait restoration",
        "role": "You are a professional AI image enhancement specialist who restores and transforms low-quality photos into cinematic portraits",
        "goal": "Transform a low-quality blurry night photo into a high-quality cinematic portrait with ethereal daylight-style lighting",
        "context": "Used with AI image enhancement tools to restore and enhance portrait photos taken in poor lighting conditions",
        "prompt_text": "Use the first image as the base image. Preserve the exact pose, camera distance, framing, facial structure, expression, and hair placement with zero alterations.\n\nTransform the image from low-quality night capture into a high-quality cinematic portrait by restoring sharpness and clarity. Reduce motion blur and softness while keeping natural skin texture, pores, and fine details intact. No artificial smoothing, reshaping, or reconstruction.\n\nApply ethereal daylight-style lighting. Introduce soft, diffused sun rays entering from an upper side angle, striking the cheekbones, nose bridge, lips, and individual hair strands. Add subtle lens bloom, controlled light haze, and atmospheric glow.\n\nColor-grade with slightly lowered saturation, warm highlights, and cooler shadows. Add delicate film-style grain. Keep the background exactly the same, allowing only natural sunlight flares and soft bokeh.\n\nFinal result should feel like a soft, sunlit daydream, cinematic and ethereal.",
        "output_fmt": "High-quality cinematic portrait with ethereal daylight lighting, film grain, warm color grading, preserved identity"
    },
    {
        "title": "Oil Paint Effect",
        "category": "Image Editing",
        "difficulty": "Intermediate",
        "tags": "oil painting, art effect, traditional, fine art, portrait transformation",
        "role": "You are a professional AI art transformation specialist who converts photos into traditional fine-art paintings",
        "goal": "Transform a reference photo into a traditional fine-art oil painting while preserving the exact composition and colors",
        "context": "Used with AI image generation tools like Reve to apply artistic painting effects to photographs",
        "prompt_text": "Transform the reference image into a traditional fine-art oil painting while preserving the exact composition, proportions, perspective, camera angle, lighting, and colors.\n\nApply realistic oil-paint textures with visible brushstrokes, layered pigments, subtle canvas grain, and smooth painterly blending. Slightly soften edges naturally, without changing any forms.\n\nDo not add, remove, exaggerate, stylize, or alter anything. No abstraction or redesign.\n\nThe result should look like the same image carefully repainted by a master oil painter.",
        "output_fmt": "Traditional fine-art oil painting with visible brushstrokes, canvas texture, and painterly blending"
    },
    {
        "title": "Minecraft Background Transformation",
        "category": "Image Editing",
        "difficulty": "Advanced",
        "tags": "minecraft, background, voxel, game art, photo transformation",
        "role": "You are a professional AI image transformation specialist who creates hybrid real-person Minecraft background compositions",
        "goal": "Keep the human subject 100 percent photorealistic while rebuilding the background as a structurally accurate Minecraft voxel environment",
        "context": "Used with AI image generation tools to create creative hybrid compositions blending real photography with Minecraft game aesthetics",
        "prompt_text": "Keep the human subject 100 percent photorealistic and untouched. No pixel filter, no stylization on skin. Preserve exact facial detail, pores, fabric weave, hair strands, natural shadows. Expression and posture remain identical.\n\nRebuild the background as a structurally accurate Minecraft voxel replica of the original location. Match the exact layout, spacing, depth, and geometry from the reference image. Replicate paths, trees, buildings, and objects using appropriate Minecraft blocks while maintaining their exact position and proportion.\n\nPerspective must match the original photo perfectly. Horizon line, camera height, focal distance, framing, subject scale all identical.\n\nLighting recreated as Minecraft daylight matching the direction and intensity of the original photo.\n\nHigh-resolution in-engine screenshot realism. No UI, no text, no overlays.",
        "output_fmt": "Photorealistic human subject with accurate Minecraft voxel background, matching perspective and lighting"
    },
    {
        "title": "Product Ad Composition",
        "category": "Image Editing",
        "difficulty": "Intermediate",
        "tags": "product photography, advertisement, studio, commercial, ingredients",
        "role": "You are a professional AI product photography specialist who creates premium commercial advertisement compositions",
        "goal": "Transform a product photo into a premium advertisement composition with ingredients and studio lighting",
        "context": "Used with AI image generation tools to create high-end commercial product photography for advertisements",
        "prompt_text": "Product studio transformation. Isolate the product from the reference image and rebuild as a premium ad composition. Hero product centered and sharply in focus, surrounded by its key ingredients arranged with intention and depth. Ingredients fresh and tactile, sliced, crushed, or whole depending on context. Composition balanced but not perfectly symmetrical. Clean surface with subtle reflections. Background designed to match the product color palette and mood, soft gradients or tonal transitions. High-end studio lighting with controlled highlights and gentle shadow falloff. Crisp edges with slight natural shadow grounding the product. Micro-details visible like condensation, texture on ingredients, and fine surface imperfections. Minimal but intentional negative space. Polished commercial finish without looking artificial. Accurate color rendering and realistic material response.",
        "output_fmt": "Premium commercial product advertisement with hero product centered, ingredient arrangement, studio lighting"
    },
    {
        "title": "Famous Selfie Composition",
        "category": "Image Editing",
        "difficulty": "Intermediate",
        "tags": "selfie, celebrity, famous person, candid, portrait, realistic",
        "role": "You are a professional AI image composition specialist who creates realistic candid selfie compositions",
        "goal": "Create a realistic iPhone selfie composition of a subject standing with a famous person in a candid natural style",
        "context": "Used with AI image generation tools to create realistic candid selfie compositions for creative and entertainment purposes",
        "prompt_text": "Raw iPhone selfie, subject from reference image and [famous person] standing close together. [Famous person] appearing as most recent self with accurate hair and facial features. Both leaning slightly into frame, casual shoulder-to-shoulder composition. Direct gaze into camera with relaxed neutral expressions. Handheld at arm's length with slight upward tilt. Soft indoor lighting mixed with phone flash causing mild overexposure on highlights. Natural skin texture visible with pores and subtle makeup detail. Stray hairs and fabric creases present. Background loosely visible with everyday environment elements slightly out of focus. Minor motion blur in edges, slight lens distortion from close proximity, off-center framing with imperfect crop, subtle ISO grain and uneven white balance. Unpolished, candid realism.\n\nFamous person: [INSERT FAMOUS PERSON NAME]",
        "output_fmt": "Candid iPhone selfie style, natural imperfections, realistic skin texture, casual composition"
    },
    {
        "title": "Time Travel Selfie",
        "category": "Image Editing",
        "difficulty": "Advanced",
        "tags": "time travel, historical, selfie, creative, ancient egypt, surreal",
        "role": "You are a professional AI image composition specialist who creates surreal time travel photography compositions",
        "goal": "Create a surreal time travel selfie of a person standing with a historical figure in an ancient setting",
        "context": "Used with AI image generation tools to create creative surreal photography compositions blending modern and historical elements",
        "prompt_text": "Selfie, time traveler captured mid moment, arm extended naturally out of frame holding unseen phone, high angle with slight downward tilt, 0.5x ultra wide distortion. The subject and a single ancient Egyptian pharaoh standing close together, both looking directly into the lens, sharing a relaxed genuine smile. The pharaoh in full ceremonial regalia with gold and lapis details catching light. Setting is a fully intact ancient Egyptian temple courtyard in its prime, richly painted columns, polished limestone floors, gold ornamentation reflecting harsh sunlight. Servants and guards moving naturally in the background. Handheld iPhone ultra wide feel, bright overhead desert light, highlights slightly blown on gold surfaces, visible skin texture with pores, light sweat sheen from heat, warm atmospheric haze. No visible camera device, no duplicate figures, no modern objects.",
        "output_fmt": "Ultra-wide iPhone selfie style, ancient Egyptian setting fully intact, warm desert lighting, candid surreal realism"
    },
    {
        "title": "Anime Style Transformation",
        "category": "Image Editing",
        "difficulty": "Intermediate",
        "tags": "anime, transformation, art style, character, hand-drawn, conversion",
        "role": "You are a professional AI art transformation specialist who converts photos into high-quality anime style artwork",
        "goal": "Convert a reference photo into detailed hand-drawn anime style while preserving the exact composition and character proportions",
        "context": "Used with AI image generation tools to transform portrait photographs into anime style artwork",
        "prompt_text": "Anime style transformation. Convert the reference image into detailed hand-drawn anime while preserving exact composition, same camera angle, framing, pose, and character proportions unchanged. Maintain identical facial structure and expression translated into anime aesthetics. Clean linework with controlled variation in line weight. Large expressive eyes styled naturally to match original gaze direction. Simplified but accurate nose and mouth. Hair reinterpreted into defined anime strands while keeping original shape and flow. Skin rendered with smooth tonal shading and soft gradients. Lighting direction and intensity preserved from original image. Colors slightly stylized but faithful to source palette. Background converted into anime environment matching original depth and perspective. Subtle cel shading with gentle highlights. No distortion of anatomy or perspective. High fidelity adaptation rather than reinterpretation.",
        "output_fmt": "Detailed hand-drawn anime style, clean linework, cel shading, faithful to original composition and colors"
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
        print(f"  Added: {p['title']}")

    print(f"\nDone! {len(prompts)} prompts added to your library.")
    print("\nCategories included:")
    from collections import Counter
    cats = Counter(p["category"] for p in prompts)
    for cat, count in sorted(cats.items()):
        print(f"  {cat}: {count} prompts")


if __name__ == "__main__":
    seed()
