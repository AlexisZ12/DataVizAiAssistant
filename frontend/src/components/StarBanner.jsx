import { useState } from 'react'

const GITHUB_URL = 'https://github.com/AlexisZ12/DataVizAiAssistant'

export default function StarBanner() {
  const [visible, setVisible] = useState(true)
  if (!visible) return null

  return (
    <div className="star-banner">
      <p className="star-banner-text">
        <span className="star-banner-star" aria-hidden="true">⭐</span>
        喜欢这个项目？到 GitHub 给作者点个 Star，支持持续更新！
      </p>
      <a className="star-banner-btn" href={GITHUB_URL} target="_blank" rel="noreferrer">
        去 GitHub ⭐ Star
      </a>
      <button
        type="button"
        className="star-banner-close"
        onClick={() => setVisible(false)}
        aria-label="关闭提示"
      >
        ✕
      </button>
    </div>
  )
}
