export default function Header() {
  return (
    <header className="header">
      <div className="container header-inner">
        <svg className="logo-icon" viewBox="0 0 24 24" fill="none" aria-hidden="true">
          <rect x="3" y="12" width="4" height="8" rx="1" fill="#3b82f6" />
          <rect x="10" y="7" width="4" height="13" rx="1" fill="#60a5fa" />
          <rect x="17" y="3" width="4" height="17" rx="1" fill="#93c5fd" />
        </svg>
        <div>
          <h1 className="header-title">AI驱动的数据可视化助手</h1>
          <p className="header-subtitle">用自然语言描述数据，自动生成精美图表</p>
        </div>
      </div>
    </header>
  )
}
