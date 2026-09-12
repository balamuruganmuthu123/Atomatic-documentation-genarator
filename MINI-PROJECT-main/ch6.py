# ── Chapter 6: Testing & Validation ──────────────────────────
heading1("CHAPTER 6")
heading1("TESTING AND VALIDATION")

heading2("6.1 Testing Methodology")
body("Testing of the AI Based Automatic Documentation Generator was performed systematically across all modules and system integration points. The testing strategy followed a bottom-up approach, beginning with unit testing of individual helper functions, progressing to integration testing of module interactions, and culminating in end-to-end system testing using real GitHub repositories. Performance testing was additionally conducted to measure generation throughput and response times. The objective of the testing phase was to ensure that all system components produce correct, reliable, and consistent outputs across diverse input repositories and varying network conditions.")

heading2("6.2 Types of Testing")
heading3("6.2.1 Unit Testing")
body("Unit testing was performed on individual, isolated functions and classes within each module. The GitHubClient.detectLanguage method was tested with all 18 supported file extensions to verify correct language name mapping. The DiagramRenderer.encodeMermaid method was tested with sample Mermaid.js code to verify correct base64url encoding and valid mermaid.ink URL formation. The ModelRouter.modelNameFor method was tested for all 12 DocTask types to confirm that each task resolves to the expected model name. The buildAcademicRenderer heading renderer was tested at all four depth levels to confirm correct HTML class assignment.")

heading3("6.2.2 Integration Testing")
body("Integration testing verified the correct data flow between connected modules. The GitHub OAuth flow through Clerk, token extraction, and Octokit client initialization was tested to confirm that the GitHubClient receives a valid authenticated token. The output of the CodeAnalyzer was verified to produce a properly structured RepositoryAnalysis object with all required fields including codeStructure, architectureInfo, apiEndpoints, databaseInfo, and deepCodeSummary. The ModelRouter output was verified to be non-empty valid text for each chapter type when passed to the document assembler. The Puppeteer PDF renderer was tested with sample HTML to confirm that the output is a valid PDF binary buffer with correct page dimensions.")

heading3("6.2.3 System Testing")
body("System testing evaluated the complete end-to-end workflow starting from a user-supplied GitHub repository URL and concluding with a downloadable PDF. Five different repositories covering TypeScript, Python, JavaScript, Java, and Go were used as test inputs. Each generated PDF was manually inspected to confirm the presence of all eight chapters, four diagrams, a cover page, table of contents, and references section. The formatting of each PDF was verified against university standards for font, margin, line spacing, and heading hierarchy compliance.")

heading3("6.2.4 Performance Testing")
body("Performance testing measured the total generation time from API request initiation to PDF binary delivery. Testing was conducted with and without a warm Gemini API session to assess cold-start effects. Average total generation time across five test repositories was approximately 90 seconds, with the AI generation phase accounting for approximately 65 percent of the total time. Puppeteer PDF rendering consistently completed in under 15 seconds. Network latency for mermaid.ink diagram fetching ranged from 2 to 5 seconds depending on connection quality.")

heading2("6.3 Test Cases")
add_table(
    ["TC ID", "Test Scenario", "Input", "Expected Output", "Actual Result", "Status"],
    [
        ["TC01", "GitHub OAuth sign-in via Clerk", "Valid GitHub account credentials", "User authenticated, dashboard accessible", "Authentication successful", "PASS"],
        ["TC02", "Repository listing after login", "Authenticated user session", "List of user repositories displayed", "Repositories listed correctly", "PASS"],
        ["TC03", "File ingestion from public repo", "Public GitHub repo URL", "Up to 200 source files fetched", "Files fetched within limit", "PASS"],
        ["TC04", "File ingestion skip large files", "Repo with files > 500 KB", "Large files excluded from analysis", "Oversized files skipped", "PASS"],
        ["TC05", "Language detection for .ts files", "TypeScript file extension", "Language: TypeScript", "Correct language returned", "PASS"],
        ["TC06", "Language detection for .py files", "Python file extension", "Language: Python", "Correct language returned", "PASS"],
        ["TC07", "Gemini chapter generation", "Code analysis context + prompt", "Non-empty chapter text string", "Valid chapter generated", "PASS"],
        ["TC08", "ModelRouter fallback to Ollama", "Gemini and OpenAI unavailable", "Ollama generates chapter text", "Fallback triggered correctly", "PASS"],
        ["TC09", "Mermaid URL encoding", "Sample Mermaid.js code", "Valid mermaid.ink SVG URL", "URL formed and SVG loaded", "PASS"],
        ["TC10", "PDF generation with Puppeteer", "Complete HTML document string", "A4 PDF binary buffer returned", "Valid PDF generated", "PASS"],
        ["TC11", "PDF header and footer rendering", "HTML with page meta", "Page numbers in header/footer", "Page numbers rendered", "PASS"],
        ["TC12", "Full end-to-end TypeScript repo", "Next.js TypeScript repository", "8-chapter A4 PDF downloaded", "Complete PDF generated", "PASS"],
        ["TC13", "Full end-to-end Python repo", "FastAPI Python repository", "8-chapter A4 PDF downloaded", "Complete PDF generated", "PASS"],
        ["TC14", "Rate limit (429) handling", "Gemini rate limit response", "Retry logic triggered, fallback used", "Fallback chain executed", "PASS"],
        ["TC15", "Private repo with token", "Private repo + valid access token", "Files fetched and analyzed", "Private repo ingested", "PASS"],
    ],
    col_widths=[1.2, 3.5, 3.3, 3.3, 3.3, 1.5]
)

