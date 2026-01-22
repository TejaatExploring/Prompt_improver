import { useState } from 'react';
import axios from 'axios';
import './App.css';

const API_URL = import.meta.env.VITE_API_URL || 'http://localhost:8000';

function App() {
  const [rawPrompt, setRawPrompt] = useState('');
  const [refinedPrompt, setRefinedPrompt] = useState('');
  const [improvements, setImprovements] = useState('');
  const [analysis, setAnalysis] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');
  const [copied, setCopied] = useState(false);
  const [detailLevel, setDetailLevel] = useState('moderate');

  const handleSubmit = async (e) => {
    e.preventDefault();
    
    if (!rawPrompt.trim() || rawPrompt.trim().length < 5) {
      setError('Please enter a prompt (at least 5 characters)');
      return;
    }

    setLoading(true);
    setError('');
    setRefinedPrompt('');
    setImprovements('');
    setAnalysis(null);
    setCopied(false);

    try {
      const response = await axios.post(`${API_URL}/api/refine`, {
        raw_prompt: rawPrompt,
        detail_level: detailLevel
      });

      setRefinedPrompt(response.data.refined_prompt);
      setImprovements(response.data.improvements);
      setAnalysis(response.data.analysis);
    } catch (err) {
      setError(
        err.response?.data?.detail || 
        'Failed to refine prompt. Please check your API configuration.'
      );
    } finally {
      setLoading(false);
    }
  };

  const handleCopy = () => {
    navigator.clipboard.writeText(refinedPrompt);
    setCopied(true);
    setTimeout(() => setCopied(false), 2000);
  };

  const handleClear = () => {
    setRawPrompt('');
    setRefinedPrompt('');
    setImprovements('');
    setAnalysis(null);
    setError('');
    setCopied(false);
  };

  return (
    <div className="app">
      <div className="container">
        <header className="header">
          <h1 className="title">✨ Prompt Refinement Tool</h1>
          <p className="subtitle">
            Transform vague prompts into clear, structured, high-quality prompts for LLMs
          </p>
        </header>

        <div className="main-content">
          {/* Input Section */}
          <section className="input-section">
            <form onSubmit={handleSubmit}>
              <label htmlFor="rawPrompt" className="label">
                Enter Your Raw Prompt
              </label>
              <textarea
                id="rawPrompt"
                className="textarea"
                value={rawPrompt}
                onChange={(e) => setRawPrompt(e.target.value)}
                placeholder="Example: Write code for login page"
                rows="6"
                disabled={loading}
              />
              
              {/* Detail Level Selector */}
              <div className="detail-level-selector">
                <label className="label-small">Detail Level:</label>
                <div className="radio-group">
                  <label className="radio-option">
                    <input
                      type="radio"
                      name="detailLevel"
                      value="simple"
                      checked={detailLevel === 'simple'}
                      onChange={(e) => setDetailLevel(e.target.value)}
                      disabled={loading}
                    />
                    <span>Simple</span>
                    <span className="radio-description">Quick & concise</span>
                  </label>
                  
                  <label className="radio-option">
                    <input
                      type="radio"
                      name="detailLevel"
                      value="moderate"
                      checked={detailLevel === 'moderate'}
                      onChange={(e) => setDetailLevel(e.target.value)}
                      disabled={loading}
                    />
                    <span>Moderate</span>
                    <span className="radio-description">Balanced (recommended)</span>
                  </label>
                  
                  <label className="radio-option">
                    <input
                      type="radio"
                      name="detailLevel"
                      value="detailed"
                      checked={detailLevel === 'detailed'}
                      onChange={(e) => setDetailLevel(e.target.value)}
                      disabled={loading}
                    />
                    <span>Detailed</span>
                    <span className="radio-description">Comprehensive</span>
                  </label>
                </div>
              </div>
              
              <div className="button-group">
                <button 
                  type="submit" 
                  className="btn btn-primary"
                  disabled={loading || !rawPrompt.trim()}
                >
                  {loading ? (
                    <>
                      <span className="spinner"></span>
                      Refining...
                    </>
                  ) : (
                    'Refine Prompt'
                  )}
                </button>
                
                {rawPrompt && !loading && (
                  <button 
                    type="button" 
                    className="btn btn-secondary"
                    onClick={handleClear}
                  >
                    Clear
                  </button>
                )}
              </div>
            </form>

            {error && (
              <div className="error-message">
                ⚠️ {error}
              </div>
            )}
          </section>

          {/* Output Section */}
          {refinedPrompt && (
            <section className="output-section">
              <div className="output-header">
                <h2 className="output-title">Refined Prompt</h2>
                <button 
                  className="btn btn-copy"
                  onClick={handleCopy}
                  title="Copy to clipboard"
                >
                  {copied ? '✓ Copied!' : '📋 Copy'}
                </button>
              </div>

              <div className="refined-prompt">
                <pre>{refinedPrompt}</pre>
              </div>

              {/* Analysis Details */}
              {analysis && (
                <div className="analysis-section">
                  <h3 className="analysis-title">Automatic Analysis</h3>
                  <div className="analysis-grid">
                    <div className="analysis-item">
                      <span className="analysis-label">Intent:</span>
                      <span className="analysis-value">{analysis.intent}</span>
                    </div>
                    <div className="analysis-item">
                      <span className="analysis-label">Domain:</span>
                      <span className="analysis-value">{analysis.domain}</span>
                    </div>
                    <div className="analysis-item">
                      <span className="analysis-label">Role:</span>
                      <span className="analysis-value">{analysis.role}</span>
                    </div>
                    <div className="analysis-item">
                      <span className="analysis-label">Output Format:</span>
                      <span className="analysis-value">{analysis.output_format}</span>
                    </div>
                  </div>

                  {analysis.missing_details && analysis.missing_details.length > 0 && (
                    <div className="missing-details">
                      <p className="analysis-label">Added Details:</p>
                      <ul>
                        {analysis.missing_details.map((detail, index) => (
                          <li key={index}>{detail}</li>
                        ))}
                      </ul>
                    </div>
                  )}
                </div>
              )}

              {/* Improvements Explanation */}
              {improvements && (
                <div className="improvements-section">
                  <h3 className="improvements-title">What Was Improved</h3>
                  <p className="improvements-text">{improvements}</p>
                </div>
              )}
            </section>
          )}
        </div>

        <footer className="footer">
          <p>
            💡 This tool improves your prompts automatically — it doesn't answer them.
          </p>
        </footer>
      </div>
    </div>
  );
}

export default App;
