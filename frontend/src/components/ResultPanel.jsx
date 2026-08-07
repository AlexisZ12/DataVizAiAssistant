import { useState } from 'react'

const CHART_NAMES = ['折线图', '散点图', '柱状图', '茎叶图', '填充图', '堆叠面积图', '阶梯图']

export default function ResultPanel({ result, loading, onModifyData, onModifyStyle, onReset }) {
  const [dataDemand, setDataDemand] = useState('')
  const [styleDemand, setStyleDemand] = useState('')
  const [showParams, setShowParams] = useState(false)

  if (!result) {
    return (
      <section className="card placeholder-card">
        <div className="placeholder-icon">
          <svg viewBox="0 0 24 24" fill="none" stroke="#93c5fd" strokeWidth="1.5" aria-hidden="true">
            <rect x="3" y="3" width="18" height="18" rx="2" />
            <path d="M3 15l5-5 4 4 5-6 4 4" strokeLinecap="round" strokeLinejoin="round" />
          </svg>
        </div>
        <p className="placeholder-text">生成的图表将显示在这里</p>
      </section>
    )
  }

  const busy = !!loading
  const chartName = CHART_NAMES[result.params.chart_type] ?? `类型 ${result.params.chart_type}`

  const submitData = () => {
    if (!dataDemand.trim() || busy) return
    onModifyData(dataDemand.trim())
    setDataDemand('')
  }

  const submitStyle = () => {
    if (!styleDemand.trim() || busy) return
    onModifyStyle(styleDemand.trim())
    setStyleDemand('')
  }

  return (
    <>
      <section className="card">
        <div className="result-head">
          <h2 className="card-title">图表结果</h2>
          <div className="result-tags">
            <span className="tag">{chartName}</span>
            <span className="tag">{result.thinking ? '深度思考' : '快速执行'}</span>
            <button type="button" className="link-btn" onClick={() => setShowParams(!showParams)}>
              作图参数 {showParams ? '▲' : '▼'}
            </button>
            <button type="button" className="btn-ghost" onClick={onReset} disabled={busy}>
              重新开始
            </button>
          </div>
        </div>

        <div className="image-wrap">
          <img src={result.image} alt="生成的图表" className="result-image" />
        </div>

        {showParams && (
          <pre className="params-view">{JSON.stringify(result.params, null, 2)}</pre>
        )}
      </section>

      <section className="modify-grid">
        <div className="card">
          <h2 className="card-title">编辑数据</h2>
          <textarea
            className="textarea"
            rows={3}
            placeholder="例如：把3月的销售额改成180"
            value={dataDemand}
            onChange={(e) => setDataDemand(e.target.value)}
          />
          <button type="button" className="btn-secondary" disabled={!dataDemand.trim() || busy} onClick={submitData}>
            修改数据
          </button>
        </div>

        <div className="card">
          <h2 className="card-title">编辑样式</h2>
          <textarea
            className="textarea"
            rows={3}
            placeholder="例如：把折线改成红色虚线，标题改成《销售额趋势》"
            value={styleDemand}
            onChange={(e) => setStyleDemand(e.target.value)}
          />
          <button type="button" className="btn-secondary" disabled={!styleDemand.trim() || busy} onClick={submitStyle}>
            修改样式
          </button>
        </div>
      </section>
    </>
  )
}