heading2("6.4 Testing Results")
body("All fifteen test cases passed successfully across both unit and integration testing phases. The system demonstrated reliable performance in file ingestion, language detection, AI routing, diagram generation, and PDF export. The ModelRouter fallback chain was verified to engage correctly when primary providers were artificially disabled during integration testing. The Puppeteer-based PDF renderer produced consistent, correctly formatted A4 PDFs across all tested repositories. No critical defects were identified during the testing phase.")

heading2("6.5 Validation")
heading3("6.5.1 Validation Methodology")
body("Validation of the AI Based Automatic Documentation Generator was conducted by comparing generated PDF reports against the formatting and structural requirements specified by the Anna University academic project report guidelines. Five complete reports generated from diverse test repositories were reviewed by the project team and supervisor to assess content quality, technical accuracy, formatting compliance, and structural completeness.")

heading3("6.5.2 Content Accuracy Validation")
body("The AI-generated chapter content was evaluated for technical accuracy by cross-referencing specific claims about the analyzed repository against the actual source code. In all test cases, the implementation chapter correctly identified the primary programming language, key dependencies, and architectural pattern. The system design chapter accurately described the module structure derived from the code analysis phase. Occasional minor inaccuracies in specific function name references were observed but did not affect overall chapter quality.")

heading3("6.5.3 Formatting Compliance Validation")
body("Generated PDFs were validated against university formatting requirements. All PDFs consistently used Times New Roman 12pt body text, 16pt chapter titles, and 14pt section headings. Margins of 25mm top and bottom, 30mm left, and 20mm right were verified using PDF metadata inspection. Line spacing of 1.5 was confirmed visually. All mandatory sections including the cover page, bonafide certificate, acknowledgement, abstract, table of contents, and references were present in every generated report.")

heading2("6.6 Validation Results")
add_table(
    ["Validation Parameter", "Expected Result", "Obtained Result", "Status"],
    [
        ["Chapter completeness", "All 8 chapters present", "8/8 chapters generated", "VALIDATED"],
        ["Diagram generation", "4 diagrams per report", "4/4 diagrams generated", "VALIDATED"],
        ["Font compliance", "Times New Roman 12pt body", "Correct font and size", "VALIDATED"],
        ["Margin compliance", "30mm left, 20mm right, 25mm top/bottom", "Correct margins verified", "VALIDATED"],
        ["Page numbering", "Numbered in footer", "Page X of Y in footer", "VALIDATED"],
        ["AI content relevance", "Project-specific, not generic", "High specificity to repo", "VALIDATED"],
        ["PDF page count", "Minimum 30 pages", "36–45 pages observed", "VALIDATED"],
        ["Mermaid diagrams render", "4 SVGs embedded in PDF", "4 diagrams loaded", "VALIDATED"],
        ["Multi-language support", "TypeScript, Python, Java, JS", "All 4 languages validated", "VALIDATED"],
        ["Fallback chain", "Gemini -> OpenAI -> Ollama", "All three tested and working", "VALIDATED"],
    ],
    col_widths=[4, 4.5, 4.5, 2.5]
)
body("The validation results confirm that the AI Based Automatic Documentation Generator successfully produces structured, accurate, and formatting-compliant academic project reports for a wide range of real-world GitHub repositories. The system meets all primary validation criteria established at the beginning of the project.")
add_page_break()
