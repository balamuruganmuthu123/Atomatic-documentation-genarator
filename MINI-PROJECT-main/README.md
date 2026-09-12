# 📄 Auto Documentation Generator

> **Free** AI-powered academic documentation generator — create professional project reports directly from your GitHub repository.

Automatically analyzes your GitHub codebase and generates **college-standard academic documentation** (8-chapter format) using Google Gemini AI (free tier) with Ollama local fallback. Outputs publication-ready PDFs with cover pages, bonafide certificates, architecture diagrams, and more.

---

## ✨ Features

- 🔗 **GitHub Integration** — Connect via OAuth, analyze any repository automatically
- 🤖 **Free AI Generation** — Powered by Google Gemini 1.5 Pro (free tier), with Ollama local fallback
- 📚 **8-Chapter Academic Format** — Introduction, Literature Survey, System Analysis, Design, Implementation, Testing, Results, Conclusion
- 📝 **Preliminary Pages** — Auto-generated cover page, bonafide certificate, acknowledgment, abstract, table of contents
- 📊 **Architecture Diagrams** — AI-generated Mermaid diagrams (system architecture, component, sequence, ER)
- 📄 **Professional PDF Export** — Times New Roman, justified text, proper margins, page numbering
- 🔐 **Secure Authentication** — Clerk-powered GitHub OAuth
- 🆓 **100% Free to Use** — No paid API keys required (Gemini free tier is sufficient)

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| **Framework** | Next.js 16 (App Router) |
| **Auth** | Clerk (GitHub OAuth) |
| **AI (Primary)** | Google Gemini 1.5 Pro (free tier) |
| **AI (Optional)** | OpenAI GPT-4o (paid, used as secondary if configured) |
| **AI (Fallback)** | Ollama (local, completely free) |
| **PDF** | Puppeteer (headless Chrome) |
| **Diagrams** | Mermaid.js via mermaid.ink API |
| **Language** | TypeScript |

---

## 📋 Prerequisites

