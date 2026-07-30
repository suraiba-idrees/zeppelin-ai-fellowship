'use client';

import { FormEvent, useState, ChangeEvent } from "react";

// Standard Structural Blueprint interface mapping for our dynamic JSON object
interface AnalysisResponse {
  match_score: number;
  missing_keywords: string[];
  suggestions: string[];
}

export default function Home() {
  const [resumeFile, setResumeFile] = useState<File | null>(null);
  const [jobDescription, setJobDescription] = useState("");
  const [isLoading, setIsLoading] = useState(false);
  const [analysisResult, setAnalysisResult] = useState<AnalysisResponse | null>(null);

  async function handleSubmit(event: FormEvent<HTMLFormElement>) {
    event.preventDefault();

    if (!resumeFile || !jobDescription.trim()) {
      alert("Please fill out all the analysis parameters.");
      return;
    }

    setIsLoading(true);
    setAnalysisResult(null); 

    try {
     const formData = new FormData();

      formData.append("resume", resumeFile);
      formData.append("job_description", jobDescription);

      const response = await fetch(`${process.env.NEXT_PUBLIC_API_URL}/api/analyze`, {
        method: "POST",
        body: formData,
      });
      
    if (!response.ok) {
      const errorData = await response.json();
      throw new Error(errorData.detail || "Something went wrong.");
}
      // 3. Temporary dynamic mock mapping wrapper to align with frontend layout display cards
      const rawData = await response.json();

      console.log(
        "Backend Connected Successfully! Raw Payload logs:",
        rawData
      );

    setAnalysisResult(rawData);

    } catch (error) {

    const message =
      error instanceof Error
      ? error.message
      : "Unknown error";

    alert(message);

} finally {

  setIsLoading(false);

}
  }
  // ⚡ NEW ACTION TRIGGER TO FRESH START THE WORKSPACE FLOW
  function handleReset() {
    setResumeFile(null);
    setJobDescription("");
    setAnalysisResult(null);
    setIsLoading(false);
    
    // Explicitly reset the native file input DOM node if needed
    const fileInput = document.getElementById("resumeFile") as HTMLInputElement;
    if (fileInput) fileInput.value = "";
  }

  function handleFileChange(event: ChangeEvent<HTMLInputElement>) {
    const file = event.target.files?.[0] || null;
    setResumeFile(file);
  }

  return (
    <div className="app-viewport-wrapper">
      <header className="app-global-navbar">
        <div className="navbar-container">
          <span className="brand-text-label">
            Zeppelin <span className="logo-accent-node">Labs</span>
          </span>
          <div className="navbar-utility-status">
            <span className="pulse-indicator-node"></span>
            <span className="status-framework-tag">Resume Feedback Engine v2.0</span>
          </div>
        </div>
      </header>

      <div className="viewport-workspace-flow">
        <div className="workspace-bounded-container">
          <div className="app-marketing-heading">
            <div className="badge-status-pill">Powered by Gemini</div>
            <h1>Optimize Your Resume For <span className="chrome-indigo-gradient">ATS Alignment</span></h1>
            <p>Scan your profile against target market framework metrics, extract missing keyword parameters, and build clear alignment scores instantly.</p>
          </div>

          <main className="product-interactive-canvas">
            <form id="screenerForm" onSubmit={handleSubmit}>
              
              {/* SECTION 1: RESUME UPLOAD */}
              <div className="canvas-workflow-section">
                <div className="workflow-header-label">
                  <span className="workflow-step-badge">01</span>
                  <label htmlFor="resumeFile" className="workflow-label-text">Ingest Candidate Profile</label>
                </div>

                <div className="mega-dropzone-interactive-container" style={{ position: 'relative' }}>
                  <input
                    type="file"
                    id="resumeFile"
                    accept=".pdf,.doc,.docx"
                    onChange={handleFileChange}
                    style={{
                      position: 'absolute',
                      top: 0,
                      left: 0,
                      width: '100%',
                      height: '100%',
                      opacity: 0,
                      cursor: 'pointer',
                      zIndex: 10
                    }}
                    required
                  />
                  <div className="dropzone-graphic-render-view" style={{ position: 'relative', zIndex: 1 }}>
                    <div className="vector-icon-circle-shell">
                      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
                        <path d="M14.5 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V7.5L14.5 2z" />
                        <polyline points="14 2 14 8 20 8" />
                        <line x1="12" y1="18" x2="12" y2="12" />
                        <polyline points="9 15 12 12 15 15" />
                      </svg>
                    </div>
                    <h3>{resumeFile ? resumeFile.name : "Drag & drop your resume file here"}</h3>
                    <p>or <span className="browse-action-link">browse from local disk</span></p>
                    <span className="file-specification-metadata">Supports PDF and DOCX documents up to 10MB</span>
                  </div>
                </div>
              </div>

              {/* SECTION 2: JOB DESCRIPTION */}
              <div className="canvas-workflow-section">
                <div className="workflow-header-label">
                  <span className="workflow-step-badge">02</span>
                  <label htmlFor="jobDescription">Target Framework / Job Description</label>
                </div>
                <div className="textarea-input-wrapper-shell">
                  <textarea
                    id="jobDescription"
                    value={jobDescription}
                    onChange={(event) => setJobDescription(event.target.value)}
                    placeholder="Paste the complete job description, operational guidelines, or technical key rules from the target company layout here..."
                    required
                  />
                </div>
              </div>

              {/* FOOTER ACTIONS */}
              <div className="canvas-action-footer-panel" style={{ display: 'flex', gap: '1rem', justifyContent: 'center' }}>
                <button 
                  type="button" 
                  onClick={handleReset} 
                  disabled={isLoading}
                  style={{
                    background: '#e2e8f0',
                    color: '#0f172a',
                    border: 'none',
                    padding: '0.85rem 1.75rem',
                    borderRadius: '9999px',
                    fontWeight: 600,
                    cursor: isLoading ? 'not-allowed' : 'pointer'
                  }}
                >
                  Clear Form
                </button>

                <button type="submit" id="submitBtn" className="premium-action-trigger-btn" disabled={isLoading}>
                  {isLoading ? (
                    <div className="interactive-loader-group">
                      <div className="chic-spinner-ring"></div>
                      <span>Processing Matrix Analytics...</span>
                    </div>
                  ) : (
                    <>
                      <span>Scan & Generate AI Matrix Analysis</span>
                      <svg className="chevron-arrow-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
                        <line x1="5" y1="12" x2="19" y2="12" />
                        <polyline points="12 5 19 12 12 19" />
                      </svg>
                    </>
                  )}
                </button>
              </div>
            </form>
          </main>

          {/* DYNAMIC METRICS OUTPUT PANEL */}
          {analysisResult && (
            <section id="resultPanel" className="results-display-sheet">
              <div className="summary-score-hero-card">
                <div className="score-ring-view">
                  <span className="score-metric-number">{analysisResult.match_score}</span>
                  <span className="score-metric-denominator">/100</span>
                </div>
                <div className="hero-text-block">
                  <h2>Framework Alignment Score</h2>
                  <p>Overall matching weight index generated via predictive AI core mapping parameters.</p>
                </div>
              </div>

              <div className="metrics-detail-grid">
                <div className="metric-card-block keyword-card">
                  <h3>Missing Keywords Space</h3>
                  <div className="tags-flex-container">
                    {analysisResult.missing_keywords.map((tag, idx) => (
                      <span key={idx} className="keyword-danger-tag">
                        <span role="img" aria-label="warning">⚠️</span> {tag}
                      </span>
                    ))}
                  </div>
                </div>

                <div className="metric-card-block optimization-card">
                  <h3>Strategic Rewrite Suggestions</h3>
                  <ol className="suggestions-ordered-list">
                    {analysisResult.suggestions.map((item, idx) => (
                      <li key={idx}>{item}</li>
                    ))}
                  </ol>
                </div>
              </div>
            </section>
          )}

        </div>
      </div>
    </div>
  );
}