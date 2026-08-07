import { useState } from 'react'

const EXAMPLE = '画出2024年各月销售额趋势，1月100，2月200，3月150，4月300，5月250，6月400'

export default function GenerateForm({ thinking, setThinking, advanced, setAdvanced, loading, onGenerate }) {
  const [description, setDescription] = useState('')
  const [showAdvanced, setShowAdvanced] = useState(false)

  const canSubmit = description.trim() && !loading

  const setAdv = (key) => (e) => setAdvanced({ ...advanced, [key]: e.target.value })

  return (
    <section className="card">
      <h2 className="card-title">生成图表</h2>

      <label className="field-label" htmlFor="demand">需求描述</label>
      <textarea
        id="demand"
        className="textarea"
        rows={10}
        placeholder={`例如：${EXAMPLE}`}
        value={description}
        onChange={(e) => setDescription(e.target.value)}
      />

      <div className="form-row">
        <label className="switch-wrap">
          <span className="field-label inline">深度思考模式</span>
          <button
            type="button"
            role="switch"
            aria-checked={thinking}
            className={`switch ${thinking ? 'on' : ''}`}
            onClick={() => setThinking(!thinking)}
          >
            <span className="switch-dot" />
          </button>
          <span className="switch-text">{thinking ? '已开启' : '已关闭'}</span>
        </label>

        <button
          type="button"
          className="link-btn"
          onClick={() => setShowAdvanced(!showAdvanced)}
        >
          高级设置 {showAdvanced ? '▲' : '▼'}
        </button>
      </div>

      {showAdvanced && (
        <div className="advanced-panel">
          <p className="advanced-hint">留空则使用服务器 .env 中的默认配置</p>
          <div className="advanced-grid">
            <div>
              <label className="field-label">API Key</label>
              <input className="input" type="password" placeholder="sk-…" value={advanced.api_key} onChange={setAdv('api_key')} />
            </div>
            <div>
              <label className="field-label">Base URL</label>
              <input className="input" placeholder="https://api.openai.com/v1" value={advanced.base_url} onChange={setAdv('base_url')} />
            </div>
            <div>
              <label className="field-label">模型</label>
              <input className="input" placeholder="gpt-4o" value={advanced.model} onChange={setAdv('model')} />
            </div>
          </div>
        </div>
      )}

      <button
        type="button"
        className="btn-primary"
        disabled={!canSubmit}
        onClick={() => onGenerate(description.trim())}
      >
        生成图表
      </button>
    </section>
  )
}
