import { useState } from 'react'
import StarBanner from './components/StarBanner'
import Header from './components/Header'
import GenerateForm from './components/GenerateForm'
import ResultPanel from './components/ResultPanel'
import { generateChart, modifyData, modifyStyle } from './api'

export default function App() {
  const [thinking, setThinking] = useState(false)
  const [advanced, setAdvanced] = useState({ api_key: '', base_url: '', model: '' })
  const [result, setResult] = useState(null)
  const [loading, setLoading] = useState('')
  const [error, setError] = useState('')

  const provider = () => {
    const p = {}
    if (advanced.api_key.trim()) p.api_key = advanced.api_key.trim()
    if (advanced.base_url.trim()) p.base_url = advanced.base_url.trim()
    if (advanced.model.trim()) p.model = advanced.model.trim()
    return p
  }

  const run = async (label, fn) => {
    setLoading(label)
    setError('')
    try {
      setResult(await fn())
    } catch (e) {
      setError(e.message)
    } finally {
      setLoading('')
    }
  }

  const handleGenerate = (description) =>
    run('AI 正在分析需求并绘制图表，通常需要 1~3 分钟，请稍候…', () =>
      generateChart({ description, thinking, ...provider() }),
    )

  const handleModifyData = (demand) =>
    run('AI 正在修改数据并重新绘制，请稍候…', () =>
      modifyData({ demand, params: result.params, thinking, ...provider() }),
    )

  const handleModifyStyle = (demand) =>
    run('AI 正在调整样式并重新绘制，请稍候…', () =>
      modifyStyle({ demand, params: result.params, thinking, ...provider() }),
    )

  return (
    <div className="page">
      <StarBanner />
      <Header />
      <main className="container main">
        {error && <div className="error-banner">{error}</div>}

        <GenerateForm
          thinking={thinking}
          setThinking={setThinking}
          advanced={advanced}
          setAdvanced={setAdvanced}
          loading={!!loading}
          onGenerate={handleGenerate}
        />

        <ResultPanel
          result={result}
          loading={loading}
          onModifyData={handleModifyData}
          onModifyStyle={handleModifyStyle}
          onReset={() => {
            setResult(null)
            setError('')
          }}
        />
      </main>

      {loading && (
        <div className="loading-overlay">
          <div className="loading-box">
            <div className="spinner" />
            <p>{loading}</p>
          </div>
        </div>
      )}
    </div>
  )
}