- **Node.js** 18+ and npm
- **Clerk Account** — [clerk.com](https://clerk.com) (free tier)
- **Google Gemini API Key** — [aistudio.google.com](https://aistudio.google.com) (free — 15 RPM, ~1M tokens/day)
- **Ollama** (optional) — [ollama.com](https://ollama.com) for local AI fallback

> **Note:** OpenAI API key is **optional**. The system works fully with just a free Gemini key.

---

## 🚀 Getting Started

### 1. Clone and Install

```bash
git clone <repository-url>
cd doc-generator
npm install
```

### 2. Configure Environment

Create a `.env.local` file:

```env
# === Authentication (Required) ===
NEXT_PUBLIC_CLERK_PUBLISHABLE_KEY=pk_test_...
CLERK_SECRET_KEY=sk_test_...
NEXT_PUBLIC_CLERK_SIGN_IN_URL=/sign-in
NEXT_PUBLIC_CLERK_SIGN_UP_URL=/sign-up

# === AI Models ===
# Primary AI (Required — free tier from Google AI Studio)
GEMINI_API_KEY=your_gemini_api_key_here

# Secondary AI (Optional — paid, improves quality if set)
# OPENAI_API_KEY=sk-...

# Local AI Fallback (Optional — requires Ollama running locally)
# LOCAL_API_URL=http://localhost:11434/v1
# LOCAL_MODEL_ROUTING=llama3.2
```

### 3. Get Your Free Gemini API Key

1. Go to [Google AI Studio](https://aistudio.google.com/)
2. Click **"Get API Key"**
3. Create a key and paste it as `GEMINI_API_KEY` in `.env.local`

### 4. Run the Development Server

```bash
npm run dev
```

Open [http://localhost:3000](http://localhost:3000) in your browser.

---

## 📖 How It Works

```
GitHub Repo → Code Analysis → AI Generation → PDF Rendering → Download
```

### Pipeline

1. **Repository Analysis** — Fetches up to 200 files, analyzes code structure using Babel AST parsing, detects frameworks, APIs, database schemas, and dependencies
2. **Context Building** — Builds a rich project context (file roles, Prisma schemas, env keys, deep code summaries) to prevent AI hallucination
3. **Chapter Generation** — Routes each of the 8 chapters to Gemini 1.5 Pro with task-specific temperature tuning
4. **Verification & Revision** — AI self-reviews each chapter against academic standards (word count, tone, technical depth) and revises if needed
5. **Diagram Generation** — AI generates Mermaid diagrams, rendered as SVGs via mermaid.ink
6. **PDF Rendering** — Puppeteer renders the full HTML document to A4 PDF with academic formatting

### AI Model Routing

| Task | Model | Temperature | Why |
|---|---|---|---|
| Code Analysis | Gemini 1.5 Pro | 0.2 | Large context window, precise |
| Chapter Writing | Gemini 1.5 Pro | 0.5–0.7 | Free, high-quality prose |
| Diagrams | Gemini 1.5 Pro | 0.3 | Structured output |
| Verification | Gemini 1.5 Pro | 0.2 | Strict formatting checks |

**Fallback chain:** Gemini → OpenAI (if key set) → Ollama (local)

---

## 📁 Project Structure

```
doc-generator/
├── app/
│   ├── page.tsx                    # Landing page
│   ├── layout.tsx                  # Root layout with Clerk provider
│   ├── dashboard/                  # Repository browser & generation UI
│   ├── academic/                   # Academic documentation form
│   ├── sign-in/                    # Clerk sign-in
│   ├── sign-up/                    # Clerk sign-up
│   └── api/
│       └── generate/
│           ├── documentation/      # Main generation endpoint
│           ├── academic/           # Academic-specific endpoint
│           └── pdf/                # PDF rendering endpoint
├── lib/
│   ├── ai/
│   │   └── model-router.ts        # Multi-model AI routing (Gemini → OpenAI → Ollama)
│   ├── documentation/
│   │   ├── academic-project-generator.ts  # Primary 8-chapter generator
│   │   └── academic-generator.ts          # Academic format generator
│   ├── github/
│   │   ├── client.ts              # GitHub API client (Octokit)
│   │   ├── analyzer.ts            # Repository analysis orchestrator
│   │   └── enhanced-analyzer.ts   # Deep code analysis (AST, deps, roles)
│   ├── pdf/
│   │   └── generator.ts           # Puppeteer PDF renderer
│   └── diagrams/
│       └── renderer.ts            # Mermaid → SVG via mermaid.ink
├── components/
│   ├── academic-form.tsx           # Academic metadata input form
│   ├── SectionSelector.tsx         # Documentation section toggles
│   └── markdown-renderer.tsx       # React markdown preview
├── types/
│   ├── academic.ts                # Academic documentation types
│   ├── documentation.ts           # General documentation types
│   └── github.ts                  # Repository analysis types
└── middleware.ts                   # Clerk auth middleware
```

---

## 📚 Generated Documentation Structure

The system produces a complete academic project report:

| Section | Contents |
|---|---|
| **Cover Page** | Project title, student details, college, university, date |
| **Bonafide Certificate** | Formal certificate template |
| **Acknowledgment** | Standard acknowledgment page |
| **Abstract** | 4-paragraph project summary (380–420 words) |
| **Table of Contents** | Auto-generated chapter listing |
| **Chapter 1** | Introduction — background, objectives, scope |
| **Chapter 2** | Literature Survey — existing systems review, research papers |
| **Chapter 3** | System Analysis — requirements, feasibility study |
| **Chapter 4** | System Design — architecture, UML diagrams, database design |
| **Chapter 5** | Implementation — modules, code snippets, algorithms |
| **Chapter 6** | Testing — test cases, strategies, results |
| **Chapter 7** | Results & Discussion — screenshots, performance metrics |
| **Chapter 8** | Conclusion — summary, future enhancements |
| **References** | Academic citations |

---

## 🔧 Troubleshooting

### "All AI providers failed"
- Ensure `GEMINI_API_KEY` is set correctly in `.env.local`
- Check your Gemini free tier quota at [Google AI Studio](https://aistudio.google.com/)
- As a backup, install [Ollama](https://ollama.com) and run `ollama pull llama3.2`

### PDF generation fails
- Puppeteer needs Chromium. On Linux, install: `apt install chromium-browser`
- On Windows/Mac, Puppeteer auto-downloads Chromium

### Diagrams not rendering in PDF
- Diagrams use `mermaid.ink` (external service). Ensure internet connectivity.
- If mermaid.ink is down, diagrams fall back to code blocks in the PDF.

---

## 📄 License

MIT
